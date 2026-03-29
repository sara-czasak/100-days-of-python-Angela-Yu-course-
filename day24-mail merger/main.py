

with open('names.txt', 'r') as file:
    names = file.readlines()
    names = [name.strip() for name in names]


with open('letter_template.txt', 'r') as file:
    letters = file.read()

for name in names:
    new = letters.replace('NAME', name)
    with open(f'./finished_letters/{name}.txt', 'w') as file:
        file.write(new)
