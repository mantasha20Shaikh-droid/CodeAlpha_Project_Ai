# TASK 2 — FAQ Chatbot

print("----Task 2 - FAQ Chatbot----")

!pip install nltk scikit-learn gradio -q

# Import Libraries
import nltk
nltk.download('punkt')

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import gradio as gr

# FAQ Questions
questions = [
    "What is AI?",
    "What is Machine Learning?",
    "What is Python?",
    "What is Deep Learning?"
]

# FAQ Answers
answers = [
    "AI means Artificial Intelligence.",
    "Machine Learning is a subset of AI.",
    "Python is a programming language.",
    "Deep Learning uses neural networks."
]

# Convert Questions to Vectors
vectorizer = TfidfVectorizer()

X = vectorizer.fit_transform(questions)

# Chatbot Function
def chatbot(user_input):

    # Handle Empty Input
    if user_input.strip() == "":
        return "Please enter a question."

    # Convert User Input to Vector
    user_vec = vectorizer.transform([user_input])

    # Similarity Check
    similarity = cosine_similarity(user_vec, X)

    # Get Best Match
    index = np.argmax(similarity)

    return answers[index]

# Gradio Interface
iface = gr.Interface(
    fn=chatbot,

    inputs=gr.Textbox(
        lines=2,
        placeholder="Ask a question..."
    ),

    outputs=gr.Textbox(label="Answer"),

    title=" FAQ Chatbot",

    description="Simple AI FAQ Chatbot using TF-IDF and Cosine Similarity"
)

# Launch App
iface.launch(debug = True)
