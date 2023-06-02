FROM python:3.11
WORKDIR /app
RUN pip install Django
RUN pip install psycopg2-binary==2.9.5
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]