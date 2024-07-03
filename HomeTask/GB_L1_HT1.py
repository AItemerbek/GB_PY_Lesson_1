# Найдите сумму цифр трехзначного числа.
num = 100

numSumm = num // 100 + num % 100 // 10 + num % 10

print(numSumm)