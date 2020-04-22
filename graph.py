import csv
from matplotlib import pyplot as plt
from matplotlib import pyplot as pt
filename = 'newindia.csv'
x=[]
y=[]
z=[]
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if row[2] not in x:
            x.append(row[2])
            y.append(row[5])
            z.append(row[4])
    plt.bar(x,y,color="pink")
    plt.title("Histogram of death rate")
    plt.xlabel('Month',fontsize = 16)
    plt.ylabel("Covid death rate in india", fontsize = 16)
    plt.show()
    
    
    ##pt.bar(x,z)
    fig = plt.figure(dpi = 128, figsize = (16,8))
    fig,ax=plt.subplots()
    ax.plot(x,y, c = 'green',marker='o',linestyle='--',label="Death comparison") #Line 1
    ax.plot(x,z, c = 'red',marker='o',linestyle='-',label="Confirmed cases comparison") 
    #Format Plot
    ax.set_title("CovidData, 2020", fontsize = 16)
    ax.set_xlabel('Month',fontsize = 16)
    ax.set_ylabel("Covid affected rate in india ", fontsize = 16)
    ax.legend()
    plt.tick_params(axis = 'both', which = 'major' , labelsize = 10)
    plt.show()
    plt.bar(x,z,color="brown")
    plt.title("Histogram of Confirmed case rate")
    plt.xlabel('Month',fontsize = 16)
    plt.ylabel("Covid affected rate in india ", fontsize = 16)
    plt.show()
    
    
filename = 'AgeGroupDetails.csv'
x=[]
y=[]
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    for row in reader:
        if row[2] not in x:
            x.append(row[1])
            y.append(row[2])       
    fig1,ax1=plt.subplots()
    ax1.set_title("CovidData, 2020\n Pie chart of confirmed rate age wis", fontsize = 16)
    ax1.pie(y,labels=x,autopct='%1.1f%%',shadow=True,startangle=180)
    ax1.axis("equal")
    plt.show()
from matplotlib import pyplot as pt
import pandas as pd
import plotly.graph_objs as go
df =pd.read_csv("datewise.csv")

ac= df["Deaths"].sum()
rvd =df["Cured"].sum()
dth = df["Active"].sum()
fig = go.Figure(data=[go.Pie(labels=['Active Cases','Cured','Death'],
                             values= [ac,rvd,dth],hole =.3)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=['#263fa3', '#2fcc41','#cc3c2f'], line=dict(color='#FFFFFF', width=2)))
fig.update_layout(title_text='Current Situation in India upto 15-4-2020',plot_bgcolor='rgb(275, 270, 273)')
fig.show()
import csv
from matplotlib import pyplot as plt
from matplotlib import pyplot as pt
import pandas as pd
import plotly.graph_objs as go
p_df =pd.read_csv("COVID19_line_list_data.csv")
tempr = p_df[['death','gender']].dropna()
rcvd = tempr[tempr['death'] == '1']
r_f = len(rcvd[rcvd['gender'] == 'female'])
r_m = len(rcvd[rcvd['gender'] == 'male'])
fig = go.Figure(data=[go.Pie(labels=['Male','Female'],
                             values= [r_m,r_f],hole =.3)])
fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=['#263fa3', '#d461bf'], line=dict(color='#FFFFFF', width=2)))
fig.update_layout(title_text='Gender wise Recovered Cases',
plot_bgcolor='rgb(275, 270, 273)')
fig.show()

import csv
from matplotlib import pyplot as plt
import pandas as pd
import plotly.express as px
#plotly.offline doesn't push your charts to the clouds
import plotly.offline as pyo

df = pd.read_csv('internationaldata.csv')

fig = px.line(df, x = 'country', y = 'active', title='Active rates across countries\nwithin 4 months')
fig.show()

df = pd.read_csv('internationaldata.csv')

fig = px.bar(df, x = 'country', y = 'deaths', title='Death rates across countries\nwithin 4 months')
fig.show()

df = pd.read_csv('covid.csv')

fig = px.bar(df, x = 'State', y = 'Deaths', title='Death rates across state\nwithin 4 months')
fig.show()

df = pd.read_csv('newindia.csv')

fig = px.scatter(df, x = 'month', y = 'deaths', title='Death rates across in India')
fig.show()

df = pd.read_csv('AgeGroupDetails.csv')

fig = px.scatter(df, x = 'AgeGroup', y = 'Percentage', title='Age group affected in India')
fig.show()


