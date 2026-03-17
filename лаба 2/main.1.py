money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
while money_capital + salary >= spend: # проверял можно  ли при помощи подушка + зарплата прожить следующий месяц
    money_capital = money_capital - spend + salary # считаю сколько капитала осталось
    count += 1 # прибавляю прожитый месяц
    spend = spend * increase + spend # индексирую траты




print("Количество месяцев, которое можно протянуть без долгов:", count)
