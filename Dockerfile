# Dockerfil
FROM python:3.8

COPY etl_process.py /app/
WORKDIR /app

RUN pip install pymongo mysql-connector-python

CMD ["python", "etl_process.py"]
