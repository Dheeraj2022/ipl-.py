#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# IPL DATA ANALYSIS


# ![iplpic2.jpg](attachment:iplpic2.jpg)

# In[2]:


# DATA Analysis
import pandas as pd
import numpy as np
#Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objs as go
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# # Importing Datasets

# In[4]:


#Importing
import warnings
warnings.simplefilter(action='ignore',category=Warning)
pd.set_option('display.max_columns',None)
matches=pd.read_csv("matches.csv")
deliveries=pd.read_csv("deliveries.csv")


# In[5]:


# Shape of data
print(matches.shape,deliveries.shape)


# In[5]:


matches.head(2)


# # Cleaning data

# In[6]:


matches[matches['city'].isna()]


# # Cleaning Data

# In[7]:


matches.loc[matches['city'].isna(),'city']='Dubai'


# In[8]:


matches[matches['winner'].isna()]
matches.loc[matches['winner'].isna(),'winnner']='No winner'
matches.loc[matches['player_of_match'].isna(),'player_of_match']='No player_of_match'


# In[9]:


matches.loc[matches['umpire1'].isna() | (matches['id']==5), ['umpire1','umpire2']]=['S Ravi', 'VK Sharma']
matches.loc[matches['umpire1'].isna() | (matches['id']==11413), ['umpire1','umpire2']]=['Bruce Oxenford', 'Sundaram Ravi']


# In[10]:


matches.drop('umpire3',axis=1,inplace=True)


# In[11]:


matches.replace(to_replace='Rising Pune Supergiant',value='Rising Pune Supergiants',inplace=True)
deliveries.replace(to_replace='Rising Pune Supergiant',value='Rising Pune Supergiants',inplace=True)


# In[12]:


matches.replace(to_replace='Delhi Capitals',value='Delhi Daredevils',inplace=True)
deliveries.replace(to_replace='Delhi Capitals',value='Delhi Daredevils',inplace=True)


# # EDA

# # Total number of matches in season

# In[20]:


total_matches_season=matches["season"].value_counts().reset_index()
total_matches_season.columns=["Season","Matches"]
#total_matches_season
sns.barplot(x="Season",y="Matches",data=total_matches_season,palette='rainbow').set(title="Total number of matches")


# In[21]:


matches_played=pd.concat([matches["team1"],matches["team2"]],axis=0)
matches_played=matches_played.value_counts().reset_index()
matches_played.columns=["Team","Total Matches Played"]
matches_played["winner"]=matches["winner"].value_counts().reset_index()["winner"]
matches_played["Winnig_percentage"]=matches_played["winner"]/matches_played["Total Matches Played"]*100
matches_played


# # Team with no. of matches played, matches winner, percentage of winning matches

# In[22]:


fig,axes=plt.subplots(nrows=1,ncols=3,figsize=(24,6))
sns.barplot(x="Team",y="Total Matches Played",data=matches_played,ax=axes[0]).set_xticklabels(
matches_played["Team"],rotation=90);
sns.barplot(x="Team",y="winner",data=matches_played,ax=axes[1]).set_xticklabels(
matches_played["Team"],rotation=90);
sns.barplot(x="Team",y="Winnig_percentage",data=matches_played,ax=axes[2]).set_xticklabels(
matches_played["Team"],rotation=90);


# # City with No. of matches played

# In[26]:


fig,axes=plt.subplots(figsize=(11,5))
matches_city=matches["city"].value_counts().reset_index().sort_values(by='city',ascending=False)
matches_city.columns=["City","No. of Matches"]
sns.barplot(x="City",y="No. of Matches",data=matches_city).set_xticklabels(matches_city["City"],rotation=70);


# # Matches Played w.r.t Stadium

# In[29]:


fig,axes=plt.subplots(figsize=(11,5))
matches_venues=matches["venue"].value_counts().reset_index().sort_values(by='venue',ascending=False)
matches_venues.columns=["Venue","No. of Matches"]
sns.barplot(x="Venue",y="No. of Matches",data=matches_venues).set_xticklabels(
matches_venues["Venue"],rotation=90);


# # Merging two datasets 

# # Total and average runs per season

# In[21]:


runs=matches.merge(deliveries,left_on='id',right_on='match_id',how='left').drop('id',axis=1)
total_runs_season=runs.groupby(['season'])['total_runs'].sum().reset_index()
matches_season=matches.groupby(['season']).count()["id"].reset_index()
matches_season.rename(columns={'id':'matches'},inplace=True)
matches_season["total_runs"]=total_runs_season["total_runs"]
matches_season["average_runs_per_match"]=matches_season["total_runs"]/matches_season['matches']
matches_season


# # Total and average runs per season(Bar plot)

# In[27]:


fig,axes=plt.subplots(nrows=2,ncols=1,figsize=(10,6))
sns.barplot(x='season',y='total_runs',data=matches_season,ax=axes[0],palette='magma').set_xticklabels(
matches_season["season"],rotation=45) 
sns.barplot(x='season',y='average_runs_per_match',data=matches_season,ax=axes[1],palette='magma').set_xticklabels(
matches_season["season"],rotation=45);


# In[ ]:




