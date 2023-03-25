FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 libgl1-mesa-glx -y
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "main.py"]
