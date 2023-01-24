from uInput_dataCollection_plotting import display_results_in_window
from uInput_dataCollection_plotting import choice_and_action
from uInput_dataCollection_plotting import create_graph

if __name__ == '__main__':
    # Choice_and_action() return variables
    caa_variables = choice_and_action()
    display_results_in_window(caa_variables)
    create_graph(caa_variables)


