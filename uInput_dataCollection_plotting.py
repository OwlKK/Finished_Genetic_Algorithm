# This can be optimized so much, TOO BAD!!!
import statistics
import numpy as np
import tkinter as tk
from matplotlib import pyplot as plt
import greedy_algorithm
from city_list_generator import read_berlin, read_kroa
from create_genetic_algorithm import geneticAlgorithmWithPlotting
from random_algorithm import random_algorithm


# from random_algorithm import random_algorithm


# Good luck reading this heh...
def choose_file():
    which_file = int(input("Type a number corresponding to file: berlin52(1) or kroA100(2)?"))
    if which_file == 1:
        chosen_file = read_berlin()

    else:
        chosen_file = read_kroa()

    return chosen_file, which_file


def choice_and_action():
    temp = choose_file()
    POPULATION = temp[0]
    file_1_or_2 = temp[1]

    loop = True
    while loop:
        POPULATIONSIZE = 100
        ELITESIZE = 25
        MUTATIONRATE = 0.001
        GENERATIONS = 100

        genetic_results = []
        random_results = []
        greedy_results = []

        print("'1' - Genetic")
        print("'2' - Random")
        print("'3' - Greedy")
        print("'4' - All")
        print("'End me' - Close program")

        what_to_do = input("Please type a number corresponding to what You want to do \n")

        run_x_times = int(input("How many times do You want to run it?\n"))

        if str(what_to_do).lower == "end me":
            print("Bye")
            break

        # add multiple runs each specified by the user
        elif int(what_to_do) == 1 or what_to_do == 4 or what_to_do == 5:
            best_custom = int(input("Best parameters I have found (1) or custom (2), or "
                                    "custom each specified (3)? \n"))
            if best_custom == 1:
                POPULATIONSIZE = 100
                ELITESIZE = 25
                MUTATIONRATE = 0.001

                if file_1_or_2 == 1:
                    GENERATIONS = 100
                if file_1_or_2 == 2:
                    GENERATIONS = 500

            if best_custom == 2:
                POPULATIONSIZE = int(input("Population size: "))
                ELITESIZE = int(input("Elite size: "))
                MUTATIONRATE = float(input("Mutation rate: "))
                GENERATIONS = int(input("Generations: "))

            if best_custom == 3:
                population_size_custom_specified = []
                elite_size_custom_specified = []
                mutation_custom_specified = []
                generations_custom_specified = []

                for k in range(0, run_x_times):
                    POPULATIONSIZE = int(input("Population size: "))
                    population_size_custom_specified.append(POPULATIONSIZE)

                    ELITESIZE = int(input("Elite size: "))
                    elite_size_custom_specified.append(ELITESIZE)

                    MUTATIONRATE = float(input("Mutation rate: "))
                    mutation_custom_specified.append(MUTATIONRATE)

                    GENERATIONS = int(input("Generations: "))
                    generations_custom_specified.append(GENERATIONS)

        # list to store progress values to later show in plot of genetic
        progress_list = []

        match int(what_to_do):
            case 1:
                print("Genetic " + str(run_x_times) + " times, cool\n")

                for i in range(run_x_times):
                    genetic_distance, bestRoute, progress = geneticAlgorithmWithPlotting(population=POPULATION,
                                                                                         populationSize=POPULATIONSIZE,
                                                                                         eliteSize=ELITESIZE,
                                                                                         mutationRate=MUTATIONRATE,
                                                                                         generations=GENERATIONS)

                    genetic_results.append(genetic_distance)
                    progress_list.append(progress)

            case 2:
                print("Random " + str(run_x_times) + " times, fun\n")
                for i in range(run_x_times):
                    random_distance, random_route = random_algorithm(POPULATION)
                    random_results.append(float(random_distance))

            case 3:
                print("Greedy " + str(run_x_times) + " times, dandy\n")
                for i in range(run_x_times):
                    greedy_distance, greedy_route = greedy_algorithm.find_min_route()
                    greedy_results.append(float(greedy_distance))

            case 4:
                print("All " + str(run_x_times) + " times, nice\n")

                for i in range(3):
                    for j in range(run_x_times):
                        if i == 0:
                            genetic_distance, bestRoute, progress = geneticAlgorithmWithPlotting \
                                (population=POPULATION,
                                 populationSize=POPULATIONSIZE,
                                 eliteSize=ELITESIZE,
                                 mutationRate=MUTATIONRATE,
                                 generations=GENERATIONS)

                            genetic_results.append(float(genetic_distance))
                            progress_list.append(progress)

                        if i == 1:
                            random_distance, random_route = random_algorithm(POPULATION)
                            random_results.append(float(random_distance))

                        if i == 2:
                            greedy_distance, greedy_route = greedy_algorithm.find_min_route()
                            greedy_results.append(float(greedy_distance))

            case 5:
                for i in range(run_x_times):
                    genetic_distance, bestRoute, progress = geneticAlgorithmWithPlotting(
                        population=POPULATION,
                        populationSize=population_size_custom_specified[i],
                        eliteSize=elite_size_custom_specified[i],
                        mutationRate=mutation_custom_specified[i],
                        generations=generations_custom_specified[i])

                    genetic_results.append(genetic_distance)
                    progress_list.append(progress)

        which_result_not_empty = []

        if len(genetic_results) != 0:
            which_result_not_empty.append(1)
        if len(random_results) != 0:
            which_result_not_empty.append(2)
        if len(greedy_results) != 0:
            which_result_not_empty.append(3)

        if 1 in which_result_not_empty:
            genetic_best = sorted(genetic_results)[0]
            genetic_mean = sum(genetic_results) / len(genetic_results)
            genetic_standard_deviation = np.std(genetic_results)
            genetic_median = statistics.median(genetic_results)

        else:
            genetic_best = genetic_mean = genetic_standard_deviation = genetic_median = progress_list = None

        if 2 in which_result_not_empty:
            random_best = sorted(random_results)[0]
            random_mean = sum(random_results) / len(random_results)
            random_standard_deviation = np.std(random_results)
            random_median = statistics.median(random_results)
        else:
            random_best = random_mean = random_standard_deviation = random_median = None

        if 3 in which_result_not_empty:
            greedy_best = sorted(greedy_results)[0]
            greedy_mean = sum(greedy_results) / len(greedy_results)
            greedy_standard_deviation = np.std(greedy_results)
            greedy_median = statistics.median(greedy_results)

        else:
            greedy_best = greedy_mean = greedy_standard_deviation = greedy_median = None

        # This is really horrible way of passing these... Too bad!!!
        wrne_and_results = [which_result_not_empty,
                            genetic_best, genetic_mean, genetic_standard_deviation, genetic_median,
                            random_best, random_mean, random_standard_deviation, random_median,
                            greedy_best, greedy_mean, greedy_standard_deviation, greedy_median,
                            run_x_times, progress_list]

        return wrne_and_results


def create_graph(caa_variables):
    j = 0
    for i in caa_variables[14]:
        graph_distances = caa_variables[14][j]
        j = j + 1

        plt.plot(graph_distances, label="run" + str(j))

        plt.title('Comparison of genetic algorithm runs')
        plt.ylabel('Distance')
        plt.xlabel('Generation')
        plt.legend()
    plt.show()


def display_results_in_window(caa_variables):
    window_height = 20

    root = tk.Tk()
    T = tk.Text(root, height=window_height, width=30)
    T.pack()

    if caa_variables[1] is not None:
        genetic_text = "GENETIC\n" + "Best result: " + str(round(caa_variables[1], 2)) + \
                       "\nMean: " + str(round(caa_variables[2], 2)) + \
                       "\nStandard deviation: " + str(round(caa_variables[3], 2)) + \
                       "\nMedian: " + str(round(caa_variables[4], 2)) + "\n"
    else:
        genetic_text = ""

    if caa_variables[5] is not None:
        random_text = "RANDOM\n" + "Best result: " + str(round(caa_variables[5], 2)) + \
                      "\nMean: " + str(round(caa_variables[6], 2)) + \
                      "\nStandard deviation: " + str(round(caa_variables[7], 2)) + \
                      "\nMedian: " + str(round(caa_variables[8], 2)) + "\n"
    else:
        random_text = ""

    if caa_variables[9] is not None:
        greedy_text = "GREEDY\n" + "Best result: " + str(round(caa_variables[9], 2)) + \
                      "\nMean: " + str(round(caa_variables[10], 2)) + \
                      "\nStandard deviation: " + str(round(caa_variables[11], 2)) + \
                      "\nMedian: " + str(round(caa_variables[12], 2)) + "\n"
    else:
        greedy_text = ""

    run_n_times_text = "Ran " + str(caa_variables[13]) + " times"

    text_to_display = run_n_times_text + "\n\n" + genetic_text + "\n" + random_text + "\n" + greedy_text

    T.insert(tk.END, text_to_display)

    tk.mainloop()
