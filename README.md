# AI Agent: Restaurant Reviews RAG (LangChain + Ollama + Chroma)

A small local RAG (retrieval-augmented generation) demo that answers questions about restaurant reviews.

- **Embeddings**: `OllamaEmbeddings` using `mxbai-embed-large`
- **Vector DB**: `Chroma` persisted to `./chroma_db`
- **LLM**: `OllamaLLM` using `qwen2.5:3b-instruct-q4_K_M`
- **Data**: `realistic_restaurant_reviews.csv`

## How it works

1. `vector.py` loads `realistic_restaurant_reviews.csv`.
2. On first run (when `./chroma_db` does not exist), it:
   - Builds `Document`s from each row (`Title` + `Review`)
   - Embeds them with Ollama embeddings
   - Stores them in a persistent Chroma collection (`restaurant_reviews`)
3. `main.py`:
   - Accepts a user question in a loop
   - Retrieves the top `k=5` most relevant reviews
   - Sends the question + retrieved context to the LLM

## Prerequisites

- **Python** 3.10+ (3.11 recommended)
- **Ollama** installed and running: https://ollama.com

Make sure these models are available locally:

```powershell
ollama pull mxbai-embed-large
ollama pull qwen2.5:3b-instruct-q4_K_M
```

## Setup (Windows PowerShell)

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -U pip
pip install langchain-ollama langchain-core langchain-chroma chromadb pandas
```

## Run

```powershell
python main.py
```

Example:

- Type a question like: `is there a vegan pizza?`
- Quit with: `q`

## Notes / Troubleshooting

- **First run is slower**: it has to embed the CSV and build the Chroma DB.
- **Persistence**: once `chroma_db/` exists, embeddings won’t be re-generated unless you delete that folder.
- **If Ollama isn’t running**: start it, then retry.
- **If you change the CSV**: delete `chroma_db/` so it rebuilds with the updated data.

## Project layout

- `main.py` — CLI loop that asks questions and prints answers
- `vector.py` — builds/loads the Chroma vector store and exposes `retriever`
- `realistic_restaurant_reviews.csv` — review dataset
- `chroma_db/` — local persistent vector database (ignored by git)
