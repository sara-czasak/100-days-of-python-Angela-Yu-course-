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




