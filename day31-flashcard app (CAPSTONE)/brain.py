import csv


# Get flashcard data
def get_data():
    with open('resources/python_concepts.csv', 'r') as file:
        reader = csv.reader(file)
        front = []
        back = []
        for row in reader:
            if row == ['Front', 'Back']:
                pass
            else:
                front.append(row[0])
                back.append(row[1])
        return front, back


def save_data(front, back):
    with open("resources/python_concepts_to_learn.csv", 'a') as file:
        file.write(f"{front},{back}\n")


