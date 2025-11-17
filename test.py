cnt = 0

with open('names.txt', 'r', encoding = 'utf-8') as file:
    for line in file:
        name = line.strip()
        if name == 'Катя':
            cnt += 1

print(f'Кол-во имени Катя в списке: {cnt}')
