# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

S = input("Введите общее количество журавликов, которое сделали все дети:  ")
S=int(S)
if S%2==1:
  print("Общее количество журавликов должно быть четным")
else:
  print("Петя и Сережа вместе сделали", S//3 ,"журавликов , каждый из них сделал ", S//6, ", а Катя сделала ", S//3*2 , "журавликов.")