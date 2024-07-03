# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.

fistClass = 20
secondClass = 21
thirdClass = 22

minDesks = (fistClass // 2 + secondClass // 2 + thirdClass // 2
            + int(fistClass % 2 > 0) + int(secondClass % 2 > 0) + int(thirdClass % 2 > 0))

print(minDesks)