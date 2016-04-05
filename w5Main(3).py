
# coding: utf-8

# In[3]:

height=raw_input("user input height(m): ")
weight=raw_input("user input weight(kg): ")
h=float(height)
w=float(weight)
def bmi(h,w):
    bmi=w/(h*h)
    if 18.5>bmi:
        res="Underweight"
    elif 18.5<=bmi<25:
        res="Normal weight"
    elif 25<=bmi<30:
        res="Overweight"
    else:
        res="Obese"
    return res
result=bmi(h,w)
print result

