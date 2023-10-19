from decouple import config
from win_lose_logic import logic

def start_game():
   my_money=int(config('MY_MONEY'))
   while my_money > 0:
       user = int(input('на какое число будете ставить?:'))
       user_money = int(input('сколько денег будете ставить?:'))
       if 31 < user or user < 0:
           print('нет такого числа')
       elif user_money > my_money:
           print('у вас нет столько денег!!!')
       else:
           if logic(user):
               my_money += user_money
           else:
               my_money -= user_money
       game_accept = int(input('будете еще играть?\n'
                               '0 - не буду\n'
                               '1 - буду\n'
                               'пишите только 0 или 1'))
       if game_accept == 0:
           break
       elif game_accept == 1:
           print(f'играем дальше у вас осталось {my_money}')
           continue
       else:
           print('мы вас не поняли\n выход из игры')
           break

       if my_money > int(config('MY_MONEY')):
           print('вы в выйграше')
       elif my_money == int(config('MY_MONEY')):
           print('ничья')
       else:
           print('ура вы проиграли')
