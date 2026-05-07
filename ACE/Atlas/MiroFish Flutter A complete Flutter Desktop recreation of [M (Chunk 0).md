---
aliases: []
area: ''
backlinks: []
created: '2026-05-07T20:18:01.742284'
id: 2184c7da
links: []
modified: '2026-05-07T20:18:01.742284'
project: ''
source: ''
status: active
summary: ''
tags:
- ingested
- chunk
title: MiroFish Flutter A complete Flutter Desktop recreation of [M (Chunk 0)
type: knowledge_chunk
---

---
chunk_id: 1589b9fc0650
source: README.md
page: 0
title: MiroFish Flutter A complete Flutter Desktop recreation of [M (Chunk 0)
keywords: ['MiroFish']
created: 2026-05-08 01:48:01
tree_path: mirofish > Page 0 > MiroFish Flutter A complete Flutter Desktop recrea
---

# MiroFish Flutter A complete Flutter Desktop recreation of [MiroFish](https://github.com/666ghj/MiroFish) — a swarm intelligence social simulation engine. ## Features - **Graph Build** — Upload documents, LLM extracts ontology + builds interactive force-directed knowledge graph - **Env Setup** — LLM generates 55+ agent profiles with stances, activity patterns, influence weights - **Simulation** — Dual-platform (Plaza + Community) parallel simulation with real-time graph updates - **Report** — ReportAgent streams analytical report with section tracing - **Interaction** — Chat with any simulated agent or ReportAgent - **Local LLM** — Supports Ollama, LM Studio, llama.cpp server (GGUF models) — no API key needed - **Interactive Graph** — Force-directed layout, zoom/pan, drag nodes, hover tooltips, edge label toggle ## Quick Setup ### 1. Create Flutter project ```powershell flutter create --platforms=windows mirofish cd mirofish ``` ### 2. Replace lib/ and pubspec.yaml Extract `mirofish_flutter.zip` and copy: - `mirofish/lib/` → your project's `lib/` - `mirofish/pubspec.yaml` → your project's `pubspec.yaml` ### 3. Install packages ```powershell flutter pub get ``` ### 4. Run ```powershell flutter run -d windows ``` --- ## LLM Configuration On first launch, click **⚙ Settings** (top right on home screen). ### Option A — Use Local LLM (no API key needed) Start one of: **Ollama** (easiest): ```bash # Install from https://ollama.com ollama pull qwen2.5:7b # or llama3, mistral, etc ollama serve ``` **LM Studio**: Download from lmstudio.ai, load any GGUF model, start local server on port 1234. **llama.cpp server**: ```bash ./server -m your-model.gguf -c 4096 --port 8080 ``` In Settings: set **Mode = Local LLM**, enter model name (e.g. `qwen2.5:7b`). ### Option B — Use API Set **Mode = API**, enter: - API Key: your OpenAI / Qwen / etc key - Base URL: `https://api.openai.com/v1` (or compatible endpoint) - Model: `gpt-4o`, `qwen-plus`, etc. --- ## Architecture ``` lib/ ├── main.dart # App entry + router ├── models/models.dart # GraphNode, AgentProfile, SimEvent, LLMConfig... ├── providers/app_provider.dart # All state + pipeline orchestration ├── services/ │ ├── llm_service.dart # API + local LLM calls (streaming) │ └── api_service.dart # Ontology, GraphRAG, agents, simulation, report ├── utils/theme.dart # MFColors, MFTheme, reusable widgets ├── widgets/graph_view.dart # Force-directed interactive graph └── screens/ ├── home_screen.dart # Step 0: Landing + LLM config ├── graph_build/ # Step 1: Ontology + GraphRAG ├── env_setup/ # Step 2: Agents + config ├── simulation/ # Step 3: Dual-platform sim ├── report/ # Step 4: AI report generation └── interaction/ # Step 5: Agent chat ``` ## Pipeline Flow ``` Upload PDF → LLM Ontology → GraphRAG Build → Agent Profiles → Sim Config → Dual-Platform Simulation → Report Generation → Agent Chat ``` Each step calls the LLM (local or API) to do real work. Without LLM configured, demo/mock data is used so you can explore the UI. ## Dependencies | Package | Use | |---|---| | `provider` | State management | | `http` | LLM API calls + streaming | | `file_picker` | PDF/document upload | | `flutter_markdown` | Report rendering | | `web_socket_channel` | Real-time updates | | `uuid` | Project/session IDs | | `dio` | Advanced HTTP | All standard packages — no native plugins, no WebView.

### Related Concepts
- [[MiroFish]]
