tickets = int(input("При покупке более 3-х билетов, действует скидка 10% от стоимости заказа!\n"
                    "Введите кол-во билетов, которое хотите приобрести: "))
list_tickets = list(range(1, tickets + 1))

old = [input("Введите возраст для каждого посетителя, через 'enter': ") for i in range(tickets)]
list_numbers = list(map(int, old))

person = dict(zip(list_tickets, list_numbers))
print("Кол-во билетов и возраст для каждого из гостей: ", person)

coast = []

for i in list_numbers:
    if i in range(0, 18):
        coast.append(0)
    elif i in range(18, 25):
        coast.append(990)
    else:
        coast.append(1390)

if tickets > 3:
    print("Общая сумма к оплате, с учетом скидки ", sum(coast) - ((sum(coast) / 100) * 10), "рублей")
else:
    print("Общая сумма к оплате: ", sum(coast), "рублей")