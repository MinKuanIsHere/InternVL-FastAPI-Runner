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

Expected output of testing the API :
```
[/] Status Code: 200 # the status
{'message': 'API is running'}
[/ping] {'message': 'hello world'} # test print 
[/gpu] {'gpu_available': True, 'gpus': ['NVIDIA GeForce RTX 4090']} # the gpu info
```

### Image-based inference via remote URL:

```bash
python3 usecase/testLLM.py
```

Template of calling LLM with API
```
# 呼叫範例
img_URL = "https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg"
# response = infer_image("Describe this image", img_URL)
response = infer_image("用繁體中文描述圖片", img_URL)
print(response["result"])
```

Expected output of testing the LLM :
```
這是一張老虎的照片。老虎正躺在綠色的草地上，頭頂正中，眼睛直視前方，表情冷靜。老虎的皮毛上有明顯的條紋，身體呈半躺姿，前肢交疊在身前。背景是綠色的草地，陽光照射在草地上，使整體畫面明亮。
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

