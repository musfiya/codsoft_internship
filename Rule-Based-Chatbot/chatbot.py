
from intents import INTENTS
from knowledge_base import KNOWLEDGE_BASE
from weather import get_weather


def detect_intent(user_input):
    """
    Detect the user's intent by comparing the normalized
    input against predefined patterns.
    """

    user_input = user_input.lower().strip()

    for intent, patterns in INTENTS.items():
        for pattern in patterns:

            pattern = pattern.lower().strip()

            # Exact match
            if user_input == pattern:
                return intent

            # Pattern appears as a complete phrase
            if f" {pattern} " in f" {user_input} ":
                return intent
        

    return "unknown"
def extract_city(user_input):
    """
    Extract a city name from common weather questions.
    """

    user_input = user_input.lower().strip()

    prefixes = [
        "weather in ",
        "temperature in ",
        "forecast in ",
        "how is the weather in ",
        "what is the weather in ",
        "what's the weather in "
    ]

    for prefix in prefixes:
        if prefix in user_input:
            city = user_input.split(prefix, 1)[1].strip()

            if city:
                return city

    return None


def generate_response(intent,user_input):
    if intent == "weather":
        city = extract_city(user_input)

        if city:
            return get_weather(city)

        return (
            "Sure! Tell me the city you want the weather for. "
            "For example: 'weather in Bangalore'."
    )

    if intent == "greeting":
        return "Hello! Nice to meet you. How can I help you?"

    elif intent == "name":
        return "I'm a rule-based NLP chatbot."

    elif intent == "how_are_you":
        return "I'm doing great! Thanks for asking."

    elif intent == "help":
        return (
            "I can answer questions about AI, machine learning, "
            "neural networks, deep learning, NLP, Python, "
            "and computer vision."
        )

    elif intent in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[intent]

    elif intent == "goodbye":
        return "Goodbye! Have a great day!"

    else:
        return (
            "I'm sorry, I don't understand that yet. "
            "Try asking me about AI, machine learning, NLP, "
            "Python, or neural networks."
        )


print("============================================")
print("        RULE-BASED NLP CHATBOT")
print("============================================")
print("Type 'bye' to exit.\n")


while True:

    user_input = input("You: ")

    intent = detect_intent(user_input)

    response = generate_response(intent,user_input)

    print("Bot:", response)

    if intent == "goodbye":
        break



