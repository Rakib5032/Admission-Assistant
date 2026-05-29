from app.rag.retriever import retriver
from langchain_core.prompts import PromptTemplate
from app.model.models import chat_model


def question_answer(query):
    context = retriver(query)

    prompt_template = PromptTemplate(
        template="""
You are a helpful admission assistant for DIU Admission Chatbot.

Answer only from the provided context.

If the context is insufficient, say:
"I don't have enough information to answer that question."

Context:
{context}

Question:
{query}
""",
        input_variables=["context", "query"]
    )

    formatted_prompt = prompt_template.format(
        context=context,
        query=query
    )

    response = chat_model.invoke(formatted_prompt)

    return {
        "success": True,
        "answer": response.content
    }