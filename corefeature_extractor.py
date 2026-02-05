# core/feature_extractor.py

from urllib.parse import urlparse
import re

def extract_features(url: str) -> dict:
    """
    Extract basic phishing-related features from a URL.
    Returns a dictionary.
    """
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    features = {
        "url_length": len(url),
        "has_https": parsed.scheme == "https",
        "has_ip": bool(re.search(r"\d+\.\d+\.\d+\.\d+", domain)),
        "subdomain_count": domain.count("."),
        "suspicious_keywords": any(
            word in url.lower()
            for word in ["login", "verify", "update", "secure", "account"]
        ),
        "uses_shortener": any(
            short in domain
            for short in ["bit.ly", "tinyurl", "t.co"]
        ),
        "path_length": len(path),
    }

    return features
