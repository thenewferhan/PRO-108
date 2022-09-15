import random 
import plotly.figure_factory as ff
import plotly.express as px



name = []
count = []
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    #print(dice1+dice2)
    name.append(dice1+dice2)
    #print(name)
    count.append(i)
   # print(count)

#fig = ff.create_distplot([name],["Ferhan Analysis"])
fig = px.bar(x=name,y=count)
fig.show()

