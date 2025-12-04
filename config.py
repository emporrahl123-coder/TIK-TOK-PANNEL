# TikTok Security Testing Configuration
# RENAME THIS FILE TO config.py AND FILL WITH YOUR TEST CREDENTIALS

class TikTokConfig:
    # API Endpoints (discovered during recon)
    ENDPOINTS = {
        'like': 'https://api.tiktok.com/api/item/like/',
        'follow': 'https://api.tiktok.com/api/user/relation/update/',
        'unlike': 'https://api.tiktok.com/api/item/like/cancel/',
        'unfollow': 'https://api.tiktok.com/api/user/relation/delete/',
    }
    
    # Test accounts (USE ONLY PROVIDED ACCOUNTS)
    TEST_ACCOUNTS = {
        'account1': {
            'session_id': 'YOUR_TEST_SESSION_ID',
            'user_id': 'TEST_USER_ID_1',
            'ms_token': 'YOUR_MS_TOKEN',
        },
        'account2': {
            'session_id': 'ANOTHER_TEST_SESSION_ID',
            'user_id': 'TEST_USER_ID_2',
            'ms_token': 'ANOTHER_MS_TOKEN',
        }
    }
    
    # Test content (videos you own/created for testing)
    TEST_VIDEOS = [
        'VIDEO_ID_1',
        'VIDEO_ID_2',
    ]
    
    # Rate limiting settings
    RATE_LIMIT_DELAY = 1.0  # seconds between requests
    
    # Headers template
    BASE_HEADERS = {
        'User-Agent': 'TikTok 26.2.0 rv:262018 (iPhone; iOS 14.4.2; en_US) Cronet',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9',
        'Origin': 'https://www.tiktok.com',
        'Referer': 'https://www.tiktok.com/',
    }
