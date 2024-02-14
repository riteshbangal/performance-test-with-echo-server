FROM python:3.8-alpine

COPY echo-server.py /app/echo-server.py

WORKDIR /app

CMD ["python", "echo-server.py"]
