FROM python:latest
WORKDIR /app
COPY . .
ADD client.py /client/
RUN pip install -r requirements.txt
WORKDIR /client/