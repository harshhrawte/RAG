from app.llm import get_llm, get_retriever, create_prompt

def answer_query(query):
    llm = get_llm()
    collection, embeddings = get_retriever()
    prompt = create_prompt()

    embedding_vector = embeddings.embed_query(query)
    results = collection.query(query_embeddings=[embedding_vector], n_results=3)

    context = "\n".join(doc for doc in results["documents"][0])
    response = llm.invoke(prompt.format(context=context, query=query))
    return response.content.strip()