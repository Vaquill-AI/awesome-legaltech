# Awesome Legaltech [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

<div align="center">
  <sup>Sponsored by</sup><br>
  <a href="https://vaquill.ai"><strong>Vaquill AI</strong></a>
  <br>
  <sub>AI-powered legal research platform for the United States. Federal and state case law, USC and CFR statutes, citation verification, contract analysis, and APIs for developers.</sub>
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
- [Deprecated / Archived](#deprecated--archived)

---

## APIs for Legal Data

Commercial and open APIs specifically designed for retrieving case law, statutes, and legal documents into applications.

- [Vaquill AI API](https://vaquill.ai/legal-api) - Developer API providing programmatic access to 8M+ US federal and state court opinions plus the complete US Code and CFR, with semantic search and citation verification. *(Sponsor)*
- [CourtListener REST API](https://www.courtlistener.com/help/api/) - **[🇺🇸 US]** Free Law Project API over 9M+ opinions, dockets, judges, and RECAP/PACER filings; free tier plus semantic search endpoint (Nov 2025).
- [LegiScan API](https://legiscan.com/legiscan) - **[🇺🇸 US]** Structured JSON for legislation in all 50 states + Congress; free tier (30K queries/month) with paid plans.
- [Open States API v3](https://docs.openstates.org/api-v3/) - **[🇺🇸 US]** Free REST API for US state legislators, bills, votes, and committees across 50 states + DC + territories.
- [USPTO Open Data Portal API](https://data.uspto.gov/) - **[🇺🇸 US]** Free patent file-wrapper, search, and PEDS endpoints; replaces the legacy beta ODP.
- [EPO Open Patent Services (OPS)](https://www.epo.org/searching-for-patents/data/web-services/ops.html) - **[🇪🇺 EU]** Free RESTful API for EPO/WIPO/national patent bibliographic data, family info, and legal status (registered-user quota).
- [The Lens Patent & Scholarly API](https://www.lens.org/lens/user/subscriptions) - **[🌍 Global]** 140M+ global patent records and scholarly citations; free tier for academic/non-commercial use.
- [EUR-Lex Webservice & CELLAR SPARQL](https://eur-lex.europa.eu/content/help/data-reuse/webservice.html) - **[🇪🇺 EU]** Free SOAP/SPARQL/REST endpoints for EU legislation, ECLI-indexed case law, and CDM-RDF metadata across 24 languages.
- [JudiLibre API (Cour de cassation)](https://api.gouv.fr/les-api/api-judilibre) - **[🇫🇷 France]** Official French Supreme Court open API for judicial case-law via PISTE; free with registration.
- [UK Parliament Open Data API](https://developer.parliament.uk/) - **[🇬🇧 UK]** REST APIs for Westminster procedural data plus the [Hansard API](https://hansard-api.parliament.uk/) for debates in JSON/XML under the Open Parliament Licence.
- [Bundestag Open Data](https://www.bundestag.de/services/opendata) - **[🇩🇪 Germany]** Plenary protocols and Drucksachen since 1949 as XML/JSON; legislative-process tracking via the DIP API.
- [Regulations.gov API](https://open.gsa.gov/api/regulationsgov/) / [Federal Register API](https://www.federalregister.gov/developers/documentation/api/v1) - **[🇺🇸 US]** GSA REST APIs for federal rules, dockets, and public comments; complementary daily Federal Register API.

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
- [ContextGem](https://github.com/shcherbak-ai/contextgem) - **[Open Source]** Python framework for LLM-based extraction from legal and business documents with declarative concept/aspect schemas.
- [Opennyai](https://github.com/OpenNyAI/Opennyai) - **[Open Source]** End-to-end Python NLP pipeline for Indian legal documents (NER, rhetorical-role labeling, summarization).
- [CiteURL](https://github.com/raindrum/citeurl) - **[Open Source]** Extensible Python citation parser that turns US/UK/EU legal citations into hyperlinks; complements Eyecite with broader jurisdictional templates.
- [Open Australian Legal Corpus Creator](https://github.com/isaacus-dev/open-australian-legal-corpus-creator) - **[Open Source]** Scripts to build the open multijurisdictional corpus of Australian legislation and case law.

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
- [HUPD (Harvard USPTO Patent Dataset)](https://huggingface.co/datasets/HUPD/hupd) - **[🇺🇸 EN]** - **[4.5M+]** - Inventor-submitted US utility patent applications 2004-2018 for patentability, classification, and summarization tasks (NeurIPS 2023).
- [IL-TUR](https://huggingface.co/datasets/Exploration-Lab/IL-TUR) - **[🇮🇳 EN + 9 Indic]** - **[~176K]** - Indian legal text understanding & reasoning benchmark across 8 tasks (NER, rhetorical roles, judgment prediction, bail, statute ID, retrieval, summarization, MT); ACL 2024.
- [gitlaw-jp](https://github.com/aluqas/gitlaw-jp) - **[🇯🇵 JA]** - **[Large]** - Complete Japanese legislation tracked as a Git repository, enabling diffs and historical analysis.
- [open-source-legislation](https://github.com/spartypkp/open-source-legislation) - **[🌍 Multi]** - SQL knowledge-graph format for global legislation with Python/TypeScript SDKs for LLM training and RAG.
### Legal Judgment Prediction (LJP)

Datasets for predicting case outcomes, charges, or penalties from court documents.

- [CAIL2018](https://github.com/china-ai-law-challenge/CAIL2018) - **[🇨🇳 China]** - **[ZH]** - **[2.6M cases]** - Charge, penalty, article prediction
- [ECtHR Dataset](https://huggingface.co/datasets/coastalcph/ecthr_cases) - **[🇪🇺 ECHR]** - **[EN]** - **[11K cases]** - Article violation prediction
- [ILDC (Indian Legal Documents Corpus)](https://github.com/Exploration-Lab/CJPE) - **[🇮🇳 India]** - **[EN]** - **[34K cases]** - Court judgment prediction and explanation
- [NyayaAnumana](https://huggingface.co/datasets/Dnyanesh1/NyayaAnumana) - **[🇮🇳 India]** - **[EN]** - **[700K+ cases]** - Largest corpus of Indian legal cases for LJP
- [CaseSumm](https://huggingface.co/datasets/ChicagoHAI/CaseSumm) - **[🇺🇸 US SCOTUS]** - **[EN]** - **[25.6K opinions]** - Paired opinions + official syllabuses
- [IndianBailJudgments-1200](https://huggingface.co/datasets/SnehaDeshmukh/IndianBailJudgments-1200) - **[🇮🇳 India]** - **[EN]** - **[1.2K judgments]** - Bail decisions with 20+ structured attributes
- [The Supreme Court Database](http://scdb.wustl.edu) - **[🇺🇸 US]** - **[EN]** - **[All SCOTUS cases since 1791]** - Votes, outcomes, justice ideology
### Legal Text Classification

- [LexGLUE](https://github.com/coastalcph/lex-glue) - **[🌍 Multi]** - **[EN]** - 7-task benchmark: EURLEX, ECHR, LEDGAR, SCOTUS, ContractNLI, CaseHOLD, ECtHR
- [LEDGAR](https://huggingface.co/datasets/coastalcph/ledgar) - **[🇺🇸 US]** - **[EN]** - 60K+ contract provisions with 12.6K labels
- [CUAD](https://www.atticusprojectai.org/cuad) - **[🇺🇸 US]** - **[EN]** - 510 annotated contracts, 41 clause types, 13K+ expert labels
- [AsyLex](https://huggingface.co/datasets/joelito/AsyLex) - **[🇨🇭 Swiss]** - **[FR/DE]** - 59K documents; 19K human-annotated entities for Refugee Law
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
- [Swiss Judgment Summarization (SLDS)](https://arxiv.org/abs/2410.13456) - **[🇨🇭 DE/FR/IT]** - **[~18K rulings]** - Multilingual Swiss court ruling-to-headnote summarization dataset (NLLP 2024)
### Legal Semantic Search & Information Retrieval

- [opinions-synthetic-query-512](https://huggingface.co/datasets/Free-Law-Project/opinions-synthetic-query-512) - **[🇺🇸 US]** - **[EN]** - High-quality Free Law Project synthetic queries for finetuning legal semantic search
- [LexTREC](https://trec.nist.gov/data/legal.html) - **[🇺🇸 US]** - **[EN]** - Foundational NIST benchmark dataset for legal e-discovery containing real corporate data with expert judgments
- [CLERC](https://github.com/neelguha/legal-ml-datasets) - **[🇺🇸 US]** - **[EN]** - Case Law Evaluation and Retrieval Corpus for dense retrieval
- [Massive Legal Embedding Benchmark (MLEB)](https://isaacus.com/mleb) - **[🌍 Multi]** - **[Open]** - A multidomain open-source benchmark for legal information retrieval.
- [german_legal_sentences](https://huggingface.co/datasets/lavis-nlp/german_legal_sentences) - **[🇩🇪 Germany]** - **[DE]** - Semantic sentence matching and citation recommendation
- [JurisTCU](https://arxiv.org/abs/2503.08379) - **[🇧🇷 PT-BR]** - **[16K docs / 150 queries]** - Brazilian Federal Court of Accounts jurisprudence IR dataset with graded relevance judgments (LREV 2025)
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
- [AdaptLLM/law-LLM](https://huggingface.co/AdaptLLM/law-LLM) - **[LLaMA-1 7B]** - **[EN]** - Domain-adapted LLM trained via reading-comprehension on a large English legal corpus.
- [AdaptLLM/law-chat](https://huggingface.co/AdaptLLM/law-chat) - **[LLaMA-2-Chat 7B]** - **[EN]** - **[Llama2]** - Conversational legal Q&A model adapted with reading-comprehension pretraining.
- [InternLM-Law](https://github.com/InternLM/InternLM-Law) - **[InternLM2-Chat 7B]** - **[ZH]** - **[Apache 2.0]** - Shanghai AI Lab Chinese legal LLM SFT-tuned on ~1M legal examples; tops LawBench on 13/20 subtasks (COLING 2025).
- [Lawyer-LLaMA](https://github.com/AndrewZhe/lawyer-llama) - **[LLaMA-13B]** - **[ZH]** - PKU's continually-pretrained Chinese legal model with judicial-exam and legal-consultation SFT data.
- [Fuzi.Mingcha](https://github.com/irlab-sdu/fuzi.mingcha) - **[ChatGLM]** - **[ZH]** - Judicial LLM from Shandong U. + China U. of Political Science & Law; statute retrieval, syllogistic reasoning, judicial dialogue.
- [Aalap-Mistral-7B](https://huggingface.co/opennyaiorg/Aalap-Mistral-7B-v0.1-bf16) - **[Mistral 7B]** - **[EN — 🇮🇳 focus]** - **[Apache 2.0]** - OpenNyAI's 32K-context instruction-tuned model for Indian paralegal tasks; matches/beats GPT-3.5-turbo on 65% of in-domain tests.
- [llama3-8b-Lawyer](https://huggingface.co/StevenChen16/llama3-8b-Lawyer) - **[Llama-3-ChatQA 8B]** - **[EN/ZH]** - **[MIT]** - LoRA-fine-tuned legal Q&A model trained on `dzunggg/legal-qa-v1` for clarifying-question lawyer-style dialogue.
- [SL-Llama-3.2-1b](https://huggingface.co/speedlegal/SL-Llama-3.2-1b) - **[Llama-3.2 1B]** - **[EN]** - **[Llama 3.2]** - PEFT/LoRA model fine-tuned on CUAD for contract clause review and risk-flagging at edge-deployable size.
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

- [Vaquill AI MCP](https://github.com/vaquill-AI/vaquill-mcp) - MCP server that connects Claude / Cursor / Windsurf / VS Code to 8M+ US federal and state court opinions plus the US Code and CFR. *(Sponsor)*
- [CourtListener MCP (DefendTheDisabled)](https://github.com/DefendTheDisabled/courtlistener-mcp) - Connects AI agents to CourtListener with semantic search, hybrid search, and citation verification to mitigate hallucination.
- [CourtListener MCP (Travis-Prall)](https://github.com/Travis-Prall/court-listener-mcp) - MCP Server for accessing CourtListener case data, court opinions, and eCFR federal regulations.
- [CourtListener MCP (khizar-anjum)](https://github.com/khizar-anjum/courtlistener-mcp) - MCP server built for searching cases by natural language legal problems across 3,352 U.S. courts.
- [agentic-ops/legal-mcp](https://github.com/agentic-ops/legal-mcp) - Comprehensive MCP server for legal workflows. Integrates AI assistants with legal databases and case management systems (Clio, etc.).
- [LegalContext MCP](https://mcp.so/server/legalcontext) - Open-source MCP server bridging law firm document management systems with AI assistants.
- [adeu (Agentic DOCX Redlining Engine)](https://github.com/dealfluence/adeu) - MCP Server enabling LLMs to inject native Track Changes and Comments into Word documents.
- [Master Claude for Legal](https://github.com/sboghossian/master-claude-for-legal) - **[Open Source]** - **[MIT]** - Skill pack for legal teams using Claude with MCP connectors. 10 reference docs (privilege, verification, long documents, practice areas), 5 starter skills (NDA triage, version diff, meeting brief, citation verifier, status synthesis), 3 firm templates. Includes the source Anthropic legal-webinar transcript and 51-question dataset.
- [Korean Law MCP](https://github.com/chrisryugj/korean-law-mcp) - **[🇰🇷 Korea]** 17 MCP tools wrapping 41 Korean government legal APIs; includes citation verification, impact graph, and time-travel diff.
- [Yargı MCP](https://github.com/saidsurucu/yargi-mcp) - **[🇹🇷 Turkey]** MCP server for Turkish legal databases (Yargıtay, Danıştay, Anayasa Mahkemesi).
- [MCP Taiwan Legal DB](https://github.com/lawchat-oss/mcp-taiwan-legal-db) - **[🇹🇼 Taiwan]** Taiwan Judicial Yuan judgments + national statute database via MCP.
- [ayunis-legal-mcp](https://github.com/ayunis-core/ayunis-legal-mcp) - **[🇩🇪 Germany]** MCP server exposing German legal codes (Gesetze-im-Internet).
- [Pasal MCP](https://github.com/ilhamfp/pasal) - **[🇮🇩 Indonesia]** MCP + REST + web app giving AI grounded access to 40k+ Indonesian regulations.
- [auslaw-mcp](https://github.com/russellbrenner/auslaw-mcp) - **[🇦🇺 🇳🇿 AU/NZ]** MCP server searching AustLII case law and legislation with OCR for scanned PDFs.
- [law-scrapper-mcp](https://github.com/numikel/law-scrapper-mcp) - **[🇵🇱 Poland]** MCP server for Polish legal acts via the Sejm API.
- [Emilie](https://github.com/veronica-builds/emilie) - **[🇨🇭 Switzerland]** Swiss sovereign legal AI; Mike fork extended with MCP client and local Apertus model support.
- [Mahender22/legal-mcp](https://github.com/Mahender22/legal-mcp) - **[🇺🇸 US]** 18 MCP tools across CourtListener case law (4M+ opinions, 400+ US courts), PACER federal filings, and Clio practice-management.
- [EU Compliance MCP](https://github.com/Ansvar-Systems/EU_compliance_MCP) - **[🇪🇺 EU]** MCP exposing 61 EU regulations (GDPR, AI Act, DORA, NIS2, MiFID II, eIDAS 2.0, CRA) with 4,095 articles and cross-regulation comparison.
- [mcp-server-legifrance](https://github.com/pylegifrance/mcp-server-legifrance) - **[🇫🇷 France]** MCP that wraps the official Légifrance/PISTE API for searching French statutes, codes, and judicial jurisprudence.
- [droit-francais-mcp](https://github.com/jmtanguy/droit-francais-mcp) - **[🇫🇷 France]** Unified MCP over Légifrance (legislation/codes/decrees) plus JudiLibre (case law) with PISTE-auth.
- [French Law MCP](https://github.com/Ansvar-Systems/French-law-mcp) - **[🇫🇷 France]** MCP exposing 3,958 French statutes (Code civil, Code pénal, Code du travail, Code de commerce, Loi I&L) verified against official sources.
- [SEC EDGAR MCP](https://github.com/stefanoamorelli/sec-edgar-mcp) - **[🇺🇸 US]** MCP for SEC EDGAR filings, financial statements, and insider-trading data — useful for securities and corporate-disclosure workflows.
- [mcp-cerebra-legal-server](https://github.com/yoda-digital/mcp-cerebra-legal-server) - MCP providing structured legal-reasoning tools (`legal_think`, follow-up, completion) with domain templates for contract, consumer-protection, and French procurement analysis.

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
- [Prest0](https://prest0.ai) - **[AI-Native]** Enterprise bilingual (English/Spanish) legal AI platform that deploys a dedicated AI agent per law firm on an isolated VM with persistent memory, Twilio voice + SMS intake, deep research, and legal-grade document drafting — purpose-built for immigration, workers' compensation, and employment law.
- [HODOS + CASEFLOW](https://hodos-caseflow.vercel.app) - **[AI-Native]** Bilingual (EN/ES) legal AI platform with per-firm multi-tenant isolation enforced by RLS-in-CI. Practice areas: immigration, PI, workers' comp, family. North Carolina jurisdictional depth (NC scaffolds across 4 verticals with county variance). 14 AI agents with layered prompt-injection defense, LEDES bill drafting, 101 USCIS/court form scaffolds with daily edition-change watcher, Retell + LiveKit voice intake. Production scale: 27,513-matter Clio mirror in ~21 hours. Anchor: Vasquez Law Firm (NC, 30+ years).
- [Suzie Law](https://github.com/firelex/suzielaw) - **[Open Source]** Self-hostable Harvey alternative built on Team Suzie: chat assistant ("Counsel"), 12 practice-area personas, 160+ agentic workflows, document Q&A with citations, tracked-change redlines, DOCX drafting, and unified legal research across 19 jurisdictions (US, UK, EU, FR, DE, IN, AU, etc.).
- [Mike](https://github.com/willchen96/mike) - **[Open Source]** Legal document assistant (Next.js + Express + Supabase + S3/R2) that lets users chat with uploaded documents using Anthropic, Gemini, or OpenAI models; BYOK per user. Hosted at [mikeoss.com](https://mikeoss.com).
- [Crosby](https://crosby.ai/) - **[AI-Native]** Sequoia/Index/Bain-backed "AI law firm" that reviews NDAs, MSAs, and DPAs in under an hour for startups like Cursor and Stripe; raised $60M Series B at $400M valuation in 2026.
- [Manifest OS](https://manifestos.com/) - **[AI-Native]** AI-native law firm operating system (immigration first, tax next); $60M Series A at $750M valuation led by Menlo Ventures (April 2026) — largest Series A in legaltech history.
- [Enter](https://www.getenter.ai/en) - **[AI-Native]** Brazilian AI agents for mass consumer and labor litigation serving Nubank, iFood, and LATAM; LatAm's first legal-AI unicorn after a $100M round led by Founders Fund and Sequoia (May 2026).
- [Lexroom.ai](https://lexroom.ai/) - **[AI-Native]** Italian vertical GenAI platform for legal research, drafting, and document analysis across EU jurisdictions; €16.2M Series A led by Base10 (Sept 2025).
- [Vesence](https://www.vesence.com/) - **[AI-Native]** Agentic AI for law firms embedded in Word, Outlook, Excel, and PowerPoint for drafting, formatting, and quality checks; $9M seed (Oct 2025).
- [Eve Legal](https://www.eve.legal/) - **[AI-Native]** End-to-end AI for plaintiff law firms (intake, medical chronologies, demand letters, discovery); $103M Series B at $1B+ valuation (Sept 2025) — plaintiff-AI unicorn alongside EvenUp.
- [Supio](https://www.supio.com/) - **[AI-Native]** Agentic AI for personal injury and mass tort firms covering intake, medical chronologies, and demand drafting; $60M Series B led by Sapphire Ventures (April 2025).
- [GC AI](https://gc.ai/) - **[AI-Native]** AI platform purpose-built for in-house legal teams (contracts, policies, compliance, employment) serving News Corp, Skims, Vercel, and Zscaler; $60M Series B at $555M valuation (Nov 2025).
- [Orbital](https://www.orbital.tech/) - **[AI-Native]** UK-origin AI for real estate due diligence and conveyancing used by Clifford Chance and Macfarlanes; powers 200,000+ transactions annually. $60M Series B led by Brighton Park Capital (Jan 2026).
- [Stella](https://github.com/stella/stella) - **[Open Source]** Open-source legal workspace built in TypeScript.
- [CourtListener (source)](https://github.com/freelawproject/courtlistener) - **[Open Source]** Django source for the largest open US court-data archive (RECAP, opinions, oral arguments, judges) maintained by Free Law Project.
- [dd-agents](https://github.com/zoharbabin/due-diligence-agents) - **[Open Source]** M&A due diligence platform orchestrating 13 AI agents (Legal, Finance, Commercial, ProductTech, Cybersecurity, HR, Tax, Regulatory, ESG + Judge, Red Flag Scanner, Executive Synthesis, Acquirer Intelligence) across a 38-step pipeline. Interactive chat mode with 14 MCP tools for citation verification, cross-contract search, and document generation. Neurosymbolic cross-domain analysis routes findings between domains via deterministic rules. Apache 2.0, `pip install dd-agents`.

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

<details>
<summary>🌍 Official Government Portals (Curated, beyond WorldLII/CommonLII coverage)</summary>

Direct links to canonical government legal-data sources for jurisdictions where the WorldLII/CommonLII/SAFLII/AsianLII coverage above points to aggregators or has thin entries.

**Latin America**
- [Ley Chile (BCN)](https://www.bcn.cl/leychile/) - 🇨🇱 Official consolidated database of Chilean laws, decrees, and Supreme Court jurisprudence linked to each norm (free).
- [SUIN-Juriscol](https://www.suin-juriscol.gov.co/) - 🇨🇴 Colombian Ministerio de Justicia portal; 87k+ norms from 1864 plus 13k+ Constitutional Court, Council of State, and Supreme Court judgments.
- [SPIJ — Sistema Peruano de Información Jurídica](https://spijweb.minjus.gob.pe/) - 🇵🇪 Ministry of Justice portal; constitutions, codes, laws from 1904, regulations from 1978, constitutional/administrative jurisprudence.
- [IMPO — Centro de Información Oficial](https://www.impo.com.uy/) - 🇺🇾 Uruguay's official Diario Oficial portal with complete legislative history from Law No. 1.
- [Gaceta Oficial de Bolivia](http://www.gacetaoficialdebolivia.gob.bo/) - 🇧🇴 Official Gazette of the Plurinational State of Bolivia.
- [Gaceta Oficial Paraguay](https://www.gacetaoficial.gov.py/) - 🇵🇾 Daily official gazette publishing Paraguayan laws and decrees.

**MENA & Arabian Peninsula**
- [Bureau of Experts at the Council of Ministers](https://www.boe.gov.sa/en/Pages/default.aspx) - 🇸🇦 Saudi Arabia's official portal for laws, regulations, royal decrees (Arabic/English).
- [UAE Legislations Platform](https://uaelegislation.gov.ae/en) - 🇦🇪 Unified portal from the General Secretariat of the UAE Cabinet covering federal laws, executive regulations, and resolutions.
- [Al-Meezan](https://www.almeezan.qa/Default.aspx?language=en) - 🇶🇦 Qatar's Ministry of Justice portal covering all in-force and historical Qatari legislation since 1961.
- [Knesset National Legislation Database](https://main.knesset.gov.il/en/activity/pages/basiclaws.aspx) - 🇮🇱 Official Knesset database of Israeli laws and parliamentary process (Hebrew/English).
- [Manshurat](https://manshurat.org/) - 🇪🇬 Searchable Egyptian Presidency Official Gazette plus other Arab-region legislation.
- [SGG Maroc — Bulletin Officiel](https://www.sgg.gov.ma/BulletinOfficiel.aspx) - 🇲🇦 Morocco's Secrétariat Général du Gouvernement Official Bulletin (Arabic + French editions).

**Southeast Asia**
- [Singapore Statutes Online](https://sso.agc.gov.sg/) - 🇸🇬 Attorney-General's Chambers free database of current and historical Singapore legislation and bills.
- [AGC Malaysia Federal Legislation](https://lom.agc.gov.my/) - 🇲🇾 Official electronic Gazette publishing all Malaysian Acts and subsidiary legislation since 2011.
- [Ratchakitcha — Royal Thai Government Gazette](https://ratchakitcha.soc.go.th/) - 🇹🇭 Official Gazette where laws take force on publication; archive from 1858 (Thai).
- [VBPL — Vietnam National Legal Documents Database](https://vbpl.vn/) - 🇻🇳 Ministry of Justice database (relaunched April 2024 with article-level structured data).
- [Supreme Court E-Library (Philippines)](https://elibrary.judiciary.gov.ph/) - 🇵🇭 Official Supreme Court online repository of decisions and Philippine Reports.

**South Asia**
- [Pakistan Code](https://pakistancode.gov.pk/) - 🇵🇰 Ministry of Justice consolidated federal statutes (English).
- [Laws of Bangladesh](http://bdlaws.minlaw.gov.bd/) - 🇧🇩 Ministry of Law information system with up-to-date Bangladesh legislation (English/Bangla).
- [Parliament of Sri Lanka — Acts & Bills](https://www.parliament.lk/en/business-of-parliament/acts-bills) - 🇱🇰 All Acts and amendments 1948-present (English/Sinhala/Tamil).

**East Asia**
- [Hong Kong e-Legislation (HKeL)](https://www.elegislation.gov.hk/) - 🇭🇰 Department of Justice's official, verified consolidated legislation portal — sole authoritative source since 2025.
- [National Database of Laws and Regulations (NPC)](https://flk.npc.gov.cn/) - 🇨🇳 Official NPC database covering statutes, legislative interpretations, and major decisions across all seven branches of Chinese law.

**Eastern Europe & former USSR**
- [Official Internet Portal of Legal Information](http://pravo.gov.ru/) - 🇷🇺 Official daily-updated repository of Russian Federation laws and federal decrees.
- [Legislation of Ukraine](https://zakon.rada.gov.ua/laws/main/en/index) - 🇺🇦 Verkhovna Rada's official legal database with English interface.
- [Adilet LIS](https://adilet.zan.kz/eng) - 🇰🇿 Kazakh Ministry of Justice Legal Information System (Kazakh/Russian/English).
- [e-Sbírka](https://zakony.gov.cz/) - 🇨🇿 Official digital collection of Czech laws launched 2024 with historical versions and EUR-Lex/N-Lex integration.
- [Slov-Lex](https://www.slov-lex.sk/web/en) - 🇸🇰 Slovak Ministry of Justice portal with binding consolidated electronic texts (Slovak/English).
- [Nemzeti Jogszabálytár (NJT)](https://njt.hu/) - 🇭🇺 Hungary's free National Legislation Database run by Magyar Közlöny.
- [Portal Legislativ](https://legislatie.just.ro/) - 🇷🇴 Romanian Ministry of Justice consolidated portal for Monitorul Oficial Part I.
- [Lex.bg](https://lex.bg/) - 🇧🇬 Comprehensive Bulgarian legal database mirroring State Gazette content.
- [PIS-RS](https://pisrs.si/) - 🇸🇮 Slovenia's Pravno-informacijski sistem with Slovenian and EU legislation, case-law links.
- [Narodne novine](https://www.nn.hr/) - 🇭🇷 Croatian Official Gazette publishing laws, regulations, and constitutional court decisions.
- [Pravno-informacioni sistem RS](http://www.pravno-informacioni-sistem.rs/) - 🇷🇸 Legal Information System of Serbia with electronic Official Gazette and case law.
- [Riigi Teataja](https://www.riigiteataja.ee/en/) - 🇪🇪 Sole official electronic State Gazette of Estonia since 2010 (Estonian/English).
- [Likumi.lv](https://likumi.lv/) - 🇱🇻 Official portal of consolidated Latvian legal acts (Latvian + selected English).
- [e-TAR](https://www.e-tar.lt/) - 🇱🇹 Lithuania's official register of legal acts.

**Nordic**
- [Retsinformation](https://www.retsinformation.dk/) - 🇩🇰 Official joint Danish legal-information system with statutes, executive orders, Folketing documents from 1985, and Ombudsman opinions.
- [Lagrummet](https://www.lagrummet.se/) - 🇸🇪 Domstolsverket-coordinated portal aggregating SFS legislation, preparatory works, and higher-court case law.
- [Lovdata](https://lovdata.no/) - 🇳🇴 Foundation-run portal with Norsk Lovtidend, consolidated legislation, Supreme Court rulings (free + paid Pro tier).
- [Finlex](https://www.finlex.fi/en) - 🇫🇮 Ministry of Justice's 30+ databanks: legislation, case law, treaties, government proposals (Finnish/Swedish/English); also [Semantic Finlex](https://data.finlex.fi/) SPARQL endpoint.
- [Stjórnartíðindi](https://www.stjornartidindi.is/) - 🇮🇸 Iceland Government Gazette online edition.

**Oceania**
- [New Zealand Legislation](https://www.legislation.govt.nz/) - 🇳🇿 Parliamentary Counsel Office portal with all Bills, Acts, and Legislative Instruments.

</details>

#### International Courts & Tribunals
- [International Court of Justice (ICJ)](https://www.icj-cij.org/decisions) - All judgments, orders, and advisory opinions since 1946; full PDF advanced search (English/French).
- [ICC Case Law Database](https://www.legal-tools.org/cld) - 6,000+ legal findings from International Criminal Court judgments and decisions since 2004 (English/French).
- [WTO Dispute Settlement Gateway](https://www.wto.org/english/tratop_e/dispu_e/dispu_e.htm) - Panel and Appellate Body reports searchable by complainant, respondent, and agreement, with the WTO Analytical Index.
- [Inter-American Court of Human Rights](https://corteidh.or.cr/casos_sentencias.cfm?lang=en) - Contentious cases, advisory opinions, provisional measures, and monitoring decisions (Spanish/English/Portuguese).
- [ITLOS — International Tribunal for the Law of the Sea](https://www.itlos.org/en/main/cases/list-of-cases/) - All UNCLOS proceedings with pleadings, judgments, and webcasts (English/French).
- [Permanent Court of Arbitration (PCA)](https://pca-cpa.org/cases/) - Inter-state, investor-state, and commercial arbitration awards and procedural orders.
- [ICSID Case Database](https://icsid.worldbank.org/cases/case-database) - Searchable repository of all registered ICSID investor-state arbitrations with decisions, awards, and arbitrator profiles.
- [African Court on Human and Peoples' Rights](https://www.african-court.org/cpmt/) - Official AfCHPR case database with judgments, procedural decisions, provisional measures, and advisory opinions.

#### Global & Multi-Jurisdictional
- [WorldLII](https://www.worldlii.org/databases.html) - Federated gateway to 2,000+ legal databases across 200+ jurisdictions via national LIIs.
- [CommonLII](http://www.commonlii.org) - Searchable legal databases from 60+ Commonwealth and common law jurisdictions.
- [GlobaLex (NYU)](https://www.nyulawglobal.org/globalex/) - Comprehensive research guides and database listings for international, comparative, and foreign law.

#### United States
- [Vaquill AI](https://vaquill.ai) - Free AI legal research across 8M+ US federal and state court opinions plus USC and CFR, with citation verification. *(Sponsor)*
- [CourtListener](https://www.courtlistener.com) - Free open case law search with API access. 9M+ opinions.
- [PACER](https://pacer.uscourts.gov) - Official US federal court docket and document system.
- [Caselaw Access Project](https://case.law) - 6.9M US court decisions, 1600s-2020. Free bulk API.
- [GovInfo](https://www.govinfo.gov) - US federal legislation, regulations, and congressional records. Bulk data/API available.
- [eCFR](https://www.ecfr.gov) - Up-to-date Code of Federal Regulations with a full bulk API.
- [OpenStates](https://openstates.org) - Open-source platform tracking US state legislation in real time.
- [AI Laws by State](https://www.ailawsbystate.com) - Free 50-state tracker for U.S. artificial intelligence legislation, sourced from primary state legislature feeds. Covers bill status, effective dates, penalty structures, and topic categorization (deepfakes, hiring, healthcare AI, disclosure, bias audits).
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

#### Germany
- [OpenJur](https://openjur.de) - Open-source database of German court decisions. Community-maintained.
- [OpenLegalData](https://openlegaldata.io) - German court decisions and legislation. REST API available.
- [Gesetze im Internet](https://www.gesetze-im-internet.de) - Official German federal law portal (all statutes). Free.

#### France
- [Legifrance](https://www.legifrance.gouv.fr) - Official French legal portal. All statutes, regulations, and major court decisions.
- [Judilibre (Cour de Cassation)](https://www.courdecassation.fr/acces-rapide/judiciaire-judilibre) - Open API for French Supreme Court decisions. GDPR-anonymized.

#### India
- [Indian Kanoon](https://indiankanoon.org) - Free access to Indian court judgments, statutes, and legal documents.
- [India Code](https://www.indiacode.nic.in/) - Central repository of all Central and State Acts and subordinate legislation.
- [Supreme Court of India](https://sci.gov.in) - Official portal with judgments from the Supreme Court of India.
- [eCourts Services](https://services.ecourts.gov.in) - Unified portal for Indian district and High Court case status.

#### Turkey
- [Avukatistan](https://avukatistan.com) - Turkish legal research and lawyer discovery platform with case law, legislation, legal questions, and practitioner profiles.

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

### Open-Source AI Research Tools

- [LawGlance](https://github.com/lawglance/lawglance) - **[Open Source]** Free RAG-based AI legal assistant with multi-jurisdictional knowledge bases.
- [OLAW (Harvard LIL)](https://github.com/harvard-lil/olaw) - **[Open Source]** Tool-based RAG workbench from Harvard Library Innovation Lab for legal AI UX research.
- [Justicio](https://github.com/bukosabino/justicio) - **[🇪🇸 Spain]** RAG assistant over the Boletín Oficial del Estado (BOE).
- [Lex (i.AI)](https://github.com/i-dot-ai/lex) - **[🇬🇧 UK]** Open UK legal API for AI agents and researchers from the UK Government's Incubator for AI.
- [GraphRAG Legal Cases](https://github.com/Azure-Samples/graphrag-legalcases-postgres) - **[Open Source]** Legal-research copilot reference architecture using GraphRAG on PostgreSQL (Azure Samples).
- [legal-tech-chat](https://github.com/tomasonjo-labs/legal-tech-chat) - **[Open Source]** Reference pipeline: CUAD extraction → Neo4j knowledge graph → LangGraph agent.

### Commercial AI Research Platforms
- [Vaquill AI](https://vaquill.ai) - **[AI-Native]** US legal research platform with agentic workflows, MCP server, and an API for developers building on top of US case law and statutes. *(Sponsor)*
- [Leya](https://leya.law) - **[AI-Native]** Agentic research and legal memo generation.
- [Paxton AI](https://paxton.ai) - **[AI-Native]** Jurisdiction-aware AI legal answers.
- [EvenUp](https://evenuplaw.com) - **[AI-Native]** Agentic demand letter generation and research for personal injury.
- [Lexlegis.AI](https://lexlegis.ai) - **[AI-Native]** Indian legal research LLM trained on 10M+ documents.
- [HAQQ Legal AI](https://haqq.ai) - **[AI-Native]** Bilingual Arabic/English legal research, contract review, and case law search for MENA jurisdictions (Lebanon, GCC, Egypt).
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
- [Accord Project Template Archive](https://github.com/accordproject/template-archive) - **[Open Source]** Smart legal contracts and templating system (Cicero / Concerto).
- [Gavel (formerly Documate)](https://www.gavel.io/) - **[Established]** No-code document automation + online legal product builder used to ship apps in estate planning, family law, real estate, probate, and immigration.

---

## Intellectual Property & Patent Tech

Platforms for patent searching, analytics, and intellectual property portfolio management.

- [PatSnap](https://www.patsnap.com) - **[AI-Native]** Patent analytics and intelligence powered by AI.
- [Anaqua](https://www.anaqua.com) - **[Established]** Comprehensive IP management system.
- [AltLegal](https://www.altlegal.com) - **[Established]** Automated trademark docketing and protection.
- [Trademarkia](https://www.trademarkia.com) - **[Established]** Global trademark search engine and registration platform.
- [Solve Intelligence](https://www.solveintelligence.com/) - **[AI-Native]** YC-backed AI for patent drafting, prosecution, and litigation used by DLA Piper, Intel, and Amgen; $40M Series B led by Visionaries (Dec 2025).
- [DeepIP](https://deepip.ai/) - **[AI-Native]** French-American AI platform spanning the full patent lifecycle (drafting, drawings, FTO, landscaping); $25M Series B led by Korelya Capital and Serena.
- [Ankar](https://ankar.ai/) - **[AI-Native]** Palantir-alumni-built AI patent OS for idea generation, drafting, prosecution, and infringement detection; €17M Series A led by Atomico (Dec 2025).
- [Patlytics](https://patlytics.ai/) - **[AI-Native]** AI patent intelligence engine for drafting, infringement detection, and invalidity analysis serving AmLaw 100 and Fortune 500; $14M Series A (Feb 2025).

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
- [Ivo](https://ivo.ai/) - **[AI-Native]** Enterprise contract review AI used by Uber, Shopify, IBM, Reddit, and Canva; $55M Series B at ~$355M valuation led by Blackbird (2025-2026).
- [SpotDraft](https://www.spotdraft.com/) - **[AI-Native]** India-headquartered CLM with on-device VerifAI for clause extraction and risk scoring; $54M Series B (Feb 2025) + $8M extension.
- [contract-review-agent](https://github.com/kipeum86/contract-review-agent) - **[Open Source]** Local-first AI agent that turns contracts into clause-level analysis with tracked-change DOCX redlines.
- [legal-redline-tools](https://github.com/evolsb/legal-redline-tools) - **[Open Source]** Generates tracked-changes Word docs and redline PDFs from AI contract reviews.

---

## Notarization & E-Signature

Platforms handling digital execution of documents and Remote Online Notarization (RON).

- [DocuSign](https://www.docusign.com) - **[Established]** The global standard for e-signatures and agreement clouds.
- [Proof (formerly Notarize)](https://www.proof.com) - **[Established]** Pioneer of Remote Online Notarization (RON).
- [OpenSign](https://github.com/OpenSignLabs/OpenSign) - **[Open Source]** Free open-source DocuSign alternative (Parse Server + React); 6.3k+ stars.

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
- [Theo AI](https://theoai.ai/) - **[AI-Native]** Predictive AI for litigation defense and settlement outcome forecasting for enterprise legal departments.
- [Briefpoint](https://briefpoint.ai/) - **[AI-Native]** Patented AI for drafting discovery requests/responses with "Bridge" client-response automation; used by 1,500+ firms.
- [Bridge Legal](https://bridgelegal.com/) - **[AI-Native]** Bridgify AI workflow stack for mass-tort and PI firms covering intake, court-required questionnaires, and lifecycle management.
- [Pattern Data](https://patterndata.ai/) - **[AI-Native]** HIPAA-compliant RAG-based engine that reads thousands of pages of medical records to score and structure mass-tort claims.
- [Steno](https://steno.com/) - **[Established]** Court-reporting agency + Steno Connect remote-deposition platform + "Transcript Genius" AI; closed $46M financing in 2024.
- [Veritext](https://www.veritext.com/) - **[Established]** National court reporting/deposition firm with Veritext Virtual, realtime transcription, and Exhibit Share.
- [Burford Capital](https://www.burfordcapital.com/) - **[Established]** NYSE/LSE-listed litigation funder ($12.1B+ committed since inception) financing single cases, portfolios, and asset recovery.
- [Omni Bridgeway](https://omnibridgeway.com/) - **[Established]** Global dispute-finance firm with ~A$3.5B cumulative capital across 11 funds, ASX-listed since 2001.
- [Qualia](https://www.qualia.com/) - **[Established]** Leading cloud title/escrow/closing platform with Qualia Clear AI for title commitments and curative-task recommendations; >1M professionals.
- [Doma](https://www.doma.com/) - **[Established]** Machine-learning title underwriting + instant fee balancing integrated with Chase, Wells Fargo, PennyMac; ~83% US residential coverage.

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
- [Klaro Legal](https://klaro.legal) - **[AI-Native]** Translates contracts, official letters, and tax notices into plain language using AI. Supports 8 languages (DE, EN, ES, FR, IT, PT, TR).
- [JustiGuide](https://justiguide.com/) - **[AI-Native]** AI immigration assistant (Dolores AI, trained on 1M+ cases) that scores visa eligibility, matches attorneys, and drafts filings in 12 languages; 47K+ users across 180+ countries.
- [Boundless Immigration](https://www.boundless.com/) - **[Established]** Software + expert legal guidance for family, employment, and citizenship cases; acquired Localyze in Oct 2025 ($73.8M raised).
- [Visalaw.ai](https://www.visalaw.ai/) - **[AI-Native]** SOC 2 Type II-certified immigration research/drafting platform co-developed with AILA on top of GPT-4 and AILA's Cookbook.
- [Docketwise](https://www.docketwise.com/) - **[Established]** Immigration-specific case management with dynamic form completion, billing, and CRM.
- [Hello Divorce](https://hellodivorce.com/) - **[Established]** Venture-backed "TurboTax for divorce" with document automation + on-demand lawyers, mediators, and divorce coaches in all 50 states.
- [Trust & Will](https://trustandwill.com/) - **[Established]** Largest US consumer estate-planning platform with attorney-network and AI features; raised $25M+ Series C (March 2025).
- [Wealth.com](https://www.wealth.com/) - **[AI-Native]** Estate-planning platform for RIAs/wirehouses with "Ester" AI doc extraction; underpins wealth managers running >$15T AUM.
- [SoloSuit](https://www.solosuit.com/) - **[AI-Native]** "TurboTax for debt-collection lawsuits" — auto-drafts answers and runs SoloSettle negotiations; has helped 350,000+ Americans protect $2.5B+ in debt.

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
- [Sphere](https://www.getsphere.com/) - **[AI-Native]** AI-native cross-border indirect tax (sales tax, VAT, GST) compliance engine serving Deel, Replit, and Lovable; $21M Series A led by a16z (Nov 2025).
- [Climate Case Chart](https://www.climatecasechart.com/) - **[Open / Academic]** Sabin Center + Arnold & Porter database of 2,600+ US and global climate-change cases across 54 jurisdictions, updated monthly.
- [Persefoni](https://www.persefoni.com/) - **[AI-Native]** "ERP of carbon" climate-accounting platform supporting CSRD, SEC climate rule, TCFD, and CDP disclosures for enterprises and financial institutions.

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
- [Recidiviz](https://www.recidiviz.org/) - **[Nonprofit]** ex-Google nonprofit building a standardized criminal-justice data layer + reentry/parole tools; live in 19 state corrections agencies.
- [Clear My Record (Code for America)](https://www.clearmyrecord.org/) - **[Nonprofit]** Code for America initiative powering automatic record-sealing/expungement; helped reduce or dismiss 144,000 California cannabis convictions.
- [World Justice Project Rule of Law Index](https://worldjusticeproject.org/rule-of-law-index/) - **[Nonprofit]** Annual data series measuring rule of law across 143 jurisdictions (95% of world population).
- [HiiL (Hague Institute for Innovation of Law)](https://www.hiil.org/) - **[Nonprofit]** Justice Accelerator (110+ startups funded since 2011), Justice Innovation Labs, and people-centred justice research.

## Foundational Research

Seminal papers that shaped the field of legal AI and NLP. Essential reading for anyone building in this space.

- [LEGAL-BERT: The Muppets straight out of Law School](https://arxiv.org/abs/2010.02559) - **[2020]** - First large-scale BERT models pretrained on EU/US legal text; established the domain-adaptation benchmark for legal NLP
- [LexGLUE: A Benchmark Dataset for Legal Language Understanding](https://arxiv.org/abs/2110.00976) - **[2022]** - 7-task legal NLP benchmark; the "GLUE for law"; drove standardized evaluation
- [LegalBench: A Collaboratively Built Benchmark for Legal Reasoning](https://arxiv.org/abs/2308.11462) - **[2023]** - 162-task benchmark built with practicing lawyers; most comprehensive LLM legal evaluation to date
- [GPT-4 Passes the Bar Exam](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233) - **[2023]** - Bommarito & Katz; showed LLMs can pass professional licensing exams; catalyzed investor and legal community attention
- [SaulLM-7B: A pioneering Large Language Model for Law](https://arxiv.org/abs/2403.03883) - **[2024]** - First open-weight LLM continually pretrained on 30B+ legal tokens with instruction tuning
- [MultiLegalPile: A 689GB Multilingual Legal Corpus](https://aclanthology.org/2024.acl-long.805/) - **[2024]** - Largest open multilingual legal pretraining dataset; 24 languages, 17 jurisdictions
- [Artificial Intelligence and Legal Analytics](https://www.cambridge.org/core/books/artificial-intelligence-and-legal-analytics/E7D705EEF392501A1DB180645917E7E0) - **[2017]** - Kevin Ashley; foundational textbook on AI and law; covers case-based reasoning, argument mining, and legal knowledge representation
- [Large Legal Fictions: Profiling Legal Hallucinations in LLMs](https://arxiv.org/abs/2401.01301) - **[2024]** - Dahl, Magesh, Suzgun & Ho (Stanford RegLab / Yale) — empirical study showing 69-88% hallucination rates on verifiable case questions (Journal of Legal Analysis 2024).
- [Hallucination-Free? Assessing the Reliability of Leading AI Legal Research Tools](https://arxiv.org/abs/2405.20362) - **[2024]** - Magesh et al. (Stanford RegLab) — first preregistered evaluation of Lexis+ AI, Westlaw AI-Assisted Research, and Ask Practical Law AI; 17-33% hallucination despite RAG claims.
- [SaulLM-54B & SaulLM-141B: Scaling Up Domain Adaptation for the Legal Domain](https://arxiv.org/abs/2407.19584) - **[2024]** - Colombo et al. (Equall) — 540B-token legal continued-pretraining recipe for Mixtral (NeurIPS 2024).
- [InternLM-Law: An Open Source Supervised Fine-tuned Large Language Model](https://arxiv.org/abs/2406.14887) - **[2024]** - Fei et al. (Shanghai AI Lab) — open-source Chinese legal LLM with 32K context, top of LawBench (COLING 2025).
- [NLP for the Legal Domain: A Survey](https://arxiv.org/abs/2410.21306) - **[2024]** - Katz et al. — most comprehensive recent legal-NLP survey of tasks, datasets, models, and challenges (ACM Computing Surveys 2025).
- [A Comprehensive Survey on Legal Summarization](https://arxiv.org/abs/2501.17830) - **[2025]** - Systematic survey of legal-summarization methods, datasets, and evaluation metrics.
- [A Reasoning-Focused Legal Retrieval Benchmark](https://arxiv.org/abs/2505.03970) - **[2025]** - Goebel et al. (CSLAW 2025) — retrieval benchmark emphasizing legal reasoning over surface matching.

---

## Peer-Reviewed Journals

Academic journals publishing peer-reviewed legal-technology, computational-law, and AI-and-law research.

- [Artificial Intelligence and Law (Springer)](https://link.springer.com/journal/10506) - Flagship peer-reviewed journal of formal/computational models of legal reasoning since 1992; IF 3.1 (2024).
- [Stanford Computational Antitrust](https://law.stanford.edu/codex-the-stanford-center-for-legal-informatics/projects/computational-antitrust/) - CodeX-hosted open-access journal led by Thibault Schrepel; cross-agency reports from 25 antitrust authorities.
- [Harvard Journal of Law & Technology (JOLT)](https://jolt.law.harvard.edu/) - Harvard Law's premier law-and-tech journal (Vol. 39 in 2025-26); also runs the JOLT Digest blog.
- [Berkeley Technology Law Journal (BTLJ)](https://btlj.org/) - America's first technology-law journal (est. 1985); 4 issues/year; Vol. 40 (2025) covers AI trade secrets, algorithmic liability, antitrust, privacy.
- [Law, Innovation and Technology (Taylor & Francis)](https://www.tandfonline.com/journals/rlit20) - Hybrid OA peer-reviewed journal on ICT, biotech, neurotech, robotics, and AI; IF 3.07 (2024).
- [Computer Law & Security Review (Elsevier)](https://www.sciencedirect.com/journal/computer-law-and-security-review) - Q1 Scopus/SSCI peer-reviewed journal on IT and computer-security law (6 issues/year since 1985); IF 4.89 (2024).
- [Indian Journal of Law and Technology (IJLT)](https://repository.nls.ac.in/ijlt/) - NLSIU Bangalore student-run open-access journal (est. 2005).

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
- [LegalBench-RAG](https://github.com/zeroentropy-ai/legalbenchrag) - First retrieval benchmark for legal RAG: 6,858 expert-annotated query/span pairs over 79M characters of NDAs, M&A agreements, commercial contracts, and privacy policies (arXiv:2408.10343).
- [LegalAgentBench](https://github.com/CSHaitao/LegalAgentBench) - LLM-agent benchmark in the Chinese legal domain: 17 real-world corpora, 37 tools, 300 annotated multi-hop reasoning + writing tasks (2024).
- [LEXam](https://github.com/LEXam-Benchmark/LEXam) - **[ICLR 2026]** Bilingual EN/DE law-school exam benchmark: 7,537 questions from 340 exams across 116 courses, mixing IRAC reasoning and MCQs.
- [LexEval](https://github.com/CSHaitao/LexEval) - **[🇨🇳 ZH]** Comprehensive Chinese legal LLM benchmark: 14,150 questions across 23 tasks covering memorization, understanding, application, and ethics.
- [ArabLegalEval](https://arxiv.org/abs/2408.07983) - **[🇸🇦 AR]** Multitask Arabic legal-knowledge benchmark over Saudi regulations, MMLU/LegalBench-style (Aug 2024).
- [ALARB](https://arxiv.org/abs/2510.00694) - **[🇸🇦 AR]** Arabic Legal Argument Reasoning Benchmark: 13K Saudi commercial-court cases with facts, court reasoning, verdicts, and cited regulations (2025).
- [ContractEval](https://arxiv.org/abs/2508.03080) - First benchmark for clause-level legal-risk identification in commercial contracts using CUAD; evaluates 4 proprietary + 15 open-source LLMs (2025).
- [MSLR (Multi-Step Legal Reasoning)](https://arxiv.org/abs/2511.07979) - **[🇨🇳 ZH]** First Chinese multi-step legal-reasoning benchmark structured around IRAC over real judicial decisions; unsaturated (o1-mini ~72% IRAC recall) (2025).
- [MASLegalBench](https://arxiv.org/abs/2509.24922) - Multi-agent-systems benchmark for deductive legal reasoning across Issue/Rule/Application/Conclusion stages (2025).
- [LegalEval-Q](https://arxiv.org/abs/2505.24826) - Regression-based framework evaluating quality (clarity, coherence, terminology) of LLM-generated legal text across 49 LLMs (2025).
- [LRAGE](https://github.com/hoorangyee/LRAGE) - Framework for evaluating RAG pipelines specifically adapted for the legal domain.
- [MLEB (source)](https://github.com/isaacus-dev/mleb) - Evaluation code for the multidomain MLEB leaderboard across 6 jurisdictions.
- [prinzbench](https://github.com/prinz-ai/prinzbench) - Benchmark ranking LLMs on legal research and obscure-information retrieval.

---

## Legal Ontologies & Knowledge Graphs

Structured vocabularies, ontologies, and knowledge graphs for representing legal concepts, relationships, and document structure.

- [EuroVoc](https://op.europa.eu/en/web/eu-vocabularies/dataset/-/resource?uri=http://publications.europa.eu/resource/dataset/eurovoc) - EU's multilingual thesaurus covering subjects of EU legislation. 7,000+ concepts in 24 languages. Used for tagging EUR-Lex documents.
- [LKIF-Core](https://github.com/RinkeHoekstra/lkif-core) - Legal Knowledge Interchange Format; OWL ontology for basic legal concepts (norms, agents, documents, time). Foundation for many legal knowledge systems.
- [SALI LMSS (Legal Matter Standard Specification)](https://www.sali.org) - Structured ontology for legal matter types, service types, and industry codes. Open standard for legal operations data.
- [Wikidata Legal Entities](https://www.wikidata.org/wiki/Wikidata:WikiProject_Law) - WikiProject Law: structured data on courts, cases, legislation, and legal concepts in Wikidata. Machine-readable and freely licensed.
- [PROLEG (Japanese Legal Ontology)](https://arxiv.org/abs/1404.0370) - Formal representation of Japanese civil law rules for logic-based legal reasoning. Developed at NII Tokyo.
- [ELI Ontology](https://data.europa.eu/eli/ontology) - European Legislation Identifier vocabulary for national/EU legislation metadata, built on FRBR; v1.5 + ELI Impact Ontology v1.0 (2024).
- [LRMoo](https://www.iflastandards.info/lrm) - IFLA Library Reference Model (object-oriented); 2024-25 successor to FRBRoo increasingly used for diachronic legal-norm modeling and graph-RAG over legislation.
- [Liquid Legal Institute — Legal Ontologies Registry](https://github.com/Liquid-Legal-Institute/Legal-Ontologies) - Curated, actively-maintained index of legal ontologies, schemas, and vocabularies (CC-BY-4.0).

---

## Standards & Protocols

Open standards and specifications relevant to legal technology and AI integration.

- [Model Context Protocol (MCP)](https://modelcontextprotocol.io) - Anthropic's open standard for connecting AI models to external data sources. Adopted by Microsoft, Google, OpenAI.
- [SALI (Standards Advancement for the Legal Industry)](https://www.sali.org) - Open standard for legal matter data (LMSS - Legal Matter Standard Specification).
- [LEDES (Legal Electronic Data Exchange Standard)](https://ledes.org) - Standard formats for legal billing (e-billing).
- [EU AI Act](https://artificialintelligenceact.eu) - World's first comprehensive AI regulation law. In force Aug 2024; full applicability Aug 2026. Directly impacts legal AI tools.
- [LegalXML / OASIS LegalDocML](https://docs.oasis-open.org/legaldocml/) - XML schema standard for legal documents (bills, statutes, regulations). Used by parliaments globally.
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
- [Stanford RegLab](https://reglab.stanford.edu/) - **[Academic]** Stanford Regulation, Evaluation, and Governance Lab; partners with IRS, courts, and local governments; behind the 2024 Westlaw/Lexis+ AI hallucination studies.
- [Yale Information Society Project (ISP)](https://law.yale.edu/isp) - **[Academic]** Yale Law School's flagship law-tech-society center (founded 1997, Jack Balkin); runs MFIA Clinic and Majority World Initiative.
- [Berkeley Center for Law & Technology (BCLT)](https://www.law.berkeley.edu/research/bclt/) - **[Academic]** UC Berkeley's interdisciplinary center for IP, privacy, cybersecurity, and AI law; co-sponsors PLSC and IPSC.
- [Maastricht Law and Tech Lab](https://www.maastrichtuniversity.nl/research/law-and-tech-lab) - **[Academic]** Co-creation lab combining law, data science, and knowledge engineering; maintains the widely-cited `awesome-legal-nlp`.
- [CIRSFID-AI / ALMA-AI (University of Bologna)](https://centri.unibo.it/alma-ai/en/scientific-units/ai-for-law-and-governance) - **[Academic]** Bologna's interdepartmental center for AI, law, and legal informatics (founded 1986); home to the Legal Blockchain Lab and Legal Machine Lab.
- [Bucerius Center for Legal Technology and Data Science](https://www.legaltechcenter.de/en/) - **[Academic]** Hamburg-based center led by Dan Katz and Dirk Hartung; runs the free annual Legal Tech Essentials lecture series with SMU.
- [NUS TRAIL — Centre for Technology, Robotics, AI and the Law](https://law.nus.edu.sg/trail/) - **[Academic]** NUS Law's interdisciplinary think-tank on AI/robotics regulation and data protection; runs AI Governance & Liability conference series.
- [SMU Centre for Digital Law](https://cdl.smu.edu.sg/) - **[Academic]** Singapore Management University NRF-funded program building DSLs for "smart" contracts and statutes (S$15M grant); hosts ICAIL 2026.
- [Atticus Project](https://www.atticusprojectai.org/) - **[Nonprofit/Academic]** Nonprofit of practicing attorneys producing open-source benchmarks (CUAD, MAUD, ACORD) and AI education for legal practice.
---

## Legaltech Ecosystem Infrastructure

Funding, incubators, regulatory sandboxes, and court-modernization programs that shape where legaltech gets built and adopted.

### Legaltech-Focused Funds

- [The LegalTech Fund](https://www.legaltech.com/) - **[VC]** First VC dedicated exclusively to legal tech (Fort Lauderdale); closed $110M Fund II in Nov 2025; 80+ portfolio companies.
- [NextLaw Ventures](https://www.nextlawventures.vc/) - **[VC]** Dentons-founded early-stage VC focused exclusively on legaltech (ROSS, Doxly, Apperio, Clause).

### Law Firm Innovation Labs

Notable, multi-cohort innovation programs and tech subsidiaries inside major law firms.

- [MDR Lab (Mishcon de Reya)](https://lab.mdr.london/) - 🇬🇧 UK's first dedicated legaltech incubator (since 2017); alumni (DraftWise, Thirdfort, ayora, Version Story) raised £100M+.
- [A&O Shearman Fuse](https://www.aoshearman.com/en/expertise/fuse) - 🇬🇧 First permanent law-firm legaltech incubator (since 2017); 90+ alumni who raised $1.5B+.
- [Slaughter and May Collaborate](https://www.slaughterandmay.com/news/slaughter-and-may-launches-legal-tech-programme/) - 🇬🇧 12-week legaltech programme (since 2019) with access to 70+ client organisations; optional investment via S+M Ventures.
- [Reed Smith Gravity Stack](https://gravitystack.com/) - 🇺🇸 Reed Smith's wholly-owned tech subsidiary (since 2018), 500+ people, builds AI for litigation, eDiscovery, and M&A.
- [DLA Piper Law&](https://www.dlapiper.com/en/insights/topics/law-and) - 🌍 Law& innovation arm with 100+ AI lawyers and tools like Aiscension, Prisca AI Compliance, Transfer.

### Regulatory Sandboxes & Bar Innovation Programs

Regulatory authorities and bar associations enabling new legal-services delivery models, including non-lawyer ownership and software-delivered legal services.

- [Utah Office of Legal Services Innovation (Sandbox)](https://utahinnovationoffice.org/) - 🇺🇸 Utah Supreme Court regulatory sandbox (since 2020, extended through 2027) authorising non-lawyer ownership and software-delivered legal services.
- [Arizona ABS Program](https://www.azcourts.gov/cld/Alternative-Business-Structures) - 🇺🇸 First US state to eliminate Rule 5.4 (2020); 136+ approved Alternative Business Structures.
- [SRA Innovate](https://www.sra.org.uk/solicitors/resources/innovate/) - 🇬🇧 Solicitors Regulation Authority programme for lawtech trials, the Virtual Innovation Hub (with Swansea), and pre-application guidance for novel legal-services models.
- [ABA Center for Innovation](https://www.americanbar.org/groups/centers_commissions/center-for-innovation/) - 🇺🇸 ABA's collaborative innovation hub; publishes the annual Innovation Trends Report.
- [ABA Task Force on Law and AI](https://www.americanbar.org/groups/leadership/office_of_the_president/artificial-intelligence/) - 🇺🇸 ABA Year 2 (2025) report concluding AI has moved from experiment to infrastructure across courts, education, and access-to-justice.

### Court Technology Modernization Programs

Major government and judicial-branch programs digitising courts, e-filing, and case management.

- [National Center for State Courts (NCSC)](https://www.ncsc.org/) - 🇺🇸 Independent nonprofit driving US state-court tech; publishes Trends in State Courts and runs the CTC conference.
- [Joint Technology Committee (JTC)](https://www.ncsc.org/our-centers-projects/joint-technology-committee) - 🇺🇸 NCSC/COSCA/NACM committee publishing court-tech standards, AI for Courts bulletin, and Cybersecurity Basics for Courts.
- [HMCTS Reform Programme](https://www.gov.uk/guidance/the-hmcts-reform-programme) - 🇬🇧 £1.3B portfolio of 44 court-modernization projects (2016–2025); delivered Common Platform and video tech in 70%+ courtrooms.
- [e-CODEX (eu-LISA)](https://www.eulisa.europa.eu/topics/e-codex) - 🇪🇺 Decentralized EU interoperability layer for cross-border judicial data exchange; integrated into eu-LISA in 2024.
- [European e-Justice Portal](https://e-justice.europa.eu/home_en) - 🇪🇺 EU's 23-language one-stop justice portal aligned with the e-Justice Strategy 2024-2028.
- [India e-Courts Mission Mode Project Phase III](https://doj.gov.in/phase-iii/) - 🇮🇳 ₹7,210 crore (2023-27) programme digitising legacy records (637+ crore pages), virtual courts, and AI/ML for case scheduling.
- [Estonia e-File](https://e-estonia.com/solutions/e-governance/justice-public-safety/) - 🇪🇪 Pan-Estonian central judicial information system underpinning e-Justice; AI speech-recognition assistant "Salme" deployed across courts.

---

## Communities, Conferences & Media

Stay current with the legaltech ecosystem.

### Communities & Forums
- [Legal Hackers](https://legalhackers.org) - Global community of lawyers, engineers, policy professionals. Local chapters worldwide.
- [LawTech.UK](https://lawtech.uk) - UK-focused legal innovation community.
- [HFforLegal (Hugging Face)](https://huggingface.co/HFforLegal) - Community for legal AI practitioners on Hugging Face.
- [CLOC (Corporate Legal Operations Consortium)](https://cloc.org) - 3,000+ member community for in-house legal operations professionals.
- [Suffolk LIT Lab Slack](https://suffolklitlab.org/howto/) - Public Slack channels from the nation's top-ranked legal-tech program; access-to-justice and document-automation focus.
- [Legal.io HQ](https://www.legal.io/) - Community of 4,000+ attorneys and legal-ops professionals (Slack + jobs board).

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
- [ICAIL — International Conference on AI and Law](https://iaail.org/) - IAAIL's flagship academic conference (since 1987); now annual. ICAIL 2025 at Northwestern; ICAIL 2026 at SMU Singapore.
- [JURIX](https://jurix.nl/) - International Conference on Legal Knowledge and Information Systems (since 1988); proceedings published in IOS Press FAIA (gold OA).
- [NLLP Workshop](https://nllpw.org/workshop/) - Premier Natural Legal Language Processing workshop co-located with EMNLP since 2021.
- [COLIEE](https://coliee.org/) - Annual Competition on Legal Information Extraction/Entailment on Japanese and Canadian case- and statute-law.
- [CodeX FutureLaw](https://conferences.law.stanford.edu/futurelaw/) - Stanford CodeX's flagship annual gathering for legal informatics; 2025 marked the 20th anniversary.
- [Global Legal Hackathon](https://globallegalhackathon.com/) - World's largest legal hackathon; runs in 75+ countries with a London-based international final.

### Newsletters & Media
- [Artificial Lawyer](https://www.artificiallawyer.com) - Deep-coverage publication on AI and legal tech. Free daily news.
- [Lawnext](https://www.lawnext.com) - Podcast and news by Bob Ambrogi on legal technology innovation.
- [Legal Tech Talk](https://legaltech-talk.com) - News and analysis on legal technology trends.
- [The Legal Innovators](https://legal-innovators.com) - Newsletter covering the business of law and legaltech.
- [Brainyacts](https://thebrainyacts.beehiiv.com/) - Josh Kubicki's near-daily newsletter on generative AI in law (6,000+ subscribers).
- [Legal IT Insider / The Orange Rag](https://legaltechnology.com/) - Caroline Hill's daily news plus monthly Orange Rag digital newsletter; running since 1995.
- [Jordan Furlong Substack](https://jordanfurlong.substack.com/) - Weekly newsletter from legal-industry analyst Jordan Furlong (replacement for his Law21 blog).
- [The Geek In Review](https://www.geeklawblog.com/podcast) - Greg Lambert and Marlene Gebauer's weekly legaltech podcast tied to 3 Geeks and a Law Blog.
- [Lawyerist Podcast](https://lawyerist.com/podcast/) - Stephanie Everett and Zack Glaser's weekly podcast on law-firm tech and management (617+ episodes).
- [LawDroid Manifesto](https://www.lawdroidmanifesto.com/podcast) - Tom Martin's Substack-hosted interview show on legal AI and access to justice.
- [Patently-O](https://patentlyo.com/) - Prof. Dennis Crouch's leading US patent-law blog with daily Federal Circuit analysis.
- [The IPKat](https://ipkitten.blogspot.com/) - UK/EU IP-law blog by Eleonora Rosati and team; multiple posts weekly.
- [Village de la Justice](https://www.village-justice.com/) - 🇫🇷 France's permanent observatory of legaltech actors plus daily legal-profession news.
- [JUVE](https://www.juve.de/) - 🇩🇪 German legal-market publication with a dedicated Legal Tech & Legal Operations section.
- [LiveLaw](https://www.livelaw.in/) - 🇮🇳 India's leading legal-news portal — Supreme Court and High Court breaking news, judgments, and analysis.

## Related Awesome Lists

- [maastrichtlawtech/awesome-legal-nlp](https://github.com/maastrichtlawtech/awesome-legal-nlp) - Legal NLP papers, models, and datasets.
- [awesome-compliance](https://github.com/topics/awesome-compliance) - Compliance-related awesome lists.
- [sindresorhus/awesome](https://github.com/sindresorhus/awesome) - The original meta awesome list.
- [openlegaldata/awesome-legal-data](https://github.com/openlegaldata/awesome-legal-data) - Curated collection of legal text-processing datasets and resources.
- [Jeryi-Sun/LLM-and-Law](https://github.com/Jeryi-Sun/LLM-and-Law) - Continually-updated paper list on LLMs applied to law.

---

## Deprecated / Archived

Entries that were previously listed but have since been archived, sunset, acquired-and-shut-down, or otherwise stopped being maintained. Kept visible so readers don't rediscover dead links and so the history of the space is preserved. An entry moves here (rather than getting deleted) when the upstream repo is GitHub-archived, the company shuts down or the product is discontinued, or there has been no meaningful activity for 2+ years. Include a short note on what happened and, where useful, a pointer to a successor.

<!-- Format:
- [Name](https://url) - **[Archived YYYY-MM]** - What it was, what happened, and (optionally) what replaced it.
-->

*No entries yet.*

---

## Contributing

Contributions are welcome! Please read the [contribution guidelines](CONTRIBUTING.md) before submitting a pull request.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.
