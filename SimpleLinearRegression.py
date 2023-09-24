import pandas as pd
import csv
import matplotlib.pyplot as plt

dataset = pd.read_csv("Salary_dataset.csv")

X = dataset['YearsExperience']
Y = dataset['Salary']

#print(dataset)

data = {
    'X_sum':0,
    'Y_sum':0,
    'XY_sum':0,
    'X2_sum':0
}

s = dataset.sum(axis=0)
c = dataset.count()
xy = (dataset['YearsExperience'] * dataset['Salary']).sum()
xx = (dataset['YearsExperience'] * dataset['YearsExperience']).sum()

data['X_sum'] = s[0]
data['Y_sum'] = s[1]
data['XY_sum'] = xy
data['X2_sum'] = xx
count = c[0]

print(data)

coefficient = ((count * data['XY_sum']) - (data['X_sum'] * data['Y_sum']))/(count * data['X2_sum'] - data['X_sum']**2)
interecept = (1/count) * (data['Y_sum'] - coefficient * data['X_sum'])

print(coefficient,interecept)

#print(s[0],s[1],c[0],c[1],xy,xx,sep='\n\n')

plt.figure(figsize=(7,5))
plt.plot(X,Y,color='red', label='Data')
plt.plot(X,coefficient * X + interecept, color='black', label='Regression line')
plt.scatter(X,Y,color='yellow')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Plot')
plt.show()

print('Success!')