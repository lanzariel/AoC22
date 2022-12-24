import numpy as np
import cvxpy as cp
import re

def optimize_blueprint(costs, time):
    ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian = costs
    cost_matrix = np.array([
        [ore_ore, clay_ore, obsidian_ore, geode_ore],
        [0, 0, obsidian_clay, 0],
        [0, 0, 0, geode_obsidian],
        [0, 0, 0, 0]
    ])

    # resource_variables[i] = how many of each resource available after minute i. resource_variables[i-1] - (costs * production_variables[i]) + robot_variables[i]
    # robot_variables[i] = how many robots are available on minute i to work. essentially robot_variables[i-1] + production_variables[i-1]
    # production_variables[i] = how many of each robot to build. can only build one per minute, restricted to using resource_variables[i-1].
    resource_variables = []
    robot_variables = []
    production_variables = []
    constraints = []
    for i in range(time + 1):
        resources = cp.Variable(4)
        robots = cp.Variable(4)
        production_decisions = cp.Variable(4, boolean=True)

        if i == 0:
            constraints.append(resources == 0)
            constraints.append(robots[0] == 1)
            constraints.append(robots[1:] == 0)
            constraints.append(production_decisions == 0)
        else:
            prev_resources = resource_variables[-1]
            constraints.append(robots == robot_variables[-1] + production_variables[-1])
            
            constraints.append(cp.sum(production_decisions) <= 1)

            constraints.append(cost_matrix @ production_decisions <= prev_resources)
            constraints.append(resources == (prev_resources + robots - (cost_matrix @ production_decisions)))

        robot_variables.append(robots)
        resource_variables.append(resources)
        production_variables.append(production_decisions)

    objective = cp.Maximize(resource_variables[-1][3])
    problem = cp.Problem(objective, constraints)
    problem.solve()

    print(problem.value)
    return problem.value

with open('input.txt') as f:
    blueprints = f.readlines()
    total_quality = 0
    for blueprint in blueprints:
        numbers = list(map(int, re.findall('\d+', blueprint)))
        bp_id, costs = numbers[0], numbers[1:]
        total_quality += bp_id * optimize_blueprint(costs, time=24)
    print(total_quality)

with open('input.txt') as f:
    blueprints = f.readlines()
    total_quality = 1
    for blueprint in blueprints[:3]:
        numbers = list(map(int, re.findall('\d+', blueprint)))
        bp_id, costs = numbers[0], numbers[1:]
        total_quality *= optimize_blueprint(costs, time=32)
    print(total_quality)
