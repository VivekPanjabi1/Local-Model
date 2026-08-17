# Zvec Semantic Search

Local-first semantic search demo combining WikiText ingestion, sentence-transformer embeddings, and a Zvec vector index.

## Features
- **Data prep**: Pull WikiText-103, clean lines, and produce refined chunks.
- **Embeddings**: Batch generation via `all-MiniLM-L6-v2` with L2 normalization.
- **Indexing**: Local Zvec collection storing chunk text + 384-d vectors.
- **CLI + UI**: Command-line builder/query plus Streamlit UI (`src/ui_zvec.py`).

## Project Layout
```
├── scripts/
│   ├── prepare_wikitext.py   # Download + clean raw dataset
│   ├── refine_chunks.py      # Secondary filtering + merging
│   └── data/
│       ├── sample_docs.txt
│       └── refined_chunks.txt
├── src/
│   ├── ingest.py             # Load + chunk documents
│   ├── embed.py              # EmbeddingModel wrapper
│   ├── index_zvec.py         # ZvecIndex build + search
│   ├── ui_zvec.py            # Streamlit app
│   └── search.py / zvec_store.py
├── app.py                    # CLI orchestrator
└── requirements.txt
```

## Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Data Pipeline
1. **Prepare WikiText**
   ```bash
   python scripts/prepare_wikitext.py
   ```
2. **Refine chunks**
   ```bash
   python scripts/refine_chunks.py
   ```
3. **Build Zvec index + sample query**
   ```bash
   python src/index_zvec.py
   ```

## Streamlit UI
```bash
streamlit run src/ui_zvec.py
```
The UI loads the existing Zvec index/embedding model, accepts queries, and displays top results with scores + latency metrics.

## Troubleshooting
- Ensure `zvec` native library is installed and discoverable.
- `scripts/data/*.txt` must exist before running the indexer.
- Re-run `python src/index_zvec.py` after updating dataset to refresh the collection.
