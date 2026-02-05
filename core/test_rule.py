from core.feature_extractor import extract_features
from core.rule_engine import score_url

url = "http://paypal.verify-login.ru"
features = extract_features(url)
result = score_url(features)

print("Features:", features)
print("Result:", result)
