from fastapi import FastAPI
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()

@app.get("/hello")
def read_root():
    return {"messsage": "Hello!"}

FastAPIInstrumentor.instrument_app(app)