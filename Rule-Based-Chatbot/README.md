# Rule-Based NLP Chatbot

## Overview

This project is a rule-based chatbot developed using Python. It uses predefined patterns and intent detection to understand common user queries and generate appropriate responses.

The project demonstrates fundamental concepts of Natural Language Processing (NLP), pattern matching, intent classification, conversation flow, and API integration.

## Features

* Rule-based intent detection
* Pattern matching for user queries
* Predefined NLP knowledge base
* Greeting and conversational responses
* AI and Machine Learning related questions
* Neural Network and Deep Learning explanations
* NLP, Python, and Computer Vision information
* Live weather information using an external API
* City extraction from weather queries
* Error handling for API failures
* Empty-input handling
* Modular Python structure

## Supported Topics

The chatbot can respond to questions related to:

* Artificial Intelligence
* Machine Learning
* Neural Networks
* Deep Learning
* Natural Language Processing
* Python
* Computer Vision

It can also retrieve current weather information for a specified city.

## How It Works

The chatbot follows a simple processing pipeline:

```text
User Input
     ↓
Input Normalization
     ↓
Intent Detection
     ↓
Pattern Matching
     ↓
 ┌───────────────────────┐
 │                       │
Knowledge Base       Weather API
 │                       │
 └───────────┬───────────┘
             ↓
      Response Generation
             ↓
        Bot Response
```

For predefined questions, the chatbot identifies the matching intent and retrieves an appropriate response from the knowledge base.

For weather-related questions, the chatbot identifies the weather intent, extracts the city name, and retrieves current weather information through the Open-Meteo API.

## Project Structure

```text
Rule-based chatbot/
│
├── chatbot.py
├── intents.py
├── knowledge_base.py
├── weather.py
├── README.md
└── .venv/
```

### `chatbot.py`

Contains the main chatbot program, intent detection, response generation, city extraction, and conversation loop.

### `intents.py`

Contains predefined user-input patterns mapped to different intents.

### `knowledge_base.py`

Contains predefined responses and explanations for supported technical topics.

### `weather.py`

Handles communication with the Open-Meteo API and converts weather information into readable responses.

## Technologies Used

* Python
* Natural Language Processing concepts
* Rule-Based Pattern Matching
* REST API
* JSON
* Requests library
* Open-Meteo API

## Example Interaction

```text
You: hi
Bot: Hello! Nice to meet you. How can I help you?

You: what is machine learning
Bot: Machine learning is a branch of artificial intelligence
where computers learn patterns from data to make predictions
or decisions.

You: what is a neural network
Bot: A neural network is a machine learning model made up of
interconnected nodes that learn patterns from data.

You: weather in Bangalore
Bot: Current weather in Bengaluru:
Temperature: XX°C
Condition: Partly cloudy
Humidity: XX%
Wind Speed: XX km/h
```

## Installation

Clone or download the project and open the project directory in a terminal.

Install the required dependency:

```bash
python -m pip install requests
```

Run the chatbot:

```bash
python chatbot.py
```

## Limitations

This chatbot is rule-based and does not use a trained machine learning or large language model.

Therefore, it can only recognize queries covered by its predefined patterns. Queries outside the supported intents may result in a fallback response.

## Learning Outcomes

This project demonstrates:

* Basic NLP concepts
* Intent identification
* Pattern matching
* Conversation flow
* Modular Python programming
* API integration
* JSON data handling
* Exception handling

## Future Improvements

Possible future improvements include:

* More advanced NLP-based intent classification
* Context-aware conversations
* Larger knowledge bases
* Sentiment analysis
* Database-backed conversation history
* Web-based user interface
* Machine-learning-based intent classification
