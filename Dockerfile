
FROM python:3.8-alpine
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
COPY  . /app
WORKDIR /app
EXPOSE 8000
CMD ["gunicorn","app:app","--access-logfile=-","--error-logfile=-","--bind","0.0.0.0:8000"]