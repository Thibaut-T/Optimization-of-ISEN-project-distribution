import pandas as pd

def getAllProjects():
    try:
        df = pd.read_excel('output.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame()
    return df