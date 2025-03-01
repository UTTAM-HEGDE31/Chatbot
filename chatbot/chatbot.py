from nltk.chat.util import Chat, reflections

# Define the list of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you. What do you need assistance with?",]
    ],
    [
        r"what is your name ?",
        ["My name is TheCleverProgrammer, but you can just call me Robot. I'm a chatbot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well, thank you!", "I'm great! How about you?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright!", "It's OK, never mind that.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"(hi|hey|hello|hola|holla)",
        ["Hello!", "Hey there!",]
    ],
    [
        r"what do you want ?",
        ["Make me an offer I can't refuse.",]
    ],
    [
        r"who created you ?",
        ["Aman Kharwal created me using Python's NLTK library.", "That's a top secret ;)"]
    ],
    [
        r"where do you live ?",
        ["I live in New Delhi, India.",]
    ],
    [
        r"is it raining in (.*)",
        ["I don't have real-time weather updates, but you can check online for %1.",]
    ],
    [
        r"how is your health ?",
        ["Health is very important, but I am a computer, so I don't need to worry about my health.",]
    ],
    [
        r"do you like (sports|games|sport) ?",
        ["I'm a big fan of Cricket!",]
    ],
    [
        r"who is your favorite (Cricketer|Batsman) ?",
        ["Virat Kohli!",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon! :) ", "It was nice talking to you. See you soon! :)"]
    ],
    [
        r"(.*)",
        ["That is nice to hear!", "Tell me more about it."]
    ],
]

# Custom reflections
my_reflections = {
    "go": "gone",
    "hello": "hey there",
    "i am": "you are",
    "i was": "you were",
    "i have": "you have",
    "i": "you",
    "me": "you"
}

# Default message at the start of the chat
print("Hi, I'm TheCleverProgrammer and I like to chat!")
print("Please type in lowercase English to start a conversation. Type 'quit' to leave.")

# Create chatbot instance
chat = Chat(pairs, my_reflections)

# Start conversation
chat.converse()
