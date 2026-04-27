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

- [APIs for Legal Data](#apis-for-legal-data)
- [Machine Learning Datasets & Corpora](#machine-learning-datasets--corpora)
  - [Pretraining Corpora & Bulk Data](#pretraining-corpora--bulk-data)
  - [Legal Judgment Prediction (LJP)](#legal-judgment-prediction-ljp)
  - [Legal Text Classification](#legal-text-classification)
  - [Legal Question Answering](#legal-question-answering)
  - [Legal Summarization](#legal-summarization)
  - [Contract Analysis](#contract-analysis)
- [Legal AI Models & Embeddings](#legal-ai-models--embeddings)
  - [Large Language Models (LLMs)](#large-language-models-llms)
  - [Embedding & BERT-style Models](#embedding--bert-style-models)
  - [Multilingual & Regional Legal Models](#multilingual--regional-legal-models)
- [MCP Servers for Legal](#mcp-servers-for-legal)
- [Full-Stack Legal Platforms & Suites](#full-stack-legal-platforms--suites)
- [Legal Research Platforms](#legal-research-platforms)
- [Document Automation & Drafting](#document-automation--drafting)
- [Intellectual Property & Patent Tech](#intellectual-property--patent-tech)
- [Contract Lifecycle Management (CLM)](#contract-lifecycle-management-clm)
- [Notarization & E-Signature](#notarization--e-signature)
- [E-Discovery & Document Review](#e-discovery--document-review)
- [Practice Management & Legal Ops](#practice-management--legal-ops)
- [E-Billing & Legal Spend Management](#e-billing--legal-spend-management)
- [Consumer Legal Services \(B2C\)](#consumer-legal-services-b2c)
- [Compliance & RegTech](#compliance--regtech)
- [Online Dispute Resolution (ODR)](#online-dispute-resolution-odr)
- [Access to Justice & Public Interest Tech](#access-to-justice--public-interest-tech)
- [Foundational Research](#foundational-research)
- [Benchmarks & Evaluation](#benchmarks--evaluation)
- [Legal Ontologies & Knowledge Graphs](#legal-ontologies--knowledge-graphs)
- [Standards & Protocols](#standards--protocols)
- [Legaltech Directories & Product Listing Platforms](#legaltech-directories--product-listing-platforms)
- [Communities, Conferences & Media](#communities-conferences--media)
- [Related Awesome Lists](#related-awesome-lists)

---

## APIs for Legal Data

Commercial and open APIs specifically designed for retrieving case law, statutes, and legal documents into applications.

- [Vaquill AI API](https://vaquill.ai/legal-api) - Developer API providing programmatic access to 20M+ Indian Supreme Court, High Court, and Tribunal judgments with semantic search and citation verification. *(Sponsor)*

---

## Machine Learning Datasets & Corpora

Curated datasets of legal texts, case law, statutes, and contracts - organized by task. Most are openly available for research.

### Data Extraction & Processing Tools

Libraries and scripts for scraping, parsing, and processing legal text to build datasets.

- [Juriscraper](https://github.com/freelawproject/juriscraper) - **[Open Source]** Python library for scraping US court websites (400+ courts, PACER).
- [Eyecite](https://github.com/freelawproject/eyecite) - **[Open Source]** Legal citation extraction and analysis tool by Free Law Project.
- [LegalCrawler](https://github.com/iliaschalkidis/LegalCrawler) - **[Open Source]** Scripts to crawl and build English legal corpora from public court websites.
- [Blackstone](https://github.com/ICLRandD/Blackstone) - **[Open Source]** 🇬🇧 spaCy NLP pipeline and model for unstructured UK legal text (NER, citations).
- [French Legal Case Anonymization](https://github.com/ELS-RD/anonymisation) - **[Open Source]** NER-based pseudo-anonymization of French court decisions.

### Pretraining Corpora & Bulk Data

Large text corpora and jurisdiction-wide raw data dumps for pretraining or fine-tuning legal language models.

- [Pile of Law](https://huggingface.co/datasets/pile-of-law/pile-of-law) - **[🇺🇸 EN]** - **[~256 GB]** - US legal and administrative text; used to train CaseLawBERT
- [MultiLegalPile](https://huggingface.co/datasets/joelito/Multi_Legal_Pile) - **[🌍 24 langs]** - **[689 GB]** - Multilingual legal pretraining corpus from 17 jurisdictions
- [LeXFiles](https://huggingface.co/datasets/lexlms/lex_files) - **[🌍 6 sys]** - **[19B tokens]** - Massive English legal corpus (EU, CoE, Canada, US, UK, India)
- [Indian Kanoon Dataset](https://indiankanoon.org) - **[🇮🇳 EN]** - **[Large]** - Indian court judgments and statutes; widely used for Indian legal NLP
- [JRC-Acquis](https://joint-research-centre.ec.europa.eu/language-technology-resources/jrc-acquis_en) - **[🇪🇺 22 langs]** - **[Large]** - Massive parallel corpus of total EU law used heavily in multilingual machine translation
- [EUR-Lex](https://eur-lex.europa.eu) - **[🇪🇺 24 langs]** - **[Large]** - Official EU legislation and case law in all EU official languages
- [Open Australian Legal Corpus](https://huggingface.co/datasets/umarbutler/open-australian-legal-corpus) - **[🇦🇺 EN]** - **[Large]** - Multijurisdictional corpus of Australian legislative and judicial documents
- [S2ORC (Legal Subset)](https://github.com/allenai/s2orc) - **[🌍 EN]** - **[136M+]** - AllenAI's massive academic paper corpus containing deep legal reasoning/law review articles
- [CourtListener Bulk Data](https://www.courtlistener.com/help/api/bulk-data/) - **[🇺🇸 EN]** - **[9M+]** - US court opinions, judge data, and oral argument metadata dumps
- [RECAP Archive](https://free.law/recap/) - **[🇺🇸 EN]** - **[Huge]** - Largest open collection of US federal PACER documents and dockets
- [Caselaw Access Project (CAP)](https://case.law) - **[🇺🇸 EN]** - **[6.9M]** - US court decisions from Harvard Law School, 1600s-2020
- [Oyez Project Audio](https://www.oyez.org/) - **[🇺🇸 EN]** - **[Large]** - Premier archive of US Supreme Court multimodal audio and aligned text transcripts
- [WIPO Lex](https://www.wipo.int/wipolex/) - **[🌍 Multi]** - **[Large]** - Global database of IP laws/treaties and WIPO Lex-Judgments for selected IP case law.
- [SSRN (Legal Scholarship Network)](https://www.ssrn.com/) - **[🌍 Multi]** - **[Large]** - Open repository of legal scholarship, preprints, and academic law papers.
- [OpenAlex](https://openalex.org/) - **[🌍 Multi]** - **[Huge]** - Scholarly metadata and abstracts with a robust API; useful for legal literature mining.
### Legal Judgment Prediction (LJP)

Datasets for predicting case outcomes, charges, or penalties from court documents.

- [CAIL2018](https://github.com/china-ai-law-challenge/CAIL2018) - **[🇨🇳 China]** - **[ZH]** - **[2.6M cases]** - Charge, penalty, article prediction
- [ECtHR Dataset](https://huggingface.co/datasets/coastalcph/ecthr_cases) - **[🇪🇺 ECHR]** - **[EN]** - **[11K cases]** - Article violation prediction
- [ILDC (Indian Legal Documents Corpus)](https://github.com/Exploration-Lab/CJPE) - **[🇮🇳 India]** - **[EN]** - **[34K cases]** - Court judgment prediction and explanation
- [NyayaAnumana](https://huggingface.co/datasets/Dnyanesh1/NyayaAnumana) - **[🇮🇳 India]** - **[EN]** - **[700K+ cases]** - Largest corpus of Indian legal cases for LJP
- [FSCS - Swiss Judgment Prediction](https://huggingface.co/datasets/swiss_judgment_prediction) - **[🇨🇭 Switzerland]** - **[DE/FR/IT]** - **[85K cases]** - Binary outcome prediction across 3 languages
- [CaseSumm](https://huggingface.co/datasets/ChicagoHAI/CaseSumm) - **[🇺🇸 US SCOTUS]** - **[EN]** - **[25.6K opinions]** - Paired opinions + official syllabuses
- [IndianBailJudgments-1200](https://huggingface.co/datasets/SnehaDeshmukh/IndianBailJudgments-1200) - **[🇮🇳 India]** - **[EN]** - **[1.2K judgments]** - Bail decisions with 20+ structured attributes
- [The Supreme Court Database](http://scdb.wustl.edu) - **[🇺🇸 US]** - **[EN]** - **[All SCOTUS cases since 1791]** - Votes, outcomes, justice ideology
### Legal Text Classification

- [LexGLUE](https://github.com/coastalcph/lex-glue) - **[🌍 Multi]** - **[EN]** - 7-task benchmark: EURLEX, ECHR, LEDGAR, SCOTUS, ContractNLI, CaseHOLD, ECtHR
- [MultiEURLEX](https://huggingface.co/datasets/multi_eurlex) - **[🇪🇺 EU]** - **[23 langs]** - 65K EU laws with 4.5K labels; multilingual classification
- [LEDGAR](https://huggingface.co/datasets/coastalcph/ledgar) - **[🇺🇸 US]** - **[EN]** - 60K+ contract provisions with 12.6K labels
- [CUAD](https://www.atticusprojectai.org/cuad) - **[🇺🇸 US]** - **[EN]** - 510 annotated contracts, 41 clause types, 13K+ expert labels
- [AsyLex](https://huggingface.co/datasets/joelito/AsyLex) - **[🇨🇭 Swiss]** - **[FR/DE]** - 59K documents; 19K human-anotated entities for Refugee Law
### Legal Question Answering

- [CaseHOLD](https://huggingface.co/datasets/casehold/casehold) - **[🇺🇸 US]** - **[EN]** - 53K multiple-choice QA from US case law (holding identification)
- [COLIEE](https://coliee.org) - **[🇨🇦 🇯🇵 EN/JA]** - **[EN]** - Annual competition: statute retrieval, entailment, QA (Canadian + Japanese law)
- [JEC-QA](https://jecqa.thunlp.org) - **[🇨🇳 China]** - **[ZH]** - 26K Chinese bar exam questions for legal reasoning
### Legal Summarization

- [BillSum](https://github.com/FiscalNote/BillSum) - **[🇺🇸 US]** - **[EN]** - 22K US Congressional and California bill summaries
- [EUR-Lex Sum](https://huggingface.co/datasets/dennlinger/eur-lex-sum) - **[🇪🇺 EU]** - **[24 langs]** - Abstractive summarization of EU legislation; 1.5K+ docs
- [Multi-LexSum](https://github.com/multilexsum/dataset) - **[🇺🇸 US]** - **[EN]** - Multi-document summarization of US civil rights court cases
- [mteb/legal_summarization](https://huggingface.co/datasets/mteb/legal_summarization) - **[🇺🇸 US]** - **[EN]** - 439 pairs of legal contracts and plain-English summaries (from TOSDR)
- [IN-Abs / UK-Abs](https://github.com/Law-AI/summarization) - **[🇮🇳 🇬🇧]** - **[EN]** - Abstractive and extractive summarization datasets for Indian and UK case judgments
### Legal Semantic Search & Information Retrieval

- [opinions-synthetic-query-512](https://huggingface.co/datasets/Free-Law-Project/opinions-synthetic-query-512) - **[🇺🇸 US]** - **[EN]** - High-quality Free Law Project synthetic queries for finetuning legal semantic search
- [LexTREC](https://trec.nist.gov/data/legal.html) - **[🇺🇸 US]** - **[EN]** - Foundational NIST benchmark dataset for legal e-discovery containing real corporate data with expert judgments
- [CLERC](https://github.com/neelguha/legal-ml-datasets) - **[🇺🇸 US]** - **[EN]** - Case Law Evaluation and Retrieval Corpus for dense retrieval
- [Massive Legal Embedding Benchmark (MLEB)](https://isaacus.com/mleb) - **[🌍 Multi]** - **[Open]** - A multidomain open-source benchmark for legal information retrieval.
- [german_legal_sentences](https://huggingface.co/datasets/lavis-nlp/german_legal_sentences) - **[🇩🇪 Germany]** - **[DE]** - Semantic sentence matching and citation recommendation
### Contract Analysis

- [CUAD](https://www.atticusprojectai.org/cuad) - **[🇺🇸 US]** - **[EN]** - See Classification section. Gold standard for contract clause extraction.
- [MAUD](https://github.com/TheAtticusProject/maud) - **[🇺🇸 US]** - **[EN]** - M&A contract understanding; 39K questions on merger agreements
- [ToS;DR](https://tosdr.org/) - **[🌍 Multi]** - **[EN]** - Phenomenal dataset mapping thousands of internet Terms of Service into machine-readable JSON grades and bullets
- [ContractNLI](https://stanfordnlp.github.io/contract-nli/) - **[🌍]** - **[EN]** - Natural language inference over non-disclosure agreements
---

## Legal AI Models & Embeddings

### Large Language Models (LLMs)

Fine-tuned or domain-pretrained LLMs specifically for legal tasks.

- [SaulLM-7B](https://huggingface.co/Equall/Saul-7B-Instruct-v1) - **[Mistral 7B]** - **[EN]** - **[MIT]** - Pretrained on 30B+ English legal tokens
- [SaulLM-54B / 141B](https://huggingface.co/Equall) - **[Mistral]** - **[EN]** - **[MIT]** - Larger variants released Nov 2024
- [Lawma-8B](https://huggingface.co/ricdomolm/lawma-8b) - **[Llama 3]** - **[EN]** - Fine-tuned for legal classification tasks
- [Lawma-70B](https://huggingface.co/ricdomolm/lawma-70b) - **[Llama 3]** - **[EN]** - Larger legal classification model
- [InLegalBERT](https://huggingface.co/law-ai/InLegalBERT) - **[BERT]** - **[EN (Indian)]** - Trained on 5.4M Indian legal documents
- [Pasal.id](https://github.com/ilhamfp/pasal) - **[Claude + RAG]** - **[ID]** - **[Open]** - RAG-powered access to 40,000+ Indonesian regulations via Claude AI
- [NyayaSahayak](https://github.com/SoulNoob/Nyaysahayak) - **[EN/HI]** - **[Open]** - AI legal assistant covering Indian Constitution, BNS 2023, IT Act
- [ChatLaw](https://github.com/PKU-YuanGroup/ChatLaw) - **[LLaMA/Ziya]** - **[ZH]** - **[CC BY-NC]** - Chinese legal LLM from Peking University; trained on 30K+ Chinese legal datasets
- [DISC-LawLLM](https://github.com/FudanDISC/DISC-LawLLM) - **[Baichuan 13B]** - **[ZH]** - **[Apache 2.0]** - Chinese legal assistant from Fudan; legal retrieval + reasoning
### Embedding & BERT-style Models

Domain-specific encoder models for legal text similarity, classification, and retrieval.

- [voyage-law-2](https://docs.voyageai.com/docs/embeddings) - **[Voyage AI (API)]** - State-of-the-art closed-source embedding model specifically trained for legal text retrieval
- [voyage-4](https://docs.voyageai.com/docs/embeddings) - **[Voyage AI (API)]** - Highly optimized general embedding model with excellent performance across professional domains including law
- [Legal-BERT](https://huggingface.co/nlpaueb/legal-bert-base-uncased) - **[`nlpaueb/legal-bert-base-uncased`]** - Pretrained on EU/US legislation + court cases
- [CaseLawBERT](https://huggingface.co/pile-of-law/legalbert-large-1.7M-2) - **[`pile-of-law/legalbert-large-1.7M-2`]** - Trained on Pile of Law corpus
- [LegalBert (JHU)](https://huggingface.co/jhu-clsp/LegalBert) - **[`jhu-clsp/LegalBert`]** - JHU CLSP legal domain adaptation
- [EmuBERT](https://huggingface.co/isaacus/EmuBERT) - **[`isaacus/EmuBERT`]** - RoBERTa-based model for Australian law; 1.4B tokens across 6 jurisdictions
- [Lawformer](https://huggingface.co/joelito/longformer-base-4096-legal) - Long-context legal document model
- Kanon 2 Embedder - **[`isaacus/kanon-2`]** - #1 on MLEB benchmark; legal semantic search + RAG; 16K token context
**Benchmark:** [MLEB (Massive Legal Embedding Benchmark)](https://huggingface.co/datasets/Kanon/MLEB) - Comprehensive evaluation for legal text embedding models (Oct 2025).

### Multilingual & Regional Legal Models

- [OpenGPT-X / Teuken-7B](https://opengpt-x.de) - **[Europe]** - **[All 24 EU langs]** - German-funded initiative; produced Teuken-7B LLM covering all official EU languages
- [LawBench Models](https://github.com/open-compass/LawBench) - **[China]** - **[ZH]** - Models evaluated on 20 Chinese legal tasks

## MCP Servers for Legal

[Model Context Protocol (MCP)](https://modelcontextprotocol.io) servers that connect AI assistants to legal data sources and workflows.

- [Vaquill AI MCP](https://github.com/vaquill-AI/vaquill-mcp) - MCP server providing AI agents with access to 20M+ Indian Supreme Court, High Court, and Tribunal judgments with semantic search and citation verification. *(Sponsor)*
- [CourtListener MCP (DefendTheDisabled)](https://github.com/DefendTheDisabled/courtlistener-mcp) - Connects AI agents to CourtListener with semantic search, hybrid search, and citation verification to mitigate hallucination.
- [CourtListener MCP (Travis-Prall)](https://github.com/Travis-Prall/court-listener-mcp) - MCP Server for accessing CourtListener case data, court opinions, and eCFR federal regulations.
- [CourtListener MCP (khizar-anjum)](https://github.com/khizar-anjum/courtlistener-mcp) - MCP server built for searching cases by natural language legal problems across 3,352 U.S. courts.
- [CanLII MCP Server](https://github.com/Alhwyn/canlii-mcp-server) - Connects AI assistants to the Canadian Legal Information Institute (CanLII) to retrieve Canadian legislation and case law.
- [uk-case-law-mcp-server](https://github.com/nationalarchives/uk-case-law-mcp-server) - MCP server that enables LLMs to search, retrieve, and cite UK legal judgments via The National Archives API.
- [US Legal MCP Server](https://github.com/a10y/us-legal-mcp) - Provides access to US Congress bills, Federal Register documents, and court opinions.
- [Open Legal Compliance MCP](https://github.com/qpd-v/open-legal-compliance-mcp) - Facilitates legal compliance analysis using free government APIs for US and EU law.
- [agentic-ops/legal-mcp](https://github.com/agentic-ops/legal-mcp) - Comprehensive MCP server for legal workflows. Integrates AI assistants with legal databases and case management systems (Clio, etc.).
- [LegalContext MCP](https://mcp.so/server/legalcontext) - Open-source MCP server bridging law firm document management systems with AI assistants.
- [adeu (Agentic DOCX Redlining Engine)](https://github.com/dealfluence/adeu) - MCP Server enabling LLMs to inject native Track Changes and Comments into Word documents.
- [Master Claude for Legal](https://github.com/sboghossian/master-claude-for-legal) - **[Open Source]** - **[MIT]** - Skill pack for legal teams using Claude with MCP connectors. 10 reference docs (privilege, verification, long documents, practice areas), 5 starter skills (NDA triage, version diff, meeting brief, citation verifier, status synthesis), 3 firm templates. Includes the source Anthropic legal-webinar transcript and 51-question dataset.

> **Note:** MCP for legal is an emerging ecosystem. Many servers are early-stage community projects. Always verify data accuracy and jurisdiction coverage before use in legal practice.

---

## Full-Stack Legal Platforms & Suites

Comprehensive platforms that handle multiple functions across the legal workflow (research, drafting, review, and matter management). 

- [Harvey AI](https://harvey.ai) - **[AI-Native]** Full-stack legal AI with 30+ autonomous agentic workflows ($8B valuation).
- [Thomson Reuters](https://thomsonreuters.com) - **[Established]** Owner of CoCounsel, Westlaw, Practical Law, and HighQ.
- [LexisNexis](https://lexisnexis.com) - **[Established]** Owner of Lexis+ AI, Protégé, and Shepard's citations.
- [Legora](https://legora.com) - **[AI-Native]** YC-backed collaborative AI workspace spanning research, drafting, and review.
- [Eudia](https://eudia.com) - **[AI-Native]** AI agents specifically designed for Fortune 500 in-house corporate legal teams.
- [DeepJudge](https://deepjudge.ai) - **[AI-Native]** Custom AI workflows applied directly to internal law firm knowledge bases.

---

## Legal Research Platforms

Browser-based platforms and search engines for case law, statutes, and dockets.

### Open / Free Access (By Jurisdiction)

### National & Regional Portals (Global)

<details>
<summary>🌍 Africa</summary>


**Angola**
- [Global Legal Information Network (Angola)](http://www.worldlii.org/int/other/GLIN/ao/)

**Botswana**
- [High Court of Botswana](http://www.saflii.org/bw/cases/BWHC/)

**Burkina Faso**
- [Conseil Constitutionnel](http://www.juriburkina.org/doc/html/bf/jug/cc/fr/)

**Cape Verde**
- [Global Legal Information Network (Cape Verde)](http://www.worldlii.org/int/other/GLIN/cv/)

**Ghana**
- [Ghana Land Law Decisions](http://www.commonlii.org/gh/cases/GHLL/)

**Kenya**
- [Constitution of Kenya Review Commission](http://www.commonlii.org/ke/other/KECKRC/)

**Lesotho**
- [Lesotho Legislation](http://www.saflii.org/ls/legis/num_act/)

**Malawi**
- [High Court of Malawi](http://www.saflii.org/mw/cases/MWHC/)

**Mauritania**
- [Global Legal Information Network (Mauritania)](http://www.worldlii.org/int/other/GLIN/mr/)

**Mauritius**
- [Mauritius Legislation](http://www.saflii.org/mu/legis/num_act/)

**Mozambique**
- [Global Legal Information Network (Mozambique)](http://www.worldlii.org/int/other/GLIN/mz/)

**Namibia**
- [High Court of Namibia](http://www.saflii.org/na/cases/NAHC/)
- [Namibia Legislation](http://www.saflii.org/na/legis/num_act/)
- [Supreme Court of Namibia](http://www.saflii.org/na/cases/NASC/)

**Nigeria**
- [Nigerian Legislation](http://www.commonlii.org/ng/legis/num_act/)
- [Supreme Court of Nigeria](http://www.commonlii.org/ng/cases/NGSC/)

**Seychelles**
- [Seychelles Legislation](http://www.commonlii.org/sc/legis/consol_act/)

**South Africa**
- [Constitutional Court of South Africa](http://www.saflii.org/za/cases/ZACC)
- [Eastern Cape Division of the High Court of South Africa](http://www.saflii.org/za/cases/ZAECHC)
- [High Court of South Africa - Free State Division](http://www.saflii.org/za/cases/ZAFSHC/)
- [High Court of South Africa - Gauteng Division](http://www.saflii.org/za/cases/ZAGPHC/)
- [High Court of South Africa - Kwazulu Natal Division](http://www.saflii.org/za/cases/ZAKZHC/)
- [High Court of South Africa - North-West Division](http://www.saflii.org/za/cases/ZANWHC/)
- [High Court of South Africa - Northern Cape Division](http://www.saflii.org/za/cases/ZANCHC/)
- [High Court of South Africa - Western Cape Division](http://www.saflii.org/za/cases/ZAWCHC/)
- [South African Numbered Legislation](http://www.saflii.org/za/legis/num_act/)
- [Supreme Court of Appeal of South Africa](http://www.saflii.org/za/cases/ZASCA)

**Swaziland**
- [High Court of Swaziland](http://www.saflii.org/sz/cases/SZHC/)

**Tanzania**
- [Law Reform Commission of Tanzania](http://www.commonlii.org/tz/other/TZLRC/)

**Tunisia**
- [Global Legal Information Network (Tunisia)](http://www.worldlii.org/int/other/GLIN/tn/)

**Uganda**
- [Constitutional Court of Uganda](http://www.saflii.org/ug/cases/UGCC/)
- [High Court of Uganda](http://www.saflii.org/ug/cases/UGHC/)
- [Supreme Court of Uganda](http://www.saflii.org/ug/cases/UGSC/)

</details>

<details>
<summary>🌍 Asia</summary>


***   [Asian Development Bank Law and Policy Resources 1999-](http://www.asianlii.org/asia/other/ADBLPRes/) (AsianLII)**
- [Asian Development Bank Law and Policy Resources](http://www.asianlii.org/asia/other/ADBLPRes/)

**Afghanistan**
- [Constitution of Afghanistan 2004](http://www.asianlii.org/af/legis/const/)

**Asia-Pacific Economic Cooperation (APEC)**
- [APEC Agreements and Declarations](http://www.asianlii.org/apec/other/agrmt/)

**Association of Southeast Asian Nations (ASEAN)**
- [ASEAN Agreements and Declarations](http://www.asianlii.org/asean/other/agrmt/)

**Bangladesh**
- [Bangladesh Law Commission Publications](http://www.commonlii.org/bd/other/BDLC/)

**Bhutan**
- [Constitution of the Kingdom of Bhutan 2005](http://www.asianlii.org/bt/legis/const/)

**Brunei**
- [Brunei Legislation](http://www.commonlii.org/bn/legis/)
- [High Court of Brunei Decisions](http://www.commonlii.org/bn/cases/BNHC/)

**China**
- [Constitution of the People's Republic of China 2004](http://www.asianlii.org/cn/legis/const/)

**Cocos (Keeling) Islands**
- [Cocos (Keeling) Islands Domain Name Decisions](http://www.worldlii.org/cc/cases/CCDND/)

**Hong Kong**
- [Court of Appeal of Hong Kong Judgments](http://www.hklii.org/hk/jud/en/hkca/)

**India**
- [Indian Legislation](http://www.commonlii.org/in/legis/num_act/)
- [Supreme Court of India](http://www.commonlii.org/in/cases/INSC/)
- [Andhra Pradesh High Court](http://www.commonlii.org/in/cases/INHCAP/)
- [Gauhati High Court](http://www.commonlii.org/in/cases/INHCG/)
- [High Court of Punjab and Haryana, Chandigarh](http://www.commonlii.org/in/cases/INPHHC/)
- [Chattisgarh High Court](http://www.commonlii.org/in/cases/INHCC/)
- [Delhi High Court](http://www.commonlii.org/in/cases/INHCD/)
- [High Court of Bombay at Goa](http://www.commonlii.org/in/cases/INGAHC/)
- [High Court of Jammu and Kashmir](http://www.commonlii.org/in/cases/INJKHC/)
- [High Court of Kerala](http://www.commonlii.org/in/cases/INKLHC/)
- [Bombay High Court](http://www.commonlii.org/in/cases/INHCB/)
- [Orissa High Court](http://www.commonlii.org/in/cases/INHCO/)
- [Madras High Court](http://www.commonlii.org/in/cases/INHCM/)
- [Allahabad High Court](http://www.commonlii.org/in/cases/INHCA/)
- [Allahabad High Court - Lucknow Bench](http://www.commonlii.org/in/cases/INHCAL/)

**Indonesia**
- [Constitutional Court of Indonesia](http://www.asianlii.org/id/cases/IDCC/)
- [Indonesian Legislation (Undang-Undang Republik Indonesia)](http://www.worldlii.org/id/legis/uu/)
- [Supreme Court of Indonesia (Mahkamah Agung)](http://www.asianlii.org/id/cases/IDSC/)

**Japan**
- [Supreme Court of Japan](http://www.asianlii.org/jp/cases/JPSC/)

**Korea (North)**
- [Constitution of the Democratic People's Republic of Korea 1998](http://www.asianlii.org/kp/legis/const/)

**Korea (South)**
- [Constitutional Court of Korea](http://www.asianlii.org/kr/cases/KRCC/)
- [Supreme Court of Korea](http://www.asianlii.org/kr/cases/KRSC/)

**Lao PDR**
- [Constitution of the Lao People's Democratic Republic 1991](http://www.asianlii.org/la/legis/const/)

**Macau, China**
- [Laws of Macau](http://www.asianlii.org/mo/legis/laws/)

**Malaysia**
- [High Court of Malaya](http://www.commonlii.org/my/cases/MYMHC/)
- [High Court of Sabah and Sarawak](http://www.commonlii.org/my/cases/MYSSHC/)

**Maldives**
- [Constitution of the Republic of Maldives 1998](http://www.asianlii.org/mv/legis/const/)

**Mongolia**
- [Constitution of the People's Republic of Mongolia 1992](http://www.asianlii.org/mn/legis/const/)

**Nepal**
- [Constitution of the Kingdom of Nepal 1990](http://www.asianlii.org/np/legis/const/)

**Pakistan**
- [Pakistan (Punjab) Legislation](http://www.commonlii.org/pk/legis/pj/consol_act/)

**Papua New Guinea**
- [Papua New Guinea Consolidated Legislation](http://www.paclii.org/pg/legis/consol_act/)
- [Supreme Court of Papua New Guinea](http://www.paclii.org/pg/cases/PGSC/)

**Philippines**
- [Acts of the Philippines](http://www.asianlii.org/ph/legis/num_act/)
- [Commonwealth Acts of the Philippines](http://www.asianlii.org/ph/legis/cth_act/)
- [Republic Acts of the Philippines](http://www.asianlii.org/ph/legis/republic_act/)
- [Supreme Court of the Philippines](http://www.asianlii.org/ph/cases/PHSC/)
- [Supreme Court of the Philippines Resolutions](http://www.asianlii.org/ph/cases/PHSCR/)

**Singapore**
- [Singapore Subordinate Legislation](http://www.commonlii.org/sg/legis/num_reg/)
- [Singaporean Legislation](http://www.asianlii.org/sg/legis/consol_act/)
- [Supreme Court of Singapore - Court of Appeal](http://www.commonlii.org/sg/cases/SGCA/)
- [Supreme Court of Singapore - High Court](http://www.commonlii.org/sg/cases/SGHC/)

**South Korea**
- [Global Legal Information Network (South Korea)](http://www.worldlii.org/int/other/GLIN/kr/)

**Sri Lanka**
- [Sri Lanka Legislation](http://www.commonlii.org/lk/legis/consol_act/)
- [Sri Lankan Supreme Court](http://www.commonlii.org/lk/cases/LKSC/)

**Taiwan**
- [Constitutional Court of the Republic of China](http://www.asianlii.org/tw/cases/TWCC/)

**Thailand**
- [Constitutional Court of the Kingdom of Thailand](http://www.asianlii.org/th/cases/THCC/)
- [Supreme Court of the Kingdom of Thailand](http://www.asianlii.org/th/cases/THSC/)
- [Thai Legislation](http://www.asianlii.org/th/legis/consol_act/)

**Timor-Leste**
- [Decree-Laws of the Democratic Republic of Timor-Leste](http://www.worldlii.org/tp/legis/decree_law/)

**Viet Nam**
- [Constitution of the Socialist Republic of Vietnam 1992](http://www.asianlii.org/vn/legis/const/)

</details>

<details>
<summary>🌍 Australasia</summary>


**Australia**
- [High Court Review](http://www.austlii.edu.au/au/journals/HCRev/)
- [Supreme Court of the Australian Capital Territory - Court of Appeal Decisions](http://www.austlii.edu.au/au/cases/act/ACTCA/)
- [Supreme Court of the Australian Capital Territory Decisions](http://www.austlii.edu.au/au/cases/act/ACTSC/)
- [High Court of Australia Bulletins](http://www.austlii.edu.au/au/other/hca/bulletin/)
- [High Court of Australia Decisions](http://www.austlii.edu.au/au/cases/cth/HCA/)
- [High Court of Australia Transcripts](http://www.austlii.edu.au/au/other/hca/transcripts/)
- [Supreme Court of New South Wales - Court of Appeal Decisions](http://www.austlii.edu.au/au/cases/nsw/NSWCA/)
- [Supreme Court of New South Wales - Court of Criminal Appeal Decisions](http://www.austlii.edu.au/au/cases/nsw/NSWCCA/)
- [Supreme Court of New South Wales Decisions](http://www.austlii.edu.au/au/cases/nsw/supreme_ct/)
- [Supreme Court of Norfolk Island Decisions](http://www.austlii.edu.au/au/cases/nf/NFSC/)
- [Supreme Court of the Northern Territory - Court of Appeal Decisions](http://www.austlii.edu.au/au/cases/nt/NTCA/)
- [Supreme Court of the Northern Territory - Court of Criminal Appeal Decisions](http://www.austlii.edu.au/au/cases/nt/NTCCA/)
- [Supreme Court of the Northern Territory Decisions](http://www.austlii.edu.au/au/cases/nt/NTSC/)
- [Supreme Court of Queensland](http://www.austlii.edu.au/au/cases/qld/QSC/)
- [Supreme Court of Queensland - Court of Appeal](http://www.austlii.edu.au/au/cases/qld/QCA/)
- [Supreme Court of South Australia](http://www.austlii.edu.au/au/cases/sa/SASC/)
- [Supreme Court of Tasmania Decisions](http://www.austlii.edu.au/au/cases/tas/supreme_ct/)
- [Supreme Court of Victoria](http://www.austlii.edu.au/au/cases/vic/VSC/)
- [Supreme Court of Victoria - Court of Appeal](http://www.austlii.edu.au/au/cases/vic/VSCA/)
- [Supreme Court of Victoria - Court of Appeal Decisions](http://www.austlii.edu.au/au/cases/vic/VICSC/)
- [Supreme Court of Western Australia](http://www.austlii.edu.au/au/cases/wa/WASC/)
- [Supreme Court of Western Australia - Court of Appeal](http://www.austlii.edu.au/au/cases/wa/WASCA/)

**New Zealand**
- [High Court of New Zealand Decisions](http://www.nzlii.org/nz/cases/NZHC/)
- [Supreme Court of New Zealand Decisions](http://www.nzlii.org/nz/cases/NZSC/)
- [Eastern Caribbean Supreme Court](http://www.commonlii.org/int/cases/ECarSC/)

**Barbados**
- [Supreme Court of Barbados Decisions](http://www.commonlii.org/bb/cases/BBSC/)

**Bermuda**
- [Bermuda Consolidated Legislation](http://www.commonlii.org/bm/legis/consol_act/)
- [Eastern Caribbean Supreme Court](http://www.commonlii.org/int/cases/ECarSC/)

**Cuba**
- [Global Legal Information Network (Cuba)](http://www.worldlii.org/int/other/GLIN/cu/)

**Dominican Republic**
- [Global Legal Information Network (Dominican Republic)](http://www.worldlii.org/int/other/GLIN/do/)

**Haiti**
- [Global Legal Information Network (Haiti)](http://www.worldlii.org/int/other/GLIN/ht/)

**Jamaica**
- [Supreme Court of Jamaica](http://www.commonlii.org/jm/cases/JMSC/)

**Trinidad and Tobago**
- [High Court of Trinidad and Tobago](http://www.commonlii.org/tt/cases/TTHC/)
- [Trinidad and Tobago Legislation](http://www.commonlii.org/tt/legis/num_act/)

</details>

<details>
<summary>🌍 Central America</summary>


***   [Central American Court of Justice 2003-](http://www.worldlii.org/int/cases/CACJ/) (WorldLII)**
- [Central American Court of Justice](http://www.worldlii.org/int/cases/CACJ/)

**Belize**
- [Belize Legislation](http://www.commonlii.org/bz/legis/consol_act/)

**Costa Rica**
- [Global Legal Information Network (Costa Rica)](http://www.worldlii.org/int/other/GLIN/cr/)

**El Salvador**
- [Global Legal Information Network (El Salvador)](http://www.worldlii.org/int/other/GLIN/sv/)

**Guatemala**
- [Global Legal Information Network (Guatemala)](http://www.worldlii.org/int/other/GLIN/gt/)

**Honduras**
- [Global Legal Information Network (Honduras)](http://www.worldlii.org/int/other/GLIN/hn/)

**Nicaragua**
- [Global Legal Information Network (Nicaragua)](http://www.worldlii.org/int/other/GLIN/ni/)

**Panama**
- [Global Legal Information Network (Panama)](http://www.worldlii.org/int/other/GLIN/pa/)

</details>

<details>
<summary>🌍 Europe</summary>


***   [Commission of the European Communities 1985-](http://www.worldlii.org/eu/cases/ECComm/) (WorldLII)**
- [Commission of the European Communities](http://www.worldlii.org/eu/cases/ECComm/)

**England and Wales**
- [England and Wales High Court (Administrative Court) Decisions](http://www.bailii.org/ew/cases/EWHC/Admin/)
- [England and Wales High Court (Admiralty Division) Decisions](http://www.bailii.org/ew/cases/EWHC/Admlty/)
- [England and Wales High Court (Chancery Division) Decisions](http://www.bailii.org/ew/cases/EWHC/Ch/)
- [England and Wales High Court (Commercial Court) Decisions](http://www.bailii.org/ew/cases/EWHC/Comm/)
- [England and Wales High Court (Exchequer Court) Decisions](http://www.bailii.org/ew/cases/EWHC/Exch/)
- [England and Wales High Court (Family Division) Decisions](http://www.bailii.org/ew/cases/EWHC/Fam/)
- [England and Wales High Court (King's Bench Division) Decisions](http://www.bailii.org/ew/cases/EWHC/KB/)
- [England and Wales High Court (Patents Court) Decisions](http://www.bailii.org/ew/cases/EWHC/Patents)
- [England and Wales High Court (Queen's Bench Division) Decisions](http://www.bailii.org/ew/cases/EWHC/QB/)
- [England and Wales High Court (Supreme Court Cost Office) Decisions](http://www.bailii.org/ew/cases/EWHC/Costs/)
- [England and Wales High Court (Technology and Construction Court) Decisions](http://www.bailii.org/ew/cases/EWHC/TCC/)

**Ireland**
- [High Court of Ireland Decisions](http://www.bailii.org/ie/cases/IEHC/)
- [Irish Legislation](http://www.bailii.org/ie/legis/num_act/)
- [Supreme Court of Ireland Decisions](http://www.bailii.org/ie/cases/IESC/)

**Malta**
- [Malta Legislation](http://www.commonlii.org/mt/legis/consol_act/)

**Northern Ireland**
- [High Court of Justice in Northern Ireland Chancery Division Decisions](http://www.bailii.org/nie/cases/NIHC/Ch/)
- [High Court of Justice in Northern Ireland Family Division Decisions](http://www.bailii.org/nie/cases/NIHC/Fam/)
- [High Court of Justice in Northern Ireland Queen's Bench Division Decisions](http://www.bailii.org/nie/cases/NIHC/QB/)

**Portugal**
- [Global Legal Information Network (Portugal)](http://www.worldlii.org/int/other/GLIN/pt/)

**Romania**
- [Global Legal Information Network (Romania)](http://www.worldlii.org/int/other/GLIN/ro/)

**Russian Federation**
- [Global Legal Information Network (Russia)](http://www.worldlii.org/int/other/GLIN/ru/)

**Scotland**
- [Acts of the Scottish Parliament](http://www.bailii.org/scot/legis/num_act/)
- [Scottish High Court of Justiciary Decisions](http://www.bailii.org/scot/cases/ScotHC/)

**Spain**
- [Global Legal Information Network (Spain)](http://www.worldlii.org/int/other/GLIN/es/)

**United Kingdom**
- [United Kingdom Legislation](http://www.bailii.org/uk/legis/num_act/)

</details>

<details>
<summary>🌍 International</summary>


***   [EPIC Alert 1994-](http://www.worldlii.org/int/journals/EPICAlert/) (WorldLII)**
- [EPIC Alert](http://www.worldlii.org/int/journals/EPICAlert/)

**Commonwealth**
- [Commonwealth Declarations and Agreements](http://www.commonlii.org/int/other/ComSecDecl/)

**Kuwait**
- [Global Legal Information Network (Kuwait)](http://www.worldlii.org/int/other/GLIN/kw/)

**Saudi Arabia**
- [Global Legal Information Network (Saudi Arabia)](http://www.worldlii.org/int/other/GLIN/sa/)

</details>

<details>
<summary>🌍 North America</summary>


***   [North American Free Trade Agreement (NAFTA) Decisions 1990-](http://www.worldlii.org/int/cases/NAFTA/) (WorldLII)**
- [North American Free Trade Agreement (NAFTA) Decisions](http://www.worldlii.org/int/cases/NAFTA/)

**Canada**
- [Supreme Court of Canada](http://www.canlii.org/en/ca/scc/)
- [Supreme Court of Canada - Applications for Leave](http://www.canlii.org/en/ca/scc-l/)
- [Supreme Court of British Columbia](http://www.canlii.org/en/bc/bcsc/)
- [Supreme Court of Newfoundland and Labrador, Court of Appeal](http://www.canlii.org/en/nl/nlca/)
- [Supreme Court of Newfoundland and Labrador, Trial Division](http://www.canlii.org/en/nl/nlsctd/)
- [Supreme Court of the Northwest Territories](http://www.canlii.org/en/nt/ntsc/)
- [Supreme Court of Nova Scotia](http://www.canlii.org/en/ns/nssc/)
- [Supreme Court of Nova Scotia (Family Division)](http://www.canlii.org/en/ns/nssf/)
- [Supreme Court of Prince Edward Island - Appeal Division](http://www.canlii.org/en/pe/pescad/)
- [Supreme Court of Prince Edward Island - Trial Division](http://www.canlii.org/en/pe/pesctd/)
- [Supreme Court of the Yukon Territory](http://www.canlii.org/en/yk/yksc/)

**Mexico**
- [Global Legal Information Network (Mexico)](http://www.worldlii.org/int/other/GLIN/mx/)

**United States of America**
- [United States Supreme Court Decisions](http://supct.law.cornell.edu/supct/)

</details>

<details>
<summary>🌍 Pacific Islands</summary>


***   [Journal of South Pacific Law 1997-](http://www.paclii.org/vu/journals/JSPL/) (PacLII)**
- [Journal of South Pacific Law](http://www.paclii.org/vu/journals/JSPL/)

**American Samoa**
- [High Court of American Samoa Decisions](http://www.paclii.org/as/cases/ASHC/)

**Commonwealth of the Northern Mariana Islands**
- [Supreme Court of Commonwealth of the Northern Mariana Islands](http://www.paclii.org/mp/cases/MPSC/)

**Cook Islands**
- [Cook Islands Legislation](http://www.paclii.org/ck/legis/num_act/)
- [High Court of the Cook Islands Decisions](http://www.paclii.org/ck/cases/CKHC/)
- [New Zealand Legislation for Cook Islands](http://www.paclii.org/ck/legis/ck-nz_act/)
- [United Kingdom Legislation for Cook Islands](http://www.paclii.org/ck/legis/ck-uk_act/)

**Federated States of Micronesia**
- [Federated States of Micronesia Consolidated Legislation](http://www.paclii.org/fm/legis/consol_act/)
- [Federated States of Micronesia Sessional Legislation](http://www.paclii.org/fm/legis/num_act/)
- [Supreme Court of Federated States of Micronesia Decisions](http://www.paclii.org/fm/cases/FMSC/)

**Fiji Islands**
- [Fiji Islands Consolidated Legislation 1985](http://www.paclii.org/fj/legis/consol_act/)
- [Fiji Islands Sessional Legislation](http://www.paclii.org/fj/legis/num_act/)
- [High Court of Fiji Decisions](http://www.paclii.org/fj/cases/FJHC/)
- [Supreme Court of Fiji Decisions](http://www.paclii.org/fj/cases/FJSC/)
- [United Kingdom Legislation for Fiji](http://www.paclii.org/fj/legis/fj-uk_act/)

**Guam**
- [Guam Consolidated Legislation](http://www.paclii.org/gu/legis/consol_act/)
- [Supreme Court of Guam](http://www.paclii.org/gu/cases/GUSC/)

**Kiribati**
- [High Court of Kiribati Decisions](http://www.paclii.org/ki/cases/KIHC/)
- [High Court of the Gilbert Islands Decisions](http://www.paclii.org/ki/cases/KIGIHC/)
- [Kiribati Consolidated Legislation](http://www.paclii.org/ki/legis/consol_act/)
- [Kiribati Sessional Legislation](http://www.paclii.org/ki/legis/num_act/)
- [United Kingdom Legislation for Kiribati](http://www.paclii.org/depth/ki/legis/ki-uk_act/)

**Marshall Islands**
- [High Court of the Marshall Islands Decisions](http://www.paclii.org/mh/cases/MHHC/)
- [Marshall Islands Consolidated Legislation 2004](http://www.paclii.org/mh/legis/consol_act/)
- [Supreme Court of the Marshall Islands Decisions](http://www.paclii.org/mh/cases/MHSC/)

**Nauru**
- [Nauru Sessional Legislation](http://www.paclii.org/nr/legis/num_act/)
- [New Zealand Legislation for Niue](http://www.paclii.org/nu/legis/nu-nz_act/)
- [Supreme Court of Nauru Decisions](http://www.paclii.org/nr/cases/NRSC/)
- [United Kingdom Legislation for Nauru](http://www.paclii.org/nr/legis/nr-uk_act/)
- [United Kingdom Legislation for Niue](http://www.paclii.org/nu/legis/nu-uk_act/)

**Niue**
- [High Court of Niue Decisions](http://www.paclii.org/nu/cases/NUHC/)
- [Niue Sessional Legislation](http://www.paclii.org/nu/legis/num_act/)

**Palau**
- [Consolidated Legislation](http://www.paclii.org/pw/legis/consol_act/)
- [Supreme Court of Palau](http://www.paclii.org/pw/cases/PWSC/)

**Papua New Guinea**
- [Papua New Guinea-High Court of Australia](http://www.paclii.org/pg/cases/PGHCA/)

**Pitcairn Islands**
- [Supreme Court of Pitcairn Islands](http://www.paclii.org/pn/cases/PNSC/)

**Samoa**
- [High Court of Samoa Decisions](http://www.paclii.org/ws/cases/WSHC/)
- [New Zealand Legislation for Samoa](http://www.paclii.org/ws/legis/ws-nz_act/)
- [Samoa Consolidated Legislation](http://www.paclii.org/ws/legis/consol_act/)
- [Samoa Sessional Legislation](http://www.paclii.org/ws/legis/num_act/)
- [Samoa-Supreme Court of New Zealand 1991](http://www.paclii.org/ws/cases/WSNZSC/)
- [Samoa-Supreme Court of New Zealand 1961](http://www.paclii.org/ws/cases/WSNZCA/)
- [Supreme Court of Samoa Decisions](http://www.paclii.org/ws/cases/WSSC/)

**Solomon Islands**
- [Solomon Islands Consolidated Legislation](http://www.paclii.org/sb/legis/consol_act/)
- [Solomon Islands Sessional Legislation](http://www.paclii.org/sb/legis/num_act/)
- [United Kingdom Legislation for Solomon Islands](http://www.paclii.org/sb/legis/sb-uk_act/)

**Tokelau**
- [New Zealand Legislation in Tokelau](http://www.paclii.org/tk/legis/tk-nz_act/)
- [Tokelau Sessional Legislation](http://www.paclii.org/tk/legis/num_act/)
- [United Kingdom Legislation in Tokelau](http://www.paclii.org/tk/legis/tk-uk_act/)

**Tonga**
- [Supreme Court of Tonga Decisions](http://www.paclii.org/to/cases/TOSC/)
- [Tonga Consolidated Legislation](http://www.paclii.org/to/legis/consol_act/)
- [Tonga Sessional Legislation](http://www.paclii.org/to/legis/num_act/)
- [United Kingdom Legislation for Tonga](http://www.paclii.org/to/legis/to-uk_act/)

**Tuvalu**
- [High Court of Tuvalu Decisions](http://www.paclii.org/tv/cases/TVHC/)
- [Tuvalu Consolidated Legislation](http://www.paclii.org/tv/legis/consol_act/)
- [Tuvalu Sessional Legislation](http://www.paclii.org/tv/indices/legis/Tuvalu_legis_1991-2000.htm)
- [United Kingdom Legislation for Tuvalu](http://www.paclii.org/tv/legis/tv-uk_act/)

**Vanuatu**
- [Supreme Court of New Hebrides Decisions](http://www.paclii.org/vu/cases/VUNHSC/)
- [Supreme Court of Vanuatu Decisions](http://www.paclii.org/vu/cases/VUSC/)
- [United Kingdom Legislation for Vanuatu](http://www.paclii.org/vu/legis/vu-uk_act/)
- [Vanuatu Consolidated Legislation](http://www.paclii.org/vu/legis/consol_act/)
- [Vanuatu Sessional Legislation](http://www.paclii.org/vu/legis/num_act/)
- [Vanuatu Sessional Legislation (French)](http://www.paclii.org/vu/legis/num_act_fr/)

</details>

#### Global & Multi-Jurisdictional
- [WorldLII](https://www.worldlii.org/databases.html) - Federated gateway to 2,000+ legal databases across 200+ jurisdictions via national LIIs.
- [CommonLII](http://www.commonlii.org) - Searchable legal databases from 60+ Commonwealth and common law jurisdictions.
- [GlobaLex (NYU)](https://www.nyulawglobal.org/globalex/) - Comprehensive research guides and database listings for international, comparative, and foreign law.

#### United States
- [CourtListener](https://www.courtlistener.com) - Free open case law search with API access. 9M+ opinions.
- [PACER](https://pacer.uscourts.gov) - Official US federal court docket and document system.
- [Caselaw Access Project](https://case.law) - 6.9M US court decisions, 1600s-2020. Free bulk API.
- [GovInfo](https://www.govinfo.gov) - US federal legislation, regulations, and congressional records. Bulk data/API available.
- [eCFR](https://www.ecfr.gov) - Up-to-date Code of Federal Regulations with a full bulk API.
- [OpenStates](https://openstates.org) - Open-source platform tracking US state legislation in real time.
- [Google Scholar Case Law](https://scholar.google.com) - Free US federal and state court opinions.

#### United Kingdom
- [BAILII](https://www.bailii.org) - Free access to British and Irish primary legal materials.
- [UK National Archives / Find Case Law](https://caselaw.nationalarchives.gov.uk) - Official UK court decisions from 2001.
- [legislation.gov.uk](https://www.legislation.gov.uk) - Full text of UK Acts of Parliament, statutory instruments.

#### European Union
- [EUR-Lex](https://eur-lex.europa.eu) - Official EU law portal. All legislation, case law, and treaties (24 languages). API available.
- [CURIA (CJEU)](https://curia.europa.eu/) - Official Court of Justice and General Court case law.
- [HUDOC (ECHR)](https://hudoc.echr.coe.int/) - European Court of Human Rights judgments, decisions, and summaries.
- [N-Lex](https://n-lex.europa.eu/) - One-stop portal to official national law databases for all EU member states.
- [OP (Publications Office)](https://data.europa.eu/en) - EU Open Data Portal including legal metadata and bulk APIs.
- [ECLI Search](https://e-justice.europa.eu/316/EN/european_case_law_identifier__ecli) - Standardized search for courts across EU member states.

#### Germany
- [OpenJur](https://openjur.de) - Open-source database of German court decisions. Community-maintained.
- [OpenLegalData](https://openlegaldata.io) - German court decisions and legislation. REST API available.
- [Gesetze im Internet](https://www.gesetze-im-internet.de) - Official German federal law portal (all statutes). Free.

#### France
- [Legifrance](https://www.legifrance.gouv.fr) - Official French legal portal. All statutes, regulations, and major court decisions.
- [Judilibre (Cour de Cassation)](https://www.courdecassation.fr/acces-rapide/judiciaire-judilibre) - Open API for French Supreme Court decisions. GDPR-anonymized.

#### India
- [Vaquill AI](https://vaquill.ai) - Free access to 20M+ Indian judgments with semantic search and citation verification. *(Sponsor)*
- [Indian Kanoon](https://indiankanoon.org) - Free access to Indian court judgments, statutes, and legal documents.
- [India Code](https://www.indiacode.nic.in/) - Central repository of all Central and State Acts and subordinate legislation.
- [Supreme Court of India](https://sci.gov.in) - Official portal with judgments from the Supreme Court of India.
- [eCourts Services](https://services.ecourts.gov.in) - Unified portal for Indian district and High Court case status.
- [OpenNyAI Datasets](https://opennyai.org/datasets) - Indian legal NLP datasets for summarization, QA, and translation.

#### China
- [China Judgments Online (Wenshu)](https://wenshu.court.gov.cn) - Official Chinese court judgment database. 140M+ decisions.
- [National Laws & Regulations Database](https://flk.npc.gov.cn/) - Official centralized repository of PRC laws and regulations.
- [PKU LawInfo (Peking University)](https://law.pku.edu.cn/lawen/) - Comprehensive Chinese laws and regulations database.
- [e-Gov Law Search (Japan)](https://elaws.e-gov.go.jp/) - Official Japanese laws and regulations portal with a full XML API.

#### Brazil
- [LexML Brasil](https://www.lexml.gov.br) - Federated search over Brazilian legislation and legal documents.
- [STF Jurisprudencia](https://portal.stf.jus.br/jurisprudencia/) - Brazilian Supreme Court (STF) decisions portal.
- [CNJ Dados Abertos](https://dadosabertos.cnj.jus.br) - National Council of Justice open judicial data and indicators.

#### Global / Multijurisdictional
- [AustLII](https://www.austlii.edu.au) - Free Australasian legal information.
- [CommonLII](https://www.commonlii.org) - Free access to common law jurisdictions worldwide.
- [WorldLII](https://www.worldlii.org) - Global free legal information network.

### Commercial AI Research Platforms
- [Vaquill AI](https://vaquill.ai) - **[AI-Native]** Indian legal research platform with agentic workflows, MCP server, and proprietary database of 20M+ judgments. *(Sponsor)*
- [Leya](https://leya.law) - **[AI-Native]** Agentic research and legal memo generation.
- [Paxton AI](https://paxton.ai) - **[AI-Native]** Jurisdiction-aware AI legal answers.
- [EvenUp](https://evenuplaw.com) - **[AI-Native]** Agentic demand letter generation and research for personal injury.
- [Lexlegis.AI](https://lexlegis.ai) - **[AI-Native]** Indian legal research LLM trained on 10M+ documents.
- [Blue J](https://bluej.com) - **[AI-Native]** AI-powered answers to complex US/Canada/UK tax questions.
- [Bloomberg Law](https://pro.bloomberglaw.com) - **[Established]** Major US legal research platform with AI brief analysis and real-time legislative monitoring.
- [vLex / Vincent AI](https://vlex.com) - **[Established]** Global coverage (1B+ documents, 17 countries) with cross-jurisdictional AI comparison.
- [Casetext / CoCounsel Core](https://casetext.com) - **[Established]** GPT-4 powered research memo generation and CARA AI brief analysis.
- [Lex Machina](https://lexmachina.com) - **[Established]** Litigation analytics predicting outcomes and benchmarking opposing counsel.
- [Docket Alarm](https://www.docketalarm.com) - **[Established]** Federal and state docket monitoring with real-time alerts.
- [Manupatra](https://www.manupatra.com) - **[Established]** Proprietary Indian legal database covering SC, HCs, and Tribunals.

---

## Document Automation & Drafting

Software for generating, assembling, and reviewing legal documents.

- [Docassemble](https://docassemble.org) - **[Open Source]** The gold standard target for guided legal interviews and document assembly.
- [Suffolk LIT Lab Assembly Line](https://github.com/SuffolkLITLab/docassemble-AssemblyLine) - **[Open Source]** Toolkit for Massachusetts court forms; reusable pattern for any jurisdiction.
- [open-agreements](https://github.com/CommonAccord/Cmacc-Org) - **[Open Source]** CommonAccord: legal documents as structured, linkable data.
- [adeu](https://github.com/dealfluence/adeu) - **[Open Source]** Agentic DOCX Redlining Engine for Word document Track Changes.

- [Spellbook](https://spellbook.legal) - **[AI-Native]** AI contract drafting and review assistant operating natively in Microsoft Word.
- [Clearbrief](https://clearbrief.com) - **[AI-Native]** AI-powered factual verification and drafting assistance in briefs.
- [HotDocs](https://www.hotdocs.com) - **[Established]** Long-established document assembly software for law firms.
- [ContractExpress](https://www.thomsonreuters.com) - **[Established]** Thomson Reuters' document automation platform.
- [Litera](https://litera.com) - **[Established]** Document drafting, proofreading, and deal management suite.

---

## Intellectual Property & Patent Tech

Platforms for patent searching, analytics, and intellectual property portfolio management.

- [PatSnap](https://www.patsnap.com) - **[AI-Native]** Patent analytics and intelligence powered by AI.
- [Anaqua](https://www.anaqua.com) - **[Established]** Comprehensive IP management system.
- [AltLegal](https://www.altlegal.com) - **[Established]** Automated trademark docketing and protection.
- [Trademarkia](https://www.trademarkia.com) - **[Established]** Global trademark search engine and registration platform.

---

## Contract Lifecycle Management (CLM)

Platforms for managing contracts from creation through execution, obligations, and renewal.

- [Ironclad](https://ironcladapp.com) - **[Established]** CLM with AI clause detection, redlining, playbooks, and Jurist AI assistant.
- [Icertis](https://www.icertis.com) - **[Established]** Enterprise CLM leader with Icertis Vera AI and agentic workflows.
- [ContractPodAi / Leah](https://www.contractpodai.com) - **[Established]** Generative AI for CLM with native Microsoft Azure OpenAI integration.
- [DocuSign CLM](https://www.docusign.com/products/clm) - **[Established]** Intelligent Agreement Management with AI-Assisted Review.
- [Robin AI](https://robinai.com) - **[AI-Native]** AI contract negotiation and review platform.
- [Luminance](https://www.luminance.com) - **[AI-Native]** AI for transactional, compliance, and litigation document review.
- [LexCheck](https://www.lexcheck.com) - **[AI-Native]** AI for contract redlining and playbook enforcement.
- [Lexion](https://lexion.ai) - **[AI-Native]** AI-powered contract management backed by Google Ventures.
- [Legartis](https://legartis.ai) - **[AI-Native]** AI contract review and risk analysis (German/European market focus).
- [LawGeex](https://www.lawgeex.com) - **[Established]** AI contract review platform pre-screening against company policies.
- [Juro](https://juro.com) - **[Established]** All-in-one contract platform popular in UK/EU.
- [Avvoka](https://avvoka.com) - **[Established]** UK document automation and negotiation platform.

- [Wraft](https://github.com/wraft/wraft) - **[Open Source]** Document lifecycle management with version control.

---

## Notarization & E-Signature

Platforms handling digital execution of documents and Remote Online Notarization (RON).

- [DocuSign](https://www.docusign.com) - **[Established]** The global standard for e-signatures and agreement clouds.
- [Proof (formerly Notarize)](https://www.proof.com) - **[Established]** Pioneer of Remote Online Notarization (RON).
- [DocVerify](https://www.docverify.com) - **[Established]** E-notary and secure electronic signature platform.

---

## E-Discovery & Document Review

Platforms for collecting, processing, reviewing, and producing electronically stored information (ESI).

- [Relativity](https://www.relativity.com) - **[Established]** Industry leader; features aiR for Review and aiR for Privilege.
- [Everlaw](https://www.everlaw.com) - **[Established]** Cloud-native with AI clustering (25M docs), trial prep, and predictive coding.
- [Nuix](https://www.nuix.com) - **[Established]** High-performance processing with Cognitive AI (CogAI) and 500+ pre-built models.
- [Reveal AI](https://www.revealdata.com) - **[Established]** AI-powered e-discovery with behavioral analytics and fraud detection.
- [Exterro](https://www.exterro.com) - **[Established]** End-to-end legal GRC platform with e-discovery and forensics.
- [Logikcull](https://www.logikcull.com) - **[Established]** Self-service cloud e-discovery for small and mid-size firms.
- [IPRO](https://ipro.com) - **[Established]** E-discovery software for large-scale review and production.
- [FreeEed](https://freeeed.org) - **[Open Source]** AI-enabled e-discovery with OCR and metadata extraction.
- [FreeEed](https://freeeed.org) - **[Open Source]** AI-enabled cross-platform e-discovery platform with text extraction, metadata processing, and OCR.

---

## Practice Management & Legal Ops

Software for running a law practice and legal department operations - case management, billing, calendaring, and workflow automation.

- [Clio](https://www.clio.com) - **[Established]** Leading cloud-based practice management suite featuring Clio Duo AI.
- [Litera](https://litera.com) - **[Established]** Document drafting, proofreading, and deal management suite.
- [NetDocuments](https://netdocuments.com) - **[Established]** Leading cloud document management system (DMS) with AI-powered search.
- [Filevine](https://www.filevine.com) - **[Established]** Legal operating system with AI-enhanced case lifecycle management.
- [Mitratech](https://mitratech.com) - **[Established]** Enterprise-scale matter management and workflow automation.
- [MyCase](https://www.mycase.com) - **[Established]** Practice management with MyCase IQ for AI writing assistance.
- [Smokeball](https://www.smokeball.com) - **[Established]** Practice management with built-in activity intelligence and billing.
- [CosmoLex](https://www.cosmolex.com) - **[Established]** Cloud-based legal accounting and practice management.
- [Darrow](https://darrow.ai) - **[AI-Native]** Litigation intelligence identifying meritorious lawsuits from public data.
- [Legalyze.ai](https://legalyze.ai) - **[AI-Native]** Litigation support specializing in AI extraction and chronology.

- [ClinicCases](https://github.com/judsonmitchell/ClinicCases) - **[Open Source]** Case management for law school clinics.
- [ArkCase](https://www.arkcase.com) - **[Open Source]** Adaptive case management for legal and government.
- [J-Lawyer](https://www.j-lawyer.org) - **[Open Source]** German law practice management.
- [Elint AI / Justice Accelerator](https://elint.in) - **[Open Source]** Blockchain case management infrastructure for courts and ADR (India/UAE).

---

## E-Billing & Legal Spend Management

Software designed for corporate legal departments to manage, audit, and analyze outside counsel spend.

- [Brightflag](https://brightflag.com) - **[AI-Native]** AI-powered invoice review and legal spend management.
- [SimpleLegal](https://www.simplelegal.com) - **[Established]** Modern corporate legal operations software.
- [CounselLink](https://counsellink.com) - **[Established]** LexisNexis enterprise legal spend and matter management.

---

## Consumer Legal Services (B2C)

Platforms delivering direct-to-consumer automated legal services, documents, and advice.

- [LegalZoom](https://www.legalzoom.com) - **[Established]** Market leader in online business formation and estate planning.
- [Rocket Lawyer](https://www.rocketlawyer.com) - **[Established]** Online legal documents and on-demand legal advice.
- [HelloPrenup](https://helloprenup.com) - **[Established]** Digital prenuptial agreement platform.
- [DoNotPay](https://donotpay.com) - **[AI-Native]** Consumer advocacy platform marketing itself as the "world's first robot lawyer".

---

## Compliance & RegTech

Tools for regulatory compliance, policy management, financial crime detection, and AI governance.

- [Drata](https://drata.com) - **[AI-Native]** GRC automation with continuous monitoring for SOC 2, ISO 27001, HIPAA, GDPR, EU AI Act.
- [Vanta](https://vanta.com) - **[Established]** Compliance automation with 375+ integrations and AI vendor risk assessment.
- [ComplyAdvantage](https://complyadvantage.com) - **[AI-Native]** AI-driven AML and financial crime detection.
- [Corlytics / Clausematch](https://www.corlytics.com) - **[Established]** RegTech for regulatory change management and compliance policy.
- [Certa](https://www.getcerta.com) - **[Established]** Third-party risk management and vendor onboarding automation.
- [OneTrust](https://www.onetrust.com) - **[Established]** Privacy, GRC, and ethics management platform with AI-powered workflows.
- [NAVEX](https://www.navex.com) - **[Established]** Integrated risk and compliance management.
- [Kira Systems](https://kirasystems.com) - **[Established]** ML-based contract analysis for due diligence and compliance.

---

## Online Dispute Resolution (ODR)

Platforms designed to resolve disputes entirely online via algorithmic, crowdsourced, or mediated mechanisms.

- [TylerTech E-Filing](https://www.tylertech.com) - **[Established]** The underlying e-filing and case management infrastructure for US state e-Courts.
- [Modria](https://www.modria.com) - **[Established]** Pioneer ODR platform (now owned by Tyler Technologies), originally built for eBay.
- [Kleros](https://kleros.io) - **[AI-Native]** Decentralized, blockchain-based crowdsourced justice protocol.

---

## Access to Justice & Public Interest Tech

Organizations and software actively using technology to advance access to justice, court systems, and open legal infrastructure.

- [Free Law Project](https://free.law) - **[Nonprofit]** Maintains CourtListener, RECAP, and Eyecite.
- [Harvard Law School - CAP](https://case.law) - **[Academic]** Open case law project containing 6.9M digitized US cases.
- [Suffolk LIT Lab](https://suffolklitlab.org) - **[Academic]** R&D center maintaining the Document Assembly Line.
- [A2J Author / CALI](https://www.a2jauthor.org) - **[Nonprofit]** Guided interview software protecting self-represented litigants.
- [Legal Services Corporation (LSC)](https://lsc.gov) - **[Government]** Federal funder of civil legal aid via Technology Initiative Grants.
- [ProBono.net](https://probono.net) - **[Nonprofit]** Online legal library providing pro bono resources for attorneys.
- [Upsolve](https://upsolve.org) - **[Nonprofit]** Free Chapter 7 bankruptcy filing tool.
- [JustFix](https://www.justfix.org) - **[Nonprofit]** Tenant rights and landlord communication tools for housing justice.
- [AsylumConnect](https://asylumconnect.org) - **[Nonprofit]** Open-source resource matching for LGBTQ+ asylum seekers.
- [Electronic Frontier Foundation (EFF)](https://eff.org) - **[Nonprofit]** Policy, advocacy, and legal defense for digital rights.
- [ABA Free Legal Answers](https://freelegalanswers.org) - **[Nonprofit]** Virtual pro bono legal advice clinic.

## Foundational Research

Seminal papers that shaped the field of legal AI and NLP. Essential reading for anyone building in this space.

- [LEGAL-BERT: The Muppets straight out of Law School](https://arxiv.org/abs/2010.02559) - **[2020]** - First large-scale BERT models pretrained on EU/US legal text; established the domain-adaptation benchmark for legal NLP
- [LexGLUE: A Benchmark Dataset for Legal Language Understanding](https://arxiv.org/abs/2110.00976) - **[2022]** - 7-task legal NLP benchmark; the "GLUE for law"; drove standardized evaluation
- [LegalBench: A Collaboratively Built Benchmark for Legal Reasoning](https://arxiv.org/abs/2308.11462) - **[2023]** - 162-task benchmark built with practicing lawyers; most comprehensive LLM legal evaluation to date
- [GPT-4 Passes the Bar Exam](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233) - **[2023]** - Bommarito & Katz; showed LLMs can pass professional licensing exams; catalyzed investor and legal community attention
- [SaulLM-7B: A pioneering Large Language Model for Law](https://arxiv.org/abs/2403.03883) - **[2024]** - First open-weight LLM continually pretrained on 30B+ legal tokens with instruction tuning
- [MultiLegalPile: A 689GB Multilingual Legal Corpus](https://aclanthology.org/2024.acl-long.805/) - **[2024]** - Largest open multilingual legal pretraining dataset; 24 languages, 17 jurisdictions
- [Artificial Intelligence and Legal Analytics](https://www.cambridge.org/core/books/artificial-intelligence-and-legal-analytics/E7D705EEF392501A1DB180645917E7E0) - **[2017]** - Kevin Ashley; foundational textbook on AI and law; covers case-based reasoning, argument mining, and legal knowledge representation
---

## Benchmarks & Evaluation

Resources for evaluating AI and NLP systems on legal tasks.

- [LegalBench](https://github.com/HazyResearch/legalbench) - 162-task benchmark for English legal reasoning in LLMs. Live leaderboard maintained at [vals.ai](https://vals.ai).
- [LawBench](https://github.com/open-compass/LawBench) - 20-task Chinese legal benchmark evaluating LLMs across three cognitive levels.
- [MLEB (Massive Legal Embedding Benchmark)](https://huggingface.co/datasets/Kanon/MLEB) - Comprehensive benchmark for legal text embedding models (Oct 2025).
- [CUAD](https://www.atticusprojectai.org/cuad) - Contract Understanding Atticus Dataset: extraction and classification benchmark for commercial contracts.
- [LEDGAR](https://metatext.io/datasets/ledgar) - Large-scale benchmark for legal contract provision classification.
- [ECtHR Task](https://huggingface.co/datasets/coastalcph/ecthr_cases) - Legal judgment prediction benchmark using ECHR cases.
- [maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) - Curated list of Legal NLP resources, models, datasets, and papers.
- [JUST-NLP 2025 Legal MT](https://codabench.org/competitions/3682/) - English-to-Hindi legal machine translation shared task benchmark; workshop at IJCNLP-AACL 2025.

---

## Legal Ontologies & Knowledge Graphs

Structured vocabularies, ontologies, and knowledge graphs for representing legal concepts, relationships, and document structure.

- [EuroVoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) - EU's multilingual thesaurus covering subjects of EU legislation. 7,000+ concepts in 24 languages. Used for tagging EUR-Lex documents.
- [LKIF-Core](https://github.com/RinkeHoekstra/lkif-core) - Legal Knowledge Interchange Format; OWL ontology for basic legal concepts (norms, agents, documents, time). Foundation for many legal knowledge systems.
- [SALI LMSS (Legal Matter Standard Specification)](https://www.sali.org) - Structured ontology for legal matter types, service types, and industry codes. Open standard for legal operations data.
- [LegalDocML / Akoma Ntoso](https://www.un.org/dgacm/en/content/akoma-ntoso) - XML + ontology for legislative and judicial document structure. Adopted by the UN, EU Parliament, national parliaments.
- [JurWordNet](https://github.com/fcroce/JurWordNet) - Legal extension of WordNet with Italian legal terminology; one of the few legal lexical ontologies in a non-English language.
- [Wikidata Legal Entities](https://www.wikidata.org/wiki/Wikidata:WikiProject_Law) - WikiProject Law: structured data on courts, cases, legislation, and legal concepts in Wikidata. Machine-readable and freely licensed.
- [PROLEG (Japanese Legal Ontology)](https://arxiv.org/abs/1404.0370) - Formal representation of Japanese civil law rules for logic-based legal reasoning. Developed at NII Tokyo.

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

## Legaltech Directories & Product Listing Platforms

Platforms that index, curate, review, or list legal technology products — useful for discovery, vendor evaluation, and market research.

- [Legaltech Hub](https://legaltechnologyhub.com) - **[Global]** - Global directory of legaltech solutions with filters by category, use case, jurisdiction, and language.
- [LawNext Legal Tech Directory](https://www.lawnext.com) - **[Global]** - Bob Ambrogi's legal tech news site with a searchable product directory covering company details, reviews, press coverage, and pricing.
- [Above the Law](https://abovethelaw.com) - **[Global]** - Legal news publication with legaltech coverage and a buyer's guide for law firm software.
- [Legal IT Professionals Directory](https://www.legaltechnology.com) - **[Global]** - Vendor database and software directory primarily for larger law firms and enterprise legal IT.
- [Theorem LTS](https://theoremlegal.com) - **[Global]** - Legal tech marketplace with comparison tools, pricing, media, and vendor demo connections.
- [G2 - Legal Software](https://www.g2.com/categories/legal) - **[Global]** - Peer review platform with verified user ratings for legal software across 33+ subcategories.
- [Capterra - Legal Software](https://www.capterra.com/legal-software/) - **[Global]** - Software comparison platform ranking legal tools by user ratings and popularity.
- [GetApp - Legal Software](https://www.getapp.com/legal-compliance-software/) - **[Global]** - Software marketplace with verified reviews, comparisons, and feature filters for legal tools.
- [Software Advice - Legal](https://www.softwareadvice.com/legal/) - **[Global]** - Platform helping law firms choose software through comparisons and analyst recommendations.
- [ISAIL (Indian Society of AI and Law)](https://isail.in) - **[Policy + Standards]** - Indian not-for-profit focused on AI policy, standards, and governance. Administers the AiStandard.io Alliance.
- [Bar and Bench](https://www.barandbench.com) - **[Media]** - Indian legal news publication with coverage of court tech, legaltech, and legal AI developments.
- [LawTech UK](https://lawtech.uk) - **[Directory + Community]** - UK government-backed initiative with an ecosystem map and resources for the UK lawtech sector.
- [LegalGeek](https://www.legalgeek.co) - **[Community + Events]** - UK legaltech conference and community with vendor showcases and market coverage.
- [Stanford CodeX](https://law.stanford.edu/codex-the-stanford-center-for-legal-informatics/) - **[Academic]** - Stanford Center for Legal Informatics. Hosts the FutureLaw conference and computational law research.
- [Legal Design Lab (Stanford)](https://law.stanford.edu/organizations/pages/legal-design-lab/) - **[Academic]** - Stanford lab focused on technology and design for access to justice.
- [Harvard Law - Innovation Programs](https://hls.harvard.edu/the-hls-innovation-program/) - **[Academic]** - Harvard Law School programs tracking legal tech and legal innovation initiatives.
- [Harvard Law - Innovation Programs](https://hls.harvard.edu/the-hls-innovation-program/) - **[Harvard Law School programs tracking legal tech and legal innovation initiatives.]** - Academic
---

## Communities, Conferences & Media

Stay current with the legaltech ecosystem.

### Communities & Forums
- [Legal Hackers](https://legalhackers.org) - Global community of lawyers, engineers, policy professionals. Local chapters worldwide.
- [LawTech.UK](https://lawtech.uk) - UK-focused legal innovation community.
- [HFforLegal (Hugging Face)](https://huggingface.co/HFforLegal) - Community for legal AI practitioners on Hugging Face.
- [CLOC (Corporate Legal Operations Consortium)](https://cloc.org) - 3,000+ member community for in-house legal operations professionals.

### Reddit Communities
- [r/LegalTech](https://reddit.com/r/legaltech) - The primary subreddit strictly dedicated to legal technology discussion, software, and AI in law.
- [r/LawFirm](https://reddit.com/r/lawfirm) - Focuses on the business of law. Highly active discussions on practice management software, marketing, and tech stacks.
- [r/Lawyers](https://reddit.com/r/lawyers) - *Private community for verified lawyers only.* Frequently discusses the practical reality and adoption of legaltech tools.
- [r/artificial](https://reddit.com/r/artificial) - Not law-specific, but frequently hosts high-level discussions on the intersection of AI, copyright, and legal compliance.

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

