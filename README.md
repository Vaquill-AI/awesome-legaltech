# Awesome Legaltech [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <sup>Sponsored by</sup><br>
  <a href="https://vaquill.ai"><strong>Vaquill AI</strong></a>
  <br>
  <sub>AI-powered legal research platform with 20M+ cases, 4-layer citation verification, contract analysis, and multilingual support & Case Law APIs- built for legal professionals.</sub>
</div>

---

> A curated list of awesome legal technology resources - open source platforms, AI models, MCP servers, companies, datasets, and tools for the global legal ecosystem.

Legal technology (legaltech) is the use of technology and software to provide legal services, automate legal work, and make law more accessible. This list covers open-source tools, commercial platforms, AI/ML models built for law, and organizations (both for-profit and non-profit) working at the intersection of law and technology.

**Contributions welcome!** Please read the [contribution guidelines](CONTRIBUTING.md) first.

---

## Contents

- [Open Source Legal Data Platforms](#open-source-legal-data-platforms)
- [Open Legal Datasets](#open-legal-datasets)
- [Legal Data by Jurisdiction](#legal-data-by-jurisdiction)
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
- [Companies](#companies)
  - [For-Profit - AI-First](#for-profit--ai-first)
  - [For-Profit - Established Legaltech](#for-profit--established-legaltech)
  - [Non-Profit & NGO](#non-profit--ngo)
- [Foundational Research](#foundational-research)
- [Legal Ontologies & Knowledge Graphs](#legal-ontologies--knowledge-graphs)
- [Benchmarks & Evaluation](#benchmarks--evaluation)
- [Standards & Protocols](#standards--protocols)
- [Legaltech Directories & Product Listing Platforms](#legaltech-directories--product-listing-platforms)
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
- [Blackstone](https://github.com/ICLRandD/Blackstone) - 🇬🇧 spaCy NLP pipeline and model for unstructured UK legal text. Covers named entity recognition, sentence segmentation, and citation detection.
- [LegalCrawler](https://github.com/iliaschalkidis/LegalCrawler) - Scripts to crawl and build English legal corpora from public court and legislative websites.
- [Juriscraper](https://github.com/freelawproject/juriscraper) - 🇺🇸 Python library for scraping US court websites. Covers 400+ courts for opinions, oral arguments, and PACER data.
- [French Legal Case Anonymization](https://github.com/ELS-RD/anonymisation) - Open-source NER-based pseudo-anonymization of French court decisions (as required by French law).
- [Eyecite](https://github.com/freelawproject/eyecite) - Open-source legal citation extraction and analysis tool by Free Law Project.
- [RECAP](https://free.law/recap/) - Browser extension + archive making PACER federal court documents freely available. Open-source by Free Law Project.

---

## Open Legal Datasets

Curated datasets of legal texts, case law, statutes, and contracts - organized by task. Most are openly available for research.

### Pretraining Corpora

Large text corpora for pretraining or fine-tuning legal language models.

| Dataset | Lang | Size | Notes |
|---|---|---|---|
| [Pile of Law](https://huggingface.co/datasets/pile-of-law/pile-of-law) | 🇺🇸 EN | ~256 GB | US legal and administrative text; used to train CaseLawBERT |
| [MultiLegalPile](https://huggingface.co/datasets/joelito/Multi_Legal_Pile) | 🌍 24 langs | 689 GB | Multilingual legal pretraining corpus from 17 jurisdictions |
| [Indian Kanoon Dataset](https://indiankanoon.org) | 🇮🇳 EN | Large | Indian court judgments and statutes; widely used for Indian legal NLP |
| [EUR-Lex](https://eur-lex.europa.eu) | 🇪🇺 24 langs | Large | Official EU legislation and case law in all EU official languages |

### Legal Judgment Prediction (LJP)

Datasets for predicting case outcomes, charges, or penalties from court documents.

| Dataset | Jurisdiction | Lang | Size | Task |
|---|---|---|---|---|
| [CAIL2018](https://github.com/china-ai-law-challenge/CAIL2018) | 🇨🇳 China | ZH | 2.6M cases | Charge, penalty, article prediction |
| [ECtHR Dataset](https://github.com/coastalcph/ecthr_cases) | 🇪🇺 ECHR | EN | 11K cases | Article violation prediction |
| [FSCS - Swiss Judgment Prediction](https://huggingface.co/datasets/swiss_judgment_prediction) | 🇨🇭 Switzerland | DE/FR/IT | 85K cases | Binary outcome prediction across 3 languages |
| [CaseSumm](https://huggingface.co/datasets/ChicagoHAI/CaseSumm) | 🇺🇸 US SCOTUS | EN | 25.6K opinions | Paired opinions + official syllabuses |
| [IndianBailJudgments-1200](https://huggingface.co/datasets/SnehaDeshmukh/IndianBailJudgments-1200) | 🇮🇳 India | EN | 1.2K judgments | Bail decisions with 20+ structured attributes |
| [The Supreme Court Database](http://scdb.wustl.edu) | 🇺🇸 US | EN | All SCOTUS cases since 1791 | Votes, outcomes, justice ideology |

### Legal Text Classification

| Dataset | Jurisdiction | Lang | Notes |
|---|---|---|---|
| [LexGLUE](https://github.com/coastalcph/lex-glue) | 🌍 Multi | EN | 7-task benchmark: EURLEX, ECHR, LEDGAR, SCOTUS, ContractNLI, CaseHOLD, ECtHR |
| [MultiEURLEX](https://huggingface.co/datasets/multi_eurlex) | 🇪🇺 EU | 23 langs | 65K EU laws with 4.5K labels; multilingual classification |
| [LEDGAR](https://huggingface.co/datasets/coastalcph/ledgar) | 🇺🇸 US | EN | 60K+ contract provisions with 12.6K labels |
| [CUAD](https://www.atticusprojectai.org/cuad) | 🇺🇸 US | EN | 510 annotated contracts, 41 clause types, 13K+ expert labels |

### Legal Question Answering

| Dataset | Jurisdiction | Lang | Notes |
|---|---|---|---|
| [CaseHOLD](https://huggingface.co/datasets/casehold/casehold) | 🇺🇸 US | EN | 53K multiple-choice QA from US case law (holding identification) |
| [COLIEE](https://coliee.org) | 🇨🇦 🇯🇵 EN/JA | EN | Annual competition: statute retrieval, entailment, QA (Canadian + Japanese law) |
| [JEC-QA](https://jecqa.thunlp.org) | 🇨🇳 China | ZH | 26K Chinese bar exam questions for legal reasoning |
| [GerLayQA](https://github.com/lavis-nlp/GerLayQA) | 🇩🇪 Germany | DE | German legal QA from layperson questions and expert answers |

### Legal Summarization

| Dataset | Jurisdiction | Lang | Notes |
|---|---|---|---|
| [BillSum](https://github.com/FiscalNote/BillSum) | 🇺🇸 US | EN | 22K US Congressional and California bill summaries |
| [EUR-Lex Sum](https://huggingface.co/datasets/dennlinger/eur-lex-sum) | 🇪🇺 EU | 24 langs | Abstractive summarization of EU legislation; 1.5K+ docs |
| [Multi-LexSum](https://github.com/multilexsum/dataset) | 🇺🇸 US | EN | Multi-document summarization of US civil rights court cases |

### Contract Analysis

| Dataset | Jurisdiction | Lang | Notes |
|---|---|---|---|
| [CUAD](https://www.atticusprojectai.org/cuad) | 🇺🇸 US | EN | See Classification section. Gold standard for contract clause extraction. |
| [MAUD](https://github.com/TheAtticusProject/maud) | 🇺🇸 US | EN | M&A contract understanding; 39K questions on merger agreements |
| [ContractNLI](https://stanfordnlp.github.io/contract-nli/) | 🌍 | EN | Natural language inference over non-disclosure agreements |

### Open Datasets by Jurisdiction

See also [Legal Data by Jurisdiction](#legal-data-by-jurisdiction) for country-specific portals.

- [CourtListener Dataset](https://www.courtlistener.com/help/api/bulk-data/) - 🇺🇸 9M+ US court opinions, judge data, oral argument recordings. [See also: Legal Research Platforms]
- [RECAP Archive](https://free.law/recap/) - 🇺🇸 Largest open collection of US federal PACER documents and dockets.
- [Caselaw Access Project (CAP)](https://case.law) - 🇺🇸 6.9M US court decisions from Harvard Law School, 1600s-2020.
- [OpenLegalData (Germany)](https://openlegaldata.io) - 🇩🇪 German court decisions, laws, and regulations.
- [LegalBench](https://github.com/HazyResearch/legalbench) - 🇺🇸 162 tasks for benchmarking LLM legal reasoning. [See also: Benchmarks]
- [LawBench](https://github.com/open-compass/LawBench) - 🇨🇳 20 tasks for benchmarking LLMs on Chinese legal reasoning. [See also: Benchmarks]

---

## Legal Data by Jurisdiction

Country-specific legal databases, portals, and open data sources.

### United States
- [PACER](https://pacer.uscourts.gov) - Official US federal court docket and document system.
- [CourtListener](https://www.courtlistener.com) - 9M+ opinions across 2,000+ US courts. Free API.
- [Caselaw Access Project](https://case.law) - 6.9M US court decisions, 1600s-2020. Free bulk API.
- [GovInfo](https://www.govinfo.gov) - US federal legislation, regulations, and congressional records. Free and open.
- [OpenStates](https://openstates.org) - US state legislation tracked in real time.

### United Kingdom
- [BAILII](https://www.bailii.org) - Free access to British and Irish primary legal materials including case law and legislation.
- [UK National Archives / Find Case Law](https://caselaw.nationalarchives.gov.uk) - Official UK court decisions from 2001. Open API available.
- [legislation.gov.uk](https://www.legislation.gov.uk) - Full text of UK Acts of Parliament, statutory instruments. Open data with API.

### European Union
- [EUR-Lex](https://eur-lex.europa.eu) - Official EU law portal. All EU legislation, case law, and treaty texts in 24 languages.
- [ECLI (European Case Law Identifier)](https://e-justice.europa.eu/content_european_case_law_identifier_ecli-175-en.do) - Standardized identifier and search for courts across EU member states.

### Germany
- [OpenJur](https://openjur.de) - Open-source database of German court decisions. Community-maintained.
- [OpenLegalData](https://openlegaldata.io) - German court decisions and legislation. REST API available.
- [Gesetze im Internet](https://www.gesetze-im-internet.de) - Official German federal law portal (all statutes). Free.

### France
- [Legifrance](https://www.legifrance.gouv.fr) - Official French legal portal. All statutes, regulations, and major court decisions.
- [Judilibre (Cour de Cassation)](https://www.courdecassation.fr/acces-rapide/judiciaire-judilibre) - Open API for French Supreme Court (Cour de Cassation) decisions. GDPR-anonymized.

### Brazil
- [LexML Brasil](https://www.lexml.gov.br) - Federated search over Brazilian legislation and legal documents. Open standards.
- [STF Jurisprudencia](https://portal.stf.jus.br/jurisprudencia/) - Brazilian Supreme Court (STF) decisions portal.
- [CNJ Dados Abertos](https://www.cnj.jus.br/sistemas/dadosabertos/) - National Council of Justice open judicial data and indicators.
- [Jusbrasil](https://www.jusbrasil.com.br) - Large legal search platform covering cases, legislation, and gazettes. Free + commercial tiers.

### India
- [Indian Kanoon](https://indiankanoon.org) - Free access to Indian court judgments, statutes, and legal documents.
- [Supreme Court of India](https://main.sci.gov.in) - Official portal with judgments from the Supreme Court of India.
- [eCourts Services](https://services.ecourts.gov.in) - Unified portal for Indian district and High Court case status and documents.

### China
- [China Judgments Online (Wenshu)](https://wenshu.court.gov.cn) - Official Chinese court judgment database. 140M+ decisions.
- [PKU LawInfo (Peking University)](https://law.pku.edu.cn/lawen/) - Comprehensive Chinese laws and regulations database.

### Japan
- [Courts of Japan (Legal Database)](https://www.courts.go.jp/english/judgments/index.html) - Supreme Court and High Court decisions in English and Japanese.
- [e-GOV Law Search](https://laws.e-gov.go.jp) - Official Japanese legislation portal. API available.

### Australia & New Zealand
- [AustLII](https://www.austlii.edu.au) - Free access to Australian and Pacific legal materials including case law, legislation, and treaties.
- [Open Australian Legal Corpus](https://huggingface.co/datasets/umarbutler/open-australian-legal-corpus) - First open multijurisdictional corpus of Australian legislative and judicial documents.

### South Korea
- [Supreme Court of Korea Legal Research Institute](https://glaw.scourt.go.kr) - Korean court decisions and statutes, with English summaries for major cases.

### Israel
- [Nevo Legal Database](https://www.nevo.co.il) - Major Israeli legal database covering legislation, regulations, and court decisions. Commercial.

---

## MCP Servers for Legal

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers that connect AI assistants to legal data sources and workflows.

- [Vaquill AI MCP](https://vaquill.ai) - MCP server providing AI agents with access to 20M+ Indian Supreme Court, High Court, and Tribunal judgments with semantic search and citation verification. *(Sponsor)*
- [agentic-ops/legal-mcp](https://github.com/agentic-ops/legal-mcp) - Comprehensive MCP server for legal workflows. Integrates AI assistants with legal databases and case management systems (Clio, etc.).
- [uk-case-law-mcp-server](https://github.com/nationalarchives/uk-case-law-mcp-server) - MCP server that enables LLMs to search, retrieve, and cite UK legal judgments via The National Archives API.
- [LegalContext MCP](https://mcp.so/server/legalcontext) - Open-source MCP server bridging law firm document management systems with AI assistants.
- [uspto-fpd-mcp](https://github.com/USPTO/uspto_fpd_mcp) - MCP server for USPTO Final Patent Decisions to improve patent analysis with LLMs.
- [CourtListener MCP](https://free.law) - Access CourtListener's legal opinion database directly from AI agents via MCP *(community integration)*.
- [adeu (Agentic DOCX Redlining Engine)](https://github.com/dealfluence/adeu) - MCP Server enabling LLMs to inject native Track Changes and Comments into Word documents.

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
| [Pasal.id](https://github.com/ilhamfp/pasal) | Claude + RAG | ID | Open | RAG-powered access to 40,000+ Indonesian regulations via Claude AI |
| [NyayaSahayak](https://github.com/SoulNoob/Nyaysahayak) | - | EN/HI | Open | AI legal assistant covering Indian Constitution, BNS 2023, IT Act |
| [ChatLaw](https://github.com/PKU-YuanGroup/ChatLaw) | LLaMA/Ziya | ZH | CC BY-NC | Chinese legal LLM from Peking University; trained on 30K+ Chinese legal datasets |
| [DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM) | Baichuan 13B | ZH | Apache 2.0 | Chinese legal assistant from Fudan; legal retrieval + reasoning |

### Embedding & BERT-style Models

Domain-specific encoder models for legal text similarity, classification, and retrieval.

| Model | HuggingFace | Notes |
|---|---|---|
| [Legal-BERT](https://huggingface.co/nlpaueb/legal-bert-base-uncased) | `nlpaueb/legal-bert-base-uncased` | Pretrained on EU/US legislation + court cases |
| [CaseLawBERT](https://huggingface.co/pile-of-law/legalbert-large-1.7M-2) | `pile-of-law/legalbert-large-1.7M-2` | Trained on Pile of Law corpus |
| [LegalBert (JHU)](https://huggingface.co/jhu-clsp/LegalBert) | `jhu-clsp/LegalBert` | JHU CLSP legal domain adaptation |
| [EmuBERT](https://huggingface.co/isaacus/EmuBERT) | `isaacus/EmuBERT` | RoBERTa-based model for Australian law; 1.4B tokens across 6 jurisdictions |
| [Lawformer](https://huggingface.co/joelito/longformer-base-4096-legal) | - | Long-context legal document model |
| [Kanon 2 Embedder](https://huggingface.co/isaacus/kanon-2) | `isaacus/kanon-2` | #1 on MLEB benchmark; legal semantic search + RAG; 16K token context |

**Benchmark:** [MLEB (Massive Legal Embedding Benchmark)](https://huggingface.co/datasets/Kanon/MLEB) - Comprehensive evaluation for legal text embedding models (Oct 2025).

### Multilingual & Regional Legal Models

| Model / Platform | Region | Language(s) | Notes |
|---|---|---|---|
| [OpenGPT-X / Teuken-7B](https://opengpt-x.de) | Europe | All 24 EU langs | German-funded initiative; produced Teuken-7B LLM covering all official EU languages |
| [LawBench Models](https://github.com/open-compass/LawBench) | China | ZH | Models evaluated on 20 Chinese legal tasks |
| [VakilAI](https://vakilai.in) | India | EN, HI | Court-ready petition and appeal drafting |
| [BharatLAW](https://github.com/BharatLAW) | India | EN | IPC-based legal chatbot using FAISS + Streamlit |
| [Legalon Technologies](https://legalon.jp) | Japan | JA | AI contract management platform for Japanese law |
| [LegalBERT (Greek)](https://huggingface.co/nlpaueb/bert-base-greek-uncased-v1) | Greece | EL | Greek legal domain BERT |

---

## Document Automation & Drafting

Tools for automating the creation of legal documents, templates, and guided interviews.

### Open Source
- [Docassemble](https://docassemble.org) - The gold standard for open-source guided legal interviews and document assembly.
- [Suffolk LIT Lab Assembly Line](https://github.com/SuffolkLITLab/docassemble-AssemblyLine) - Toolkit for Massachusetts court forms; reusable pattern for any jurisdiction.
- [A2J Author](https://a2j-author.org) - CALI's tool for creating guided interviews helping self-represented litigants generate legal documents.
- [open-agreements](https://github.com/CommonAccord/Cmacc-Org) - CommonAccord: legal documents as structured, linkable data.
- [adeu](https://github.com/dealfluence/adeu) - Agentic DOCX Redlining Engine for LLM-powered Word document Track Changes.
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
- [CourtListener](https://www.courtlistener.com) - Free open case law search with API access. 9M+ opinions. [Bulk data API](https://www.courtlistener.com/help/api/bulk-data/) available.
- [Juriscraper](https://github.com/freelawproject/juriscraper) - Open-source Python library for scraping American court websites for opinions, oral arguments, and PACER data.
- [PACER](https://pacer.uscourts.gov) - Official US federal court docket and document system. Source of all federal case filings.
- [Fastcase](https://www.fastcase.com) - Often provided free through bar associations. Integrates Vincent AI.
- [Google Scholar Case Law](https://scholar.google.com) - Free US federal and state court opinions.
- [AustLII](https://www.austlii.edu.au) - Free Australasian legal information.
- [CommonLII](https://www.commonlii.org) - Free access to common law jurisdictions worldwide.
- [WorldLII](https://www.worldlii.org) - Global free legal information network.
- [OpenStates](https://openstates.org) - Open-source platform tracking US state legislation in real time.

### Commercial AI Research Platforms
- [Vaquill AI](https://vaquill.ai) - AI-native Indian legal research platform with agentic research workflows, persistent memory, MCP server, proprietary database of 20M+ original SC/HC/Tribunal judgments and dockets, contract analysis, and multilingual support. *(Sponsor)*
- [Westlaw + CoCounsel](https://legal.thomsonreuters.com/en/products/westlaw) - Thomson Reuters flagship with GPT-4 powered AI assistant. 50-state surveys, deposition prep, brief analysis.
- [Bloomberg Law](https://pro.bloomberglaw.com) - Major US legal research platform with AI-powered brief analysis, docket tracking, real-time legislative monitoring, and transactional tools.
- [LexisNexis / Lexis+ AI](https://www.lexisnexis.com) - Multi-model AI (Claude 3, GPT-4o, Mistral 7B). Drafting guidance, statute summaries, Shepard's citations.
- [vLex / Vincent AI](https://vlex.com) - Global coverage (1B+ documents, 17 countries). AI jurisdictional comparison, contract redlining.
- [Casetext / CoCounsel Core](https://casetext.com) - GPT-4 powered research memo generation, document Q&A, CARA AI brief analysis.
- [Lex Machina](https://lexmachina.com) - Thomson Reuters litigation analytics platform. Predicts outcomes and benchmarks opposing counsel using federal court data.
- [Docket Alarm](https://www.docketalarm.com) - Federal and state docket monitoring + analytics platform. Real-time alerts on new filings.
- [Paxton AI](https://www.paxton.ai) - AI legal research assistant with jurisdiction-aware answers.
- [VIDUR AI](https://vidur.in) - AI research platform for Indian corporate, tax, and regulatory law. Integrates knowledge from 250+ specialists and major publishers.
- [Manupatra](https://www.manupatra.com) - Proprietary Indian legal database covering Supreme Court, High Courts, and Tribunals. Includes analytics, case tracking, and contract tools.

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
- [LawGeex](https://www.lawgeex.com) - AI contract review platform; pre-screens contracts against company policies before legal review.
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

---

## Companies

### For-Profit - AI-First

Companies founded primarily to bring AI capabilities to the legal sector. **Agentic** = platform supports autonomous multi-step AI task execution.

| Company | Focus | Agentic | Notable Feature | HQ |
|---|---|---|---|---|
| [Harvey AI](https://harvey.ai) | Full-stack legal AI | Yes | 30+ autonomous workflow solutions; $8B valuation, $818M raised 2025 | San Francisco, USA |
| [Legora](https://legora.com) | Collaborative legal AI | Yes | YC-backed; collaborative AI workspace for legal research, drafting, and review; $816M total raised, $5.55B valuation (2026) | Stockholm, Sweden |
| [EvenUp](https://evenuplaw.com) | Personal injury | Yes | Agentic demand letter generation; $1B+ valuation | San Francisco, USA |
| [Leya](https://leya.law) | Research & memos | Yes | Agentic research and memo generation; $25M Series A | Stockholm, Sweden |
| [Eudia](https://eudia.com) | In-house corporate legal | Yes | AI agents for Fortune 500 legal teams; $105M Series A (General Catalyst, 2025) | USA |
| [Blue J](https://bluej.com) | Tax research AI | No | AI-powered answers to complex US/Canada/UK tax questions; $122M Series D (2025) | Toronto, Canada |
| [Spellbook](https://spellbook.legal) | Contract drafting | No | Real-time AI drafting in Microsoft Word | Toronto, Canada |
| [Robin AI](https://robinai.com) | Contract review | No | AI negotiation and redlining; $71.7M raised | London, UK |
| [Luminance](https://luminance.com) | Document intelligence | No | Transactions, litigation, compliance review | London, UK |
| [Lexlegis.AI](https://lexlegis.ai) | Indian legal research | No | LLM on 10M+ Indian legal documents | Mumbai, India |
| [Paxton AI](https://paxton.ai) | Legal research | No | Jurisdiction-aware AI answers | USA |
| [Darrow](https://darrow.ai) | Litigation intelligence | Yes | Identifies meritorious lawsuits from public data | Tel Aviv, Israel |
| [Legalyze.ai](https://legalyze.ai) | Litigation support | Yes | AI extraction + chronology + drafting | USA |
| [Clearbrief](https://clearbrief.com) | Legal writing | No | AI-powered factual verification in briefs | USA |
| [DeepJudge](https://deepjudge.ai) | Knowledge workflows | Yes | Bespoke AI workflows on internal law firm data | Zurich, Switzerland |
| [Legartis](https://legartis.ai) | Contract review | No | AI for German/European legal contracts | Zurich, Switzerland |
| [Elint AI / Justice Accelerator](https://elint.in) | Court tech | No | AI + blockchain case management for courts/ADR | India/UAE |

### For-Profit - Established Legaltech

Legacy leaders and growth-stage companies that have added AI capabilities.

| Company | Focus | Notable | HQ |
|---|---|---|---|
| [Thomson Reuters](https://thomsonreuters.com) | Research + AI | CoCounsel, Westlaw, Practical Law, Lex Machina | Toronto, Canada |
| [LexisNexis](https://lexisnexis.com) | Research + AI | Lexis+ AI, Protégé, Shepard's citations | New York, USA |
| [Relativity](https://relativity.com) | E-discovery | RelativityOne cloud, aiR for Review/Privilege | Chicago, USA |
| [Everlaw](https://everlaw.com) | E-discovery | Cloud-native, AI clustering, trial prep | Oakland, USA |
| [Ironclad](https://ironcladapp.com) | CLM | Jurist AI, AI clause detection | San Francisco, USA |
| [Icertis](https://icertis.com) | CLM | OmniModel™, Icertis Vera | Bellevue, USA |
| [DocuSign](https://docusign.com) | Agreements + CLM | IAM, AI-Assisted Review, DocuSign Analyzer | San Francisco, USA |
| [Clio](https://clio.com) | Practice management | Clio Duo AI, $3B valuation | Vancouver, Canada |
| [Filevine](https://filevine.com) | Legal operations | AI-enhanced case lifecycle management | Salt Lake City, USA |
| [Mitratech](https://mitratech.com) | Legal ops + CLM | Enterprise-scale matter management, TeamConnect, TAP Workflow Automation | Austin, USA |
| [vLex](https://vlex.com) | Legal research | Vincent AI, 1B+ docs, global coverage | Barcelona, Spain |
| [Litera](https://litera.com) | Doc tools + due diligence | Acquired Kira Systems; document drafting, proofreading, and deal management suite | Chicago, USA |
| [NetDocuments](https://netdocuments.com) | Cloud DMS | Leading cloud document management system for law firms; AI-powered search and organization | Lehi, USA |
| [HighQ (Thomson Reuters)](https://legal.thomsonreuters.com/en/products/highq) | Legal collaboration | Secure client portals, matter management, and workflow automation for law firms | London, UK |
| [Nuix](https://nuix.com) | Investigations + eDiscovery | Cognitive AI (CogAI), 500+ Nuix Neo models | Sydney, Australia |
| [ContractPodAi](https://contractpodai.com) | CLM | Leah AI, Leah Marketplace, Microsoft Azure partner | London, UK |
| [Lexion](https://lexion.ai) | AI CLM | AI-powered contract management backed by Google Ventures; 90% faster contract review | Seattle, USA |
| [Juro](https://juro.com) | Contract management | All-in-one contract platform popular in UK/EU; native browser editor with AI assistance | London, UK |
| [Avvoka](https://avvoka.com) | Contract automation | UK-based document automation and negotiation platform used by top-tier law firms | London, UK |

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
| [OpenLaw / Tribute Labs](https://openlaw.io) | Smart contracts | Blockchain-based legal agreements on Ethereum; rebranded as Tribute Labs (DAO incubator) in 2021 | Startup/Open |

## Foundational Research

Seminal papers that shaped the field of legal AI and NLP. Essential reading for anyone building in this space.

| Paper | Year | What it introduced |
|---|---|---|
| [LEGAL-BERT: The Muppets straight out of Law School](https://arxiv.org/abs/2010.02559) | 2020 | First large-scale BERT models pretrained on EU/US legal text; established the domain-adaptation benchmark for legal NLP |
| [LexGLUE: A Benchmark Dataset for Legal Language Understanding](https://arxiv.org/abs/2110.00976) | 2022 | 7-task legal NLP benchmark; the "GLUE for law"; drove standardized evaluation |
| [LegalBench: A Collaboratively Built Benchmark for Legal Reasoning](https://arxiv.org/abs/2308.11462) | 2023 | 162-task benchmark built with practicing lawyers; most comprehensive LLM legal evaluation to date |
| [GPT-4 Passes the Bar Exam](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233) | 2023 | Bommarito & Katz; showed LLMs can pass professional licensing exams; catalyzed investor and legal community attention |
| [SaulLM-7B: A pioneering Large Language Model for Law](https://arxiv.org/abs/2403.03883) | 2024 | First open-weight LLM continually pretrained on 30B+ legal tokens with instruction tuning |
| [MultiLegalPile: A 689GB Multilingual Legal Corpus](https://aclanthology.org/2024.acl-long.805/) | 2024 | Largest open multilingual legal pretraining dataset; 24 languages, 17 jurisdictions |
| [Artificial Intelligence and Legal Analytics](https://www.cambridge.org/core/books/artificial-intelligence-and-legal-analytics/E7D705EEF392501A1DB180645917E7E0) | 2017 | Kevin Ashley; foundational textbook on AI and law; covers case-based reasoning, argument mining, and legal knowledge representation |

---

## Legal Ontologies & Knowledge Graphs

Structured vocabularies, ontologies, and knowledge graphs for representing legal concepts, relationships, and document structure.

- [EuroVoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) - EU's multilingual thesaurus covering subjects of EU legislation. 7,000+ concepts in 24 languages. Used for tagging EUR-Lex documents.
- [LKIF-Core](https://github.com/RinkeHoekstra/lkif-core) - Legal Knowledge Interchange Format; OWL ontology for basic legal concepts (norms, agents, documents, time). Foundation for many legal knowledge systems.
- [SALI LMSS (Legal Matter Standard Specification)](https://www.sali.org) - Structured ontology for legal matter types, service types, and industry codes. Open standard for legal operations data.
- [LegalDocML / Akoma Ntoso](https://www.un.org/dgacm/en/content/akoma-ntoso) - XML + ontology for legislative and judicial document structure. Adopted by the UN, EU Parliament, national parliaments.
- [JurWordNet](https://github.com/fcroce/JurWordNet) - Legal extension of WordNet with Italian legal terminology; one of the few legal lexical ontologies in a non-English language.
- [Wikidata Legal Entities](https://www.wikidata.org/wiki/Wikidata:WikiProject_Law) - WikiProject Law: structured data on courts, cases, legislation, and legal concepts in Wikidata. Machine-readable and freely licensed.
- [PROLEG (Japanese Legal Ontology)](https://www.nii.ac.jp/en/fellows/satoh/) - Formal representation of Japanese civil law rules for logic-based legal reasoning. Developed at NII Tokyo.

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
- [JUST-NLP 2025 Legal MT](https://codabench.org/competitions/3682/) - English-to-Hindi legal machine translation shared task benchmark; workshop at IJCNLP-AACL 2025.

---

## Standards & Protocols

Open standards and specifications relevant to legal technology and AI integration.

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) - Anthropic's open standard for connecting AI models to external data sources. Adopted by Microsoft, Google, OpenAI.
- [SALI (Standards Advancement for the Legal Industry)](https://www.sali.org) - Open standard for legal matter data (LMSS - Legal Matter Standard Specification).
- [LEDES (Legal Electronic Data Exchange Standard)](https://ledes.org) - Standard formats for legal billing (e-billing).
- [EU AI Act](https://artificialintelligenceact.eu) - World's first comprehensive AI regulation law. In force Aug 2024; full applicability Aug 2026. Directly impacts legal AI tools.
- [LegalXML / OASIS LegalDocML](https://docs.oasis-open.org/legaldocml/) - XML schema standard for legal documents (bills, statutes, regulations). Used by parliaments globally.
- [Akoma Ntoso (AKN)](https://www.un.org/dgacm/en/content/akoma-ntoso) - XML vocabulary for parliamentary, legislative, and judicial documents. Used by UN, EU, and national parliaments.
- [EDRM (Electronic Discovery Reference Model)](https://edrm.net) - Industry standard framework for e-discovery workflows, data models, and specifications.

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
- [Legalweek](https://www.legalweek.com) - Annual legaltech conference in New York.
- [ILTACON](https://www.iltanet.org/events/iltacon) - International Legal Technology Association annual conference.
- [CLOC Global Institute](https://cloc.org) - Annual conference for corporate legal operations.
- [LegalGeek](https://www.legalgeek.co) - UK-based innovation conference for the legal industry.

### Newsletters & Media
- [Artificial Lawyer](https://www.artificiallawyer.com) - Deep-coverage publication on AI and legal tech. Free daily news.
- [Lawnext](https://www.lawnext.com) - Podcast and news by Bob Ambrogi on legal technology innovation.
- [Legal Tech Talk](https://legaltech-talk.com) - News and analysis on legal technology trends.
- [The Legal Innovators](https://legal-innovators.com) - Newsletter covering the business of law and legaltech.

## Legaltech Directories & Product Listing Platforms

Platforms that index, curate, review, or list legal technology products — useful for discovery, vendor evaluation, and market research.

### Global Directories

| Platform | Description | Type |
|---|---|---|
| [Legaltech Hub](https://legaltechnologyhub.com) | Global directory of legaltech solutions with filters by category, use case, jurisdiction, and language. Vendors can submit products for listing. | Global |
| [LawNext Legal Tech Directory](https://www.lawnext.com) | Bob Ambrogi's legal tech news site with a searchable product directory covering company details, reviews, press coverage, and pricing. | Global |
| [Above the Law](https://abovethelaw.com) | Legal news publication with legaltech coverage and a buyer's guide for law firm software. | Global |
| [Legal IT Professionals Directory](https://www.legaltechnology.com) | Vendor database and software directory primarily for larger law firms and enterprise legal IT. | Global |
| [Theorem LTS](https://theoremlegal.com) | Legal tech marketplace with comparison tools, pricing, media, and vendor demo connections. | Global |
| [G2 - Legal Software](https://www.g2.com/categories/legal) | Peer review platform with verified user ratings for legal software across 33+ subcategories. | Global |
| [Capterra - Legal Software](https://www.capterra.com/legal-software/) | Software comparison platform ranking legal tools by user ratings and popularity. | Global |
| [GetApp - Legal Software](https://www.getapp.com/legal-compliance-software/) | Software marketplace with verified reviews, comparisons, and feature filters for legal tools. | Global |
| [Software Advice - Legal](https://www.softwareadvice.com/legal/) | Platform helping law firms choose software through comparisons and analyst recommendations. | Global |

### India-Specific

| Platform | Description | Type |
|---|---|---|
| [ISAIL (Indian Society of AI and Law)](https://isail.in) | Indian not-for-profit focused on AI policy, standards, and governance. Administers the AiStandard.io Alliance; runs the AiStandard.io Summit. Relevant for tracking Indian AI-law policy. | Policy + Standards |
| [Bar and Bench](https://www.barandbench.com) | Indian legal news publication with coverage of court tech, legaltech, and legal AI developments. | Media |

### UK & Europe

| Platform | Description | Type |
|---|---|---|
| [LawTech UK](https://lawtech.uk) | UK government-backed initiative with an ecosystem map and resources for the UK lawtech sector. | Directory + Community |
| [LegalGeek](https://www.legalgeek.co) | UK legaltech conference and community with vendor showcases and market coverage. | Community + Events |

### Academic & Research

| Platform | Description | Type |
|---|---|---|
| [Stanford CodeX](https://law.stanford.edu/codex-the-stanford-center-for-legal-informatics/) | Stanford Center for Legal Informatics. Hosts the FutureLaw conference and computational law research. | Academic |
| [Legal Design Lab (Stanford)](https://law.stanford.edu/organizations/pages/legal-design-lab/) | Stanford lab focused on technology and design for access to justice. | Academic |
| [Harvard Law - Innovation Programs](https://hls.harvard.edu/the-hls-innovation-program/) | Harvard Law School programs tracking legal tech and legal innovation initiatives. | Academic |

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
