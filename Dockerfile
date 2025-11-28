FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY model.pkl .
COPY inference.py .

RUN mkdir -p /input/logs
RUN mkdir -p /output

ENTRYPOINT ["python", "inference.py"]
