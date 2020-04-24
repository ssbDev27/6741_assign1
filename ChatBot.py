from NLP_Parser import parse_question
from query_executor import runQuery


def main():
    print("Hello! I am your Concordia University Chatbot, How may I help you today? (type 'exit' for closing the bot)")
    while(True):
        #step 1 :question input
        question = input()

        if(question.lower().strip()=="exit"):
            print("Thank you for using Concordia University Chatbot! Hope to see you again")
            exit(0)
        #step 2: parse question
        parsed_ques=parse_question(question)
        print(parsed_ques,"here")
        print(runQuery(parsed_ques[0],parsed_ques[1:]))
        #step 3: build answer
        answer=""
        print(answer)
        #step 3: Ask Again
        print("Hey! Do you have any other questions? (type 'exit' for closing the bot)")



if __name__ == "__main__":
    main()