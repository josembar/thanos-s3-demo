FROM python:3.9-alpine

ENV OTEL_EXPORTER_OTLP_METRICS_ENDPOINT="http://127.0.0.1:4317"
ENV OTEL_EXPORTER_OTLP_METRICS_PROTOCOL="grpc"

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]