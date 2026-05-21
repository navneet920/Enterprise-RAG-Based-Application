from langchain_huggingface import HuggingFaceEndpoint,ChatHuggingFace
from dotenv import load_dotenv
from app.core.config import settings

load_dotenv()
llm = HuggingFaceEndpoint(

    repo_id="deepseek-ai/DeepSeek-V4-Flash",
    task="text-generation",
)
llm=ChatHuggingFace(llm=llm)

def generate_response(prompt: str):

    response = llm.invoke(prompt)

    return response