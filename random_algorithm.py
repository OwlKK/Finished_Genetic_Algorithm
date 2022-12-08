from fitness import Fitness
from createFirstPopulation import createRoute


def random_algorithm(cityList):
    random_route = createRoute(cityList)
    random_route_distance = Fitness(random_route)
    print('\n' + 'RRD: ')
    for item in random_route_distance:
        print(item, end=" ")
