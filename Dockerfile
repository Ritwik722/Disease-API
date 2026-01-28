FROM python:3.10-slim

WORKDIR /opt/ml/code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY serve.py .

ENV SAGEMAKER_PROGRAM serve.py

ENTRYPOINT ["python", "serve.py"]
