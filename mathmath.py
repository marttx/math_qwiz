import random
def qwiz(a, b):
    one=random.randint(a, b)
    two=random.randint(a, b)
    znak=random.choice(["-", "*", "+", "/"])
    new=f"{one}{znak}{two}"
    return new
def check_answer(new, user_answer):
    try:
        user_answer=round(user_answer, 2)
        return user_answer==eval(new)
    except ValueError:
        return False
def math_quiz(number_of_questions=1):
    otvet=0
    print("Добро пожаловать в игру")
    for i in range(number_of_questions):
        new=qwiz(200, 1000)
        user_answer=input(f"{new}= ")
        if check_answer(new, user_answer):
            otvet+=1
    print("Тест завершен")
    print(f"вы набрали {otvet} баллов")
    if otvet>=number_of_questions*0.9:
        print("ваша оценка 5")
    elif otvet>=number_of_questions*0.6:
        print("ваша оценка 4")
    else:
        print("попробуй ещё")
math_quiz(1)









