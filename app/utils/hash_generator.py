import hashlib

def generate_short_code(url):
    """Create a 6-character hash from a URL"""
    hash_object = hashlib.sha256(url.encode())
    return hash_object.hexdigest()[:6]
