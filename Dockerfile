FROM python:3.13-alpine as build

ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

WORKDIR /code
COPY pyproject.toml poetry.lock requirements.txt /code/
RUN pip install -r requirements.txt

FROM python:3.13-alpine

WORKDIR /code

COPY --from=build /usr/local/lib/python3.13/site-packages/ /usr/local/lib/python3.13/site-packages/
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY . .
