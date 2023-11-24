import matplotlib.pyplot as plt

# Create two lists representing subject names and marks obtained
subjects = ['Math', 'English', 'Science', 'History']
marks = [90, 85, 88, 92]

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(marks, labels=subjects, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Marks Distribution by Subject')
plt.show()
