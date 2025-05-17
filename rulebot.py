import re

def chatbot():
    print("Hello! I'm RuleBot. How can I help you today? (type 'exit' to end)\n")
    
    while True:
        user_input = input("You: ").lower()
        
        if user_input == 'exit':
            print("RuleBot: Goodbye! Have a great day!")
            break

        # Rule-based responses
        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("RuleBot: Hello there! How can I assist you?")
        
        elif re.search(r"\bhow are you\b", user_input):
            print("RuleBot: I'm just a program, but thanks for asking!")

        elif re.search(r"\b(what can you do|help)\b", user_input):
            print("RuleBot: I can answer basic questions, greet you, or tell you the time!")

        elif re.search(r"\btime\b", user_input):
            from datetime import datetime
            now = datetime.now().strftime("%H:%M:%S")
            print(f"RuleBot: The current time is {now}.")

        elif re.search(r"\b(name|who are you)\b", user_input):
            print("RuleBot: I'm RuleBot, your simple rule-based chatbot.")

        elif re.search(r"\bthank(s| you)\b", user_input):
            print("RuleBot: You're welcome!")

        elif re.search(r"\bbye\b", user_input):
            print("RuleBot: Bye! Take care.")
            break
        
        else:
            print("RuleBot: Sorry, I didn’t understand that. Could you please rephrase?")

# Run the chatbot
chatbot()
