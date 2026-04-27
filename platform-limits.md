# Platform Limits

## X (Twitter) API v2 Rate Limits

Limits are typically per 15 minutes unless otherwise noted.

| Category | Endpoint | Method | Per App Limit | Per User Limit | Notes |
|---|---|---|---|---|---|
| **Posts** | `/2/tweets` | GET | 3,500/15min | 5,000/15min | Tweet lookup |
| | `/2/tweets/search/recent` | GET | 450/15min | 300/15min | Recent search (10 default, 100 max results; 512 query length) |
| | `/2/tweets/search/all` | GET | 1/sec, 300/15min | 1/sec | Full-archive search (10 default, 500 max results; 1024 query length) |
| | `/2/users/:id/tweets` | GET | 10,000/15min | 900/15min | User timelines |
| | `/2/users/:id/mentions` | GET | 450/15min | 300/15min | User mentions timelines |
| | `/2/tweets` | POST | 10,000/24hrs | 100/15min | Manage posts (create) |
| | `/2/tweets/:id` | DELETE | — | 50/15min | Manage posts (delete) |
| **Users** | `/2/users`, `/2/users/:id`, `/2/users/by`, `/2/users/by/username/:username` | GET | 300/15min | 900/15min | User lookup |
| | `/2/users/me` | GET | — | 75/15min | Authenticated user lookup |
| | `/2/users/search` | GET | 300/15min | 900/15min | Search users |
| | `/2/users/:id/following` | POST | — | 50/15min | Manage follows (create) |
| | `/2/users/:source_user_id/following/:target_user_id` | DELETE | — | 50/15min | Manage follows (delete) |
| **Media** | `/2/media/upload` | POST | 50,000/24hrs | 500/15min | Media upload (single file) |
| | `/2/media/upload` | GET | 100,000/24hrs | 1,000/15min | Media upload status |
| | `/2/media/upload/initialize` | POST | 180,000/24hrs | 1,875/15min | Media upload (initialize chunked) |
| | `/2/media/upload/:id/append` | POST | 180,000/24hrs | 1,875/15min | Media upload (append chunk) |
| | `/2/media/upload/:id/finalize` | POST | 180,000/24hrs | 1,875/15min | Media upload (finalize chunked) |

## LinkedIn API Rate Limits

LinkedIn API rate limits are not publicly documented by endpoint. They are determined by the application's usage and can be viewed in the Developer Portal ([https://www.linkedin.com/developers/apps](https://www.linkedin.com/developers/apps)) under the Analytics tab after making at least one request to an endpoint. Limits reset daily at midnight UTC. There are both application-level and member-level limits.

## Instagram API Rate Limits

Direct access to Instagram API rate limit documentation was not successful through provided tools. Generally, Instagram (Meta) APIs enforce platform-level rate limits as well as Graph API-level limits, which can be user-based, app-based, or a combination. Developers typically need to consult their Meta Developer Dashboard for specific rate limits applicable to their app and usage. Common practices include limits on the number of API calls per user and per app within a given time window (e.g., hour or 24-hour period). For media uploads, there are often limits on file size and number of uploads per day.
