# Optimize in future
from city import City


def read_berlin():
    my_file = open("berlin52.tsp", "r")
    data = my_file.read()

    # replacing end splitting the text
    # when newline ('\n') is seen.
    data_into_list = data.split("\n")
    for i in range(6):
        data_into_list.pop(0)

    data_into_list = data_into_list[:len(data_into_list) - 3]

    cities = []
    for i in range(0, len(data_into_list)):
        cities.insert(i, file_line_to_city_object_berlin(data_into_list.__getitem__(i)))
    my_file.close()
    return cities


def read_kroa():
    my_file = open("kroA100.tsp", "r")
    data = my_file.read()

    data_into_list = data.split("\n")
    for i in range(6):
        data_into_list.pop(0)

    data_into_list = data_into_list[:len(data_into_list) - 2]

    cities = []
    for i in range(0, len(data_into_list)):
        cities.insert(i, file_line_to_city_object_kroa(data_into_list.__getitem__(i)))
    my_file.close()
    return cities


def file_line_to_city_object_berlin(line: str):
    words = line.split(' ')
    return City(posNum=int(words[0]), x=int(cut_last_2_chars(words[1])), y=int(cut_last_2_chars(words[2])))


def file_line_to_city_object_kroa(line: str):
    words = line.split(' ')
    return City(posNum=int(words[0]), x=int(words[1]), y=int(words[2]))


def cut_last_2_chars(org_string: str):
    size = len(org_string)
    return org_string[:size - 2]
