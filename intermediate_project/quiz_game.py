questions= [
    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Neptune"],
        "answer": "B"
    },
    {
        "question": "What is the boiling point of water at sea level?",
        "choices": ["A) 50°C", "B) 75°C", "C) 100°C", "D) 125°C"],
        "answer": "C"
    },
    {
        "question": "Which element is known as the 'building block of life'?",
        "choices": ["A) Oxygen", "B) Carbon", "C) Hydrogen", "D) Nitrogen"],
        "answer": "B"
    },
    {
        "question": "What is the hardest natural substance on Earth?",
        "choices": ["A) Gold", "B) Iron", "C) Diamond", "D) Platinum"],
        "answer": "C"
    }
]

def quiz(questions):
    score = 0  
    
    for item in questions:
        print(item["question"]) 
        print("\n".join(item["choices"])) 
        
        answer = input("Your answer (A/B/C/D): ").upper()
        while answer not in ["A", "B", "C", "D"]:
            print("Invalid input. Please enter A, B, C, or D.")
            answer = input("Your answer (A/B/C/D): ").upper()
        
        if answer == item["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {item['answer']}.\n")
    
    print(f"Quiz completed! You got {score} out of {len(questions)} correct.")

quiz(questions)
