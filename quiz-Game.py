import random        # USING RANDOM MODULE FOR RE-ARRANGING THE QUESTIONS

# SETS OF QUESTIONS
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Paris", "Berlin", "Madrid"],
        "answer": 2,
    },
    {
        "question": "What is the tallest mountain in the world?",
        "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
        "answer": 1,
        "hint": "It's located in the Himalayas."
    },
    {
        "question": "Which of these is NOT a primary color?",
        "options": ["Red", "Yellow", "Orange", "Blue"],
        "answer": 3,
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 3,
        "hint": "Often referred to as a 'gas giant'"
    },
    {
        "question": "What is the abbreviation for the United States of America?",
        "options": ["USA", "UK", "USSR", "NATO"],
        "answer": 1,
    },
    {
        "question": "Photosynthesis is the process by which plants use sunlight to create:",
        "options": ["Water", "Oxygen", "Carbon", "Dioxide", "Soil"],
        "answer": 2,
        "hint": "Plants breathe in what gas and release what gas during photosynthesis?"
    },
    {
        "question": "How many sides does a hexagon have?",
        "options": ["3", "4", "6", "8"],
        "answer": 3,
    },
    {
        "question": "What is the language spoken in China?",
        "options": ["French", "Mandarin", "Spanish", "Arabic"],
        "answer": 2,
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Michelangelo", "Leonardo da Vinci", "Vincent van Gogh", "Pablo Picasso"],
        "answer": 2,
        "hint": "Think about a famous Renaissance artist from Italy"
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Euro", "Dollar", "Yen", "Rupee"],
        "answer": 3
    },
]

# FUNCTION FOR DISPLAYING QUESTIONS
def displayQuest(q_data):
    """PRINTS THE QUESTIONS AND OPTIONS"""
    print(q_data['question'])
    for i, answer in enumerate(q_data['options'], start=1):
        print(f"{i}. {answer}")

# FUNCTION FOR FETCHING ANSWER FROM USER
def userAnswer(num_ops):
    """GETS USERS INPUT FOR THEIR ANSWER"""
    while True:
        try:
            answer = int(input("Enter Your Answer(1-"+str(num_ops)+"): "))
            if 1<= answer <= num_ops:
                return answer
            else:
                print('Invalid answer. Please enter a number between 1 and', num_ops)
        except ValueError:
            print('Invalid Input. Please enter a number.')

# FUNCTION FOR CHECKING THE ANSWER
def checkAnswer(user_ans, correct_ans):
    """CHECKS IF THE USERS ANSWER IS CORRECT OR NOT"""
    return user_ans == correct_ans

# MAIN FUNCTION FOR SHUFFLING THE QUESTIONS
def main():
    random.shuffle(quiz_data)
    score= 0
    for question in quiz_data:
        displayQuest(question)
        user_ans = userAnswer(len(question['options']))
        if checkAnswer(user_ans , question["answer"]):
            print('CORRECT')
            print()
            score+= 1
        else:
            print("INCORRECT")
            print()
            if 'hint' in question:
                print('Hint: ', question['hint'])

    print(f"Final Score: {score} / {len(quiz_data)}")

# IF STATEMENT FOR EXECUTING THE GAME
if __name__ == "__main__":
    main()
