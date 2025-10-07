import numpy as np

gender, age, occupation, sleep_duration, quality_sleep, physical_activity, stress_levels, BMI, blood_pressure = np.loadtxt("Sleep_health_and_lifestyle_dataset.csv" , usecols = (2, 3, 4, 5, 6, 7, 8, 9, 10), unpack=True)