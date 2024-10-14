import pandas as pd

def findFailedMerges(file1,file2):

    df1 = pd.read_excel(file1)
    df2= pd.read_csv(file2)

    merged_df = pd.merge(df1,df2,on="Change Number",how="outer",indicator=True)

    failed_merges=merged_df[merged_df['_merge']!='both']

    return failed_merges


if __name__ == "__main__":
    file1 = "Universal Changes Backlog.xlsx"
    file2 = "Untitled query.csv"
    final = findFailedMerges(file1,file2)

    final.to_excel("failed_merges.xlsx",Index = False)