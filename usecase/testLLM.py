import os
from dotenv import load_dotenv
import requests
import base64

load_dotenv()
HOST = os.getenv("HOST")
PORT = os.getenv("PORT")
url = f"http://{HOST}:{PORT}"

# test inference
def infer_image(prompt, image_path_or_url):
    if image_path_or_url.startswith("http://") or image_path_or_url.startswith("https://"):
        # 如果是 URL，下載圖片
        response = requests.get(image_path_or_url)
        b64_image = base64.b64encode(response.content).decode()
    else:
        # 否則當作本地檔案
        with open(image_path_or_url, "rb") as f:
            b64_image = base64.b64encode(f.read()).decode()

    payload = {
        "prompt": prompt,
        "image_base64": b64_image
    }

    res = requests.post(f"{url}/infer", json=payload)
    return res.json()


# 呼叫範例
img_URL = "https://raw.githubusercontent.com/open-mmlab/mmdeploy/main/tests/data/tiger.jpeg"
# response = infer_image("Describe this image", img_URL)
response = infer_image("用繁體中文描述圖片", img_URL)
print(response["result"])
