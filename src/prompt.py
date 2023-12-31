prompt_template = """
Use the following piece of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to generate any random answer from your own

Context:{context}
Question:{question}

Only return the helpful answer and nothing else
helpful answer:
"""