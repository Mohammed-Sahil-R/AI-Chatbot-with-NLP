import nltk
from nltk.stem import WordNetLemmatizer
import random
import json

lemmatizer = WordNetLemmatizer()

intents_data = {
    "intents": [
        {"tag": "greeting",
         "patterns": ["Hi", "Hello", "Hey", "Good day", "Greetings"],
         "responses": ["Hello!", "Hi there!", "How can I assist you today?", "Pleased to meet you!"]},
        {"tag": "farewell",
         "patterns": ["Bye", "See you later", "Goodbye", "Talk to you later"],
         "responses": ["Goodbye!", "See you soon!", "Take care! Have a great day!"]},
        {"tag": "codtech_info",
         "patterns": ["What is CODTECH", "Tell me about the internship", "What do you do", "About the company"],
         "responses": ["CODTECH offers technology internships and training programs.", "This is a Python internship organized by CODTECH IT Solutions."]},
        {"tag": "thanks",
         "patterns": ["Thank you", "Thanks", "That helps"],
         "responses": ["You're welcome!", "Anytime!", "Glad I could help."]}
    ]
}

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def get_tag(sentence):
    sentence_words = clean_up_sentence(sentence)
    best_match_tag = None
    max_match_count = 0
    
    for intent in intents_data['intents']:
        # Create a single list of all unique lemmatized words from all patterns in the current intent
        intent_words = clean_up_sentence(' '.join(intent['patterns']))
        
        # Count the number of user words that match the intent's pattern words
        match_count = sum(1 for word in sentence_words if word in intent_words)
        
        if match_count > max_match_count:
            max_match_count = match_count
            best_match_tag = intent['tag']

    return best_match_tag

def get_response(tag):
    if tag:
        for intent in intents_data['intents']:
            if intent['tag'] == tag:
                return random.choice(intent['responses'])
    return "I'm sorry, I couldn't understand that query. Can you please rephrase it?"


# Main Chat Loop
print("🤖 Chatbot: Hello! I'm your CODTECH assistant. Type 'quit' or 'exit' to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']:
        print("🤖 Chatbot: Goodbye!")
        break

    tag = get_tag(user_input)
    response = get_response(tag)
    print(f"🤖 Chatbot: {response}")
