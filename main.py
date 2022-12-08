from city_list_generator import readData
from create_genetic_algorithm import geneticAlgorithmWithPlotting
from random_algorithm import random_algorithm
from greedy_algorithm import greedy_algorithm

if __name__ == '__main__':
    cityList = readData()

    # BEST PARAMETERS I HAVE FOUND, DONT TOUCH
    # !!! AND ESPECIALLY DONT TOUCH MUTATION RATE !!!
    POPULATION = cityList
    POPULATIONSIZE = 100
    ELITESIZE = 25
    MUTATIONRATE = 0.001
    GENERATIONS = 500

    bestRoute = geneticAlgorithmWithPlotting(population=POPULATION, populationSize=POPULATIONSIZE,
                                             eliteSize=ELITESIZE, mutationRate=MUTATIONRATE, generations=GENERATIONS)

    print('\n' + 'Best route: ')
    for item in bestRoute:
        print(item, end=" ")

    # TODO WORK ON RANDOM
    # random_algorithm(cityList)

    # greedy_algorithm(cityList)
