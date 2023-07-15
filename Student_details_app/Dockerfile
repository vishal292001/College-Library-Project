FROM postgres
FROM python:3.8



WORKDIR .

COPY . ./app

COPY requirements.txt .

RUN pip install -r requirements.txt


CMD ["python", "./app/student_details_app.py"]

