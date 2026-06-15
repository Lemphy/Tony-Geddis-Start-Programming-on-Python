# 4.10 Рост платы за обучение
price_per_sem = 145000 # цена за семестр
YEARS = 5
PROCENT = 3
total = 0
for year in range(YEARS):
    price_at_current_year = price_per_sem * 2
    print(f"Плановая сумма обучения за {year+1} год - {price_at_current_year:,.2f}$")
    total += price_at_current_year
    if year != YEARS - 1:
        price_per_sem *= (1 + (3 / 100))
print(f"Всего потребуется {total:,.2f}$")
