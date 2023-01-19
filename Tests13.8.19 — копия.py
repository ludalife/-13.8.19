tickets = int(input("Введите сколько билетов нужно?: "))
person = tickets
cash = 0
while person != 0:
    age_for_ticket = int(input(f'Возраст для билета № {person} ? '))
    if age_for_ticket < 18:
        print('Билет бесплатный')
    elif 25 > age_for_ticket >= 18:
        cash += 990
        print('Стоимость билета 990 рублей')
    else:
        cash += 1390
        print('Стоимость билета 1390 рублей')
    person -= 1

if tickets > 3:
    sale = cash - ((cash / 100) * 10)
    print(f'Итого к оплате {sale} рублей, с учетом скидки 10%')
else:
    print(f'Итого к оплате {cash} руб.')