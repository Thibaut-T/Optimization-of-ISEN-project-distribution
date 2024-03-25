import pandas as pd

def getAllProjects():
    df = pd.read_excel('output.xlsx')
    return df