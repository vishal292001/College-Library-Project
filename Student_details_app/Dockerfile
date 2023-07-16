
FROM python:3.8



WORKDIR /app

COPY ./app ./app

COPY requirements.txt .

RUN pip install -r requirements.txt


CMD ["python", "./app/student_details_app.py"]

