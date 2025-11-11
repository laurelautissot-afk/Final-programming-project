
#Programming in Science 401-SN1-RE sect.00004 and sect.00003
#Tiago Bortoletto Vaz
#Marielle Suloukji 6291739
#Laure Tissot 2480659
#Angeliki Stathopoulos 2373277 
#14 November 2025 

############################# DELIVERABLE 3 #######################################################################################################################################################

#Import data 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
# These will be the variables that we will use, that are intresting # Note: (When putting _ was not working)
# This is the uniltered data
print(data["Gender"], data["Age"], data["Sleep Duration"], data["Quality of Sleep"], data["Physical Activity Level"], data["Stress Level"], data["BMI Category"], data["Blood Pressure"], data["Sleep Disorder"])


# Filter data: apply filter using loops and conditionals: We have to seprate male and females to compare both datas.
# Create an empty list to add all roles where the gender is male and edited it to add another for females
male_rows = []
female_rows = []
# Note: Data iterrows is a pandas DataFrame method that lets you loop (iterate) through each row of your DataFrame one by one.
for i, row in data.iterrows():
    if row["Gender"] == "Male":
        male_rows.append(row)
    elif row["Gender"] == "Female":
        female_rows.append(row)
# Convert the list back to a DataFrame
male_rows = pd.DataFrame(male_rows)
female_rows = pd.DataFrame(female_rows)
print(male_rows)
print(female_rows)



########################### 2) Preliminary steps #####################################################################################################################################################

##################################### a ###########################################################################################################################################################
#Prints out different statistical relationships between for each column

print(data.describe())
###################################### b ##########################################################################################################################################################
#Allows us to is there are any duplicates in each individual rows
#However since each row is unique we dont need to drop any rows

duplicated_entries = data.duplicated() 
print(duplicated_entries)
######################################## c #########################################################################################################################################################
#Allows us to identify is any of our rows have any missing information, which none of them do
#So its not neccesary to delete any rows

print(data.isnull())
######################################## d #########################################################################################################################################################


############################## 3) Univariate non graphical EDA ########################################################################################################################################
#Mean for each column
print("The average age from the dataset is;", data['Age'].mean())
print("The average sleep duration from the dataset is;",data['Sleep Duration'].mean())
print("The average quality of sleep from the dataset is;",data['Quality of Sleep'].mean())
print("The average physical activity from the dataset is;",data['Physical Activity Level'].mean())
print("The average stress level from the dataset is;",data['Stress Level'].mean())
print("The average heart rate from the dataset is;",data['Heart Rate'].mean())
print("The average daily steps from the dataset is;",data['Daily Steps'].mean())

#Median for each column
print("The median for the ages in the datset are:" , data['Age'].median())
print("The median for the sleep duration in the datset are:" , data['Sleep Duration'].median())
print("The median for the quality of sleep in the datset are:" , data['Quality of Sleep'].median())
print("The median for the physical activity in the datset are:" , data['Physical Activity Level'].median())
print("The median for the stress level in the datset are:" , data['Stress Level'].median())
print("The median for the heart rate in the datset are:" , data['Heart Rate'].median())
print("The median for the daily steps in the datset are:" , data['Daily Steps'].median())

#Mode for each column
print("The most reccuring age is:" , data['Age'].mode())
print("The most reccuring sleep duration is:" , data['Sleep Duration'].mode())
print("The most reccuring quality of sleep score is:" , data['Quality of Sleep'].mode())
print("The most reccuring physicial activity level is:" , data['Physical Activity Level'].mode())
print("The most reccuring stress level is:" , data['Stress Level'].mode())
print("The most reccuring heart rate is:" , data['Heart Rate'].mode())
print("The most reccuring daily steps is:" , data['Daily Steps'].mode())

#Standard deviation for each column
import statistics
print("The standard deviation for the ages in the dataset is:" , statistics.stdev(data['Age']))
print("The standard deviation for the sleep duration in the dataset is:" , statistics.stdev(data['Sleep Duration']))
print("The standard deviation for the quality of sleep in the dataset is:" , statistics.stdev(data['Quality of Sleep']))
print("The standard deviation for the physical activity in the dataset is:" , statistics.stdev(data['Physical Activity Level']))
print("The standard deviation for the stress level in the dataset is:" , statistics.stdev(data['Stress Level']))
print("The standard deviation for the heart rate in the dataset is:" , statistics.stdev(data['Heart Rate']))
print("The standard deviation for the daily steps in the dataset is:" , statistics.stdev(data['Daily Steps']))

#Variance for each column
print("The variance of age for this dataset is:" , statistics.variance(data['Age']))
print("The variance of sleep duration for this dataset is:" , statistics.variance(data['Sleep Duration']))
print("The variance of quality of sleep for this dataset is:" , statistics.variance(data['Quality of Sleep']))
print("The variance of physical activity for this dataset is:" , statistics.variance(data['Physical Activity Level']))
print("The variance of stress level for this dataset is:" , statistics.variance(data['Stress Level']))
print("The variance of heart rate for this dataset is:" , statistics.variance(data['Heart Rate']))
print("The variance of daily steps for this dataset is:" , statistics.variance(data['Daily Steps']))

#Skewness for each column

#Kurtosis for each column

#Quartiles for each column


#Analysing the data of our categorical values
print(data.value_counts('Occupation'))
#calculates the proportions of occupations for our sample size
total_occupations = len(data)
print((data.value_counts('Occupation')/total_occupations))
#the mode of the categorical columns(most frequently and num unique categories )
print(data['Occupation'].mode())
print("The number of unique occupations is:", data['Occupation'].nunique())


print(data.value_counts('BMI Category'))
print((data.value_counts('BMI Category')/total_occupations))
print(data['BMI Category'].mode())
print("The number of unique BMI categories is:", data['BMI Category'].nunique())

print(data.value_counts('Sleep Disorder'))
print((data.value_counts('Sleep Disorder')/total_occupations))
print(data['Sleep Disorder'].mode())
print("The number of unique types of sleep disorders is:", data['Sleep Disorder'].nunique())


############################### 4) Univariate graphical EDA ###########################################################################################################################################

##################################### a ############################################################################################################################################################

###################################### b ###########################################################################################################################################################

###################################### c #########################################################################################################################################################

####################################### d #########################################################################################################################################################

###################################### e ############################################################################################################################################################

###################################### f ############################################################################################################################################################

####################################### g #########################################################################################################################################################




################################# 5) Multivariate non graphical EDA ####################################################################################################################################

##################################### a ############################################################################################################################################################
#   Q: Make use of this approach at least 3 times with different variables from your dataset. 
#1) The realtionship between Gender and Sleep Disorder. This can be done using boxplaot. Here one axis is numercial and the other is categorical.
#This plot shows the median sleep duration and spead for both genders 
sns.catplot(data=data, x= "Gender", y="Sleep Disorder", kind="violin")
plt.title("Comparison between males and females with sleep durations")
plt.xlabel("Gender") #category
plt.ylabel("Sleep Duration") 
plt.show()
# 2) The raltionship between BMIcategory and Quality of sleep conditioned by gender. We can use  scatterplots to visualize how Quality of Sleep changes with BMI Category.
sns.catplot(data=data,x="BMI Category", y="Sleep Disorder", kind="bar", hue="Gender")
plt.title(" BMI Category how it effect Sleep Disorder with Gender ")
plt.xlabel("BMI Category")
plt.ylabel("Sleep Disorder")
plt.show()
#3) Occupation vs Sleep duration  conditioned by Gender. We can use the scatter (swarm) to visualize their relatioship.
sns.catplot(data=data, x="Occupation", y="Sleep Duration", hue="Gender", kind="swarm")
plt.title("Occupation by Activity Level with Gender")
plt.xlabel("Occupation")
plt.ylabel("Sleep Duration")
plt.show()

###################################### b ###########################################################################################################################################################
# Q: Now use proportions or percentages rather than raw counts (use the “normalize” parameter from crosstab())
# corsstab will compute a simple cross tabulation of two (or more) factors / The normalize parameter in pd.crosstab() converts raw counts into proportions or percentages instead of showing just totals.
# 1
# 2
# 3
###################################### c ###########################################################################################################################################################
# Q



################################# 6) Multivariate non graphical EDA ####################################################################################################################################

##################################### a ############################################################################################################################################################
# a ) 1 plot using Faceting feature (col parameter in the relplot() function) 
# The Relationship between Age and Sleep Duration
sns.relplot( data=data, x="Age", y="Sleep Duration", col="Gender", kind="scatter")
plt.suptitle("The Realationship between Age and Sleep Duration")
plt.show()

# b ) 1 plot representing 5 variables at once (x, y, hue, size, col)
# Using same as 1: Relationship between age and Sleep duration
# (will write seperently to explain each variable )
sns.relplot( data=data,
    x="Age", y="Sleep Duration",
    hue="Gender",              # Note: Colors that represent males and females 
    size="Quality of Sleep",   # Note: point size shows sleep quality rating
    col="Sleep Disorder",      # Note:represents the facet by disorder type
    kind="scatter",
)
plt.suptitle("The Realationship between Age and Sleep Duration (Added colors for gender, sized by Sleep Quality, and aceted by Sleep Disorder")
plt.show()

# c ) 1 plot using line instead of points (find a variable that makes sense emphasizing continuity and explain why)
# Using same as 1: Relationship between age and stess leves. The lineplot can be apropriate here because age is typically a coninuous number therfore the trend observed will be more accuarte.
sns.lineplot( data=data , x="Age", y="Stress Level")
plt.title("The Realtionship between Age and Stress Levels")
plt.xlabel("Age")
plt.ylabel("Stress Level")
plt.show()

# d ) 1 plot illustrating standard deviation
# The Realationship between Occupationd and Sleep Duration
sns.relplot(
    data=data,
    x="Occupation", y="Sleep Duration",
    kind="line",
    errorbar="sd"       # Note: show standard deviation 
)
plt.title("Average Sleep Duration by Occupation including a Standard Deviation)")
plt.xlabel("Occupation")
plt.xticks(rotation=90)
plt.ylabel("Sleep Duration ")
plt.show()

# e ) 1 plot including a linear regression
# The Relationship between Quality of Sleep and Sleep Duration
sns.lmplot( data=data, x="Sleep Duration", y="Quality of Sleep", hue="Gender")
plt.title("The Realtionship between Quality of Sleep and Sleep Duration by Gender including a Linear Regression")
plt.xlabel("Sleep Duration")
plt.ylabel("Quality of Sleep")
plt.show()

###################################### b ###########################################################################################################################################################
# a
# b
# c
# d
# e
# f
# g
# h 
# i 
# j 
###################################### c ###########################################################################################################################################################
# a
# b
# c






