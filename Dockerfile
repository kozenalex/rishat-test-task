FROM python:latest

RUN pip3 install poetry

WORKDIR $HOME/stripe_buy
COPY . .
RUN poetry install

CMD ["make", "migrate", "&&", "gunicorn", "stripe_buy.wsgi"]