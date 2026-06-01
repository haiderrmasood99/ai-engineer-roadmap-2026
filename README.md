# AI Engineer Roadmap 2026

An opinionated roadmap for becoming an AI engineer who can build, evaluate, and ship real systems.

This is not a list of every course on the internet. It is a practical path through the skills that show up again and again in production AI work: Python, data handling, deep learning basics, LLM systems, retrieval, evaluation, deployment, monitoring, and domain judgment.

The central question behind the roadmap is simple:

> Can you build AI systems that work outside a notebook?

## Who This Is For

- Backend engineers moving into AI.
- ML beginners who want a project-first path.
- Students building a serious portfolio.
- Career switchers who need to avoid endless course collecting.
- Working developers who want to understand LLM systems, evaluation, and deployment.

## Start Here By Background

| Background | Suggested Path |
|---|---|
| Backend engineer | Skim Phase 1 for math and data gaps, then start Phase 3. |
| ML beginner | Do Phases 1 and 2 in order, but build something every week. |
| Career switcher | Start with Phase 1 and use the portfolio templates early. |
| Data analyst | Strengthen Python packaging, APIs, testing, and deployment before going deep on models. |
| Student | Use the phase projects as portfolio anchors, not just practice exercises. |

## Roadmap Overview

| Phase | Outcome | Estimated Time | Build |
|---|---|---:|---|
| 1. Foundations | Python, backend basics, data handling, math fundamentals | 6-8 weeks | CLI data pipeline |
| 2. Deep Learning | Train, debug, and evaluate neural networks | 6-10 weeks | Image classifier with failure analysis |
| 3. LLM Systems | RAG, evals, fine-tuning, agents, cost-aware design | 8-12 weeks | Production-style RAG system |
| 4. MLOps | Versioning, CI, monitoring, deployment | 6-8 weeks | Model deployment pipeline |
| 5. Specialisation | Healthcare, fintech, AI systems, or MLOps depth | 8+ weeks | Domain portfolio project |

## Resource Pages

- [Phase 1: Foundations](resources/phase-1-foundations.md)
- [Phase 2: Deep Learning](resources/phase-2-deep-learning.md)
- [Phase 3: LLMs](resources/phase-3-llms.md)
- [Phase 4: MLOps](resources/phase-4-mlops.md)
- [Phase 5: Specialisation](resources/phase-5-specialisation.md)

Each phase page includes what to learn, what to build, what to skip, and how to know you are ready to move on.

## Portfolio Templates

Use these templates when you want projects that prove practical engineering ability instead of only model training:

- [Healthcare AI Safety](portfolio-templates/healthcare-ai-safety.md)
- [Medical Image AI](portfolio-templates/medical-image-ai.md)
- [Production RAG](portfolio-templates/production-rag.md)
- [LLM Gateway](portfolio-templates/llm-gateway.md)
- [Fintech AI Compliance](portfolio-templates/fintech-ai-compliance.md)

## Related Starter Repositories

See [repos.md](repos.md) for companion starter projects that match the roadmap topics.

## What To Skip

- Passive course marathons with no shipped project.
- Notebook-only portfolios.
- Prompt engineering without evaluation.
- RAG demos without retrieval tests.
- Fine-tuning before you understand data quality and inference cost.
- Agents without logging, limits, and failure handling.

## Validate The Repo

Install test dependencies and run:

```bash
python scripts/validate_roadmap.py
python -m pytest
```

The validation script checks that the roadmap links, resource files, paper notes, and portfolio templates are present.
