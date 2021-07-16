#Объект
flowers = ['Розы','Ромашки','Гвоздики','Тюльпаны']
accessories = ['Бумага','Целлофан','Ленточка']
the_cost_of_flowers = {
    'Роза' : 5,
    'Ромашка' : 7,
    'Гвоздика' : 4,
    'Тюльпан' : 3 
}
the_cost_of_accessories = {
    'Бумага' : 1,
    'Целофан' : 0.50 ,
    'Ленточка' : 0.50
}
sorting_substance = {
    'Роза' : 1,
    'Гвоздика' : 1.5,
    'Тюльпан' : 3,
    'Ромашка' : 2 
}
freshness_level = ('Свежие','Вчерашние','Вялые')
length_of_colors = (40 , 50 , 60 , 80)
length_of_colors_dict = {
    'Роза' : 100,
    'Гвоздика' : 60,
    'Тюльпан' : 40,
    'Ромашка' : 80 
}
count = 0
flag = True
bouquet = {}
cost_bouquet = {}
length_bouquet = {}
sorting_bouquet = {}
#Методы
#Посторение иерархии цветов соласно стоимости
print("Иерархия цветов согласно стоимости:\n")
for value in sorted(the_cost_of_flowers.values()):
     for key in the_cost_of_flowers.keys():
        if the_cost_of_flowers[key] == value:
            print (key,'-' ,the_cost_of_flowers[key])
#Сортировка аксессуаров по цене
print("Иерархия аксессуаров согласно стоимости:\n")
for value in sorted(the_cost_of_accessories.values()):
     for key in the_cost_of_accessories.keys():
        if the_cost_of_accessories[key] == value:
            print (key,'-' ,the_cost_of_accessories[key])
#Сортировка цветов в букете на основе свежести
print("\nИерархия цветов согласно свежести:\n")
for value in sorted(sorting_substance.values()):
     for key in sorting_substance.keys():
        if sorting_substance[key] == value:
            print (key,'-' , sorting_substance[key])
#Сортировка цветов в букете на основе длины стебля
print("Иерархия цветов согласно длины стебля:\n")
for value in sorted(length_of_colors_dict.values()):
     for key in length_of_colors_dict.keys():
        if length_of_colors_dict[key] == value:
            print (key,'-' ,length_of_colors_dict[key])
#Сборка букета
answer = input('Ты хочешь собрать букет ? y/n \n')
while True:
    if answer.lower() == 'y':
        print('Хорошо, выбирайте что у нас есть из иерархии.')
        while True:
            answer_flower = input('Введите цветок который хотите.\nЕсли хотите закончить то введите n\n')
            print(bouquet)
            if answer_flower.lower() != 'n':
                if answer_flower in the_cost_of_flowers:
                    if answer_flower not in bouquet:
                        bouquet[answer_flower] = the_cost_of_flowers[answer_flower]
                    elif answer_flower in bouquet:
                        print('Такой цветок уже есть в букете.')
                else:
                    print('Такого цветка у нас нет, выбери дургой цветок.')
            elif answer_flower == 'n':
                if len(bouquet) > 0:
                    print('Вот такой букет у тебя получился:')
                    for key in bouquet:
                        print (key)
                    print('Сортировка букета на основе цены (в рублях):')
                    for value in sorted(bouquet.values()):
                        for key in bouquet.keys():
                            if bouquet[key] == value:
                                print (key,'-' ,bouquet[key])
                    break
                elif len(bouquet) == 0:
                    print('Вы не смогли собрать букет, досвидули!')
                    break
        break
    else:
        print('Досвидания!')
        break     
#Сборка аксессуаров           
if len(bouquet) != 0:
        answer_bouquet = input('Вы хотите добавить акссесуары ? y/n \n')
        while True:
            if answer_bouquet.lower() == 'y':
                while True:
                    our_answer_bouquet = input('Выбире аксессуары из иерархии:\nЕсли хочешь закончить нажми n\n')
                    print(cost_bouquet)
                    if our_answer_bouquet != 'n':
                        if our_answer_bouquet in the_cost_of_accessories:
                            if our_answer_bouquet not in cost_bouquet:
                                cost_bouquet[our_answer_bouquet] = the_cost_of_accessories[our_answer_bouquet]
                            elif our_answer_bouquet in cost_bouquet:
                                print('Такой аксессуар у вас уже есть.')
                        else:
                            print('Такоко аксессуара у нас нет.')
                    elif our_answer_bouquet == 'n':
                        if len(cost_bouquet) > 0:
                            print('Вот такие аксессуары ты выбрал:')
                            for key in cost_bouquet:
                                print(key)
                            print('Сортировка аксессуаров по цене (в рублях):')
                            for value in sorted(cost_bouquet.values()):
                                for key in cost_bouquet.keys():
                                    if cost_bouquet[key] == value:
                                        print (key,'-' ,cost_bouquet[key])
                            break
                        elif len(cost_bouquet) == 0:
                            print('Вы не смогли собрать аксессуары, досвидули!')
                            break
                break
            else:
                print('Досвидания')
                break
#Определить стоимость букета
if len(bouquet) != 0:
    sum_bouquet = sum(bouquet.values())
    print('С вас за букет: '+str(sum_bouquet)+' рублей.')
if len(cost_bouquet) != 0:
    sum_cost_bouquet = sum(cost_bouquet.values())
    print('С вас за аксуссуары: '+str(sum_cost_bouquet)+' рублей.')
    print('Итого за все с вас:',sum_bouquet + sum_cost_bouquet,' рублей.')
#Сортировка по свежести и по длине стебля
if len(cost_bouquet) != 0:
    answer = input('Хотите выполнить сортировку по свежести ? y/n\n')
    while True:
        if answer.lower() =='y':
            while True:
                answer_sort = input('Введите ваш букет, пожалуйста.\nЕсли хотите закончить то введите n\n')
                print(sorting_bouquet)
                if answer_sort.lower() != 'n':
                    if answer_sort in sorting_substance:
                        if answer_sort not in sorting_bouquet:
                            sorting_bouquet[answer_sort] = sorting_substance[answer_sort]
                        elif answer_sort in sorting_bouquet:
                            print('Такой цветок уже есть в букете.')
                    else:
                        print('Такого цветка у нас нет, выбери дургой цветок.')
                elif answer_sort == 'n':
                    if len(sorting_bouquet) > 0:
                        print('Вот такой букет у тебя получился:')
                        for key in sorting_bouquet:
                            print (key)
                        print('Сортировка букета на основе свежести:\n1 - Свежие\n2 - Вчерашние\n3 - Вялые')
                        for value in sorted(sorting_bouquet.values()):
                            for key in sorting_bouquet.keys():
                                if sorting_bouquet[key] == value:
                                    print (key,'-' ,sorting_bouquet[key])
                        break
                    elif len(sorting_bouquet) == 0:
                        print('Ну желание клиента законy.')
                        break
            break
        else:
            print('Ну желание клиента закон.')
            break  
if len(sorting_bouquet) != 0:
    answer = input('Хотите выполнить сортировку по длине стебля ? y/n\n')
    while True:
        if answer.lower() =='y':
            while True:
                answer_len = input('Введите ваш букет, пожалуйста.\nЕсли хотите закончить то введите n\n')
                print(length_bouquet)
                if answer_len.lower() != 'n':
                    if answer_len in length_of_colors_dict:
                        if answer_len not in length_bouquet:
                            length_bouquet[answer_len] = length_of_colors_dict[answer_len]
                        elif answer_len in length_bouquet:
                            print('Такой цветок уже есть в букете.')
                    else:
                        print('Такого цветка у нас нет, выбери дургой цветок.')
                elif answer_len == 'n':
                    if len(length_bouquet) > 0:
                        print('Вот такой букет у тебя получился:')
                        for key in length_bouquet:
                            print (key)
                        print('Сортировка букета на основе длины стебля:\n40 см\n60 см\n80 см\n100 см')
                        for value in sorted(length_bouquet.values()):
                            for key in length_bouquet.keys():
                                if length_bouquet[key] == value:
                                    print (key,'-' ,length_bouquet[key])
                        break
                    elif len(length_bouquet) == 0:
                        print('Ну желание клиента закон.')
                        break
            break
        else:
            print('Ну желание клиента закон.')
            break
