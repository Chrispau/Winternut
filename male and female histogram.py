import os.path
# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'Zip_Code1.csv')
#initialize the aggregators
jurisdiction1 = []
female1 = []
male1 = []
total1 = []
datafile = open(filename,'r')
data = datafile.readlines()
for line in data[1:]:
    jurisdiction, total, female_count, female_percent, male_count, male_percent = line.split(',')
    if total > '25':
        jurisdiction1 += [jurisdiction]
        female1 += [female_count]
        male1 += [male_count]
        total1 += [total]
        
             
                  
                       
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
 
objects = jurisdiction1
y_pos = np.arange(len(objects))
performance = total1
 
plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Total Population')
plt.title('Jurisdictions Based on their Populations')
 
plt.show()

