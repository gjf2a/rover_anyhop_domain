from rover import *
from pyhop_anytime import *
# To install pyhop_anytime: pip3 install git+https://github.com/gjf2a/pyhop_anytime


# Every pyhop planner should have a method named start which sets up the initial task list from the goals
def start(state, goals):
    ## YOUR CODE HERE ##
    pass

## WRITE ADDITIONAL METHODS HERE ##


def make_rover_planner():
    planner = Planner()
    planner.declare_operators(calibrate, communicate_image_data, communicate_rock_data, communicate_soil_data, drop,
                              navigate, sample_rock, sample_soil, take_image)
    planner.declare_methods(start) # Include all other methods you write as parameters
    return planner


if __name__ == '__main__':
    anyhop_main(make_rover_planner())