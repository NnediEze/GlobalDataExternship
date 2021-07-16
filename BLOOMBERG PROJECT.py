#!/usr/bin/env python
# coding: utf-8

# In[191]:


import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.font_manager import FontProperties


# In[192]:


deals = pd.read_csv("PE_deals_final.csv")
deals


# In[193]:


deals.dtypes


# In[194]:


#drop unnecessary columns  
deal1 = deals.drop(columns=["buy_currency", "buy_description","last_update_timestamp","portco_city_of_domicile", "buy_action_USD_curr_spot_rate", "sell_action_USD_curr_spot_rate", "sell_currency", "sell_description", "investor_ticker", "portco_ticker"])


# In[195]:


#convert to datetime 
new_date = pd.to_datetime(deal1.start_date, format="%m/%d/%y %I:%M %p")
deal1.start_date = new_date
deal1


# In[196]:


#table for sector and buys deals and date 
table1 = deal1.loc[:,["portco_industry_sector", "buy_action_id_string", "start_date"]]

table1.dtypes
#Filter by covid-dates Q1 2019 - Q1 2021 
Filter1 = (table1.start_date > "2019-01-01") & (table1.start_date < "2021-04-01")
table1 = table1.loc[Filter1,["portco_industry_sector", "buy_action_id_string", "start_date"]]

#Filter out null values in sector column
Filter2 = (table1.portco_industry_sector != "#N/A Field Not Applicable Equity") & (table1.portco_industry_sector != "#N/A Requesting Data... Equity") & (table1.portco_industry_sector != "")
table1 = table1.loc[Filter2, ["portco_industry_sector", "buy_action_id_string", "start_date"]]

#drop duplicates
table1.drop_duplicates(subset=["buy_action_id_string"])

#add new column that has month,date,quarter in string form, drop start_date
year = table1.start_date.dt.year
quarter = table1.start_date.dt.quarter

table1 = table1.assign(Year=year)
table1 = table1.assign(Quarter=quarter)
table1 = table1.drop(columns = "start_date")

#pivot table 
sectors = table1.groupby(by = ["portco_industry_sector", "Year", "Quarter"]).count()
sectors2 = sectors.reset_index()
sectors2.columns = ["Sector", "Year", "Quarter", "Deal_Count"]
sectors


# In[208]:


#plots 

#Basic Materials 
Filter = (sectors2.Sector == "Basic Materials")
chart1 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
x = np.array(["Q1'19", "Q2'19", "Q3'19", "Q4'19", "Q1'20", "Q2'20", "Q3'20", "Q4'20", "Q1'21"])
y1 = chart1.Deal_Count

p1, = plt.plot(x,y1,marker="o", label = "Basic Materials")

#Communications 
Filter = (sectors2.Sector == "Communications")
chart2 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y2 = chart2.Deal_Count

p2, = plt.plot(x,y2,marker="o", label = "Communications")

#Consumer, Cyclical
Filter = (sectors2.Sector == "Consumer, Cyclical")
chart3 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y3 = chart3.Deal_Count

p3, = plt.plot(x,y3,marker="o", label="Consumer, Cyclical")

#Consumer, Non-Cyclical 
Filter = (sectors2.Sector == "Consumer, Non-cyclical")
chart4 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y4 = chart4.Deal_Count

p4, = plt.plot(x,y4,marker="o", label="Consumer, Non-cyclical")

#Diversified
Filter = (sectors2.Sector == "Diversified")
chart5 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y5 = chart5.Deal_Count

p5, = plt.plot(x,y5,marker="o", label="Diversified")

#Energy
Filter = (sectors2.Sector == "Energy")
chart6 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y6 = chart6.Deal_Count

p6, = plt.plot(x,y6,marker="o", label="Energy")

#Financial
Filter = (sectors2.Sector == "Financial")
chart7 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y7 = chart7.Deal_Count

p7, = plt.plot(x,y7,marker="o", label="Financial")

#Industrial
Filter = (sectors2.Sector == "Industrial")
chart10 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y10 = chart10.Deal_Count

p8, = plt.plot(x,y10,marker="o", label="Industrial")

#Technology 
Filter = (sectors2.Sector == "Technology")
chart11 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y11 = chart11.Deal_Count

p9, = plt.plot(x,y11,marker="o", label="Technology")

#Utilities 
Filter = (sectors2.Sector == "Utilities")
chart12 = sectors2.loc[Filter, ["Sector", "Year", "Quarter", "Deal_Count"]]
y12 = chart12.Deal_Count

p10, = plt.plot(x,y12,marker="o", label="Utilities ")


plt.xlabel("")
fontP = FontProperties()
fontP.set_size('medium')
plt.legend(handles=[p1, p2, p3, p4, p5, p6, p7, p8, p9, p10], title='Legend', bbox_to_anchor=(1.05, 1), loc='upper left', prop=fontP)



# In[216]:


chart10

