# Here are some of the questions 
questions = [
    ["Who is Shah Rukh Khan?", "WWE Wrestler", "Plumber", "Actor", "Astronaut", 3],
    ["What is the capital of France?", "Berlin", "Paris", "Rome", "London", 2],
    ["Which planet is known as the Red Planet?", "Earth", "Venus", "Mars", "Jupiter", 3],
    ["What is the largest mammal?", "Shark", "Blue Whale", "Elephant", "Giraffe", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Shakespeare", "Jane Austen", "Charles Dickens", "Homer", 1],
    ["What is the square root of 64?", "8", "10", "6", "12", 1],
    ["Which country is known as the Land of the Rising Sun?", "India", "South Korea", "Japan", "China", 3],
    ["Who painted the Mona Lisa?", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "Vincent van Gogh", 3],
    ["What is the fastest land animal?", "Horse", "Lion", "Cheetah", "Elephant", 3],
    ["Which ocean is the largest?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["What is the smallest country in the world?", "San Marino", "Vatican City", "Monaco", "Liechtenstein", 2]
]

#Respected prizes as per the questiions
prizes = [10000, 20000, 30000, 50000, 100000, 500000, 900000, 1000000, 150000, 190000, 5000000]

i = 0
for question in questions:
    print(f"{question[0]}")
    print(f"Options are: \n(1){question[1]}\n(2){question[2]}\n(3){question[3]}\n(4){question[4]}")

    # check weather answers are correct or not
    output = int(input("Select any option from [1, 2, 3, 4]: "))
    if output == question[5]:
        print("Correct answer!")
    else:
        print("You lost... Better luck next time!")
        break
    print(f"you won prize money of: {prizes[i]}")

    i += 1
