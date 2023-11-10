import matplotlib.pyplot as plt

# Create two lists representing subject names and marks obtained
subjects = ['Math', 'English', 'Science', 'History']
marks = [90, 85, 88, 92]

# Bar chart
plt.figure(figsize=(8, 6))
plt.bar(subjects, marks, color=['gold', 'lightcoral', 'lightskyblue', 'lightgreen'])
plt.title('Marks by Subject')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.show()
