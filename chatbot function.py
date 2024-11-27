"""
#task 1
def bank_chatbot():
    user_data={
        "account_balance":5000,
        "recent_transactions":["$100 - Amazon","$50 - Grocery","$200 - Gym"],
        "support_contact":"1800-123-456"
        }
    def respond_to_user(input_query):
        if "balance" in input_query.lower():
            return f"Your account balance is ${user_data['account_balance']}."
        elif "transactions" in input_query.lower():
            return "Your recent transactions are:"+",".join(user_data["recent_transactions"])
        elif "contact" in input_query.lower():
            return f"You can reach support at: {user_data['support_contact']}."
        else:
            return "sorry, I didn't understand that. Please ask about 'balance','transactions', or 'contact'. "
    print("Welcome to the Bank Chatbot!")
    while True:
        user_input=input("How can i help you? (Type 'exit' to quit):")
        if user_input.lower()=="exit":
            print("Thank you for using the Bank Chatbot. Goodbye!")
            break
        else:
            response=respond_to_user(user_input)
            print(response)
bank_chatbot()
"""

#task 2
def quiz():
    quiz_data={
        "What is the capital of France?":"Paris",
        "Which is biggest palnet in solar system?":"Jupiter",
        "What is the chemical symbol for water?":"H2O",
        "Who discovered gravity":"Issac Newton",
        "What is Dhoni's jersey number":"7"
        }
    score=0
    total_questions=len(quiz_data)
    for question,correct_answer in quiz_data.items():
        print(question)
        user_answer=input("Your answer:").strip()
        if user_answer.lower()==correct_answer.lower():
            print("Correct!\n")
            score+=1
        else:
            print(f"Wrong.The correct answer is {correct_answer}.\n")
    print(f"Quiz completed! Your final score is {score}/{total_questions}.")
quiz()
            
    
    

