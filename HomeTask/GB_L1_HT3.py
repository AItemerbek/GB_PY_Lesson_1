# Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

number = 385916

leftNum = number // 100_000 + number % 100_000 // 10_000 + number % 10_000 // 1000
rightNum = number % 1000 // 100 + number % 100 // 10 + number % 10

if  leftNum == rightNum:
    print('yes')
else:
    print('no')