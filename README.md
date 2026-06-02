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
- [AI Workdeck](https://github.com/zeweihan/aiworkdeck) - **[Open Source]** AI-native IDE workspace for legal and document-heavy workflows — "VS Code for lawyers." Self-hosted (Java/Spring Boot + Vue + Electron + Docker, AGPLv3). Features MCP agent orchestration, OCR, due-diligence risk flagging, evidence-chain management, WPS WebOffice integration, and smart clipboard. Supports air-gapped deployment with Ollama + local storage.

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
- [IN-Abs / UK-Abs](https://github.com/Law-AI/summarization) - **[🇮🇳 🇬🇧]** - **[EN]** - Abstractive and extractive summarization datasets for Indian and UK case judgment�=D�ECB1�]x�G!j�(�+my�.����^6��-jThr_cases) - Legal judgment prediction benchmark using ECHR cases.
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
