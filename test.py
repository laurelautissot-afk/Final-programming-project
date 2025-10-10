#   Changed how we impotded our data so we can import strings as well
import pandas as pd
data = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
# These will be the varables that we will use, that are intresting (When putting _ was not working)
print(data["Gender"], data["Age"], data["Sleep Duration"], data["Quality of Sleep"], data["Physical Activity Level"], data["Stress Level"], data["BMI Category"], data["Blood Pressure"], data["Sleep Disorder"])
                                                               