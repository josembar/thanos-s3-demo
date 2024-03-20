FROM otel/opentelemetry-collector:latest

COPY otel-config-local.yaml /etc/otelcol/otel-config-local.yaml

CMD ["--config" "/etc/otelcol/otel-config-local.yaml"]