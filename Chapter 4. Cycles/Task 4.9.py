# 4.9 Уровень океана
YEARS = 25
MM_PER_YEAR = 1.6
total = 0
for year in range(YEARS):
    total += MM_PER_YEAR
    print(f'{year + 1} год - {total:.1f}мм.')
