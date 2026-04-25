import nltk
import string
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from faqs import faqs

# Download required NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

class FAQChatbot:
    def __init__(self):
        self.faqs = faqs
        self.stemmer = PorterStemmer()
        self.stop_words = set(stopwords.words('english'))
        self.vectorizer = TfidfVectorizer()
        
        # Preprocess all FAQ questions
        self.faq_questions = [faq['question'] for faq in self.faqs]
        self.faq_answers = [faq['answer'] for faq in self.faqs]
        self.processed_questions = [self.preprocess(q) for q in self.faq_questions]
        
        # Fit vectorizer on all FAQ questions
        self.tfidf_matrix = self.vectorizer.fit_transform(self.processed_questions)
    
    def preprocess(self, text):
        """Clean and preprocess text using NLTK"""
        # Lowercase
        text = text.lower()
        # Remove punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        # Tokenize
        tokens = word_tokenize(text)
        # Remove stopwords and stem
        tokens = [
            self.stemmer.stem(token)
            for token in tokens
            if token not in self.stop_words and token.isalpha()
        ]
        return ' '.join(tokens)
    
    def get_response(self, user_question):
        """Find the best matching FAQ and return its answer"""
        if not user_question.strip():
            return {
                "answer": "Please type a question so I can help you!",
                "matched_question": None,
                "confidence": 0
            }
        
        # Preprocess user question
        processed_user_q = self.preprocess(user_question)
        
        if not processed_user_q.strip():
            return {
                "answer": "I couldn't understand your question. Please try rephrasing it.",
                "matched_question": None,
                "confidence": 0
            }
        
        # Vectorize user question and compute cosine similarity
        user_vector = self.vectorizer.transform([processed_user_q])
        similarities = cosine_similarity(user_vector, self.tfidf_matrix).flatten()
        
        # Get best match
        best_idx = np.argmax(similarities)
        best_score = similarities[best_idx]
        
        # Threshold: if similarity is too low, return fallback
        if best_score < 0.1:
            return {
                "answer": "I'm sorry, I don't have an answer for that question. Please try asking something related to Artificial Intelligence or Machine Learning!",
                "matched_question": None,
                "confidence": round(float(best_score) * 100, 2)
            }
        
        return {
            "answer": self.faq_answers[best_idx],
            "matched_question": self.faq_questions[best_idx],
            "confidence": round(float(best_score) * 100, 2)
        }
    
    def get_all_questions(self):
        """Return list of all FAQ questions"""
        return self.faq_questions


# Test the chatbot
if __name__ == "__main__":
    bot = FAQChatbot()
    print("FAQ Chatbot initialized! Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! Have a great day!")
            break
        
        response = bot.get_response(user_input)
        print(f"Bot: {response['answer']}")
        if response['matched_question']:
            print(f"  (Matched: '{response['matched_question']}' | Confidence: {response['confidence']}%)")
        print()
