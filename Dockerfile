FROM python:3.11
WORKDIR /SMM_BACKEND
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "smartmaritime.wsgi:application" ]

