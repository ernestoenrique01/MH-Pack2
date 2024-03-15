# Example of using two metaheuristics for maximizing or minimizing a function

# import the implementation of several search procedures
from MH240210 import set_problem, \
                     set_default_parameters, print_parameters, set_parameters, \
                     print_solution, systematicSearch, \
                     mh_RandomSearch, mh_RandomWalk, \
                     mh_HillClimbing, mh_LocalSearch, \
                     mh_EvolutionStrategy, mh_GeneticAlgorithm, \
                     execute_mh, compare_search_procedures, print_results

# ----------------------------------------------------------------------
# Import the objective function and operator from the corresponding problem
# ----------------------------------------------------------------------
#from problemTSP import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
from problemPack2 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination, show_solution
#from problemDifConsNumbers import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemDifConsBinary import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemOneMax import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction1 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction2 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction3 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction4 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemMathFunction5 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemConsecutiveSorted import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemAscendingOrder import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination
#from problemModelFineTuning1 import objective_function, present_problem, random_solution, not_random_solution, random_change, not_random_change, random_combination

# Suggestion: Change the imported file to change the problem!!!!!

# Set the imported aspects of the problem configuration for the metaheuristics
set_problem(objective_function,present_problem, \
            random_solution,not_random_solution, \
            random_change,not_random_change,random_combination)

# present the problem
present_problem()

'''
# ----------------------------------------------------------------------
# General configuration of the search procedures: By default
# ----------------------------------------------------------------------
OBJECTIVE_MAX   = True       # goal of the optimization, True: maximization, False: minimization
MAX_TRIALS      = 1000       # maximum number of solutions to be explored by each metaheuristic
ECHO            = False      # printing some traces of the run
GENERATION_SIZE =  10        # number of generations, for P-metaheuristics
BEST_REFERENCES =   4        # number of solutions considered in the construction of the next generation, for P-metaheuristics
GENERATIONAL    =  False     # type of replacement in P-metaheuristics, True: generational, False: SteadyState
SYSTEMATIC_S_INI=  True      # Systematic search, True: From an arbitrary initial solution, False: from random solution
RUNS=1                       # Repetitions of the metaheuristics
CRITERION = 'TA'             # 'TA': Treshold accepting, 'RRT': Record-to-Record Travel
TRESHOLD = 1                 # For TA and RRT
TRIALS_BEFORE_RESTART = 50   # For Local Search, trials before restart the search
'''

# Set the parameters for a Hill Climbing
# 2000 trials, minimize
# ECHO to show the steps of the execution
parameters = {'MAX_TRIALS': 1000, \
              'OBJECTIVE_MAX':True}
set_parameters(parameters)
print()
print('Execute Hill Climbing with parameters ',parameters)
solHC_max = mh_HillClimbing()
print()
print('Solution obtained by Hill Climbing')
show_solution(solHC_max)