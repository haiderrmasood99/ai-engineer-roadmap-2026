# AI Engineer Roadmap 2026

This is the roadmap I would follow if I were starting again: production AI first, course collecting last.

It is built around one question:

> Can this person ship AI systems that work in the real world?

## Start Here By Background

- Backend engineer: start with Phase 3 after skimming Phase 1 math/data gaps.
- ML beginner: do Phases 1 and 2 in order, but build every week.
- Career switcher: use Phase 1 plus the portfolio templates; do not hide in theory.

## Phases

| Phase | Outcome | Time | Build |
|---|---|---:|---|
| 1. Foundations | Python, backend, data, math basics | 6-8 weeks | CLI data pipeline |
| 2. Deep Learning | Train, debug, and evaluate neural nets | 6-10 weeks | image classifier + failure analysis |
| 3. LLMs | RAG, evals, fine-tuning, agents, cost | 8-12 weeks | production RAG system |
| 4. MLOps | versioning, CI, monitoring, deployment | 6-8 weeks | model deployment pipeline |
| 5. Specialisation | healthcare, fintech, system design, or MLOps depth | 8+ weeks | domain portfolio project |

## What To Skip

- Passive course marathons with no shipped project.
- Notebook-only portfolios.
- Prompt engineering without evaluation.
- RAG demos without retrieval tests.
- Fine-tuning before you understand data quality and inference cost.

## Repo Ecosystem

See [repos.md](repos.md) for the eight starter repos behind the content strategy.

## Resource Pages

- [Phase 1: Foundations](resources/phase-1-foundations.md)
- [Phase 2: Deep Learning](resources/phase-2-deep-learning.md)
- [Phase 3: LLMs](resources/phase-3-llms.md)
- [Phase 4: MLOps](resources/phase-4-mlops.md)
- [Phase 5: Specialisation](resources/phase-5-specialisation.md)

## Portfolio Templates

- [Healthcare AI Safety](portfolio-templates/healthcare-ai-safety.md)
- [Medical Image AI](portfolio-templates/medical-image-ai.md)
- [Production RAG](portfolio-templates/production-rag.md)
- [LLM Gateway](portfolio-templates/llm-gateway.md)
- [Fintech AI Compliance](portfolio-templates/fintech-ai-compliance.md)

## Validation

```powershell
python scripts\validate_roadmap.py
python -m pytest
```
