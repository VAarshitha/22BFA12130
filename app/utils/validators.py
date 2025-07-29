import re

def is_valid_url(url):
    """Basic URL format validation"""
    return url.startswith("http://") or url.startswith("https://")
