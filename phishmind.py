# phishmind.py
from core.feature_extractor import extract_features
from core.rule_engine import score_url
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
import json, os

console = Console()

def scan_url(url):
    features = extract_features(url)
    result = score_url(features)
    return features, result

def display(features, result):
    table = Table(title="Extracted Features")
    table.add_column("Feature", style="magenta")
    table.add_column("Value", style="green")

    for k, v in features.items():
        if k != "suspicious_keywords":
            table.add_row(k, str(v))
        else:
            table.add_row(k, str(v["high_risk"] + v["neutral"]))

    console.print(table)
    console.print(f"[bold yellow]Score:[/bold yellow] {result['score']}")
    console.print(f"[bold red]Verdict:[/bold red] {result['verdict']}")
    if result["reasons"]:
        console.print("[bold cyan]Reasons:[/bold cyan]")
        for r in result["reasons"]:
            console.print(f"- {r}")

def save_output(url, features, result):
    os.makedirs("output", exist_ok=True)
    out_file = os.path.join("output", "result.json")
    with open(out_file, "w") as f:
        json.dump({"url": url, "features": features, "result": result}, f, indent=4)
    console.print(f"[bold green]Result saved to {out_file}[/bold green]")

def main():
    console.print("[bold cyan]PhishMind — AI-assisted Phishing URL Detector[/bold cyan]\n")

    choice = Prompt.ask("Scan single URL or batch from file? (single/batch)", choices=["single", "batch"], default="single")

    if choice == "single":
        url = Prompt.ask("Enter the URL to scan")
        features, result = scan_url(url)
        display(features, result)
        save_output(url, features, result)

    else:  # batch scanning
        file_path = Prompt.ask("Enter file path with URLs (one per line)")
        if not os.path.exists(file_path):
            console.print("[bold red]File not found[/bold red]")
            return
        results = []
        with open(file_path, "r") as f:
            for line in f:
                url = line.strip()
                if url:
                    features, result = scan_url(url)
                    results.append({"url": url, "features": features, "result": result})
                    display(features, result)
        save_file = os.path.join("output", "batch_result.json")
        with open(save_file, "w") as f:
            json.dump(results, f, indent=4)
        console.print(f"[bold green]Batch results saved to {save_file}[/bold green]")

if __name__ == "__main__":
    main()
