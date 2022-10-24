ticket = int(input("Какое количество билетов Вы хотите приобрети?"))
age = [int(input("Сколько Вам лет?")) for i in range(ticket)]
print(age)
print(', '.join(map(str,age)))
a1 = str(age).strip('[]')
if a1 < str(18):
   s = 0
   print (s)
elif str(18) <= a1 <= str(25):
   s = 990
   print (s)
else:
   s = 1390
   print(s)


   #Программа работает, если ввести количество 1 билет, если ввести больше, не смогла сделать так,
   #чтобы рассчитывалась сумма. Рассчитывается только первое число.










