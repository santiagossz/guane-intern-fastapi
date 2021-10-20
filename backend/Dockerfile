
FROM python:3.8.10
COPY requirements.txt /app/
WORKDIR /app
RUN pip install -r requirements.txt
COPY . /app

CMD ["uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "5010","--reload"]
