import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


def get_gemini_response(prompt):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=gemini_api_key, temperature=0.0)
    chain = llm | StrOutputParser()
    llm_response = chain.invoke(prompt)
    return llm_response
