# syntax=docker/dockerfile:1
FROM python

WORKDIR /HW6_Docker/app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python3 pokemonDB_app.py