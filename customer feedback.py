import pandas as pd
data = {
    'ID': [1, 2, 3, 4],
    'Customer': ['Alice', 'Bob', 'Charlie', 'Dana'],
    'Satisfaction_Score': [4, 3, 5, 2],
    'Feedback': ['Good', 'Average', 'Excellent', 'Poor']
}
df = pd.DataFrame(data)
average_satisfaction_score = df['Satisfaction_Score'].mean()
print("a) Average satisfaction score:", average_satisfaction_score)
good_feedback_customers = df[df['Feedback'] == 'Good']['Customer'].count()
print("b) Number of customers who provided 'Good' feedback:", good_feedback_customers)
excellent_feedback_percentage = (df[df['Feedback'] == 'Excellent']['Customer'].count() / len(df)) * 100
print("c) Percentage of customers who provided 'Excellent' feedback:", excellent_feedback_percentage)
lowest_satisfaction_customer = df.loc[df['Satisfaction_Score'].idxmin()]['Customer']
print("d) Customer who provided the lowest satisfaction score:", lowest_satisfaction_customer)
most_common_feedback = df['Feedback'].mode()[0]
print("e) Most common type of feedback received:", most_common_feedback)
