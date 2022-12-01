from city_list_generator import readData
from create_genetic_algorithm import geneticAlgorithm
from plotting import plotting

if __name__ == '__main__':
    cityList = readData()
    bestRoute = geneticAlgorithm(population=cityList, popSize=100,
                                 eliteSize=20, mutationRate=0.01, generations=500)

    print('\n' + 'Best route: ')
    for item in bestRoute:
        print(item, end=" ")

    plotting(population=cityList, populationSize=100,
             eliteSize=20, mutationRate=0.01, generations=100)
