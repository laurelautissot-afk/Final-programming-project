#   Changed how we imported our data so we can import strings as well
import pandas as pd
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
# These will be the varables that we will use, that are intresting (When putting _ was not working)
# This is the uniltered data
print(data["Gender"], data["Age"], data["Sleep Duration"], data["Quality of Sleep"], data["Physical Activity Level"], data["Stress Level"], data["BMI Category"], data["Blood Pressure"], data["Sleep Disorder"])


# Filter data: apply filter using loops and conditionals: will only look at males
# Create an empty list to add all roles where the gender is male.
filtered_rows = []
#  Data iterros is a pandas DataFrame method that lets you loop (iterate) through each row of your DataFrame one by one.
for i, row in data.iterrows():
    if row["Gender"] == "Male":
        filtered_rows.append(row)
# Convert the list back to a DataFrame
filtered_data = pd.DataFrame(filtered_rows)
print(filtered_data)

# Import a bar graph: Sleep duration Vs. Occupation, to analyse their relationship.
import matplotlib.pyplot as plt
# Group data  by Occupation and calculate average Sleep duration (aka mean)
avg_sleep = data.groupby("Occupation")["Sleep Duration"].mean()
# Create a bar chart: with diffrent colors and line style
plt.bar(avg_sleep.index, avg_sleep.values, color=["pink", "purple"], edgecolor = "red")
plt.xlabel("Occupation")
plt.ylabel("Average Sleep Duration (Hours)")
plt.title("Average Sleep Duration by Occupation (Males Only)")
# Used rotation to space out the names of the occupations on the x axis
plt.xticks(rotation=90)
plt.show()
