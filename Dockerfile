FROM python:latest

RUN pip3 install poetry

WORKDIR $HOME/
COPY . .
RUN poetry install

RUN DJANGO_SUPERUSER_PASSWORD=Qwerty123 make silentaddadmin

CMD ["make", "migrate", "&&", "make", "start"]