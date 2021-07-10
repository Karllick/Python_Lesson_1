duration = int(input('Введите время:'))
minute = (duration // 60) % 60
sec = duration % 60
hours = (duration // 3600) % 24
day = duration // 86400
if duration < 59:
    print(f"{sec} сек")
elif 60 <= duration < 3599:
    print(f'{minute} мин {sec} сек')
elif 3600 <= duration < 86400:
    print(f'{hours} час {minute} мин {sec} сек')
elif 86400 <= duration:
    print(f'{day} дн {hours} час {minute} мин {sec} сек')
