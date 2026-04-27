# Social Account Setup and Month 1 Content Calendar for Framed

## Phase 1: Social Account Setup

This phase outlines the steps and required information for setting up Framed's social media accounts on X (Twitter), Instagram, and LinkedIn.

### 1.1 Account Creation/Verification & Credentials

**Action Required:** Manual creation/verification of accounts if they do not already exist, and secure provision of API credentials.

| Platform | Required Credentials / Information | Storage Recommendation |
|---|---|---|
| **X (Twitter)** | API Key, API Secret, Access Token, Access Token Secret | Environment Variables / Secure Vault |
| **Instagram** | Access Token (User or Page), App ID, App Secret | Environment Variables / Secure Vault |
| **LinkedIn** | Client ID, Client Secret, Access Token (User or Page) | Environment Variables / Secure Vault |

**Note:** For Instagram and LinkedIn, access tokens often have a limited lifespan and may require refresh mechanisms. The specific type of access token (user or page) will depend on the desired posting capabilities (e.g., posting as a user vs. posting as a business page).

### 1.2 API Integration (Conceptual Outline)

This section provides a high-level overview of API integration for each platform. Actual implementation will require detailed study of each platform's API documentation.

#### X (Twitter)
*   **Authentication:** OAuth 1.0a User Context (for posting on behalf of a user) or OAuth 2.0 Bearer Token (for app-only actions).
*   **Posting Content:** Use the `POST /2/tweets` endpoint for text-based posts. Media attachments (images/videos) require prior upload via the Media API (`POST /2/media/upload` and associated endpoints).
*   **Character Limits:** 280 characters for text posts. Media uploads do not directly count towards this limit but are referenced in the tweet.

#### Instagram
*   **Authentication:** Instagram Graph API uses OAuth 2.0. Access tokens are typically obtained through Facebook Login or the Instagram Basic Display API.
*   **Posting Content:** Requires a Business Account or Creator Account. Use the Instagram Graph API endpoints, specifically for publishing photos (`POST /{ig-user-id}/media`) and videos, and then publishing the container (`POST /{ig-user-id}/media_publish`).
*   **Content Types:** Supports images (JPG, PNG) and videos (MP4, MOV). Specific aspect ratios and resolutions apply.

#### LinkedIn
*   **Authentication:** OAuth 2.0. Requires an application registered on the LinkedIn Developer Portal.
*   **Posting Content:** Use the Share API (`POST /v2/shares`). Content can include text, URLs, and uploaded media. For images/videos, prior upload to LinkedIn's URN (Uniform Resource Name) system is often required.
*   **Character Limits:** Varies by type of share (e.g., URL share, text share). Images and videos are typically linked after upload.

## Phase 2: Month 1 Content Calendar (Conceptual)

This phase outlines a basic content strategy and suggested content types for the first month.

### 2.1 Content Strategy

*   **Goal:** Establish brand presence, introduce Framed's value proposition, engage early followers.
*   **Audience:** Primarily B2B (creators, businesses) and B2C (end-users of creative content).
*   **Themes:** Product features, use cases, industry insights, behind-the-scenes, community spotlights.
*   **Frequency:** Aim for 3-5 posts per week per platform, adjusting based on engagement and platform best practices.

### 2.2 Content Creation (Placeholder Examples)

| Week | Theme | X (Tweet) Example | Instagram Post Idea | LinkedIn Post Idea |
|---|---|---|---|---|
| **1** | **Introduction & Value** | "Hello world! 👋 Framed is here to help creators showcase their work like never before. #FramedApp #CreativeCommunity" | Carousel: 1. Framed logo. 2. UI screenshot. 3. Text overlay: "Your art, beautifully framed." | Article: "Introducing Framed: Elevating Creative Portfolios with AI" (explaining vision and benefits) |
| **2** | **Feature Spotlight: AI Framing** | "Transform your art with AI-powered framing on Framed! ✨ Auto-adjusts for optimal display. #AIFraming #ArtTech" | Short video demo of AI framing in action. | "The Future of Digital Art Display: How AI is Revolutionizing Presentation" (focus on tech aspect) |
| **3** | **User Story / Use Case** | "Meet [CreatorName], using Framed to captivate their audience. See how! [Link to blog post]" | "Creator Spotlight: @[CreatorHandle]" with a stunning framed artwork and a quote. | "Case Study: [Industry] Artists Boost Engagement with Framed's [Feature]" |
| **4** | **Behind the Scenes / Team** | "A peek into the passion behind Framed! Our team is dedicated to empowering creators. #TeamFramed #StartupLife" | Team photo or short video discussing a feature. | "Building Framed: Our Journey to Empowering the Creative Economy" (team culture, mission) |

### 2.3 Scheduling/Publishing Mechanism

*   **Initial:** Manual posting or using a free tier of a social media management tool (e.g., Buffer, Hootsuite) for scheduling.
*   **Future Consideration:** Develop custom scripts for automated publishing for efficiency and integration with other systems, once the content strategy is validated and API limits are understood in practice.
