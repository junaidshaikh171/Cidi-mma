FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install flask gunicorn

EXPOSE 3000

CMD ["gunicorn", "--bind", "0.0.0.0:3000", "app:app"]
