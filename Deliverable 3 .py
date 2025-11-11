
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
#This module allows us to do more complicated probability distributions, thus a deeper statistical analysis
from scipy.stats import skew
#Skewness will allow us to analyse whether one side of the distribution is favoured over another
#If the value is 0, the distribution is symetrical
#If the value is positive, the right side of the distribution is favoured(a larger tail)
#If the value is negative, the left side of the distribution is favoured(a larger tail)
age_skew = skew(data['Age'])
duration_skew = skew(data['Sleep Duration'])
quality_skew = skew(data['Quality of Sleep'])
activity_skew = skew(data['Physical Activity Level'])
stress_skew = skew(data['Stress Level'])
heart_rate_skew = skew(data['Heart Rate'])
steps_skew = skew(data['Daily Steps'])

my_list = (age_skew , duration_skew , quality_skew , activity_skew , stress_skew , heart_rate_skew , steps_skew)

print(my_list)

for item in my_list:
    if item == 0:
        print("The distribution is symetrical")
    
    if item < 0:
            print("The left side of the distribution is favoured")

    else:
        print("The right side of the distribution is favoured")

#Kurtosis for each column
#Kurtosis is essentially the amount of values/the probability of falling outside of the normal curve. They represent the tail ends of the normal distributon.
from scipy.stats import kurtosis
#the value we got from this calculation is moderate(-0.91), which indicates that the tails of our normal distribution graph aren't too large
#0.5-(-0.5) is considerent normal, -1/1 - 0.5/(-0.5) is considered moderate and anything greater then 1/-1 it is considered very large tails
print("The chances of the age falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Age']))
print("The chances of a individuals sleep duration falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Sleep Duration']))
print("The chances of a persons quality of sleep falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Quality of Sleep']))
print("The chances of the physicial activity level falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Physical Activity Level']))
print("The chances of an individuals stress level falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Stress Level']))
print("The chances of someones heart rate falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Heart Rate']))
print("The chances of the daily steps falling into one of the two extremes of the normal distribution is:" , 
      kurtosis(data['Daily Steps']))


#Quartiles for each column
import numpy as np

###Quatiles for age
print("The Q1 for the age column is:" , np.percentile(data['Age'] , 25))
print("The Q2 for the age column is:" , np.percentile(data['Age'] , 50))
print("The Q3 for the age column is:" , np.percentile(data['Age'] , 75))

###Quartiles for sleep duration
print("The Q1 for the sleep duration column is:" , np.percentile(data['Sleep Duration'] , 25))
print("The Q2 for the sleep duration  column is:" , np.percentile(data['Sleep Duration'] , 50))
print("The Q3 for the sleep duration  column is:" , np.percentile(data['Sleep Duration'] , 75))

###Quartiles for quality of sleep
print("The Q1 for the quality of sleep column is:" , np.percentile(data['Quality of Sleep'] , 25))
print("The Q2 for the quality of sleep column is:" , np.percentile(data['Quality of Sleep'] , 50))
print("The Q3 for the quality of sleep column is:" , np.percentile(data['Quality of Sleep'] , 75))

###Quartiles for physical activity
print("The Q1 for the physical activity column is:" , np.percentile(data['Physical Activity Level'] , 25))
print("The Q2 for the physical activity column is:" , np.percentile(data['Physical Activity Level'] , 50))
print("The Q3 for the physical activity column is:" , np.percentile(data['Physical Activity Level'] , 75))

###Quartiles for stress levels
print("The Q1 for the stress level column is:" , np.percentile(data['Stress Level'] , 25))
print("The Q2 for the stress level column is:" , np.percentile(data['Stress Level'] , 50))
print("The Q3 for the stress level column is:" , np.percentile(data['Stress Level'] , 75))

###Quartiles for heart rate
print("The Q1 for the heart rate column is:" , np.percentile(data['Heart Rate'] , 25))
print("The Q2 for the heart rate column is:" , np.percentile(data['Heart Rate'] , 50))
print("The Q3 for the heart rate column is:" , np.percentile(data['Heart Rate'] , 75))

###Quartiles for daily steps
print("The Q1 for the daily step column is:" , np.percentile(data['Daily Steps'] , 25))
print("The Q2 for the daily step column is:" , np.percentile(data['Daily Steps'] , 50))
print("The Q3 for the daily step column is:" , np.percentile(data['Daily Steps'] , 75))


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
sns.catplot(data=data, x= "Sleep Disorder", y="Quality of Sleep", hue= "Gender", kind="violin", inner=None)
plt.title("Comparison between males and females, with their reationship between Quality of Sleep and Sleep Disorders")
plt.ylabel("Quality of Sleep") #category
plt.xlabel("Sleep Duration") 
plt.show()
# 2) The raltionship between BMIcategory and Quality of sleep conditioned by gender. We can use  scatterplots to visualize how Quality of Sleep changes with BMI Category.
sns.catplot(data=data,x="BMI Category", y="Heart Rate", kind="bar", hue="Gender")
plt.title(" Comparison between males and females, with their BMI Category how it effect their Heart Rate ")
plt.xlabel("BMI Category")
plt.ylabel("Heart Rate")
plt.show()
#3) Occupation vs Sleep duration  conditioned by Gender. We can use the scatter (swarm) to visualize their relatioship.
sns.catplot(data=data, y="Occupation", x="Sleep Duration", hue="Gender", jitter= True)#in order to see how many data points per category
plt.title("The Relationship between Occupation and Sleep Duration conditionned by Gender")
plt.ylabel("Occupation")
plt.xlabel("Sleep Duration")
plt.show()
sns.catplot(data=data, y="Occupation", x="Sleep Duration", hue="Gender", jitter=False)
plt.title("The Relationship between Occupation and Sleep Duration conditionned by Gender")
plt.ylabel("Occupation")
plt.xlabel("Sleep Duration")
plt.show()

###################################### b ###########################################################################################################################################################


###################################### c ###########################################################################################################################################################
# Q Generate at least one three-way frequency table (3 or more variables, by giving a list of variables to crosstab() rather than single variables)



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
plt.title("The Realationship between Age and Sleep Duration (Added colors for gender, sized by Sleep Quality, and aceted by Sleep Disorder")
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
plt.title("The Realtionship between Quality of Sleep and Sleep Duration conditionned by Gender including a Linear Regression")
plt.xlabel("Sleep Duration")
plt.ylabel("Quality of Sleep")
plt.show()

###################################### b ###########################################################################################################################################################
#a) 1 categorical scatter plot with jitter enabled
# The relationship between BMI category and Sleep duration
sns.catplot( data=data, kind="strip", x="Heart Rate", y="Daily Steps", hue="Sleep Duration", jitter=True)
plt.title("The Realtionship between Heart Rate and ")
plt.xlabel("Heart Rate")
plt.ylabel("Daily Steps")
plt.show()

#b) 1 categorical scatter plot with jitter disabled (explain your choice of variable for this one)
# By dissabeling jitter we can se the tre alighnemnt of values along the y- axis and avoid false precisisons. Stress level is a discrete value, therfore intressting to look at with this particualr case.
sns.catplot( data=data, kind="strip", x="Stress Level", y="Physical Activity Level", jitter=False) #Note: False dissable jitter
plt.title("The Realtionship between Stress Level and  Physical Activity Level")
plt.xlabel("Stress Level")
plt.xticks(rotation = 90)
plt.ylabel("Physical Activity Level")
plt.show()

#c) 1 “beeswarm” plot representing 3 variables
sns.catplot( data=data, kind="swarm", x="Occupation", y="Quality of Sleep", hue="Gender")
plt.title("The Realtionship between Occupation and Quality of Sleep, and how gender can differ in both categories.")
plt.xlabel("Occupation")
plt.xticks(rotation=90)
plt.ylabel("Quality of Sleep")
plt.show()

#d) 1 box plot representing 3 variables
sns.catplot( data=data, kind="box", x="BMI Category", y="Sleep Duration")
plt.title("The Realtionship between BMI Category and Sleep Duration")
plt.xlabel("BMI Category")
plt.ylabel("Sleep Duration")
plt.show()

#e) 1 box plot showing the shape of the distribution (boxenplot())
#f) 1 split violin plot representing 3 variables with bandwidth adjusted for better visualization
#g) 1 violin plot with scatter points inside the violin shapes
#h) 1 bar plot representing 3 variables showing 97% confidence intervals
#i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
#j) 1 bar plot showing the number of observations in each category
###################################### c ###########################################################################################################################################################
#a) 1 “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.
#b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).
#c) 1 “heatmap” plot representing 3 variables, again of kind kde.






