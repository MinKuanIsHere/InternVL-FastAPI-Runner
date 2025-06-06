# InternVL-FastAPI-Runner

A lightweight, local deployment for multimodal visual-language inference using [OpenGVLab/InternVL3-1B](https://huggingface.co/OpenGVLab/InternVL3-1B) via [LMDeploy](https://github.com/InternLM/lmdeploy) and FastAPI. This project supports GPU-accelerated inference.

---

## 🔧 Requirements

- GPU (recommended: NVIDIA RTX 4090 or higher)
- Docker & Docker Compose
- CUDA driver (recommended >= 12.1)
- Python 3.10+
- Linux or WSL (preferred)

---

## 🚀 Quickstart

### 1. Edit `.env`

```env
HOST=localhost
PORT=8000
UID=username
GPU_ID=0
````

### 2. Build and launch container

```bash
docker compose up --build
```

After launch, the FastAPI server will be accessible at `http://localhost:8000`.

---

## 🔌 API Endpoints

| Route    | Method | Description                             |
| -------- | ------ | --------------------------------------- |
| `/`      | GET    | Root check                              |
| `/ping`  | GET    | Health check                            |
| `/gpu`   | GET    | Check if CUDA/GPU is available          |
| `/infer` | POST   | Perform multimodal inference with image |

---

## Testing

You can test the API using the included scripts in the `usecase/` folder:

### Basic endpoint tests:

```bash
python3 usecase/testAPI.py
```

Testing the API state:
```
import os
from dotenv import load_dotenv
import requests

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
url = f"http://{HOST}:{PORT}"

# Test root ("/")
try:
    res = requests.get(url)
    print(f"[/] Status Code: {res.status_code}")
    print(res.json())
except requests.exceptions.RequestException as e:
    print(f"[/] Connection error: {e}")
```

### Image-based inference via remote URL:

```bash
python3 usecase/testLLM.py
```

---

## Project Structure

```
llm_test/
├── app/
│   ├── app.py              # FastAPI entrypoint
│   ├── model_loader.py     # LMDeploy pipeline setup
│   ├── utils.py            # Base64 image tools
│   └── requirements.txt    # Python dependencies
├── usecase/
│   ├── testAPI.py          # Ping/GPU/Infer test
│   └── testLLM.py          # URL-based image inference
├── .env                    # Local config (HOST, PORT, GPU ID)
├── docker-compose.yml      # GPU container config
├── Dockerfile              # PyTorch + LMDeploy base image
```

---

## ⚙️ LMDeploy Settings

`model_loader.py` configures the model with:

* `session_len=16384` → maximum context length
* `tp=1` → tensor parallelism (set to 1 GPU)
* `chat_template='internvl2_5'` → InternVL official chat template

You can customize inference parameters:

```python
pipe(prompt, temperature=0.2, top_p=0.9, max_new_tokens=300)
```

---

## 📎 References

* [OpenGVLab/InternVL3-1B on Hugging Face](https://huggingface.co/OpenGVLab/InternVL3-1B)
* [LMDeploy GitHub](https://github.com/InternLM/lmdeploy)

