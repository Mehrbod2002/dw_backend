FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app/src
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# cat dwbank.sql | docker exec -i dwbank_db psql -U "mhmd" -d "postgres"
# docker exec -t postgres-container pg_dump -U postgres -d mydb -F c -b -v
# cat sql/dwdumpdata.sql | docker exec -i dwbank_db pg_restore -U "mhmd" -d "postgres" --clean --no-owner