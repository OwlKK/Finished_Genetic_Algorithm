from uInput_dataCollection_plotting import display_results_in_window
from uInput_dataCollection_plotting import choice_and_action
from uInput_dataCollection_plotting import create_graph

# I wanted to include the random seed function for testing
# but a month ago only god and I knew how it worked.
# Now, only god knows it...

if __name__ == '__main__':
    caa_variables = choice_and_action()
    display_results_in_window(caa_variables)
    create_graph(caa_variables)


