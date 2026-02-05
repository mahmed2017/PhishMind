🚨 PhishMind

AI-Assisted Phishing URL Detection Engine

PhishMind is a security-focused Python tool designed to analyze, explain, and classify suspicious URLs using layered heuristics inspired by real-world phishing tactics.

Unlike simple keyword scanners, PhishMind focuses on contextual risk, brand impersonation, and domain abuse patterns commonly used in modern phishing campaigns.

🔍 What Problem Does PhishMind Solve?

Phishing URLs are increasingly:

Short-lived

Brand-spoofed

Designed to bypass naive keyword filters

Most beginner tools fail because they:

Treat all keywords equally

Ignore brand/domain mismatch

Miss risky TLD patterns

PhishMind fixes that.

⚙️ Core Capabilities
✅ URL Feature Extraction

PhishMind analyzes:

URL length & structure

HTTPS presence

IP-based URLs

Subdomain depth

Path complexity

URL shorteners

Obfuscation patterns ([.], missing scheme, etc.)

🚨 Phishing Heuristics Engine

Risk is calculated using weighted logic, not flat rules:

Credential-harvesting keywords (login, verify, secure)

Brand impersonation detection (e.g., paypal, google)

Brand ↔ domain mismatch analysis

High-risk TLD detection (.ru, .tk, .zip, etc.)

Trusted domain whitelisting

🧠 Explainable Decisions

PhishMind doesn’t just give a verdict — it explains why:

Verdict: High Risk (Phishing)
Reasons:
- Brand impersonation detected: paypal
- Brand/domain mismatch
- High-risk TLD detected (.ru)
- No HTTPS detected


This makes it suitable for:

Learning

SOC-style triage

Security research

📊 Clear Risk Classification

Each scan returns:

Extracted features

Numerical risk score

Human-readable verdict

Detailed reasoning

JSON output for automation

🖥️ Example Output
Enter the URL to scan: paypal.verify-login.ru

Score: 9.5
Verdict: High Risk (Phishing)

Reasons:
- Brand impersonation detected: paypal
- Domain mismatch detected
- High-risk TLD detected (.ru)
- Credential-harvesting keywords detected

🚀 How to Run
git clone https://github.com/yourusername/PhishMind.git
cd PhishMind
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python phishmind.py

🧩 Project Structure
PhishMind/
│
├── core/
│   ├── feature_extractor.py
│   ├── rule_engine.py
│   ├── explainability.py
│
├── output/
│   └── result.json
│
├── phishmind.py
├── requirements.txt
└── README.md

🛡️ Why This Project Matters

PhishMind is built with a security mindset, not a demo mindset.

It demonstrates:

Threat modeling

Defensive thinking

Explainable security logic

Real phishing detection principles

This is not a toy URL checker.

🧠 Future Roadmap

🔄 Batch URL scanning

🧪 HTML form & password field detection

📈 Machine learning model integration

🌐 WHOIS / domain age analysis

🧠 Confidence scoring

📦 API version (FastAPI)

⚠️ Disclaimer

This tool is intended for educational and defensive security research only.
Do not use it for offensive or malicious purposes.

⭐ Contribute

Pull requests, ideas, and improvements are welcome — especially from:

Cybersecurity learners

Blue team enthusiasts

Threat intelligence researchers
