from random import randint

def logic(user):
    win_value = randint(1, 30)
    if user == win_value:
        print(f'вы выйграли, выйгрышное число {win_value}')
        return True
    else:
        print(f'вы проиграли, выйгрышное число {win_value}')
        return False