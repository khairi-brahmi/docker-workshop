FROM python:3.8

WORKDIR /app


COPY requirements.txt .

COPY app.py .

COPY test_app.py .

RUN pip install -r requirements.txt


EXPOSE 5000

CMD ["python", "app.py"]