"""
режимы открытия файла:

"""

def write_to_db(grade, name, photo):
    filename = 'text.txt'

    with open(filename, 'a') as file:
        file.write(grade)
        file.write('\t')
        file.write(name)
        file.write('\t')
        file.write(photo)
        file.write('\n')
