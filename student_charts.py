import pandas as pd
import matplotlib.pyplot as plt


# STEP 1: Read the CSV file
df = pd.read_csv("students.csv")

print(df.head())          # first 5 rows
print(df.shape)           # (rows, columns)
print(df.describe())      # mean, min, max etc.


# STEP 2: Make one new column
# Average of the 3 tests + final exam for each student
df["average"] = df[["test1", "test2", "test3", "final"]].mean(axis=1)


# CHART 1: LINE PLOT  -> shows change over time
# Question: Is the class improving from test to test?
exams = ["test1", "test2", "test3", "final"]
class_average = df[exams].mean()            # average of each exam column

plt.figure(figsize=(7, 5))
plt.plot(exams, class_average, marker="o", color="green")
plt.title("Class Average Across Exams")
plt.xlabel("Exam")
plt.ylabel("Average Marks")
plt.grid(True)
plt.savefig("1_line_plot.png")
plt.show()


# CHART 2: SCATTER PLOT -> shows relationship between 2 numbers
# Question: Do students who study more score more?
plt.figure(figsize=(7, 5))
plt.scatter(df["study_hours"], df["final"], color="orange")
plt.title("Study Hours vs Final Marks")
plt.xlabel("Study Hours per Day")
plt.ylabel("Final Marks")
plt.savefig("2_scatter_plot.png")
plt.show()


# CHART 3: HISTOGRAM -> shows how values are spread out
# Question: How are the final marks distributed?
plt.figure(figsize=(7, 5))
plt.hist(df["final"], bins=6, color="skyblue", edgecolor="black")
plt.title("Distribution of Final Marks")
plt.xlabel("Final Marks")
plt.ylabel("Number of Students")
plt.savefig("3_histogram.png")
plt.show()


# CHART 4: BAR CHART -> compares categories
# Question: Who are the top 5 students?
top5 = df.sort_values("final", ascending=False).head(5)

plt.figure(figsize=(7, 5))
plt.bar(top5["name"], top5["final"], color="purple")
plt.title("Top 5 Students (Final Marks)")
plt.xlabel("Student")
plt.ylabel("Final Marks")
plt.savefig("4_bar_chart.png")
plt.show()


# CHART 5: PIE CHART -> shows parts of a whole
# Question: How many students are in each grade?
def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 65:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "D"

df["grade"] = df["final"].apply(get_grade)   # apply our function to every row
grade_counts = df["grade"].value_counts()     # count students per grade

plt.figure(figsize=(6, 6))
plt.pie(grade_counts, labels=grade_counts.index, autopct="%1.1f%%")
plt.title("Grade Distribution")
plt.savefig("5_pie_chart.png")
plt.show()
