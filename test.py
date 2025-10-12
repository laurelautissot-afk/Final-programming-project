############################### PART 3 #####################################

#Changed how we imported our data so we can import strings as well
import pandas as pd
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
# These will be the varables that we will use, that are intresting (When putting _ was not working)
# This is the uniltered data
print(data["Gender"], data["Age"], data["Sleep Duration"], data["Quality of Sleep"], data["Physical Activity Level"], data["Stress Level"], data["BMI Category"], data["Blood Pressure"], data["Sleep Disorder"])


# Filter data: apply filter using loops and conditionals: We will only look at males
# Create an empty list to add all roles where the gender is male.
filtered_rows = []
#  Data iterrows is a pandas DataFrame method that lets you loop (iterate) through each row of your DataFrame one by one.
for i, row in data.iterrows():
    if row["Gender"] == "Male":
        filtered_rows.append(row)
# Convert the list back to a DataFrame
filtered_data = pd.DataFrame(filtered_rows)
print(filtered_data)


############################### PART 4 #######################################
import matplotlib.pyplot as plt
############################### C ###########################################
# Import a bar graph: Sleep duration Vs. Occupation, to analyse their relationship.
#The relationship between occupation and sleep is important because different jobs can affect sleep duration. Job demands can influence how much rest people get. So important to analyse the realationship.
# Group data by Occupation and calculate average Sleep duration (aka mean)
avg_sleep = data.groupby("Occupation")["Sleep Duration"].mean()
# Create a bar chart: with diffrent colors and line style # Each bar represents an occupation (from index) The height of the bar is the corresponding average sleep duration (from values).
plt.bar(avg_sleep.index, avg_sleep.values, color=["pink", "purple"], edgecolor = "red")
plt.xlabel("Occupation")
plt.ylabel("Average Sleep Duration (Hours)")
plt.title("Average Sleep Duration by Occupation (Males Only)")
# Used rotation to space out the names of the occupations on the x axis, if not they will go on top of each other. 
plt.xticks(rotation=90)
plt.show() #like print

############################### D ############################################
#Scatter plot: Sleep Duration vs Quality of Sleep (Males Only) with grid
#The scatter plot shows how sleep duration relates to sleep quality for males. It helps identify trends, such as whether longer or shorter sleep affects quality.
plt.scatter(filtered_data["Sleep Duration"], filtered_data["Quality of Sleep"], color="pink")
plt.xlabel("Sleep Duration (Hours)")
plt.ylabel("Quality of Sleep")
plt.title("Quality of Sleep vs Sleep Duration (Males Only)")
plt.grid()
plt.show()

############################## E ###########################################




############################# F ############################################
# Scatter plot: Physical activity Vs. Stress levels. 
#To see the realationship between the two and if performing more physical activity improves stress, which therfore impoves sleep.
plt.scatter(filtered_data["Physical Activity Level"], filtered_data["Stress Level"], color="pink")
plt.xlabel("Physical Activity Level")
plt.ylabel("Stress Level")
plt.title("Physical Activity vs Stress Level (Males Only)")
plt.grid()
plt.show()

############################ G ############################################

################################# H #######################################

################################# I ########################################