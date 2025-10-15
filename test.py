############################### PART 3 #############################################################################################################################################

#Changed how we imported our data (so we can import strings as well)
import pandas as pd
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
# These will be the variables that we will use, that are intresting # Note: (When putting _ was not working)
# This is the uniltered data
print(data["Gender"], data["Age"], data["Sleep Duration"], data["Quality of Sleep"], data["Physical Activity Level"], data["Stress Level"], data["BMI Category"], data["Blood Pressure"], data["Sleep Disorder"])


# Filter data: apply filter using loops and conditionals: We will only look at males
# Create an empty list to add all roles where the gender is male.
filtered_rows = []
# Note: Data iterrows is a pandas DataFrame method that lets you loop (iterate) through each row of your DataFrame one by one.
for i, row in data.iterrows():
    if row["Gender"] == "Male":
        filtered_rows.append(row)
# Convert the list back to a DataFrame
filtered_data = pd.DataFrame(filtered_rows)
print(filtered_data)


############################### PART 4 #################################################################################################################################################################
import matplotlib.pyplot as plt

############################### C #####################################################################################################################################################################
# Bar Graph:Sleep duration Vs. Occupation, to analyse their relationship.
# To organize and visualize the relationship between occupation and sleep duration. (This is to see if different jobs can affect sleep duration. Job demands can influence how much rest people get. So it is important to analyse this realationship.)
avg_sleep = data.groupby("Occupation")["Sleep Duration"].mean() # Note: Group data by Occupation and calculate average Sleep duration (aka mean)
# Create a bar chart: with diffrent colors and line style # Note: Each bar represents an occupation (from index) The height of the bar is the corresponding average sleep duration (from values).
plt.bar(avg_sleep.index, avg_sleep.values, color=["pink", "purple"], edgecolor = "red")
plt.xlabel("Occupation")
plt.ylabel("Average Sleep Duration (Hours)")
plt.title("Average Sleep Duration by Occupation (Males Only)")
plt.xticks(rotation=90) # Note: Used rotation to space out the names of the occupations on the x axis, if not they will go on top of each other. 
plt.show() # Note: Like print

############################### D ######################################################################################################################################################################
# Scatter plot: Sleep Duration vs Quality of Sleep (Males Only) with grid
# To visualy organize and  shows how sleep duration relates to sleep quality for males. (It helps identify trends, such as whether longer or shorter sleep affects quality.)
plt.scatter(filtered_data["Sleep Duration"], filtered_data["Quality of Sleep"], color="pink", edgecolor='red')
plt.xlabel("Sleep Duration (Hours)")
plt.ylabel("Quality of Sleep")
plt.title("Quality of Sleep vs Sleep Duration (Males Only)")
plt.grid()
plt.show()

############################## E #####################################################################################################################################################################
#Two subplots side by side in one figure: Compare "Age  vs Sleep Duration" and "Age vs Stress Level" (Males Only)
#To visualy organise and shows the realation between sleep duration and age. Also, how stress levels change with age as well.
fig, axes = plt.subplots(1, 2) # Note: this creates single figure that has two sublots (Axes) in it ex: 1 = row 2 = collums.
# Subplot 1 (axe 0): Age Vs Sleep Duration (want scatter) # Note: We have to add axe and set to tell the diffrence between them (because each suplot has its own SET of axes)
axes[0].scatter(filtered_data["Age"], filtered_data["Sleep Duration"], color="magenta")
axes[0].set_title("Age vs Sleep Duration (Males)")
axes[0].set_xlabel("Age")
axes[0].set_ylabel("Sleep Duration (Hours)")
# Subplot 2 (axe 1): Age Vs Stress level
axes[1].scatter(filtered_data["Age"], filtered_data["Stress Level"], color="pink")
axes[1].set_title("Age vs Stress Level (Males)")
axes[1].set_xlabel("Age")
axes[1].set_ylabel("Stress Level")

############################# F ######################################################################################################################################################################
#Scatter plot: Physical activity Vs. Stress levels. 
#To visualy organize and see the realationship between Physical activity and Stress levels. To determine if performing more physical activity improves stress, which therfore impoves sleep.
plt.scatter(filtered_data["Physical Activity Level"], filtered_data["Stress Level"], color="pink", edgecolor="red")
plt.xlabel("Physical Activity Level")
plt.ylabel("Stress Level")
plt.title("Physical Activity vs Stress Level (Males Only)")
plt.grid()
plt.show()

############################ G ######################################################################################################################################################################
#Bar plot: Number of males in each stress level, number of males in each quality of sleep level
#To visualy organize how many males in each stress level and show the distribution
stress_count=filtered_data["Stress Level"].value_counts()
plt.bar(stress_count.index, stress_count.values, color='pink', edgecolor='red')
plt.title("Stress Level (Males Only)")
plt.xlabel("Stress Level")
plt.ylabel("Number of Males")
plt.show()
#Bar plot
#To visualy organize how many males per quality of sleep index and show the distribution
stress_count=filtered_data["Quality of Sleep"].value_counts()
plt.bar(stress_count.index, stress_count.values, color='pink', edgecolor='red')
plt.title("Quality of Sleep (Males Only)")
plt.xlabel("Quality of Sleep")
plt.ylabel("Number of Males")
plt.show()
################################# H #################################################################################################################################################################
#Histogram: used to organize continuous values
#To show the distribution of how long males sleep
plt.hist(filtered_data["Sleep Duration"], bins=8, color='pink', edgecolor= 'red')
plt.title("Sleep Duration (Males Only)")
plt.xlabel("Hours of Sleep")
plt.ylabel("Number of Males")
plt.show()
#To show the distribution of how many steps males walk
plt.hist(filtered_data["Daily Steps"], bins=14, color='pink', edgecolor= 'red')
plt.title("Daily Steps (Males Only)")
plt.xlabel("Daily Steps")
plt.ylabel("Number of Males")
plt.show()

################################# I ##################################################################################################################################################################
#Pie chart: BMI Category among Males
#To show the different and most common health status of males, its visual and clear.
filtered_data["BMI Category"]= filtered_data["BMI Category"].replace({"Normal": "Normal Weight"})
bmi_counts = filtered_data["BMI Category"].value_counts()
plt.pie(bmi_counts, labels=bmi_counts.index, autopct='%1.1f%%', colors=["pink", "purple", "red"])
plt.title("BMI Categories (Males Only)")
plt.show()
#Pie chart: Sleep Disorder among Males
#To show the different and most common sleep disorders of males, its visual and clear.
filtered_data["Sleep Disorder"]=filtered_data["Sleep Disorder"].fillna("None")
disorder_counts = filtered_data["Sleep Disorder"].value_counts(dropna=False)
plt.pie(disorder_counts, labels=disorder_counts.index, autopct='%1.1f%%', colors=["pink", "purple", "red"])
plt.title("Sleep Disorders (Males Only)")
plt.show()