
def write_card(name, birth_year, year):
    with open('bday_card.txt', 'r') as file:
        content = file.read()
    content = content.replace('[NAME]', name.title())
    content = content.replace('[AGE]', str(year - int(birth_year)))
    return content

write_card('Sara', 1995, 2026)
