import pandas as pd
from random import randint
from scipy.spatial import distance_matrix
from city_list_generator import read_berlin

cityList = read_berlin()


def create_matrix(cities=cityList):
    coordinates = []
    cityNames = []

    # getting coordinates and names into lists
    i = 0
    while i < len(cityList):
        temp = []
        temp.append(cities[i].x)
        temp.append(cities[i].y)
        coordinates.append(temp)

        cityNames.append('City' + str(cities[i].posNum))
        i = i + 1

    df = pd.DataFrame(coordinates, columns=['x', 'y'], index=cityNames)
    Matrix = pd.DataFrame(distance_matrix(df.values, df.values), index=df.index, columns=df.index)
    Matrix = Matrix.round(3)

    return Matrix


def smallest_not_0_in_column(df, columnName):
    df = df.loc[df[columnName] >= 0]  # with >= 0 goes through every city

    smallest_column_number = df[columnName].min()
    smallest_column_number_id = df[columnName].idxmin()
    return smallest_column_number, smallest_column_number_id


def find_min_route():
    matrix = create_matrix()
    distances_sum = 0
    visitedCitiesList = []

    # start with random city
    city_pos_num = randint(0, len(cityList))

    # for the number of cities in a file find the shortest distance in each column
    # 52 iterations !!! --- 51 distances between all the cities +1 for the starting point

    for i in range(0, len(cityList)):
        SCN, SCNID = smallest_not_0_in_column(matrix, "City" + str(city_pos_num))  # SCNID -> "City22"

        SCNID_number = int(SCNID[4:]) - 1

        visitedCitiesList.append(SCNID)

        distances_sum = distances_sum + SCN

        # replace used city with 9999999 (because 0 might be usefull in future)
        for j in range(0, len(cityList)):
            matrix.iat[SCNID_number, j] = 9999999

    # manage last (starting)city in list
    visitedCitiesList.append(visitedCitiesList[0])

    print("Greedy distance: " + str(distances_sum))
    print("Greedy path: " + str(visitedCitiesList) + "\n")

    greedy_distance = distances_sum
    greedy_route = visitedCitiesList

    return greedy_distance, greedy_route
