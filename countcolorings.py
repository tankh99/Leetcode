# Variables (Regions)
variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
colors = ['Red', 'Green', 'Blue', 'Purple', 'White']
# Domains (Colors available for each region)
domains = {
    'A': colors,
    'B': colors,
    'C': colors,
    'D': colors,
    'E': colors,
    'F': colors,
    'G': colors,
}

# Constraints: Neighbors should not have the same color
constraints = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D', 'E', 'F'],
    'D': ['B', 'C', 'E'],
    'E': ['C', 'D', 'F'],
    'F': ['E', 'C'],
    'G': []
}

# CSP Object (to pass into functions)
csp = {
    'variables': variables,
    'domains': domains,
    'constraints': constraints
}

def count_colorings(csp, varIndex, assignment):
    if len(csp['variables']) == len(assignment):
        return 1
    count = 0
    var = csp['variables'][varIndex]
    variables = csp['variables']
    for color in colors:
        if is_consistent(csp, var, color, assignment):
            assignment[var] = color
            count += count_colorings(csp, varIndex + 1, assignment)
            del assignment[var]
    return count
        
# Iterate through all neighbours of the specifi variable, and for each number, each if their colour
def is_consistent(csp, var, color, assignment):
    constraints = csp['constraints']
    neighbours = constraints[var]
    for neighbour in neighbours:
        if neighbour in assignment and assignment[neighbour] == color:
            return False
    return True

def main():
    variables = csp['variables']
    # for var in variables:
    #     count_colorings(csp, var, {})
    return count_colorings(csp, 0, {})
    # return count_colorings(csp, i, {})
    # for i,var in enumerate(variables):

ans = main()
print(ans)