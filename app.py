from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langserve import add_routes
from dotenv import load_dotenv
import uvicorn
import os

load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

app = FastAPI(
    title="LangServe Groq Example",
    description="An example FastAPI application using LangServe with Groq model.",
    version="1.0.0",
)

model = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.7
)

# Prompts
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words"
)

prompt2 = ChatPromptTemplate.from_template(
    "Write me a poem about {topic} for a 5 years child with 100 words"
)

# Routes
add_routes(
    app,
    model,
    path="/groq"
)

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)

add_routes(
    app,
    prompt2 | model,
    path="/poem"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)