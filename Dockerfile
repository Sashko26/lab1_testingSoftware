FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
ADD server.py /server/
WORKDIR /server/



