# Product Requirements Document (PRD) – ai‑upgrade‑path

**Project**: ai‑upgrade‑path  
**Repository**: https://github.com/axentx/ai-upgrade-path  
**Owner**: Senior Product / Engineering Lead  
**Last Updated**: 2026‑06‑11  

---

## 1. Executive Summary  

ai‑upgrade‑path is a **continuous AI learning platform** that empowers software engineers, data scientists, and AI practitioners to stay current with the latest AI research, tools, and industry best‑practice. Leveraging Axentx’s shared knowledge base (pgvector) and the company’s high‑volume, high‑quality datasets, the platform delivers personalized learning paths, real‑time skill assessments, and a community‑driven ecosystem for knowledge exchange.

---

## 2. Problem Statement  

- **Rapid Technological Change**: AI research publishes new papers, frameworks, and models at a rate that outpaces traditional learning channels.  
- **Skill Gaps**: Developers often lack structured guidance to transition from legacy knowledge (e.g., classic ML) to cutting‑edge AI (e.g., LLMs, multimodal models).  
- **Fragmented Resources**: Existing learning resources are scattered across MOOCs, blogs, and corporate training, making it hard to curate a coherent, up‑to‑date curriculum.  
- **Retention & Engagement**: Without continuous reinforcement, developers lose momentum and fail to apply new skills in production.

---

## 3. Target Users  

| Persona | Role | Pain Points | Desired Outcomes |
|---------|------|-------------|------------------|
| **Senior Engineer** | Lead AI/ML Engineer | Needs quick updates on new frameworks, wants to mentor juniors. | Rapidly integrate new tech into projects, mentor team. |
| **Data Scientist** | Research & Production | Struggles to keep up with latest papers, wants practical implementation guidance. | Translate research into production code. |
| **AI Enthusiast** | Early‑Career Developer | Limited time, wants a structured learning path. | Build a portfolio of modern AI projects. |
| **Team Lead** | Technical Lead | Needs to assess team skill levels, plan training budgets. | Data‑driven training roadmap, measurable skill improvement. |

---

## 4. Goals & Success Metrics  

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Deliver Continuous Learning** | % of users completing at least 1 learning module per month | ≥ 70% |
| **Ensure Relevance** | Average time from publication to platform inclusion | ≤ 14 days |
| **Improve Skill Levels** | Pre‑/post‑assessment score improvement | ≥ 20% |
| **Foster Community** | Active community posts per 100 users | ≥ 5 |
| **Drive Retention** | Monthly active users (MAU) growth | 30% QoQ |
| **Validate ROI** | % of users who apply new skills in production | ≥ 50% |

---

## 5. Key Features (Prioritized)

| # | Feature | Description | Priority | Acceptance Criteria |
|---|---------|-------------|----------|---------------------|
| 1 | **Personalized Learning Path** | Uses user profile + skill assessment to recommend a sequence of modules (papers, tutorials, projects). | ★★★★★ | • Path adapts to skill gaps <br>• 90% of users follow at least 80% of recommended path |
| 2 | **Real‑time Knowledge Graph** | Integrates the shared BRAIN (pgvector) to surface the latest research, tools, and community discussions. | ★★★★★ | • New papers appear in the feed within 14 days <br>• 95% of recommended content is relevant |
| 3 | **Skill Assessment Engine** | Pre‑ and post‑module quizzes, coding challenges, and automated code review via vLLM inference. | ★★★★☆ | • Assessment accuracy ≥ 85% <br>• 80% of users complete both assessments |
| 4 | **Community Forum & Peer Review** | Threaded discussions, upvote system, and peer‑review of code snippets. | ★★★★☆ | • ≥ 5 community posts per 100 users <br>• 70% of posts receive constructive feedback |
| 5 | **Progress Dashboard** | Visual metrics (skill heatmap, streaks, badge system). | ★★★☆☆ | • Dashboard loads < 2 s <br>• 90% of users view dashboard ≥ once per week |
| 6 | **Content Curation Pipeline** | Automated ingestion of arXiv, ACL, NeurIPS, and GitHub releases; human curation for quality. | ★★★☆☆ | • 95% of curated content passes quality gates |
| 7 | **API for External Integrations** | Expose endpoints for LMS, CI/CD pipelines to fetch learning paths and assessments. | ★★☆☆☆ | • API uptime ≥ 99.9% <br>• 3rd‑party integrations in production |
| 8 | **Compliance & Licensing Layer** | Ensure all content respects licenses (Apache‑2.0, MIT, CC‑BY‑4.0). | ★★☆☆☆ | • No license violations in 90‑day audit |

---

##
