#!/usr/bin/env python
# coding: utf-8

# # DAEN 690 Capstone Project

# ## Import Libraries

# In[82]:


#imports
import pandas as pd
import matplotlib.pyplot as plt


# ## Importing Dataset and Creating DataFrame

# In[83]:


#load US Dataset
df = pd.read_csv("USM00072712-data.txt", sep = '\t', header = None)


# In[84]:


df


# In[85]:


#Assigning columns
id_ = []
year = []
month = []
day = []
hour =[]
reltime = []
numlev = []
p_src = []
np_src = []
lat = []
lon = []

lvltyp1 = []
lvltyp2 = []
etime = []
press = []
pflag = []
gph = []
zflag = []
temp = []
tflag = []
rh = []
dpdp = []
wdir = []
wspd = []

for line in df[0]:
    if "USM00072712" in line:
        id_.append(line[0:12].strip())
        year.append(line[13:17].strip())
        month.append(line[18:20].strip())
        day.append(line[21:23])
        hour.append(line[24:26])
        reltime.append(line[27:31])
        numlev.append(line[33:36])
        p_src.append(line[37:45])
        np_src.append(line[46:54])
        lat.append(line[56:62])
        lon.append(line[64:71])
        lvltyp1.append(None)
        lvltyp2.append(None)
        etime.append(None)
        press.append(None)
        pflag.append(None)
        gph.append(None)
        zflag.append(None)
        temp.append(None)
        tflag.append(None)
        rh.append(None)
        dpdp.append(None)
        wdir.append(None)
        wspd.append(None)
    else:
        id_.append(None)
        year.append(None)
        month.append(None)
        day.append(None)
        hour.append(None)
        reltime.append(None)
        numlev.append(None)
        p_src.append(None)
        np_src.append(None)
        lat.append(None)
        lon.append(None)
        lvltyp1.append(line[0:1].strip())
        lvltyp2.append(line[1:2].strip())
        etime.append(line[4:8].strip())
        press.append(line[10:15].strip())
        pflag.append(line[15:16].strip())
        gph.append(line[17:21].strip())
        zflag.append(line[21:22].strip())
        temp.append(line[23:27].strip())
        tflag.append(line[27:28].strip())
        rh.append(line[29:33].strip())
        dpdp.append(line[35:39].strip())
        wdir.append(line[41:45].strip())
        wspd.append(line[47:51].strip())


# In[86]:


#Creating DataFrame
us_df = pd.DataFrame({
    'id_': id_,
    'year': year,
    'month': month,
    'day': day,
    'hour': hour,
    'reltime': reltime,
    'numlev': numlev,
    'p_src': p_src,
    'np_src': np_src,
    'lat': lat,
    'lon': lon,
    'lvltyp1': lvltyp1,
    'lvltyp2': lvltyp2,
    'etime': etime,
    'press': press,
    'pflag': pflag,
    'gph': gph,
    'zflag': zflag,
    'temp': temp,
    'tflag': tflag,
    'rh': rh,
    'dpdp': dpdp,
    'wdir': wdir,
    'wspd': wspd})


# In[87]:


#Combining Headers with variables
us_df['id_'].fillna(method = 'ffill', inplace = True)
us_df['year'].fillna(method = 'ffill', inplace = True)
us_df['month'].fillna(method = 'ffill', inplace = True)
us_df['day'].fillna(method = 'ffill', inplace = True)
us_df['hour'].fillna(method = 'ffill', inplace = True)
us_df['reltime'].fillna(method = 'ffill', inplace = True)
us_df['numlev'].fillna(method = 'ffill', inplace = True)
us_df['p_src'].fillna(method = 'ffill', inplace = True)
us_df['np_src'].fillna(method = 'ffill', inplace = True)
us_df['lat'].fillna(method = 'ffill', inplace = True)
us_df['lon'].fillna(method = 'ffill', inplace = True)


# In[88]:


#Drop rows with null values
us_df = us_df.dropna()


# In[89]:


us_df


# In[90]:


#Loading Canadian Dataset
df2 = pd.read_csv("CAM00071701-data.txt", sep = '\t', header = None)


# In[91]:


df2


# In[92]:


#Assigning columns
id_2 = []
year2 = []
month2 = []
day2 = []
hour2 =[]
reltime2 = []
numlev2 = []
p_src2 = []
np_src2 = []
lat2 = []
lon2 = []

lvltyp12 = []
lvltyp22 = []
etime2 = []
press2 = []
pflag2 = []
gph2 = []
zflag2 = []
temp2 = []
tflag2 = []
rh2 = []
dpdp2 = []
wdir2 = []
wspd2 = []

for line in df2[0]:
    if "CAM00071701" in line:
        id_2.append(line[0:12].strip())
        year2.append(line[13:17].strip())
        month2.append(line[18:20].strip())
        day2.append(line[21:23])
        hour2.append(line[24:26])
        reltime2.append(line[27:31])
        numlev2.append(line[33:36])
        p_src2.append(line[37:45])
        np_src2.append(line[46:54])
        lat2.append(line[56:62])
        lon2.append(line[64:71])
        lvltyp12.append(None)
        lvltyp22.append(None)
        etime2.append(None)
        press2.append(None)
        pflag2.append(None)
        gph2.append(None)
        zflag2.append(None)
        temp2.append(None)
        tflag2.append(None)
        rh2.append(None)
        dpdp2.append(None)
        wdir2.append(None)
        wspd2.append(None)
    else:
        id_2.append(None)
        year2.append(None)
        month2.append(None)
        day2.append(None)
        hour2.append(None)
        reltime2.append(None)
        numlev2.append(None)
        p_src2.append(None)
        np_src2.append(None)
        lat2.append(None)
        lon2.append(None)
        lvltyp12.append(line[0:1].strip())
        lvltyp22.append(line[1:2].strip())
        etime2.append(line[4:8].strip())
        press2.append(line[10:15].strip())
        pflag2.append(line[15:16].strip())
        gph2.append(line[17:21].strip())
        zflag2.append(line[21:22].strip())
        temp2.append(line[23:27].strip())
        tflag2.append(line[27:28].strip())
        rh2.append(line[29:33].strip())
        dpdp2.append(line[35:39].strip())
        wdir2.append(line[41:45].strip())
        wspd2.append(line[47:51].strip())


# In[93]:


#Creating DataFrame
can_df = pd.DataFrame({
    'id_': id_2,
    'year': year2,
    'month': month2,
    'day': day2,
    'hour': hour2,
    'reltime': reltime2,
    'numlev': numlev2,
    'p_src': p_src2,
    'np_src': np_src2,
    'lat': lat2,
    'lon': lon2,
    'lvltyp1': lvltyp12,
    'lvltyp2': lvltyp22,
    'etime': etime2,
    'press': press2,
    'pflag': pflag2,
    'gph': gph2,
    'zflag': zflag2,
    'temp': temp2,
    'tflag': tflag2,
    'rh': rh2,
    'dpdp': dpdp2,
    'wdir': wdir2,
    'wspd': wspd2})


# In[94]:


#Combining Headers with variables
can_df['id_'].fillna(method = 'ffill', inplace = True)
can_df['year'].fillna(method = 'ffill', inplace = True)
can_df['month'].fillna(method = 'ffill', inplace = True)
can_df['day'].fillna(method = 'ffill', inplace = True)
can_df['hour'].fillna(method = 'ffill', inplace = True)
can_df['reltime'].fillna(method = 'ffill', inplace = True)
can_df['numlev'].fillna(method = 'ffill', inplace = True)
can_df['p_src'].fillna(method = 'ffill', inplace = True)
can_df['np_src'].fillna(method = 'ffill', inplace = True)
can_df['lat'].fillna(method = 'ffill', inplace = True)
can_df['lon'].fillna(method = 'ffill', inplace = True)


# In[95]:


#Drop rows with null values
can_df = can_df.dropna()


# In[96]:


can_df


# ## Preprocessing

# In[ ]:





# ## Functions

# ### Temperature converts to Fahrenheit

# In[1]:


def celsius_to_fahrenheit(celsius):
    if celsius == 9999:
        return 9999
    else:
        return (celsius * 9/5) + 32


# In[ ]:


# ex creating Fahrenheit column in US dataframe
# us_df['Fahrenheit'] = us_df['temp'].astype(float).apply(celsius_to_fahrenheit)


# ### Relative Humidity to Ice

# In[ ]:





# ### Pressure to Pressure Altitude

# In[2]:


def calculate_pressure_altitude(pressure):
    if pressure == -9999:
        return -9999
    
    pressure /= 100

    pressure_altitude = (1 - (pressure / 1013.25) ** 0.190284) * 145366.45
    return round(pressure_altitude, 2)


# In[ ]:


# ex creating pressure altitude column in US dataframe
# us_df['Pressure Altitude'] = us_df['press'].astype(float).apply(calculate_pressure_altitude)


# ### Add Conversions Back to DataFrame

# In[ ]:





# ### Filter Dates

# In[ ]:





# ### Filter Pressure Altitude

# In[ ]:





# ### Capture When Temp below -42 Fahrenheit, RH above 100%, and pressure altitude below 4,300  feet

# In[ ]:




