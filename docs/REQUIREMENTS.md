# REQUIREMENTS.md

## Overview
The `ai-upgrade-path` platform is a continuous AI learning system designed to empower tech professionals with up-to-date, actionable knowledge in response to rapid advancements in artificial intelligence. This document outlines the functional, non-functional, and operational requirements for the initial production release (v1.0).

All requirements are grounded in the existing Axentx context, including available datasets (e.g., `conversations`, `query-resp`, `messages`), validated frameworks (vLLM, SGLang), and alignment with the existing portfolio to avoid duplication.

---

## Functional Requirements

**FR-1: Personalized Learning Path Generation**  
The system shall generate individualized learning paths for users based on:  
- Self-reported skill level (beginner, intermediate, advanced)  
- Role (e.g., ML engineer, data scientist, full-stack developer)  
- Learning goals (e.g., "master LLM fine-tuning", "understand AI safety")  
- Historical engagement data (if available)  
Paths must be updated weekly or upon detection of new relevant advancements.

**FR-2: Real-Time Content Ingestion from Verified Sources**  
The system shall ingest and process technical content from:  
- GitHub repositories (e.g., `vllm-project/vllm`, `sgl-project/sglang`)  
- Hacker News, Lemmy:programming, arXiv  
- Official documentation updates from major AI frameworks  
Content must be parsed, summarized, and tagged within 6 hours of publication.

**FR-3: Skill Gap Analysis Engine**  
The system shall compare user profiles against current industry trends derived from:  
- Job postings (scraped and anonymized)  
- Open-source contribution patterns  
- Axentx internal demand signals (from HR/BD queue)  
Output shall include a prioritized list of skills to acquire.

**FR-4: Community Knowledge Sharing Interface**  
The system shall support:  
- User-submitted learning summaries (text, code snippets)  
- Peer validation via upvotes and expert review tags  
- Integration with Axentx BRAIN (pgvector) to store and retrieve community contributions  
All submissions must be attributed and licensed under MIT or CC-BY-4.0.

**FR-5: Progress Tracking & Validation**  
The system shall:  
- Track user completion of learning modules  
- Offer micro-assessments (multiple choice, code exercises)  
- Issue verifiable skill badges stored on-chain (via Axentx validation layer)  
- Support export of achievement records in standard formats (JSON-LD, Open Badges)

**FR-6: AI-Generated Learning Materials**  
Using SGLang and vLLM:  
- Dynamically generate concise summaries of complex papers or releases  
- Create beginner-friendly analogies and diagrams (via text-to-image API)  
- Structure content into modular, testable units  
All generations must be grounded in source material and cite references.

---

## Non-Functional Requirements

**Performance**  
- Learning path generation: < 2 seconds response time for 95% of requests  
- Content ingestion pipeline: < 6-hour latency from source publish to availability  
- Support concurrent users: 10,000+ active sessions (simulated via load testing)

**Reliability**  
- 99.9% uptime for core API services (SLA enforced via monitoring)  
- Data backup: daily snapshots of user progress and community content  
- Failover: redundant processing queues for ingestion and generation pipelines

**Security**  
- Authentication: OAuth2 + GitHub login only (no password storage)  
- Data minimization: collect only role, skill level, goals, and engagement  
- All user data encrypted at rest (AES-256) and in transit (TLS 1.3)  
- No PII stored in Axentx BRAIN; anonymized embeddings only

**Scalability**  
- Modular microservices architecture (Kubernetes-native)  
- Auto-scaling for inference workloads (vLLM/SGLang pods)  
- Queue-based ingestion (Kafka or equivalent)

**Maintainability**  
- All services must have CI/CD via `arkashira` GitHub Actions  
- Logging: structured logs to centralized observability platform  
- Documentation: OpenAPI spec for all APIs, hosted via Redoc

---

## Constraints

- **No duplication**: Must not replicate content or functionality from existing Axentx portfolio items (e.g., no reimplementation of IPC or dev tooling tutorials unless directly tied to AI upskilling).  
- **Tech stack**: Must use vLLM for inference and SGLang for structured generation (per C. Frameworks).  
- **Data usage**: Only use datasets with compatible licenses (apache-2.0, mit, cc-by-4.0); auto dataset may be used with filtering for AI-relevant content.  
- **BRAIN integration**: All generated learning content and user progress summaries must be indexed in the shared pgvector BRAIN with metadata tags.  
- **Validation gate**: No feature ships without QA and reviewer approval; proof of demand required via HR/BD signal.

---

## Assumptions

- Users are technically proficient (developers, engineers, data scientists).  
- External APIs (GitHub, arXiv, HN) remain stable and accessible.  
- vLLM and SGLang support required structured output formats (e.g., JSON, YAML) for content generation.  
- Axentx BRAIN is available and writable via authenticated API.  
- Community contributions will be moderated via automated filters + reviewer agent gate.  
- Skill validation badges will be recognized by partner employers (via BD pipeline).
