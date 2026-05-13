FROM python:3.14

WORKDIR /app

COPY . .

RUN pip install flask

EXPOSE 3000

CMD ["python", "app.py"]