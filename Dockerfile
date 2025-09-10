FROM python:3.12-alpine

WORKDIR /app/app
COPY app/requirements.txt .
RUN pip3 install --no-cache-dir -r ./requirements.txt

COPY . .
CMD ["python", "main.py"]
