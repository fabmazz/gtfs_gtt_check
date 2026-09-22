FROM python:3-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./parse_gtfs.py .

CMD ["python", "parse_gtfs.py"]
