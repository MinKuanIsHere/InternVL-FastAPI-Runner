from fastapi import FastAPI
from pydantic import BaseModel
from utils import decode_image
from model_loader import load_pipeline
import torch

app = FastAPI()
pipe = load_pipeline()

class InferenceRequest(BaseModel):
    prompt: str
    image_base64: str

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/infer")
def infer(req: InferenceRequest):
    image = decode_image(req.image_base64)
    # response = pipe((req.prompt, image))
    response = pipe(
            (req.prompt, image),
            temperature=0.2,
            top_p=0.9,
            max_new_tokens=300
        )
    return {"result": response.text}

@app.get("/ping")
def health_check():
    return {"message": "hello world"}

@app.get("/gpu")
def check_gpu():
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        gpu_list = [torch.cuda.get_device_name(i) for i in range(gpu_count)]
        return {"gpu_available": True, "gpus": gpu_list}
    else:
        return {"gpu_available": False, "gpus": []}
