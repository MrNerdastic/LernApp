import os
import random

# Define the questions and their options
questions = [
    {
        "question": "What is the largest desert in the world?",
        "correct_answer": "Sahara",
        "options": ["Sahara", "Kalahari", "Gobi", "Atacama"]
    },
    {
        "question": "What is the chemical symbol for water?",
        "correct_answer": "H2O",
        "options": ["H2O", "O2", "CO2", "NaCl"]
    },
    {
        "question": "Who was the first president of the United States?",
        "correct_answer": "George Washington",
        "options": ["George Washington", "Thomas Jefferson", "Abraham Lincoln", "John Adams"]
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "correct_answer": "William Shakespeare",
        "options": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"]
    },
    {
        "question": "What is the value of pi to two decimal places?",
        "correct_answer": "3.14",
        "options": ["3.14", "3.00", "3.12", "3.16"]
    },
    {
        "question": "What is the highest-grossing film of all time (as of 2023)?",
        "correct_answer": "Avatar",
        "options": ["Avatar", "Titanic", "Avengers: Endgame", "Star Wars: The Force Awakens"]
    },
    {
        "question": "Who is known as the 'King of Pop'?",
        "correct_answer": "Michael Jackson",
        "options": ["Michael Jackson", "Elvis Presley", "Prince", "Freddie Mercury"]
    },
    {
        "question": "What does HTTP stand for in web technology?",
        "correct_answer": "HyperText Transfer Protocol",
        "options": ["HyperText Transfer Protocol", "HyperText Transmission Protocol", "High Transfer Text Protocol", "Hyperlink Text Transfer Protocol"]
    }
]

# Create files for each question
output_directory = '/mnt/data/questions'  # Directory to save question files
os.makedirs(output_directory, exist_ok=True)

for index, q in enumerate(questions, start=1):
    file_name = f"{index}.frage"
    file_path = os.path.join(output_directory, file_name)
    
    # Prepare the content for the file
    content = [
        q["question"],
        q["correct_answer"],
        "",  # Free line
    ] + q["options"] + [""]  # Add options and a free line at the end
    
    # Randomly shuffle the options
    random.shuffle(content[3:])  # Shuffle only the options part
    content = content[:3] + content[3:]  # Keep the question and correct answer first
    
    # Write to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        for line in content:
            f.write(line + "\n")

# List of created files
os.listdir(output_directory)
