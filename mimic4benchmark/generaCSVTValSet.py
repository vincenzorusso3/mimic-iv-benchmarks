import os
import pandas as pd
import numpy

folder = os.listdir('./') #
#del folder[-1:]

myProb=[]
for i in range(len(folder)):
    test = numpy.random.choice(numpy.arange(0, 2), p=[0.8, 0.2])
    myProb.append(test)

print(len(myProb))
print(len(folder))

df = pd.DataFrame(myProb,folder)
#print(df[0].value_counts())
df.to_csv('valset.csv',header=False)
