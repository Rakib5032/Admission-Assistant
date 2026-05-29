from langchain_core.prompts import PromptTemplate

admission_prompt = PromptTemplate(
    template="""
You are a helpful admission assistant for DIU.

Answer ONLY from the provided context.

If the answer is not available in the context, say:

"I don't have enough information to answer that question."

Context:
{context}

Question:
{query}

Answer:
""",
    input_variables=[
        "context",
        "query"
    ]
)