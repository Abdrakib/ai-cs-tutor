import gradio as gr
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Load embedding model
embed_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Knowledge base
examples = [
    {
        "question": "What is recursion?",
        "answer": "Recursion is a programming technique where a function calls itself to solve smaller versions of the same problem. A recursive solution usually has a base case to stop the calls and a recursive case to continue the process."
    },
    {
        "question": "What is a stack in computer science?",
        "answer": "A stack is a linear data structure that follows the Last In, First Out rule (LIFO). The last element added is the first element removed."
    },
    {
        "question": "What is a queue?",
        "answer": "A queue is a data structure that follows First In First Out (FIFO). The first element added is the first element removed."
    },
    {
        "question": "What is Big O notation?",
        "answer": "Big O notation describes how the running time or memory usage of an algorithm grows as the input size increases."
    },
    {
        "question": "What is binary search?",
        "answer": "Binary search is an algorithm used to find elements in a sorted list by repeatedly dividing the search interval in half."
    },
    {
        "question": "What is a linked list?",
        "answer": "A linked list is a data structure composed of nodes where each node stores data and a reference to the next node."
    },
]

texts = [f"Question: {e['question']} Answer: {e['answer']}" for e in examples]

# Create embeddings
embeddings = embed_model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)

dimension = embeddings.shape[1]

# FAISS index
index = faiss.IndexFlatIP(dimension)
index.add(np.array(embeddings, dtype=np.float32))

SIMILARITY_THRESHOLD = 0.45


def retrieve_answer(question):

    query_embedding = embed_model.encode(
        [question],
        convert_to_numpy=True,
        normalize_embeddings=True
    )

    scores, indices = index.search(np.array(query_embedding, dtype=np.float32), 1)

    score = float(scores[0][0])
    idx = int(indices[0][0])

    if score < SIMILARITY_THRESHOLD:
        return "I don't have enough information to answer that question yet."

    return examples[idx]["answer"]


def tutor(question):
    if not question.strip():
        return "Please ask a computer science question."

    return retrieve_answer(question)


demo = gr.Interface(
    fn=tutor,
    inputs=gr.Textbox(lines=2, placeholder="Ask a computer science question..."),
    outputs=gr.Textbox(label="Tutor Answer"),
    title="AI Computer Science Tutor",
    description="Ask beginner-friendly computer science questions and get short explanations.",
    examples=[
        ["What is recursion?"],
        ["What is a stack in computer science?"],
        ["What is Big O notation?"],
        ["What is binary search?"]
    ],
)

demo.launch()
