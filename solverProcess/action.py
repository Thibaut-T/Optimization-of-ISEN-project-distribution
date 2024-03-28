from pulp import LpProblem, LpMaximize, LpVariable, LpBinary, lpSum, LpAffineExpression
import pandas as pd
from numpy import transpose

def solve(students_projects_array):
    ##################################################################
                        
    lp_file = 'common/output.lp'
    projects_students_array = transpose(students_projects_array)
    max_students_per_project = 7
    min_students_per_project = 3
    bigM = 99999

    ##################################################################

    model = LpProblem(name="assign_students_to_projects", sense=LpMaximize)

    variables_normal = {(i, j): LpVariable(name=f"s{i+1}p{j+1}n", cat=LpBinary) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))}

    binary_variables = {j: LpVariable(name=f"b{j}", cat=LpBinary) for j in range(len(projects_students_array))}

    tmp = [(variables_normal[i, j],students_projects_array[i][j]) for i in range(len(students_projects_array)) for j in range(len(students_projects_array[i]))]

    model += LpAffineExpression(tmp)

    for i in range(len(students_projects_array)):
        model += lpSum(variables_normal[i, j] for j in range(len(students_projects_array[i]))) <= 1

    for j in range(len(projects_students_array)):
        model += lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j]))) <= max_students_per_project

    for j in range(len(projects_students_array)):
        model += lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j]))) <= bigM * binary_variables[j]

    for j in range(len(projects_students_array)):
        model += lpSum(variables_normal[i, j] for i in range(len(projects_students_array[j]))) >= min_students_per_project * binary_variables[j]



    model.writeLP(lp_file)
    model.solve()

    result_array = [[variables_normal[i, j].varValue for j in range(len(students_projects_array[i]))] for i in range(len(students_projects_array))]

    print(result_array)

    result_df = pd.DataFrame(result_array)
    result_df.to_csv('common/result.csv', index=False)

def tmp_table():
    return 