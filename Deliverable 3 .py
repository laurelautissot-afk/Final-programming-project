
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

#I made my variables into a dictionary so that i can analyse the value and the columns for the value of the skew
#by doing this i can add the name and item argument to print out those desired values
my_list = {"age_skew" : skew(data['Sleep Duration']), 
           "duration_of_sleep_skew" : skew(data['Sleep Duration']) , 
           "quality_of_sleep_skew" : skew(data['Quality of Sleep']), 
           "physical_activity_skew" : skew(data['Physical Activity Level']) , 
           "stress_level_skew" : skew(data['Stress Level']), 
           "heart_rate_skew" : skew(data['Heart Rate']), 
           "daily_steps_skew" : skew(data['Daily Steps'])}


for name , item in my_list.items():
    if item == 0:
        print("The distribution is symetrical" , name , item )
#by adding the variable item, we are also printing out the value assigned to the variable so we can see why they are leaning to one side    
    if item < 0:
            print("The left side of the distribution is favoured for" , name, item )

    else:
        print("The right side of the distribution is favoured for" , name , item )

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
# NUMERICAL VALUES: age, sleep duration, quality of sleep, physical activity, stress level, heart rate, daily steps
numerical_data=["Age", "Sleep Duration", "Quality of Sleep", "Physical Activity Level", "Stress Level", "Heart Rate", "Daily Steps"]
##################################### a ############################################################################################################################################################
bins_for_each_variable={"Age": 8, "Sleep Duration": 12, "Quality of Sleep": 5, "Physical Activity Level": 8, "Stress Level": 5, "Heart Rate": 10, "Daily Steps": 7}
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i]) 
    plt.title("Histogram for " + i)

###################################### b ###########################################################################################################################################################
#conditioned on Gender
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="Gender") 
    plt.title("Histogram for " + i + " Conditioned on Gender")
#conditioned on BMI Category
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="BMI Category") 
    plt.title("Histogram for " + i + " Conditioned on BMI Category") ######### normal=normal weight ###################3
    
###################################### c #########################################################################################################################################################
#Stack histogram conditioned on Gender
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="Gender", multiple="stack") 
    plt.title("Stack Histogram for " + i + " Conditioned on Gender")
#Stack histogram conditioned on BMI Category
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="BMI Category", multiple="stack") 
    plt.title("Stack Histogram for " + i + " Conditioned on BMI Category")

####################################### d #########################################################################################################################################################
#Dodge histogram conditioned on Gender
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="Gender", multiple="dodge") 
    plt.title("Dodge Histogram for " + i + " Conditioned on Gender")
#Dodge histogram conditioned on BMI Category
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="BMI Category", multiple="dodge") 
    plt.title("Dodge Histogram for " + i + " Conditioned on BMI Category")

###################################### e ############################################################################################################################################################
#Normalized histogram statistics conditioned on Gender
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="Gender", stat="density", common_norm=False)
    plt.title("Normalized Histogram Statistics for " + i + " Conditioned on Gender")
#Normalized histogram statistics conditioned on BMI Category
for i in numerical_data:
    sns.displot(data, x=i, bins=bins_for_each_variable[i], hue="BMI Category", stat="density", common_norm=False)
    plt.title("Normalized Histogram Statistics for " + i + " Conditioned on BMI Category")

###################################### f ############################################################################################################################################################
#Kernel Density Estimation
for i in numerical_data:
    sns.displot(data, x=i, kind="kde", bw_adjust=2) 
    plt.title("Kernel Density Estimation for " + i)
#Kernel Density Estimation conditioned on Gender
for i in numerical_data:
    sns.displot(data, x=i, hue="Gender", kind="kde", bw_adjust=2)
    plt.title("Kernel Density Estimation for " + i + " Conditioned on Gender")
#Kernel Density Estimation conditioned on BMI Category
for i in numerical_data:
    sns.displot(data, x=i, hue="BMI Category", kind="kde", bw_adjust=2)
    plt.title("Kernel Density Estimation for " + i + " Conditioned on BMI Category")
    
####################################### g #########################################################################################################################################################
#Empirical Cummulative Distribution conditioned on Gender
for i in numerical_data:
    sns.displot(data, x=i, hue="Gender", kind="ecdf")
    plt.title("Empirical Cummulative Distribution for " + i + " Conditioned on Gender")
#Empirical Cummulative Distribution conditioned on BMI Category
for i in numerical_data:
    sns.displot(data, x=i, hue="BMI Category", kind="ecdf")
    plt.title("Empirical Cummulative Distribution for " + i + " Conditioned on BMI Category")
    
#a) What is the distribution of the variable? (is the data normally distributed, skewed, bimodal, etc?)
##
#b) Are there any outliers? (are there extreme values that fall outside the typical range?)
#
#c) What is the spread and central tendency? (where is the median? How spread out is the data?)
#
#d) Is the data symmetric or skewed? (is the data skewed left or right?)
#
#e) How frequent are certain ranges of values? (which value ranges are most common?)
#



################################# 5) Multivariate non graphical EDA ####################################################################################################################################

##################################### a ############################################################################################################################################################
#   Q: Make use of this approach at least 3 times with different variables from your dataset. 
#1) The realtionship between Quality of sleep and Sleep Disorder. This can be done using violin. 
sns.catplot(data=data, x= "Sleep Disorder", y="Quality of Sleep", hue= "Gender", kind="violin", inner=None)
plt.title("Comparison between males and females, with their reationship between Quality of Sleep and Sleep Disorders")
plt.ylabel("Quality of Sleep") #category
plt.xlabel("Sleep Disorder") 
plt.show()
# 2) The raltionship between BMIcategory and Heart Rate conditioned by gender.
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
# Q: Now use proportions or percentages rather than raw counts (use the “normalize” parameter from crosstab())
# Corsstab will compute a simple cross tabulation of two (or more) factors / The normalize parameter in pd.crosstab() converts raw counts into proportions or percentages instead of showing just totals.
# Asked the teacher for clearer data used Gender because: You use normalize for when you’re comparing counts of categories. So that is why we have to use gender and replace it with the other numerical value. 
# 1
question_a_gender_sleepdisorder = pd.crosstab(data["Gender"], data["Sleep Disorder"], normalize='index') * 100 #I put x a 100 to give me a percentage
print("The Percentenges between Gender and Sleep Disorder:" , question_a_gender_sleepdisorder)

# 2
question_b_BMIcategory_Heartrate = pd.crosstab(data["BMI Category"], data["Gender"], normalize="index") * 100
print("The Percentenges between BMI Category and Gender:" , question_b_BMIcategory_Heartrate)

# 3
question_c_Occupation_Gender = pd.crosstab(data["Occupation"], data["Gender"], normalize="index") * 100
print("The Percentenges between Gender and Occupation:" , question_c_Occupation_Gender )

###################################### c ###########################################################################################################################################################
# Q Generate at least one three-way frequency table (3 or more variables, by giving a list of variables to crosstab() rather than single variables)
three_way_table_question_c = pd.crosstab(index=[data["Gender"], data["Sleep Disorder"]], columns=data["BMI Category"]) # Note: index = the rows of the table
print(three_way_table_question_c)

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
# The relationship between Heart Rate and Daily Steps 
sns.catplot( data=data, kind="strip", x="Heart Rate", y="Daily Steps", hue="Sleep Duration", jitter=True)
plt.title("The Realtionship between Heart Rate and Daily Steps")
plt.xlabel("Heart Rate")
plt.ylabel("Daily Steps")
plt.show()

#b) 1 categorical scatter plot with jitter disabled (explain your choice of variable for this one)
# By dissabeling jitter we can see that there is an alignment of values along the y- axis and we can avoid false precisisons. Stress level is a discrete value, therfore intressting to look at with this particualr case.
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
sns.catplot(data=data, x="BMI Category", y="Sleep Duration", kind="boxen")
plt.title("Distribution shape of Quality of Sleep across BMI Categories")
plt.xlabel("BMI Category")
plt.ylabel("Quality of Sleep")
plt.show()

#f) 1 split violin plot representing 3 variables with bandwidth adjusted for better visualization
sns.catplot(data=data, x="Sleep Disorder", y="Sleep Duration", hue="Gender", kind="violin", inner="stick", split=True, bw=0.3) # use split = True to make the plot cleaner to compare bothe genders 
plt.title(" The Relationship between Sleep Duration and Sleep Disorder split by Gender ")
plt.xlabel("Sleep Disorder")
plt.ylabel("Sleep Duration")
plt.show()

#g) 1 violin plot with scatter points inside the violin shapes
violin_withpoints = sns.catplot( data=data, x="BMI Category", y="Physical Activity Level", kind="violin", inner=None)
sns.swarmplot(data=data, x="BMI Category",y="Physical Activity Level", color="k", size=2)
plt.title(" The Relationship between Heart Rate and BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Physical Activity Level")
plt.show()

#h) 1 bar plot representing 3 variables showing 97% confidence intervals
sns.catplot(data=data, x="BMI Category", y="Heart Rate", hue="Gender", kind="bar", errorbar=("pi", 97)) #percentile interval
plt.title("Comparison between males and females with their Mean Heart Rate by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Heart Rate")
plt.show()

#i) 1 point plot representing 3 variables showing 90% confidence intervals and lines in dashed style
sns.catplot(data=data, x="BMI Category", y="Heart Rate", hue="Gender", kind="point", errorbar=("pi", 90), linestyle="--") #percentile interval
plt.title("Comparison between males and females with their Mean Heart Rate by BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Heart Rate")
plt.show()

#j) 1 bar plot showing the number of observations in each category
sns.catplot(data=data, x="BMI Category", kind="count", hue="Gender") 
plt.title("Number of Observations in each BMI Category")
plt.xlabel("BMI Category")
plt.ylabel("Count")
plt.show()


###################################### c ###########################################################################################################################################################
#a) 1 “heatmap” plot representing 2 variables with color intensity bar and adjusted bin width.
sns.displot(data, x="Physical Activity Level", y="Sleep Duration", cbar=True, binwidth=(5,0.3))
plt.title("Relation Between Sleep Duration and Physical Activity Level Using a Heatmap Plot")
plt.show()

#b) 1 distribution plot with 2 variables making use of bivariate density contours with amount of curves and its lowest level adjusted (use a kernel density estimation displot()).
sns.displot(data, x="Sleep Duration", y="Stress Level", kind="kde", levels=10, thresh=0.2) #making use of bivariate density contours with amount of curves and its lowest level adjusted 
plt.title("Relation Between Sleep Duration and Stress Level Using a Bivariate KDE Distribution")
plt.show()

#c) 1 “heatmap” plot representing 3 variables, again of kind kde.
sns.displot(data, x="Sleep Duration", y="Stress Level", kind="kde", levels=10, thresh=0.2, hue="Gender", fill= True, cbar=True) #making use of bivariate density contours with amount of curves and its lowest level adjusted 
plt.title("Relation Between Sleep Duration and Stress Level Using a Bivariate KDE Distribution conditioned on Gender")
plt.show()
