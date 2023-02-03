#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
num = float(input("Enter a distance in km: "))
ans = num / 1.61
print("There are", round(ans, 2), "miles in", num, "km.")
time_min = float(input("Enter a time in minutes: "))

pace = time_min / ans
print("Your average pace is", round(pace, 2), "minutes per mile.")

time_hr = time_min / 60
speed = ans / time_hr
print("Your average speed is", round(speed, 2), "miles per hour.")
os.system("pause")


# In[ ]:




