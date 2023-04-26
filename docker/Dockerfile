
FROM python:3.8.10

RUN pip install Flask==2.2.2 redis requests
RUN pip install requests==2.2.0
RUN pip install matplotlib==3.7.1
RUN pip install redis

COPY aw_app.py /aw_app.py

CMD ["python3", "aw_app.py"]
