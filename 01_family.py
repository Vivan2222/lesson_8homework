# -*- coding: utf-8 -*-
import random

from colorama import Fore
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.
class Man:
    salery_money = 0
    eat_food = 0
    coats = 0

    def __init__(self, name, house):
        self.name = name
        self.fullness = 30
        self.happy = 100
        self.house = house
        house.family+=1

    def __str__(self):
        return Fore.GREEN + f'{self.__class__.__name__}, {self.name}, сытость {self.fullness}, счастье {self.happy}, '

    def eat(self):
        if self.house.food < 30:
            # print(Fore.RED + 'Нет еды в доме')
            return 'Нет еды в доме'
        else:
            # print(Fore.CYAN + f'{self.name}, поел')
            self.fullness += 30
            self.house.food -= 30
            Man.eat_food += 30

    def touch_cat(self):
        # print(f'{self.name} гладит кота')
        self.happy += 10


class House:
    cats=0
    family=0
    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0
        self.cat_food = 30

    def __str__(self):
        return Fore.GREEN + f'{self.__class__.__name__} Количество денег {self.money}, количество еды {self.food},' \
f' грязь {self.dirt}, кошачья еда {self.cat_food}'


class Husband(Man):
    def __init__(self, name, house, salary):
        super().__init__(name, house)
        self.salary=salary
    def work(self):
        self.house.money += salary
        self.fullness -= 10
        self.happy -= 10
        Man.salery_money += 150
        # print(Fore.CYAN + f'{self.name} работал {self.house.money}')

    def gaming(self):
        self.happy += 10
        self.fullness -= 10
        # print(Fore.CYAN + f'{self.name} играет в WOT')

    def act(self):
        if self.fullness < 20:
            self.eat()
        elif self.happy <= 50:
            self.gaming()
        elif self.house.money < 360:
            self.work()
        elif self.house.dirt >= 90:
            self.happy -= 10


class Wife(Man):
    def shopping(self):
        if self.house.money < 32:
            pass
            # print(Fore.RED + 'Недостаточно денег')
        else:
            # print(Fore.BLUE + f'{self.name} сходила в магазин')
            self.fullness -= 10
            self.house.food += self.house.family*18

            self.house.money -= self.house.family*18
    def shopping_cat_food(self):
        if self.house.money>self.house.cats*14:
            self.house.cat_food += self.house.cats * 14
            self.fullness-=10
            self.house.money-=self.house.cats*14
            # print(Fore.BLUE+f'{self.name} куила еды коту')
        else:
            pass
            # print(Fore.RED+'Не хватает денег на еду коту')




    def buy_fur_coat(self):
        if self.house.money < 350:
            pass
            # print(Fore.RED + 'Не хватает денег для покупки шубы')
        else:
            self.happy += 60
            self.fullness -= 10
            # print(Fore.BLUE + f'{self.name} купила шубу')
            Man.coats += 1

    def clean_house(self):
        # print(Fore.BLUE + f'{self.name} убралась в доме')
        self.fullness -= 10
        self.happy -= 10
        self.house.dirt -= self.house.dirt

    def act(self):
        if self.fullness < 20:
            self.eat()
        elif self.house.food < self.house.family*24:
            self.shopping()
        elif  self.house.cat_food < self.house.cats * 12:
            self.shopping_cat_food()
        elif self.house.dirt >= 90:
            self.happy -= 10
            self.clean_house()
        elif self.happy < 10:
            self.touch_cat()
        elif self.house.money >= 350:
            self.buy_fur_coat()

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.fullness = 30
        self.house.cats+=1

    def __str__(self):
        return f'{self.__class__.__name__}, имя {self.name}, сыотость {self.fullness}'

    def eat(self):
        if self.house.cat_food < 10:
            # print(Fore.RED +'Нет кошачей еды')
            self.fullness-=10
        else:
            # print(f'кот {self.name} поел')
            self.house.cat_food -= 10
            self.fullness += 20

    def sleep(self):
        # print(f'кот {self.name} спит')
        self.fullness -= 10

    def soil(self):
        # print(f'Кот {self.name} дерет обои')
        self.house.dirt += 5
        self.fullness -= 10

    def act(self):
        dice=random.randint(1, 2)

        if self.fullness <= 15:
            self.eat()
        else:
            if dice==1:
                self.sleep()
            else:
                self.soil()



# home = House()
# serge = Husband(name='Сережа', house=home)
# masha = Wife(name='Маша', house=home)
# cat = Cat('Adolf', home)
# for day in range(365):
#     print(Fore.YELLOW + '================== День {} =================='.format(day))
#     if serge.happy <= 0 or serge.fullness <= 0 or masha.happy <= 0 or masha.fullness <= 0 or cat.fullness <= 0:
#         print(Fore.RED + 'умер')
#         break
#     home.dirt += 10
#     serge.act()
#     masha.act()
#     cat.act()
#     print(serge)
#     print(masha)
#     print(home)
#     print(cat)
# print(f'Заработано денег {Man.salery_money}, сьедено еды {Man.eat_food}, куплено шуб {Man.coats}')


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child(Man):
    def __str__(self):
        return Fore.GREEN + f'{self.__class__.__name__} {self.name}, сытость {self.fullness} счастье {self.happy}'

    def eat(self):
        if self.house.food < 10:
            pass
            # print(Fore.RED + 'Недостаточно еды')
        else:
            # print( Fore.MAGENTA+f'Ребенок {self.name} поел')
            self.fullness += 10
            self.house.food -= 10

    def sleep(self):
        # print(Fore.MAGENTA + f'Ребенок {self.name} спит')
        self.fullness -= 5

    def act(self):
        if self.fullness <= 15:
            self.eat()
        else:
            self.sleep()


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.



class Simulation:
    def __init__(self, food_incidents, money_incidents):
        self.food_incidents_list=[]
        self.money_incidents_list=[]
        for i in range(food_incidents):
            self.food_incidents_list.append(random.randint(1, 365))
        for i in range(money_incidents):
            self.money_incidents_list.append(random.randint(1, 365))

    def experiment(self, salary):
        home = House()
        serge = Husband(name='Сережа', house=home, salary=salary)
        masha = Wife(name='Маша', house=home)
        kolya = Child(name='Коля', house=home)
        cat_list = []
        max_cats=1
        while True:
            for i in range(max_cats):
                murzik = Cat(name='Мурзик', house=home)
                cat_list.append(murzik)
            for day in range(1, 366):
                if day in self.food_incidents_list:
                    home.food/=2
                if day in self.money_incidents_list:
                    home.money/=2
                # print(Fore.YELLOW + '================== День {} =================='.format(day))
                if serge.happy < 0 or serge.fullness < 0 or masha.happy < 0 or masha.fullness < 0:
                    print(Fore.RED + 'умер')
                serge.act()
                masha.act()
                kolya.act()
                # print(serge)
                for cat in cat_list:
                    if cat.fullness < 0:
                        # print(Fore.RED + 'Умер кот')
                        return len(cat_list)-1
                    else:
                        cat.act()
                        # print(cat)
                if day>365:
                    max_cats += 1
                    break





# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

life = Simulation(6, 6)
for salary in range(50, 401, 50):
    max_cats = life.experiment(salary)
    print(Fore.YELLOW+f'При зарплате {salary} максимально можно прокормить {max_cats} котов')