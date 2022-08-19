def card_num(card):
    return '*' * (len(card)-4) + card[-4:]
print(card_num(input('Введите номер карты:' )))

