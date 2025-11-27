# AI-Chatbot-with-NLP

## Objective:
To build a functional, rule-based conversational AI Chatbot using Natural Language Processing (NLP) techniques to process user queries and provide contextual answers.

## Knowledge Base and Intent Mapping:
The chatbot's knowledge is structured in a **JSON-like dictionary** defining multiple `intents` (e.g., 'greeting', 'farewell', 'codtech_info'). Each intent maps a list of user phrases (`patterns`) to a list of suitable replies (`responses`).

## Natural Language Processing (NLP) Pipeline:
The **NLTK (Natural Language Toolkit)** library handles core text processing:
1.  **Tokenization**: User input is broken down into tokens (words).
2.  **Lemmatization**: Tokens are reduced to their root form (e.g., 'running' becomes 'run') using `WordNetLemmatizer` to ensure consistent pattern matching.
3.  **Intent Matching**: A simple **Bag-of-Words (BoW)** method is employed. The script counts matching lemmatized tokens between the user's query and the stored patterns to determine the most likely intent tag.

## Conversational Interface:
The script runs in a continuous interactive loop. Once the intent is matched, the `get_response()` function randomly selects a reply from the available responses for that intent, adding variety to the conversation. A fallback response is provided if no intent is matched.

The final deliverable is the **Python script** (`chatbot.py`) that runs the interactive chatbot program.

# OUTPUT
<img width="580" height="245" alt="Image" src="https://github.com/user-attachments/assets/2720d1ce-e8de-45f6-ae98-3fcb0f764cdb" />
