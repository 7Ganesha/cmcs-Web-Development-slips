import matplotlib.pyplot as plt

# Create two lists representing subject names and marks obtained
subjects = ['Math', 'English', 'Science', 'History']
marks = [90, 85, 88, 92]

# Pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Marks Distribution by Subject (Pie Chart)')

# Bar chart
plt.subplot(1, 2, 2)
plt.bar(subjects, marks, color=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.xlabel('Subjects')
plt.ylabel('Marks')
plt.title('Marks Distribution by Subject (Bar Chart)')

plt.tight_layout()
plt.show()
