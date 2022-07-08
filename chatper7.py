import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
# print("How old are you ?")
# age = input("Please input your age:")
# print("so %s years old" %age)

column_names = ['age',              #39
                'workclass',        #State-gov
                'fnlwgt',           #77516
                'education',        #Bachelors
                'educational-num',  #13
                'marital-status',   #Never-married
                'occupation',       #Adm-clerical
                'relationship',     #Not-in-family
                'race',             #White
                'gender',           #Male
                'capital-gain',     #2174
                'capital-loss',     #0
                'hours-per-week',   #40
                'native-country',   #United-States
                'income']           #<=50K
#数据合并
train = pd.read_csv('adult.data.txt', sep=",\s", header=None, names = column_names, engine = 'python')
test = pd.read_csv('adult.test.txt', sep=",\s", header=None, names = column_names, engine = 'python')
test['income'].replace(regex=True,inplace=True,to_replace=r'\.',value=r'')
adult = pd.concat([test,train])
adult.reset_index(inplace = True, drop = True)
#查看数据
# print(adult.count())
# print(adult[['age','educational-num']].tail())

fig = plt.figure(figsize=(20,15))
cols=5
rows = math.ceil(float(adult.shape[1]/cols))
for i,column in enumerate(adult.columns):
    ax = fig.add_subplot(rows,cols,i+1)
    ax.set_title(column)
    if adult.dtypes[column] == np.object:
        adult[column].value_counts().plot(kind="bar", axes=ax)
    else:
        adult[column].hist(axes=ax)
        plt.xticks(rotation="vertical")
plt.subplots_adjust(hspace=0.9,wspace=0.2)
# plt.savefig("a1.png")
plt.show()
