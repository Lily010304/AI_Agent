from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever

model = OllamaLLM(model="qwen2.5:3b-instruct-q4_K_M")

template = """
You are a helpful assistant for answering questions about restaurant reviews. Use the following retrieved reviews to answer the question. If you don't know the answer, say you don't know.
question: {question}
context: {context}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    question = input("Please enter your question (press q to quit): \n\n")

    if question == "q":
        break
    context = retriever.invoke(question)
    res = chain.invoke({"question": question, "context": context})
    print("\n\nAnswer: \n\n", res, "\n\n")
