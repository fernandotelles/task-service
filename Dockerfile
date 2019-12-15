FROM python:3.7-slim-stretch

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

ENV FLASK_APP=app.py

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]