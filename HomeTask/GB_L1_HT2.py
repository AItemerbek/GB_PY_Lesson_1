# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

sum = 24

if sum % 6 == 0:
    print(sum // 6, sum // 6 * 4, sum // 6)
else:
    print('Сумма журавликов не соответствует условию задачи')
