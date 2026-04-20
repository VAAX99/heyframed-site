// ── Stripe Payment Link URLs ──────────────────────────
// After creating your Payment Links in Stripe Dashboard, paste the URLs here.
// Make sure each link has metadata set: { tier: "framed" } / { tier: "framed+" }
const STRIPE_LINKS = {
  framed:      'https://buy.stripe.com/REPLACE_WITH_FRAMED_LINK',
  framed_plus: 'https://buy.stripe.com/REPLACE_WITH_FRAMED_PLUS_LINK'
};

// ── Checkout button event listeners (replaces inline onclick) ────
document.addEventListener('DOMContentLoaded', () => {
  document.getElementById('btnCheckoutFramed').addEventListener('click', () => openCheckout('framed'));
  document.getElementById('btnCheckoutFramedPlus').addEventListener('click', () => openCheckout('framed_plus'));
  document.getElementById('btnBrowsePacks').addEventListener('click', openPacksPreview);
  document.getElementById('checkoutModal').addEventListener('click', closeCheckoutOverlay);
  document.getElementById('btnModalClose').addEventListener('click', closeCheckout);
  document.getElementById('btnProceedCheckout').addEventListener('click', proceedToCheckout);
  document.getElementById('chatIdInput').addEventListener('keydown', (e) => {
    if (e.key === 'Enter') proceedToCheckout();
  });
});

// ── Checkout Modal ────────────────────────────────────
let _currentTier = null;

function openCheckout(tier) {
  _currentTier = tier;
  const badge = document.getElementById('modalTierBadge');
  badge.textContent = tier === 'framed_plus' ? '✦ Framed+  —  $9.99/mo' : '✦ Framed  —  $4.99/mo';
  document.getElementById('chatIdInput').value = '';
  document.getElementById('chatIdError').style.display = 'none';
  document.getElementById('checkoutModal').classList.add('open');
  setTimeout(() => document.getElementById('chatIdInput').focus(), 150);
}

function closeCheckout() {
  document.getElementById('checkoutModal').classList.remove('open');
}

function closeCheckoutOverlay(e) {
  if (e.target === document.getElementById('checkoutModal')) closeCheckout();
}

function proceedToCheckout() {
  const raw   = document.getElementById('chatIdInput').value.trim();
  const error = document.getElementById('chatIdError');
  if (!raw || !/^\d{5,15}$/.test(raw)) {
    error.style.display = 'block';
    document.getElementById('chatIdInput').focus();
    return;
  }
  error.style.display = 'none';

  const base = STRIPE_LINKS[_currentTier];
  if (!base || base.includes('REPLACE_WITH')) {
    showCheckoutNotice('Payment links coming soon. Thank you for your interest.');
    return;
  }

  // Show loading state on button
  const btn = document.getElementById('btnProceedCheckout');
  const originalText = btn.textContent;
  btn.disabled = true;
  btn.style.opacity = '0.7';
  btn.style.cursor = 'not-allowed';
  btn.innerHTML = '<span style="display:inline-block;width:14px;height:14px;border:2px solid rgba(240,180,41,0.3);border-top-color:#F0B429;border-radius:50%;animation:spin 0.8s linear infinite;margin-right:8px;vertical-align:middle;"></span>Processing...';

  const url = base + '?client_reference_id=' + encodeURIComponent(raw);
  trackAnalytics('form-submit', { form: 'checkout-modal', tier: _currentTier, chat_id_length: raw.length });
  trackAnalytics('checkout-start', { tier: _currentTier, chat_id_length: raw.length, handoff: 'telegram_chat_id_to_stripe' });
  
  // Simulate a small delay before redirecting to show loading state
  setTimeout(() => {
    closeCheckout();
    window.open(url, '_blank');
    // Reset button state after modal closes
    btn.disabled = false;
    btn.style.opacity = '1';
    btn.style.cursor = 'pointer';
    btn.innerHTML = originalText;
  }, 600);
}

function openPacksPreview() {
  showCheckoutNotice('Wallpaper packs are coming soon. Check back shortly for the first collections.');
}

function showCheckoutNotice(message) {
  const existing = document.getElementById('siteNotice');
  if (existing) existing.remove();

  const notice = document.createElement('div');
  notice.id = 'siteNotice';
  notice.style.cssText = 'position:fixed;left:50%;bottom:24px;transform:translateX(-50%);z-index:9999;max-width:min(92vw,520px);padding:14px 18px;border-radius:12px;background:rgba(13,17,23,0.96);color:#e6edf3;border:1px solid rgba(240,180,41,0.35);box-shadow:0 16px 40px rgba(0,0,0,0.35);font-size:14px;line-height:1.5;';
  notice.textContent = message;
  document.body.appendChild(notice);
  setTimeout(() => notice.remove(), 5000);
}

function trackAnalytics(eventName, props = {}) {
  if (typeof plausible === 'function') {
    plausible(eventName, { props });
  }
  if (window.gtag) {
    window.gtag('event', eventName, props);
  }
}

function getScrollDepthBucket() {
  const doc = document.documentElement;
  const scrollable = Math.max(doc.scrollHeight - window.innerHeight, 1);
  const depth = Math.min(100, Math.round((window.scrollY / scrollable) * 100));
  if (depth >= 100) return '100';
  if (depth >= 75) return '75';
  if (depth >= 50) return '50';
  if (depth >= 25) return '25';
  return '0';
}

let lastScrollBucket = '0';
let exitIntentSent = false;

document.addEventListener('click', (event) => {
  const target = event.target.closest('[data-analytics]');
  if (!target) return;
  trackAnalytics(target.dataset.analytics, {
    label: target.dataset.analyticsLabel || target.textContent.trim().slice(0, 80)
  });
});

window.addEventListener('scroll', () => {
  const bucket = getScrollDepthBucket();
  if (bucket !== lastScrollBucket) {
    lastScrollBucket = bucket;
    trackAnalytics('scroll-depth', { bucket });
  }
}, { passive: true });

document.addEventListener('mouseleave', (event) => {
  if (exitIntentSent || event.clientY > 0) return;
  exitIntentSent = true;
  trackAnalytics('exit-intent', { section: getScrollDepthBucket() });
});

document.addEventListener('keydown', e => {
  if (e.key === 'Escape') closeCheckout();
});

// ── Lightweight experiment assignment ────────────────
const EXPERIMENT_STORAGE_PREFIX = 'framed-exp-';

function hashExperimentKey(key) {
  let hash = 0;
  for (let i = 0; i < key.length; i++) {
    hash = (hash * 31 + key.charCodeAt(i)) >>> 0;
  }
  return hash;
}

function getVariant(experimentName) {
  const storageKey = EXPERIMENT_STORAGE_PREFIX + experimentName;
  try {
    const existing = localStorage.getItem(storageKey);
    if (existing === 'A' || existing === 'B') return existing;
  } catch (_) {}

  const bucket = (hashExperimentKey(`${experimentName}:${navigator.userAgent}`) % 100) < 50 ? 'A' : 'B';
  try {
    localStorage.setItem(storageKey, bucket);
  } catch (_) {}
  return bucket;
}

const pricingHeadlineVariant = getVariant('pricing-headline');
if (pricingHeadlineVariant === 'B') {
  const headline = document.querySelector('#pricing .section-title');
  const subtitle = document.querySelector('#pricing .section-sub');
  if (headline) headline.textContent = 'Choose your cinematic wallpaper plan.';
  if (subtitle) subtitle.textContent = 'Pick the tier that fits how you use Telegram, then upgrade when you want more control.';
}
trackAnalytics('experiment-assigned', { experiment: 'pricing-headline', variant: pricingHeadlineVariant });

// ── Nav scroll effect ─────────────────────────────────
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => {
  nav.classList.toggle('scrolled', window.scrollY > 40);
});

// ── Hero bg load animation ────────────────────────────
const heroBg = document.getElementById('heroBg');
const img = new Image();
img.onload = () => heroBg.classList.add('loaded');
img.src = 'https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=1920&q=85&fit=crop';
setTimeout(() => heroBg.classList.add('loaded'), 100);

// ── Reveal on scroll ──────────────────────────────────
const reveals = document.querySelectorAll('.reveal');
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => {
    if (e.isIntersecting) {
      e.target.classList.add('visible');
      observer.unobserve(e.target);
    }
  });
}, { threshold: 0.12 });
reveals.forEach(el => observer.observe(el));

trackAnalytics('page-view', { path: window.location.pathname });

// ── Telegram link handling ───────────────────────────
document.addEventListener('click', (e) => {
  const link = e.target.closest('a[href="#telegram"]');
  if (link) {
    e.preventDefault();
    trackAnalytics('telegram-join', { source: link.dataset.analyticsLabel || 'unknown' });
    window.open('https://t.me/framed_wallpapers', '_blank', 'noopener,noreferrer');
  }
});