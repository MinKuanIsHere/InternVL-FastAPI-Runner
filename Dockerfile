FROM pytorch/pytorch:2.2.2-cuda12.1-cudnn8-runtime

WORKDIR /app
COPY app /app

RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
