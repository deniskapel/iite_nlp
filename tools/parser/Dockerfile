FROM python:3.9-slim as builder

RUN mkdir /src

COPY ./requirements.txt /src/requirements.txt

RUN pip install --no-cache-dir -U pip \ 
    && pip install --user --no-cache-dir -r /src/requirements.txt \
    && find /usr/local/lib/python3.9 -name '__pycache__' | xargs rm -r \
    && find /root/.local/ -follow -type f -name '*.png' -delete \
    && find /root/.local/ -follow -type f -name '*.jpg' -delete \
    && find /root/.local/ -follow -type f -name '*.txt' -delete \
    && find /root/.local/ -follow -type f -name '*.jpeg' -delete \
    && find /root/.local/ -follow -type f -name '*.js.map' -delete \
    && find /root/.local/ -follow -type f -name '*.a' -delete \
    && find /root/.local/ -follow -type f -name '*.md' -delete \
    && find /root/.local/ -follow -type f -name '*.pyc' -delete \
    && find /root/.local/ -name '*.c' -delete \
    && find /root/.local/ -name '*.pxd' -delete \
    && find /root/.local/ -name '*.pyd' -delete

FROM python:3.9-slim AS runner
COPY --from=builder /root/.local /root/.local
COPY . /src

WORKDIR /src

ARG SERVICE_PORT
ENV SERVICE_PORT ${SERVICE_PORT}

CMD python -m gunicorn --workers=1 server:app -b 0.0.0.0:${SERVICE_PORT}