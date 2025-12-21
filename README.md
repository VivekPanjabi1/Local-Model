# Local LLM Lab

Experimental workspace for running and fine-tuning large language models locally on an RTX 4060 + 13th-gen Intel i9 machine. The goal is to explore LoRA/QLoRA adapters, track experiments, and document best practices for consumer-grade hardware.

## Repo Layout

| Path | Description |
| --- | --- |
| `src/` | Core Python modules (`main.py`, helpers for data prep, training, inference). |
| `scripts/` | Utility scripts (dataset downloaders, cleanup helpers). |
| `notebooks/` | Jupyter notebooks for exploration, evaluation, visualization. |
| `data/raw/` | Unprocessed datasets (keep large files out of git). |
| `data/processed/` | Cleaned/tokenized data ready for training. |
| `models/base/` | Base checkpoints or symlinks to HF cache. |
| `models/finetuned/` | LoRA adapters and merged weights. |
| `configs/` | JSON/YAML configs describing training/inference runs. |
| `experiments/` | Logs, metrics, and notes per experiment. |
| `logs/` | Console logs, TensorBoard traces, or evaluation reports. |

## Quick Start

1. **Environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt  # create this file when ready
   ```
2. **Check GPU**
   ```bash
   nvidia-smi
   ```
3. **Run placeholder app**
   ```bash
   python src\main.py
   ```

## Next Steps

1. Add `requirements.txt` (transformers, accelerate, peft, bitsandbytes, datasets, etc.).
2. Implement data ingestion + LoRA training scripts.
3. Track each experiment in `experiments/` with metrics + observations.
