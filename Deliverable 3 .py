
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

###################################### b ##########################################################################################################################################################

######################################## c #########################################################################################################################################################

######################################## d #########################################################################################################################################################




############################## 3) Univariate non graphical EDA ########################################################################################################################################




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
# 1) The realtionship between Gender and Sleep Disorder. This can be done using boxplaot. Here one axis is numercial and the other is categorical.
#This plot shows the median sleep duration and spead for both genders 
sns.catplot(data=data, x= "Gender", y="Sleep Duration", kind="box")
plt.title("Comparison between males and females with sleep durations")
plt.xlabel("Gender") #category
plt.ylabel("Sleep Duration") #numercial
plt.show()
# 2) The raltionship between BMIcategory and Quality of sleep conditioned by gender. We can use  scatterplots to visualize how Quality of Sleep changes with BMI Category.
sns.catplot(data=data,x="BMI Category", y="Quality of Sleep", kind="bar", hue="Gender")
plt.title("Quality of Sleep by BMI Category with Gender ")
plt.xlabel("BMI Category")
plt.ylabel("Quality of Sleep")
plt.show()
#3) Physical Activity vs Sleep duration  conditioned by Gender. We can use the scatter (swarm) to visualize their relatioship.
sns.catplot(data=data, x="Physical Activity Level", y="Sleep Duration", hue="Gender", kind="swarm")
plt.title("Sleep Duration by Activity Level with Gender")
plt.xlabel("Physical Activity Level")
plt.ylabel("Sleep Duration")
plt.show()

###################################### b ###########################################################################################################################################################
# We use pd.crosstab() with the “normalize” parameter to show proportions (in %) rather than raw counts.
#1) Relationship between Gender and Sleep Disorder
#2) Relationship between BMI Category and Sleep Disorder
#3) Reationship between Sleep Duratuon and Physical Activity levleks
###################################### c ###########################################################################################################################################################




################################# 6) Multivariate non graphical EDA ####################################################################################################################################

##################################### a ############################################################################################################################################################
# a 
# b
# c
# d
# e
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






