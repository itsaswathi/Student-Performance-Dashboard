import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('students.csv')

# Add risk level
df['Risk_Level'] = df.apply(lambda x: 'At-Risk' if (x['Marks'] < 50 or x['Attendance (%)'] < 60) else 'Safe', axis=1)

# Correlation heatmap
correlation = df[['Marks', 'Attendance (%)', 'Logins']].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Top vs Struggling students
top_students = df[df['Marks'] >= 70]
low_students = df[df['Marks'] < 50]

plt.bar(top_students['Name'], top_students['Marks'], color='green', label='Top')
plt.bar(low_students['Name'], low_students['Marks'], color='red', label='Struggling')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Top vs Struggling Students")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Attendance vs Marks
sns.scatterplot(data=df, x='Attendance (%)', y='Marks', hue='Risk_Level', palette={'At-Risk': 'red', 'Safe': 'blue'})
plt.title("Attendance vs Marks")
plt.show()
