# 🧠 AI Computer Science Tutor

An interactive AI tutor that answers beginner-friendly computer science questions.

The system uses **semantic search with embeddings and FAISS** to retrieve the most relevant explanation from a curated computer science knowledge base before returning an answer.

This project demonstrates how **retrieval-based AI systems** can reduce hallucinations and provide reliable explanations.

---

# 🚀 Live Demo

Try the AI tutor here:

https://huggingface.co/spaces/Abdourakib/ai-computer-science-tutor

Users can ask questions such as:

* What is recursion?
* What is a stack in computer science?
* What is Big O notation?
* What is the difference between a process and a thread?

---

# 🧠 How It Works

The system follows a **retrieval-based pipeline**:

1. The user asks a computer science question.
2. The question is converted into an embedding.
3. FAISS performs a semantic search on stored explanations.
4. The most relevant explanation is retrieved.
5. The system returns the answer if similarity is high enough.

If the system does not find a reliable match, it returns a fallback message instead of hallucinating.

---

# ⚙️ Technologies Used

* Python
* Sentence Transformers
* FAISS (vector search)
* NumPy
* Gradio
* Hugging Face Spaces

---

# 📂 Project Structure

```
ai-computer-science-tutor
│
├── app.py
├── requirements.txt
├── AI_computer_science_Tutor_project.ipynb
└── README.md
```

---

# ▶️ Run Locally

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/ai-computer-science-tutor.git
cd ai-computer-science-tutor
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the application:

```
python app.py
```

The Gradio interface will start in your browser.

---

# 💡 Example Questions

Try asking:

* What is recursion?
* What is a stack?
* What is Big O notation?
* What is binary search?

---

# 🎯 Future Improvements

Possible improvements for the project:

* larger CS knowledge base
* hybrid retrieval + generation
* web search fallback
* conversational interface
* more CS topics

---

# 👨‍💻 Author

Rakib Abente

Computer Science student passionate about Artificial Intelligence, Machine Learning, and building real-world AI applications.
