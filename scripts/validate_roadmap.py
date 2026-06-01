from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "repos.md",
    "resources/phase-1-foundations.md",
    "resources/phase-2-deep-learning.md",
    "resources/phase-3-llms.md",
    "resources/phase-4-mlops.md",
    "resources/phase-5-specialisation.md",
    "portfolio-templates/healthcare-ai-safety.md",
    "portfolio-templates/medical-image-ai.md",
    "portfolio-templates/production-rag.md",
    "portfolio-templates/llm-gateway.md",
    "portfolio-templates/fintech-ai-compliance.md",
    "papers/2026-q1.md",
    "papers/2026-q2.md",
    "papers/2026-q3.md",
    "papers/2026-q4.md",
]
REPO_NAMES = [
    "healthcare-ai-safety-patterns",
    "medical-image-ai-starter",
    "production-rag-toolkit",
    "token-economics-calculator",
    "llm-gateway-starter",
    "llm-memory-patterns",
    "fintech-ai-compliance-kit",
    "ai-engineer-roadmap-2026",
]


def validate() -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED:
        path = ROOT / relative
        if not path.exists():
            errors.append(f"missing {relative}")
        elif len(path.read_text(encoding="utf-8").strip()) < 40:
            errors.append(f"too short {relative}")
    repos_text = (ROOT / "repos.md").read_text(encoding="utf-8")
    for repo in REPO_NAMES:
        if repo not in repos_text:
            errors.append(f"repo missing from repos.md: {repo}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(error)
        return 1
    print("roadmap validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
