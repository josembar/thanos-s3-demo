import os, uuid

from fastapi import FastAPI

from opentelemetry.sdk.resources import SERVICE_NAME, Resource

from opentelemetry import metrics
# from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader, ConsoleMetricExporter

from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

# Service name is required for most backends
service_name = os.getenv('OTEL_SERVICE_NAME') or "test-service"
print(f"service name: {service_name}")
resource = Resource(attributes={
        SERVICE_NAME: service_name
})

metrics_endpoint_environment_variables = ["OTEL_EXPORTER_OTLP_ENDPOINT", "OTEL_EXPORTER_OTLP_METRICS_ENDPOINT"]
if any(variable in metrics_endpoint_environment_variables for variable in os.environ):
    print(f"endpoint: {os.getenv('OTEL_EXPORTER_OTLP_ENDPOINT') or os.getenv('OTEL_EXPORTER_OTLP_METRICS_ENDPOINT')}")
    reader = PeriodicExportingMetricReader(OTLPMetricExporter())
else: 
    reader = PeriodicExportingMetricReader(ConsoleMetricExporter())
meterProvider = MeterProvider(resource=resource, metric_readers=[reader])
metrics.set_meter_provider(meterProvider)

@app.get("/hello")
def read_hello():
    return {"messsage": "Hello!"}

@app.get("/uuid")
def read_uuid():
    myuuid = uuid.uuid4()
    return {"messsage": str(myuuid)}

FastAPIInstrumentor.instrument_app(app)