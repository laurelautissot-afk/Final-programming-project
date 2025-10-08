import numpy as np

Age, Sleep_duration, Quality_sleep, Physical_activity, Stress_levels = np.loadtxt("Sleep_health_and_lifestyle_dataset.csv" , skiprows=1, usecols=( 2, 4, 5, 6, 7), unpack=True, delimiter=',')

