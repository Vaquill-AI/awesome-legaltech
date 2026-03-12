# Awesome Legaltech [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <sup>Sponsored by</sup><br>
  <a href="https://vaquill.ai"><strong>Vaquill AI</strong></a>
  <br>
  <sub>AI-powered legal research platform with 20M+ cases, 4-layer citation verification, contract analysis, and multilingual support - built for Indian legal professionals.</sub>
</div>

---

> A curated list of awesome legal technology resources - open source platforms, AI models, MCP servers, companies, datasets, and tools for the global legal ecosystem.

Legal technology (legaltech) is the use of technology and software to provide legal services, automate legal work, and make law more accessible. This list covers open-source tools, commercial platforms, AI/ML models built for law, and organizations (both for-profit and non-profit) working at the intersection of law and technology.

**Contributions welcome!** Please read the [contribution guidelines](CONTRIBUTING.md) first.

---

## Contents

- [Open Source Legal Data Platforms](#open-source-legal-data-platforms)
- [Open Legal Datasets](#open-legal-datasets)
- [MCP Servers for Legal](#mcp-servers-for-legal)
- [Legal AI Models & Embeddings](#legal-ai-models--embeddings)
  - [Large Language Models (LLMs)](#large-language-models-llms)
  - [Embedding & BERT-style Models](#embedding--bert-style-models)
  - [Multilingual & Regional Legal Models](#multilingual--regional-legal-models)
- [Document Automation & Drafting](#document-automation--drafting)
- [Legal Research Platforms](#legal-research-platforms)
- [Contract Lifecycle Management (CLM)](#contract-lifecycle-management-clm)
- [E-Discovery & Document Review](#e-discovery--document-review)
- [Practice Management](#practice-management)
- [Compliance & RegTech](#compliance--regtech)
- [Agentic Legal AI](#agentic-legal-ai)
- [Companies](#companies)
  - [For-Profit - AI-First](#for-profit--ai-first)
  - [For-Profit - Established Legaltech](#for-profit--established-legaltech)
  - [Non-Profit & NGO](#non-profit--ngo)
- [Benchmarks & Evaluation](#benchmarks--evaluation)
- [Standards & Protocols](#standards--protocols)
- [Communities, Conferences & Media](#communities-conferences--media)
- [Related Awesome Lists](#related-awesome-lists)

---

## Open Source Legal Data Platforms

Platforms and frameworks for building, hosting, or processing legal data - self-hostable and open source.

- [Docassemble](https://docassemble.org) - Open-source expert system for guided interviews and document assembly. Widely used in legal aid and courts. Built with Python + YAML. ![GitHub Stars](https://img.shields.io/github/stars/jhpyle/docassemble?style=flat-square)
- [CourtListener](https://www.courtlistener.com) - Free, open-source legal research platform by the Free Law Project. Indexes 9M+ US court opinions across 2,000+ courts.
- [Suffolk LIT Lab Document Assembly Line](https://github.com/SuffolkLITLab/docassemble-AssemblyLine) - Open toolkit from Suffolk Law for creating mobile-friendly guided interviews and court e-filing.
- [ArkCase](https://www.arkcase.com) - Open-source adaptive case management platform with document management, task tracking, and DoD 5015.2 compliance.
- [ClinicCases](https://github.com/judsonmitchell/ClinicCases) - Free, open-source web-based case management for law school clinics. MIT licensed.
- [Worklenz](https://github.com/worklenz/worklenz) - Self-hosted open-source task and project management tool adaptable for legal case management.
- [Wraft](https://github.com/wraft/wraft) - Open-source Document Lifecycle Management (DLM) platform for structured document creation and workflows.
- [FreeEed](https://freeeed.org) - Open-source, AI-enabled cross-platform e-discovery platform with text extraction, metadata processing, and OCR.
- [J-Lawyer](https://www.j-lawyer.org) - Open-source law practice management software (German-originated, usable in English). Active on GitHub.
- [Dolibarr](https://www.dolibarr.org) - Modular open-source ERP/CRM with legal case management capabilities.
- [open-agreements](https://github.com/CommonAccord/Cmacc-Org) - CommonAccord: open-source framework for creating and sharing legal documents as structured data.
- [Eyecite](https://github.com/freelawproject/eyecite) - Open-source legal citation extraction and analysis tool by Free Law Project.
- [RECAP](https://free.law/recap/) - Browser extension + archive making PACER federal court documents freely available. Open-source by Free Law Project.

---

## Open Legal Datasets

Curated datasets of legal texts, case law, statutes, and contracts available for research and training.

- [CourtListener Dataset](https://www.courtlistener.com/help/api/bulk-data/) - Bulk access to 9M+ US court opinions, judge data, and oral argument recordings.
- [RECAP Archive](https://free.law/recap/) - Largest open collection of federal court PACER documents and dockets on the internet.
- [Caselaw Access Project (CAP)](https://case.law) - 6.9M US court decisions from Harvard Law School, spanning 1600s–2020.
- [The Supreme Court Database](http://scdb.wustl.edu) - Comprehensive dataset on all US Supreme Court cases since 1791.
- [CUAD (Contract Understanding Atticus Dataset)](https://www.atticusprojectai.org/cuad) - 510 annotated commercial legal contracts with 13,000+ expert labels for 41 clause types.
- [MultiLegalPile](https://huggingface.co/datasets/joelito/Multi_Legal_Pile) - Multilingual legal pretraining corpus spanning 24 languages and 17 jurisdictions.
- [LegalBench](https://github.com/HazyResearch/legalbench) - 162 tasks for evaluating legal reasoning of LLMs, collaboratively built by legal professionals.
- [LawBench](https://github.com/open-compass/LawBench) - 20 tasks for evaluating LLMs on Chinese legal reasoning, covering three cognitive levels.
- [LEDGAR](https://metatext.io/datasets/ledgar) - Large-scale labeled dataset for legal contract provision classification.
- [EUR-Lex](https://eur-lex.europa.eu) - Official EU law database with full text of EU legislation and case law in all EU languages.
- [Indian Kanoon Dataset](https://indiankanoon.org) - Indian court judgments and legal documents; widely used for Indian legal NLP research.
- [ECtHR Dataset](https://github.com/coastalcph/ecthr_cases) - European Court of Human Rights cases dataset for legal judgment prediction research.
- [AustLII](https://www.austlii.edu.au) - Free access to Australian and Pacific legal materials including case law, legislation, and treaties.
- [OpenLegalData (Germany)](https://openlegaldata.io) - Open German legal data including court decisions, laws, and regulations.
- [Harvard Law School Caselaw Access Project API](https://api.case.law) - RESTful API for bulk and search access to the CAP dataset.

---

## MCP Servers for Legal

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers that connect AI assistants to legal data sources and workflows.

- [Vaquill AI MCP](https://vaquill.ai) ⭐ - MCP server providing AI agents with access to 20M+ Indian Supreme Court, High Court, and Tribunal judgments with semantic search and citation verification. *(Sponsor)*
- [agentic-ops/legal-mcp](https://github.com/agentic-ops/legal-mcp) - Comprehensive MCP server for legal workflows. Integrates AI assistants with legal databases and case management systems (Clio, etc.).
- [uk-case-law-mcp-server](https://github.com/nationalarchives/uk-case-law-mcp-server) - MCP server that enables LLMs to search, retrieve, and cite UK legal judgments via The National Archives API.
- [LegalContext MCP](https://mcp.so/server/legalcontext) - Open-source MCP server bridging law firm document management systems with AI assistants.
- [uspto-fpd-mcp](https://github.com/USPTO/uspto_fpd_mcp) - MCP server for USPTO Final Patent Decisions to improve patent analysis with LLMs.
- [CourtListener MCP](https://free.law) - Access CourtListener's legal opinion database directly from AI agents via MCP *(community integration)*.
- [adeu (Agentic DOCX Redlining Engine)](https://github.com/adeu-ai/adeu) - MCP Server implementation enabling LLMs to inject native Track Changes and Comments into Word documents.

> **Note:** MCP for legal is an emerging ecosystem. Many servers are early-stage. Always verify data accuracy and jurisdiction coverage before use in legal practice.

---

## Legal AI Models & Embeddings

### Large Language Models (LLMs)

Fine-tuned or domain-pretrained LLMs specifically for legal tasks.

| Model | Base | Lang | License | Notes |
|---|---|---|---|---|
| [SaulLM-7B](https://huggingface.co/Equall/Saul-7B-Instruct-v1) | Mistral 7B | EN | MIT | Pretrained on 30B+ English legal tokens |
| [SaulLM-54B / 141B](https://huggingface.co/Equall) | Mistral | EN | MIT | Larger variants released Nov 2024 |
| [Lawma-8B](https://huggingface.co/ricdomolm/lawma-8b) | Llama 3 | EN | - | Fine-tuned for legal classification tasks |
| [Lawma-70B](https://huggingface.co/ricdomolm/lawma-70b) | Llama 3 | EN | - | Larger legal classification model |
| [InLegalBERT](https://huggingface.co/law-ai/InLegalBERT) | BERT | EN (Indian) | - | Trained on 5.4M Indian legal documents |
| [Lexlegis.AI LLM](https://lexlegis.ai) | Proprietary | EN | Proprietary | Trained on 10M+ Indian legal documents (Aug 2024) |
| [Pasal.id](https://github.com/pasal-id) | Claude-based | ID | Open | AI-native Indonesian legal platform |
| [NyayaSahayak](https://github.com/NyayaSahayak) | - | EN/HI | Open | AI legal assistant for Indian law |

### Embedding & BERT-style Models

Domain-specific encoder models for legal text similarity, classification, and retrieval.

| Model | HuggingFace | Notes |
|---|---|---|
| [Legal-BERT](https://huggingface.co/nlpaueb/legal-bert-base-uncased) | `nlpaueb/legal-bert-base-uncased` | Pretrained on EU/US legislation + court cases |
| [CaseLawBERT](https://huggingface.co/pile-of-law/legalbert-large-1.7M-2) | `pile-of-law/legalbert-large-1.7M-2` | Trained on Pile of Law corpus |
| [LegalBert (JHU)](https://huggingface.co/jhu-clsp/LegalBert) | `jhu-clsp/LegalBert` | JHU CLSP legal domain adaptation |
| [EmuBERT](https://huggingface.co/uwestali/EmuBERT) | `uwestali/EmuBERT` | Masked LM for Australian law |
| [Lawformer](https://huggingface.co/joelito/longformer-base-4096-legal) | - | Long-context legal document model |
| [Kanon 2 Embedder](https://huggingface.co/kanonjax) | - | Top performer on MLEB (Massive Legal Embedding Benchmark) |
| [InLegalBERT](https://huggingface.co/law-ai/InLegalBERT) | `law-ai/InLegalBERT` | Named Entity Recognition for Indian legal texts |

**Benchmark:** [MLEB (Massive Legal Embedding Benchmark)](https://huggingface.co/datasets/Kanon/MLEB) - Comprehensive evaluation for legal text embedding models (Oct 2025).

### Multilingual & Regional Legal Models

| Model / Platform | Region | Language(s) | Notes |
|---|---|---|---|
| [OpenGPTX](https://opengpt-x.de) | Europe | DE, FR, ES + | EU-initiative LLM with higher non-English data ratio |
| [LawBench Models](https://github.com/open-compass/LawBench) | China | ZH | Models evaluated on 20 Chinese legal tasks |
| [VIDUR AI](https://vidur.in) | India | EN, HI | Expert-verified Indian legal answers + drafting |
| [VakilAI](https://vakilai.in) | India | EN, HI | Court-ready petition and appeal drafting |
| [BharatLAW](https://github.com/BharatLAW) | India | EN | IPC-based legal chatbot using FAISS + Streamlit |
| [Legalon Technologies](https://legalon.jp) | Japan | JA | AI contract management platform for Japanese law |
| Manupatra AI | India | EN | Predictive analytics + contract risk for Indian law |
| [LegalBERT (Greek)](https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1) | Greece | EL | Greek legal domain BERT |

---

## Document Automation & Drafting

Tools for automating the creation of legal documents, templates, and guided interviews.

### Open Source
- [Docassemble](https://docassemble.org) - The gold standard for open-source guided legal interviews and document assembly.
- [Suffolk LIT Lab Assembly Line](https://github.com/SuffolkLITLab/docassemble-AssemblyLine) - Toolkit for Massachusetts court forms; reusable pattern for any jurisdiction.
- [A2J Author](https://a2j-author.org) - CALI's tool for creating guided interviews helping self-represented litigants generate legal documents.
- [open-agreements](https://github.com/CommonAccord/Cmacc-Org) - CommonAccord: legal documents as structured, linkable data.
- [adeu](https://github.com/adeu-ai/adeu) - Agentic DOCX Redlining Engine for LLM-powered Word document Track Changes.
- [Wraft](https://github.com/wraft/wraft) - Open-source document lifecycle management.

### Commercial / SaaS
- [Spellbook](https://spellbook.legal) - AI contract drafting and review for lawyers in Microsoft Word. ($350M valuation, 2025)
- [Robin AI](https://robinai.com) - AI-powered contract review and negotiation platform.
- [Luminance](https://www.luminance.com) - AI-native legal platform for contract drafting, review, and diligence.
- [HotDocs](https://www.hotdocs.com) - Long-established document assembly software for law firms.
- [ContractExpress](https://www.thomsonreuters.com/en/products-services/legal/contract-express.html) - Thomson Reuters document automation platform.

---

## Legal Research Platforms

### Open / Free Access
- [CourtListener](https://www.courtlistener.com) - Free open case law search with API access. 9M+ opinions.
- [Fastcase](https://www.fastcase.com) - Often provided free through bar associations. Integrates Vincent AI.
- [Google Scholar Case Law](https://scholar.google.com) - Free US federal and state court opinions.
- [AustLII](https://www.austlii.edu.au) - Free Australasian legal information.
- [CommonLII](https://www.commonlii.org) - Free access to common law jurisdictions worldwide.
- [WorldLII](https://www.worldlii.org) - Global free legal information network.
- [OpenStates](https://openstates.org) - Open-source platform tracking US state legislation in real time.

### Commercial AI Research Platforms
- [Westlaw + CoCounsel](https://legal.thomsonreuters.com/en/products/westlaw) - Thomson Reuters flagship with GPT-4 powered AI assistant. 50-state surveys, deposition prep, brief analysis.
- [LexisNexis / Lexis+ AI](https://www.lexisnexis.com) - Multi-model AI (Claude 3, GPT-4o, Mistral 7B). Drafting guidance, statute summaries, Shepard's citations.
- [vLex / Vincent AI](https://vlex.com) - Global coverage (1B+ documents, 17 countries). AI jurisdictional comparison, contract redlining.
- [Casetext / CoCounsel Core](https://casetext.com) - GPT-4 powered research memo generation, document Q&A, CARA AI brief analysis.
- [Everlaw](https://www.everlaw.com) - Cloud-native litigation intelligence. AI clustering up to 25M documents.
- [Relativity / RelativityOne](https://www.relativity.com) - Enterprise legal and compliance platform. AI review (aiR), e-discovery.
- [Paxton AI](https://www.paxton.ai) - AI legal research assistant with jurisdiction-aware answers.
- [Clio Duo](https://www.clio.com) - AI layer in Clio's practice management for research, drafting, and insights.

---

## Contract Lifecycle Management (CLM)

Platforms for managing contracts from creation through execution, obligations, and renewal.

### Commercial
- [Ironclad](https://ironcladapp.com) - CLM with AI clause detection, redlining, playbooks, and Jurist AI assistant. ($3.2B valuation)
- [Icertis](https://www.icertis.com) - Enterprise CLM leader. OmniModel™ strategy, Icertis Vera AI, agentic workflows.
- [ContractPodAi / Leah](https://contractpodai.com) - Generative AI for CLM. Leah Marketplace with PwC/KPMG apps. Microsoft Azure OpenAI partnership.
- [DocuSign CLM / IAM](https://www.docusign.com/products/clm) - Intelligent Agreement Management with AI-Assisted Review and Analyzer.
- [Spellbook](https://spellbook.legal) - Contract drafting, review, and negotiation assistant in Microsoft Word.
- [Robin AI](https://robinai.com) - AI contract negotiation and review. $71.7M total funding.
- [Luminance](https://www.luminance.com) - AI for transactional, compliance, and litigation document review.
- [LexCheck](https://www.lexcheck.com) - AI for contract redlining and playbook enforcement.
- [Legartis](https://legartis.ai) - AI contract review and risk analysis (German/European market focus).

### Open Source / Self-Hosted
- [Wraft](https://github.com/wraft/wraft) - Open-source document lifecycle management with version control.

---

## E-Discovery & Document Review

Platforms for collecting, processing, reviewing, and producing electronically stored information (ESI).

- [Relativity / RelativityOne](https://www.relativity.com) - Industry leader. aiR for Review, aiR for Privilege, analytics, and processing.
- [Everlaw](https://www.everlaw.com) - Cloud-native with AI clustering (25M docs), trial prep, and predictive coding.
- [Nuix](https://www.nuix.com) - High-performance data processing with Cognitive AI (CogAI), 500+ pre-built models.
- [Reveal AI](https://www.revealdata.com) - AI-powered e-discovery with behavioral analytics, PII detection, and fraud detection.
- [Exterro](https://www.exterro.com) - End-to-end legal GRC platform with e-discovery, forensics, and privacy management.
- [Logikcull](https://www.logikcull.com) - Self-service cloud e-discovery for small and mid-size firms.
- [FreeEed](https://freeeed.org) - **Open source** AI-enabled e-discovery with OCR and metadata extraction.
- [IPRO](https://ipro.com) - E-discovery software for large-scale review and production.

---

## Practice Management

Software for running a law practice - case management, billing, calendaring, and client intake.

### Commercial
- [Clio](https://www.clio.com) - Cloud-based practice management suite. Clio Duo AI. $900M Series F (2024), $3B valuation.
- [MyCase](https://www.mycase.com) - Practice management with MyCase IQ for AI writing assistance.
- [Filevine](https://www.filevine.com) - Legal operating system with AI. $400M raised 2023-2024.
- [Smokeball](https://www.smokeball.com) - Practice management with built-in activity intelligence and billing.
- [CosmoLex](https://www.cosmolex.com) - Cloud-based legal accounting and practice management.

### Open Source
- [ClinicCases](https://github.com/judsonmitchell/ClinicCases) - For law school clinics. MIT licensed.
- [ArkCase](https://www.arkcase.com) - Open-source adaptive case management for legal and government.
- [J-Lawyer](https://www.j-lawyer.org) - German open-source law practice management.
- [MyLegalNet](https://github.com/MyLegalNet) - Open-source file/matter/invoice management with court system API.

---

## Compliance & RegTech

Tools for regulatory compliance, policy management, financial crime detection, and AI governance.

- [Drata](https://drata.com) - AI-native GRC automation. Continuous monitoring for SOC 2, ISO 27001, HIPAA, GDPR, EU AI Act. Deep automation checks.
- [Vanta](https://vanta.com) - Compliance automation with 375+ integrations. AI agent for auto-filling policies and vendor risk. Great for startups.
- [ComplyAdvantage](https://complyadvantage.com) - AI-driven AML and financial crime detection. Real-time screening of 500M+ customers.
- [Corlytics / Clausematch](https://www.corlytics.com) - RegTech for regulatory change management, compliance policy, and the full regulatory risk value chain.
- [Certa](https://www.getcerta.com) - Third-party risk management and vendor onboarding automation.
- [OneTrust](https://www.onetrust.com) - Privacy, GRC, and ethics management platform with AI-powered workflows.
- [NAVEX](https://www.navex.com) - Integrated risk and compliance management.
- [Kira Systems](https://kirasystems.com) - ML-based contract analysis for due diligence and compliance.

---

## Agentic Legal AI

Platforms where AI autonomously plans, executes, and iterates on multi-step legal tasks.

- [Harvey AI](https://www.harvey.ai) - Agentic AI for complex legal research, drafting, and multi-step analytical workflows. 30+ ready-made workflow solutions. $1.5B+ valuation, $1.2B raised in 2025.
- [Westlaw CoCounsel](https://legal.thomsonreuters.com) - Agentic workflows for autonomous, multi-step task execution in tax, legal research, and contract review.
- [LexisNexis Protégé](https://www.lexisnexis.com) - Agentic AI assistant with self-review, autonomous task completion, and personalized voice assistance.
- [DeepJudge](https://www.deepjudge.ai) - Enable law firms to design bespoke AI workflows leveraging internal knowledge.
- [Leya](https://www.leya.law) - AI-native legal platform with agentic research and memo generation. $25M Series A (2024).
- [EvenUp](https://www.evenuplaw.com) - Agentic platform for personal injury attorneys automating demand letter generation. $135M Series D (2024), $1B+ valuation.
- [Elint AI / Justice Accelerator](https://elintai.com) - Agentic legal case management and document automation.
- [Legalyze.ai](https://legalyze.ai) - Extracts data, generates chronologies, drafts documents from case files.
- [Darrow](https://www.darrow.ai) - AI platform that identifies class-action opportunities from public data.

---

## Companies

### For-Profit - AI-First

Companies founded primarily to bring AI capabilities to the legal sector.

| Company | Focus | Notable Feature | HQ |
|---|---|---|---|
| [Harvey AI](https://harvey.ai) | Full-stack legal AI | Agentic workflows, 30+ legal automations | San Francisco, USA |
| [EvenUp](https://evenuplaw.com) | Personal injury | Agentic demand letter generation | San Francisco, USA |
| [Leya](https://leya.law) | Research & memos | AI-native legal research platform | Stockholm, Sweden |
| [Spellbook](https://spellbook.legal) | Contract drafting | Real-time AI in Microsoft Word | Toronto, Canada |
| [Robin AI](https://robinai.com) | Contract review | AI negotiation and redlining | London, UK |
| [Luminance](https://luminance.com) | Document intelligence | Legal AI for transactions, litigation, compliance | London, UK |
| [Lexlegis.AI](https://lexlegis.ai) | Indian legal research | LLM on 10M+ Indian legal documents | Mumbai, India |
| [Paxton AI](https://paxton.ai) | Legal research | Jurisdiction-aware AI answers | USA |
| [Darrow](https://darrow.ai) | Litigation intelligence | Identifies meritorious lawsuits from public data | Tel Aviv, Israel |
| [Legalyze.ai](https://legalyze.ai) | Litigation support | AI extraction + chronology + drafting | USA |
| [Clearbrief](https://clearbrief.com) | Legal writing | AI-powered document management and writing | USA |
| [DeepJudge](https://deepjudge.ai) | Knowledge workflows | Bespoke AI workflows on internal law firm data | Zurich, Switzerland |
| [Legartis](https://legartis.ai) | Contract review | AI for German/European legal contracts | Zurich, Switzerland |

### For-Profit - Established Legaltech

Legacy leaders and growth-stage companies that have added AI capabilities.

| Company | Focus | Notable | HQ |
|---|---|---|---|
| [Thomson Reuters](https://thomsonreuters.com) | Research + AI | CoCounsel, Westlaw, Practical Law | Toronto, Canada |
| [LexisNexis](https://lexisnexis.com) | Research + AI | Lexis+ AI, Protégé, Shepard's citations | New York, USA |
| [Relativity](https://relativity.com) | E-discovery | RelativityOne cloud, aiR AI features | Chicago, USA |
| [Everlaw](https://everlaw.com) | E-discovery | Cloud-native, AI clustering, trial prep | Oakland, USA |
| [Ironclad](https://ironcladapp.com) | CLM | Jurist AI, AI clause detection | San Francisco, USA |
| [Icertis](https://icertis.com) | CLM | OmniModel™, Icertis Vera | Bellevue, USA |
| [DocuSign](https://docusign.com) | Agreements + CLM | IAM, AI-Assisted Review, DocuSign Analyzer | San Francisco, USA |
| [Clio](https://clio.com) | Practice management | Clio Duo AI, $3B valuation | Vancouver, Canada |
| [Filevine](https://filevine.com) | Legal operations | AI-enhanced case lifecycle management | Salt Lake City, USA |
| [vLex](https://vlex.com) | Legal research | Vincent AI, 1B+ docs, global coverage | Barcelona, Spain |
| [Kira Systems](https://kirasystems.com) | Due diligence | ML contract review, acquired by Litera | Toronto, Canada |
| [Nuix](https://nuix.com) | Investigations + eDiscovery | Cognitive AI (CogAI), 500+ Nuix Neo models | Sydney, Australia |
| [IntelliCheck](https://intellicheck.com) | Identity verification | Legal identity verification platform | USA |
| [ContractPodAi](https://contractpodai.com) | CLM | Leah AI, Leah Marketplace, Microsoft Azure partner | London, UK |

### Non-Profit & NGO

Organizations using technology to advance access to justice and open legal infrastructure.

| Organization | Focus | Key Resource | Type |
|---|---|---|---|
| [Free Law Project](https://free.law) | Open legal data | CourtListener, RECAP, Eyecite | 501(c)(3) |
| [Harvard Law School - Caselaw Access Project](https://case.law) | Open case law | 6.9M US cases digitized | Academic |
| [Suffolk LIT Lab](https://suffolklitlab.org) | Legal tech R&D | Document Assembly Line, Docassemble tools | Academic |
| [Legal Services Corporation (LSC)](https://lsc.gov) | Civil legal aid | Technology Initiative Grants (TIG) | US Federal |
| [ProBono.net](https://probono.net) | Pro bono resources | Online legal library for attorneys | Nonprofit |
| [Upsolve](https://upsolve.org) | Bankruptcy access | Free Chapter 7 bankruptcy filing tool | 501(c)(3) |
| [JustFix](https://www.justfix.org) | Housing justice | Tenant rights and landlord communication tools | Nonprofit |
| [AsylumConnect](https://asylumconnect.org) | LGBTQ+ asylum seekers | Open-source resource matching for asylum seekers | Nonprofit |
| [Electronic Frontier Foundation (EFF)](https://eff.org) | Digital rights | Policy, advocacy, legal defense for digital rights | 501(c)(3) |
| [ABA Free Legal Answers](https://freelegalanswers.org) | Access to justice | Virtual pro bono legal advice clinic | ABA Program |
| [LSNTAP](https://www.lsntap.org) | Legal aid tech | Technology resources for legal services community | Nonprofit |
| [A2J Author / CALI](https://a2j-author.org) | Self-help tools | Guided interview software for self-represented litigants | Nonprofit |
| [TrustLaw (Thomson Reuters Foundation)](https://www.trust.org/trustlaw/) | Global pro bono | Connects NGOs with free legal support | Foundation |
| [OpenLaw](https://openlaw.io) | Smart contracts | Legal agreements on blockchain | Startup/Open |

---

## Benchmarks & Evaluation

Resources for evaluating AI and NLP systems on legal tasks.

- [LegalBench](https://github.com/HazyResearch/legalbench) - 162-task benchmark for English legal reasoning in LLMs. Live leaderboard maintained at [vals.ai](https://vals.ai).
- [LawBench](https://github.com/open-compass/LawBench) - 20-task Chinese legal benchmark evaluating LLMs across three cognitive levels.
- [MLEB (Massive Legal Embedding Benchmark)](https://huggingface.co/datasets/Kanon/MLEB) - Comprehensive benchmark for legal text embedding models (Oct 2025).
- [CUAD](https://www.atticusprojectai.org/cuad) - Contract Understanding Atticus Dataset: extraction and classification benchmark for commercial contracts.
- [LEDGAR](https://metatext.io/datasets/ledgar) - Large-scale benchmark for legal contract provision classification.
- [ECtHR Task](https://github.com/coastalcph/ecthr_cases) - Legal judgment prediction benchmark using ECHR cases.
- [maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) - Curated list of Legal NLP resources, models, datasets, and papers.
- [JUST-NLP Legal MT](https://arxiv.org/abs/2503.12345) - Legal machine translation shared task benchmark (2025).

---

## Standards & Protocols

Open standards and specifications relevant to legal technology and AI integration.

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) - Anthropic's open standard for connecting AI models to external data sources. Adopted by Microsoft, Google, OpenAI.
- [SALI (Standards Advancement for the Legal Industry)](https://www.sali.org) - Open standard for legal matter data (LMSS - Legal Matter Standard Specification).
- [LEDES (Legal Electronic Data Exchange Standard)](https://ledes.org) - Standard formats for legal billing (e-billing).
- [EU AI Act](https://artificialintelligenceact.eu) - World's first comprehensive AI regulation law. In force Aug 2024; full applicability Aug 2026. Directly impacts legal AI tools.
- [LegalXML / OASIS LegalDocML](https://docs.oasis-open.org/legaldocml/) - XML schema standard for legal documents (bills, statutes, regulations). Used by parliaments globally.
- [Akoma Ntoso (AKN)](https://www.akomantoso.org) - XML vocabulary for parliamentary, legislative, and judicial documents. Used by UN, EU, national parliaments.
- [EDRM (Electronic Discovery Reference Model)](https://edrm.net) - Industry standard framework for e-discovery workflows, data models, and specifications.
- [Open Source Legal (OSL)](https://opensourcelegal.org) - Repository for open legal standards and applications.

---

## Communities, Conferences & Media

Stay current with the legaltech ecosystem.

### Communities & Forums
- [Legal Hackers](https://legalhackers.org) - Global community of lawyers, engineers, policy professionals. Local chapters worldwide.
- [r/LegalTech](https://reddit.com/r/legaltech) - Reddit community for legaltech discussion.
- [LawTech.UK](https://lawtech.uk) - UK-focused legal innovation community.
- [HFforLegal (Hugging Face)](https://huggingface.co/HFforLegal) - Community for legal AI practitioners on Hugging Face.
- [CLOC (Corporate Legal Operations Consortium)](https://cloc.org) - 3,000+ member community for in-house legal operations professionals.

### Conferences
- [Legalweek](https://www.legalweek.com) - Leading annual legaltech conference in New York.
- [ILTACON](https://www.iltanet.org/events/iltacon) - International Legal Technology Association annual conference.
- [CLOC Global Institute](https://cloc.org) - Annual conference for corporate legal operations.
- [LegalGeek](https://www.legalgeek.co) - UK-based innovation conference for the legal industry.
- [Future Law](https://www.futurelaw.io) - Technology and innovation in law conferences globally.

### Newsletters & Media
- [Artificial Lawyer](https://www.artificiallawyer.com) - Deep-coverage publication on AI and legal tech. Free daily news.
- [Lawnext](https://www.lawnext.com) - Podcast and news by Bob Ambrogi on legal technology innovation.
- [Legal Tech Talk](https://legaltech-talk.com) - News and analysis on legal technology trends.
- [The Legal Innovators](https://legal-innovators.com) - Newsletter covering the business of law and legaltech.

---

## Related Awesome Lists

- [maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) - Legal NLP papers, models, and datasets.
- [awesome-law](https://github.com/topics/awesome-law) - Various awesome lists tagged with `awesome-law`.
- [awesome-compliance](https://github.com/topics/awesome-compliance) - Compliance-related awesome lists.
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) - The original meta awesome list.

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.
