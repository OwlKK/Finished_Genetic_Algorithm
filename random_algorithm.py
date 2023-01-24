# The same in de facto made in "Initial distance: " part of create_genetic_algorithm just without the path
# But I will use it anyway

from create_first_population import createRoute


def routeDistance(route, distance=0):
    if distance == 0:
        pathDistance = 0
        for i in range(0, len(route)):
            fromCity = route[i]
            toCity = None

            if i + 1 < len(route):
                toCity = route[i + 1]

            # extra calculation so we come back to the starting city
            else:
                toCity = route[0]

            pathDistance += fromCity.distance(toCity)
        distance = pathDistance
    return distance


def random_algorithm(cityList):
    # create route
    random_route = createRoute(cityList)

    random_distance = routeDistance(route=random_route)

    print('Random distance: ' + str(random_distance))

    print('Random path: ' + str(random_route)  + "\n")

    return random_distance, random_route
