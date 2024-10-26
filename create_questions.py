import os
import random

# Define the questions, correct answers, and options
questions = [
    ("What is the capital of France?", "Paris", ["London", "Berlin", "Madrid", "Paris"]),
    ("What is 2 + 2?", "4", ["3", "4", "5", "6"]),
    ("What is the largest planet in our Solar System?", "Jupiter", ["Earth", "Mars", "Venus", "Jupiter"]),
    ("What is the boiling point of water?", "100", ["90", "80", "100", "120"]),
    ("Who wrote '1984'?", "George Orwell", ["Aldous Huxley", "George Orwell", "Ray Bradbury", "J.K. Rowling"]),
    ("What is the square root of 16?", "4", ["2", "3", "4", "5"]),
    ("What is the currency of Japan?", "Yen", ["Dollar", "Euro", "Yen", "Won"]),
    ("How many continents are there?", "7", ["5", "6", "7", "8"]),
    ("What gas do plants absorb?", "Carbon dioxide", ["Oxygen", "Nitrogen", "Carbon dioxide", "Helium"]),
    ("Who painted the Mona Lisa?", "Leonardo da Vinci", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"]),
    ("What is the smallest prime number?", "2", ["1", "2", "3", "5"])
]

# Create the output folder
folder_name = "example"
os.makedirs(folder_name, exist_ok=True)

# Generate each file with questions
for i, (question, correct_answer, options) in enumerate(questions, 1):
    # Shuffle options with the correct answer at a random position
    shuffled_options = options[:]
    random.shuffle(shuffled_options)
    
    # Write to file
    file_name = f"{i}.frage"
    with open(os.path.join(folder_name, file_name), 'w') as file:
        file.write(f"{question}\n")
        file.write(f"{correct_answer}\n")
        for idx, option in enumerate(shuffled_options, 1):
            file.write(f"{option}\n")

print(f"10 files with questions created in '{folder_name}' folder.")
