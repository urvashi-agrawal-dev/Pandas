import pandas as pd
data={
    'ID':[1,2,3,4],
    'Name':['Alice','Bob','Charlie','Dana'],
    'Salary':[50000,60000,55000,65000],
    'Department':['Marketing','Finance','HR','Operations']
}
df=pd.DataFrame(data)
average_salary=df['Salary'].mean()
print("Average salary across all departments",average_salary)
department_highest_avg_salary=df.groupby('Department')['Salary'].mean().idxmax()
print("department has highest salary",department_highest_avg_salary)
total_salary_expense=df.groupby('Department')['Salary'].sum()
print("Total salary expense for each department",total_salary_expense)
highest_paid_employee=df.loc[df['Salary'].idxmax()]['Name']
print("Highest paid emploee:",highest_paid_employee)
highest_salary=df['Salary'].max()
difference=highest_salary-average_salary
print("difference between the salary",difference)
