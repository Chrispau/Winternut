import os.path
# Get the directory name for data files
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'Zip_Code1.csv')
#initialize the aggregators
jurisdiction1 = []
female1 = []
male1 = []
datafile = open(filename,'r')
data = datafile.readlines()
for line in data[1:]:
    jurisdiction, total, female_count, female_percent, male_count, male_percent = line.split(',')
    jurisdiction1 += [jurisdiction]
    female1 += [female_count]
    male1 += [male_count]

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,1)
ax.plot(jurisdiction1, female1,'#0000FF')
ax.plot(jurisdiction1, male1,'#FF00FF')

ax.set_title('Jurisdictions based on Gender')

fig.show()