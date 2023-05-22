# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))
firstNumber = number // 100
secondNumber = (number % 100) // 10
thirdNumber = number % 10
sumNumber = firstNumber + secondNumber + thirdNumber
print(sumNumber)
