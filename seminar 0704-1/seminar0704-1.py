#Найдите сумму цифр трехзначного числа.
#Пример:
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

Number = input("Введите трехзначное число: ")
Number = int(Number)

Number1 = Number%10
Number = Number//10
Number2 = Number%10
Number = Number//10
print("Сумма всех цифр заданного числа равна :", Number + Number1 + Number2)
