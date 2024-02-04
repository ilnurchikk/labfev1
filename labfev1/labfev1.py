###################1 ОТОБРАЖАЕТ ФОРМОТИРОВАННЫЙ ТЕКСТ

def ex_1():
    return "“Don't let the noise of others' opinions\n drown out your own inner voice.\" \n\t\t\t\t\t\t\t Steve Jobs"
print(ex_1())



###########################2#функция котороя принимает два числа и качестве параметра и отображает все не четные числа между ними
# def ex_2(a, b):
#
#     print(f"между числами {a} и {b}, содержатся следующие нечетные числа ")
#     for i in range(a, b +1):
#         if i % 2 !=0:
#             print(i, end=" ")
#
# ex_2(1, 10)
#
# num = int(input("enter num"))
#
# num_1 = int(input("enter num"))
#
# ex_2(num, num_1)

######################################3

# def ex_3():
#     a = int(input("введите размер линии: "))
#     b = input("Введите направление линии если горизонтальная напишите 'gor' если вертикальная напишите 'ver': ")
#     c = input("Введите символ линиии: ")
#     if b == "gor":
#         print(c * a)
#     elif b == "ver":
#         for i in range(a):
#             print(c)

# ex_3()

################4

# def as_4(a, b, c, d):
#     return max(a, b, c, d)
# print (as_4(1, 5, 7, 8))

################5


# def as_5():
#
#     a = int(input("первое значение"))
#     b = int(input("второе значение"))
#     sum1 = 0
#     for i in range(a, b + 1):
#         sum1 += i
#     return sum1
# print(as_5())

####################6

# def as_6():
#     a = int(input("Узнайте простое ли число"))
#
#     if a % 2 == 0:
#         return False
#     else:
#         return True
#
# print(as_6())

########################7
chas = input('Введите любое шестизначное число: ')
def as_7(chas):
    a = []
    if len(a) != 6:
        [a.append(int(i)) for i in chas]
        ch1 = a[:3]
        as2 = a[3:]
        s1 = sum(ch1)
        s2 = sum(as2)
        if s1 == s2:
            print("Cчастливое")
        else:
            print("Несчастливое")
print(as_7(chas))
