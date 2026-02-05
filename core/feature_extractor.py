# core/feature_extractor.py
from urllib.parse import urlparse
import re

HIGH_RISK_KEYWORDS = ["verify", "secure", "update", "account", "confirm"]
NEUTRAL_KEYWORDS = ["login", "signin", "auth"]

def extract_features(url: str) -> dict:
    """Extract features for phishing detection"""
    parsed = urlparse(url)
    domain = parsed.netloc
    path = parsed.path

    features = {
        "url": url,
        "domain": domain,
        "url_length": len(url),
        "has_https": parsed.scheme == "https",
        "has_ip": bool(re.search(r"\d+\.\d+\.\d+\.\d+", domain)),
        "subdomain_count": domain.count("."),
        "suspicious_keywords": {
            "high_risk": [k for k in HIGH_RISK_KEYWORDS if k in url.lower()],
            "neutral": [k for k in NEUTRAL_KEYWORDS if k in url.lower()],
        },
        "uses_shortener": any(
            short in domain
            for short in ["bit.ly", "tinyurl", "t.co"]
        ),
        "path_length": len(path)
    }
    return features
