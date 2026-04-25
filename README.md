# 🤖 AI FAQ Chatbot

A smart FAQ Chatbot built using **Python**, **NLTK**, and **Cosine Similarity** that matches user questions to predefined FAQs and returns the most relevant answer.

---

## 📌 Features

- ✅ Natural Language Processing using **NLTK**
- ✅ Text preprocessing (tokenization, stemming, stopword removal)
- ✅ **TF-IDF Vectorization** for text representation
- ✅ **Cosine Similarity** for question matching
- ✅ Beautiful **Chat UI** with Flask web interface
- ✅ FAQ panel with all available topics
- ✅ Confidence score shown for each answer
- ✅ Suggestion chips for quick questions

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python 3.x | Core language |
| Flask | Web framework |
| NLTK | NLP preprocessing |
| Scikit-learn | TF-IDF & Cosine Similarity |
| NumPy | Numerical operations |
| HTML/CSS/JS | Frontend UI |

---

## 📁 Project Structure

```
faq_chatbot/
│
├── app.py              # Flask web application
├── chatbot.py          # Core chatbot logic (NLP + Matching)
├── faqs.py             # FAQ dataset (questions & answers)
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
│
└── templates/
    └── index.html      # Chat UI frontend
```

---

## ⚙️ How It Works

1. **User** types a question in the chat interface
2. The question is **preprocessed** (lowercased, punctuation removed, tokenized, stopwords removed, stemmed)
3. **TF-IDF Vectorizer** converts the question into a vector
4. **Cosine Similarity** is calculated between the user's question and all FAQ questions
5. The FAQ with the **highest similarity score** is selected
6. Its **answer is returned** to the user with confidence score

---

## 🚀 Setup & Run

### Step 1: Clone the repository
```bash
git clone https://github.com/your-username/faq_chatbot.git
cd faq_chatbot
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the application
```bash
python app.py
```

### Step 4: Open in browser
```
http://localhost:5000
```

---

## 💻 Run Without Web UI (Terminal Mode)

```bash
python chatbot.py
```

---

## 📊 FAQ Topics Covered

- Artificial Intelligence
- Machine Learning
- Deep Learning
- Neural Networks
- NLP & NLTK
- Supervised / Unsupervised / Reinforcement Learning
- Computer Vision & YOLO
- Python, TensorFlow, PyTorch
- Overfitting, Transfer Learning, GANs
- And more...

---

## 🎓 Internship Project

**Task 2: Chatbot for FAQs**  
Completed as part of AI Internship program.

---

## 📄 License

This project is open source and available under the MIT License.
