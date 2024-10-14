import pandas as pd

def FindUniqueRows(file1,file2):
    df1 = pd.DataFrame(pd.read_csv(file1))
    df2 = pd.DataFrame(pd.read_excel(file2))
    
    unique_to_file1=df1.merge(df2,how="left",indicator=True).query('_merge=="left_only"').drop('_merge',axis=1)

    return unique_to_file1


file1 = "Universal Changes Backlog.xlsx"
file2= "Untitled query.csv"

final = FindUniqueRows(file1,file2).to_csv("final.csv")

return final