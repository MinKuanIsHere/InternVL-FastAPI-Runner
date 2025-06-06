import base64
from PIL import Image
import io

def decode_image(base64_string: str) -> Image.Image:
    """
    將 base64 字串轉換為 PIL Image，給模型用。
    """
    if ',' in base64_string:
        base64_string = base64_string.split(',')[1]
    img_data = base64.b64decode(base64_string)
    return Image.open(io.BytesIO(img_data)).convert("RGB")
