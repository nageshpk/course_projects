#import module
from random import randrange as r
from time import time as t
#ask how many questions user wants
n_questions = int(input("How many questions you want? "))
#set score start to zero
score = 0
#loop through number of questions
start = t()
for n in range(n_questions):
    num1, num2 = r(1,11), r(1,11)
    ans = num1 * num2
    user_answer = int(input(f'{num1} * {num2} = '))
    if user_answer == ans:
        score += 1
    end = t()


print(f"Thank you for playing! \nYou got correct answers for {score} out of {n_questions} questions ({round(score/n_questions*100)}%) in {round(end-start, 1)} seconds ({round((end-start)/n_questions, 1)} seconds/question)")

