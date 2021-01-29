FROM python:3.8.3-slim-buster

RUN apt-get update \
    && apt-get install -y --no-install-recommends make curl supervisor \
    && rm -rf /var/lib/apt/lists/*

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
ENV PYTHONUNBUFFERED 1
EXPOSE 8010
ARG APP_DIR=/var/app
ENV PYTHONPATH=${APP_DIR}
WORKDIR ${APP_DIR}
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH=/root/.poetry/bin:${PATH}

COPY poetry.lock Makefile pyproject.toml ./
COPY gallery/ ${APP_DIR}/gallery/
RUN make install
CMD ["make", "run-prod"]