from flask import Flask, render_template, request, jsonify
from chatbot import FAQChatbot

app = Flask(__name__)

# Initialize chatbot once at startup
print("Initializing FAQ Chatbot...")
bot = FAQChatbot()
print("Chatbot ready!")

@app.route('/')
def index():
    """Render the main chat interface"""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat API requests"""
    data = request.get_json()
    
    if not data or 'message' not in data:
        return jsonify({'error': 'No message provided'}), 400
    
    user_message = data['message'].strip()
    
    if not user_message:
        return jsonify({'error': 'Empty message'}), 400
    
    # Get response from chatbot
    response = bot.get_response(user_message)
    
    return jsonify({
        'answer': response['answer'],
        'matched_question': response['matched_question'],
        'confidence': response['confidence']
    })

@app.route('/faqs', methods=['GET'])
def get_faqs():
    """Return all available FAQ questions"""
    questions = bot.get_all_questions()
    return jsonify({'questions': questions})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
