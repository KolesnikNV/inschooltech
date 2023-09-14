FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
COPY docker-entrypoint.sh .
RUN pip3 install -r requirements.txt --no-cache-dir
COPY .env ./
COPY labs/ ./
RUN chmod +x docker-entrypoint.sh
ENTRYPOINT ["./docker-entrypoint.sh"]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "labs.wsgi:application"]

