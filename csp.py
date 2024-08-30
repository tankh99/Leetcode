# Variables (Regions)
variables = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
colors = ['Red', 'Green', 'Blue']
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

def backtracking_search(csp):
    
    def select_unassigned(csp, assignment):
        variables = csp['variables']
        for var in variables:
            if var not in assignment:
                return var
            
        return None
    
    # Most 
    def order_domain_values(val, csp, assignment):
        domain = csp['domains'][val]
        # Sort by most constrained value
        # domain = sorted(domain, key=lambda val: sum([is_consistent(var, val, assignment, csp) for var in csp['variables'] if v not in assignment]))
        domain = sorted(domain, key=lambda val: sum([is_consistent(var, val, assignment, csp) for var in csp['variables'] if var not in assignment]))
        # print(domain)
        return domain

    # Return true iff all neighbours of the current variable doesn't share the same value
    def is_consistent(var, value, assignment, csp):
        constraints = csp['constraints']
        neighbours = constraints[var]
        for neighbour in neighbours:
            if neighbour in assignment and assignment[neighbour] == value:
                return False
        return True

    assignments = []
    def backtrack(csp, assignment):
        if len(assignment) == len(csp['variables']):
            return assignment
        
        var = select_unassigned(csp, assignment)
        domain_values = order_domain_values(var, csp, assignment)
        for val in domain_values:
            if is_consistent(var, val, assignment, csp):
                assignment[var] = val
                assignment = backtrack(csp, assignment)
                if assignment:
                    return assignment
                    # assignments.append(assignment)
                    # break

                del assignment[var]


        return None

    def backtrack_count(csp, assignment):
        if len(assignment) == len(csp['variables']):
            global count
            count += 1
            return assignment
        
        var = select_unassigned(csp, assignment)
        domain_values = order_domain_values(var, csp, assignment)
        for val in domain_values:
            if is_consistent(var, val, assignment, csp):
                assignment[var] = val
                assignment = backtrack(csp, assignment)
                if assignment:
                    return assignment
                del assignment[var] 


        return None
    print(assignments)
    return backtrack(csp, {})

count = 0

def num_assignments(csp):
    for var in csp['variables']:
        for color in colors:
            
            result = backtracking_search(csp)
    print(result)
    return count

res = backtracking_search(csp)
# res = num_assignments(csp)
print(res)