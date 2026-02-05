# core/rule_engine.py

TRUSTED_DOMAINS = [
    "google.com", "x.com", "facebook.com", "github.com",
    "microsoft.com", "apple.com", "amazon.com"
]

def is_trusted_domain(domain: str) -> bool:
    return any(domain.endswith(td) for td in TRUSTED_DOMAINS)

def score_url(features: dict) -> dict:
    score = 0
    reasons = []

    # URL length
    if features["url_length"] > 75:
        score += 2
        reasons.append("URL is very long")
    elif features["url_length"] > 50:
        score += 1
        reasons.append("URL length is moderately long")

    # HTTPS
    if not features["has_https"]:
        score += 2
        reasons.append("No HTTPS detected")

    # IP address in domain
    if features["has_ip"]:
        score += 3
        reasons.append("IP address in domain (suspicious)")

    # Subdomain
    if features["subdomain_count"] > 3:
        score += 1
        reasons.append("Too many subdomains")

    # Keywords
    high_risk = len(features["suspicious_keywords"]["high_risk"])
    neutral = len(features["suspicious_keywords"]["neutral"])
    if high_risk > 0:
        score += high_risk * 2
        reasons.append(f"High-risk keywords detected: {features['suspicious_keywords']['high_risk']}")
    if neutral > 0:
        score += neutral * 0.5
        reasons.append(f"Neutral keywords detected: {features['suspicious_keywords']['neutral']}")

    # URL shorteners
    if features["uses_shortener"]:
        score += 2
        reasons.append("Uses URL shortener")

    # Path length
    if features["path_length"] > 20:
        score += 1
        reasons.append("Long URL path detected")

    # Trusted domains reduce risk
    if is_trusted_domain(features["domain"]):
        score -= 2
        reasons.append(f"Trusted domain detected: {features['domain']}")

    # Final verdict
    if score >= 6:
        verdict = "High Risk (Likely Phishing)"
    elif score >= 3:
        verdict = "Medium Risk"
    else:
        verdict = "Low Risk (Probably Safe)"

    return {"score": score, "verdict": verdict, "reasons": reasons}
