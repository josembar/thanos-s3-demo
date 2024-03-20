import os

from fastapi import FastAPI

from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import metrics
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

# Service name is required for most backends
resource = Resource(attributes={
    SERVICE_NAME: "test-service"
})

metrics_endpoint_environment_variables = ["OTEL_EXPORTER_OTLP_ENDPOINT", "OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"]
if any(variable in metrics_endpoint_environment_variables for variable in os.environ):
    reader = PeriodicExportingMetricReader(OTLPMetricExporter())
else: 
    reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(meterProvider)

@app.get("/hello")
def read_root():
    return {"messsage": "Hello!"}

FastAPIInstrumentor.instrument_app(app)