from langchain_core.runnables import(
    RunnablePassthrough,
    RunnableLambda
)
from langchain_core.output_parsers import StrOutputParser

from app.rag.retriever import retriever
from app.prompts.prompts import admission_prompt
from app.model.models import chat_model

rag_chain = (
    {
        "context": RunnableLambda(retriever),
        "query": RunnablePassthrough()
    }
    | admission_prompt
    | chat_model
    | StrOutputParser()
)