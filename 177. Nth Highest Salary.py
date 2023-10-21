import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    employee = employee.sort_values('salary', ascending=False).drop_duplicates(subset=['salary'])
    employee = employee.iloc[N - 1:N]
    return employee[['salary']]
    
    
