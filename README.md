# Shortest-Path
Shortest Path is a university project where we implemented in python Djikstra and Bellman Ford algorithims

There are two diffrent well known algoritims for short path solving wich are Djikstra and Bellman Ford.

# Djikstra
This one is fast but only works with positive ponderations, if it hapends the algotithim will loop on a 'negative path'.
To avoid doing that a verification is done on the incidence matrix and raise an error on negative values.

# Bellman Ford 
Is slower because he can assume negative path ponderations.