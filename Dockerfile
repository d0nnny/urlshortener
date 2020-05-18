FROM python:3.8

LABEL Author="Dee"
LABEL version="0.0.1b"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "url_shortener" 
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /urlshortener
WORKDIR /urlshortener

COPY Pip* /urlshortener/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /urlshortener

EXPOSE 5000

CMD flask run --host=0.0.0.0