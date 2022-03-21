#!/usr/bin/env python
# coding: utf-8

# Importing the required libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
import plotly.express as px
from streamlit_timeline import timeline
import plotly.graph_objects as go
import seaborn as sns
import plotly.figure_factory as ff

###########################

st.set_page_config(layout="wide")

st.title('How various factors have influenced the housing prices over the past 2 decades - A case Study 📔')

st.sidebar.markdown('''
# Contents
- [Introduction](#introduction)
- [Brief Timeline](#a-brief-timeline-of-major-economic-events)
- [The Past 2 Decades](#factors-and-how-they-influenced-the-past-2-decades)
    - [Demand](#demand)
        - [Population](#population)
        - [Unemployment](#unemployment)
        - [Income](#income)
        - [Mortgage Rate](#mortgage-rate)
        - [Debt](#household-debt)
    - [Supply](#supply)
        - [Permits](#new-single-family-unit-permits)
        - [Existing home sales](#existing-home-sales)
        - [Foreclosures](#foreclosures)
- [Most Influencial Factor](#determining-the-most-influencial-factor)
    - [Correlation Analysis](#correlation-analysis)
    - [Explanatory Regression Analysis](#explanatory-regression-analysis)
- [Conclusion](#conclusion)
- [Biblography](#biblography)
        

''', unsafe_allow_html=True)

###########################    

st.header('Introduction')
col1,col2 = st.columns((2,1))
col1.write('''

Saying that the housing market is influenced by a myriad of factors could be an understatement. 
The entire process of reverse engineering something as complex and as complicated as a housing market requires in-depth and 
unbiased analysis which in turn produces credible predictive analytics.

The **S&P CoreLogic Case-Shiller U.S. National Home Price NSA Index** measures the change in the value of the U.S. 
residential housing market by tracking the purchase prices of single-family homes, which I have used as a proxy for home prices.

As of October 2021, there were 208.4 million single-family dwelling units in the United States and only 37.8 million multifamily units. 
**The size of single-family housing units has steadily risen since the start of the 21st century.**

There is an upward trend in the average size of floor area in new single-family homes. In 1975, a new home had an average floor area of about 1,660 square feet.
By 2019, this figure had **increased by** about 900 square feet.

''')

labels = ['Multi-family dwelling unit', 'Single Family dewlling unit', 'Others']
sizes = [37.75, 208.36, 10.67]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("The single-family units as a fraction of all the housing units in USA", pad = 20)

col2.pyplot(fig1)

st.write('''
The interavtive rgraph below shows how the S&P CoreLogic Case-Shiller U.S. National Home Price NSA Index has changed in the past 2 years. 
The data has been adjusted to show quaterly mean.
''')

col1,col2 = st.columns((2,1))

df = pd.read_csv('./data/cleaned/snp.csv')
df.rename(columns = {'CSUSHPISA':'Index'}, inplace = True)
fig = px.line(df, x='DATE', y='Index')
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
col1.plotly_chart(fig)

col2.markdown('''_
\n 
The Case Shiller Home Price Index averaged 169.87 points from 2000 until 2021. 
\n It reached an all-time high of 257.10 points in April 2021.
\nIt reached a record low of 100 points in January 2000.
''')

###########################
st.header('A Brief Timeline ⏱️ of Major Economic Events')
with open('data.json', "r") as f:
    data = f.read()

# render timeline
timeline(data, height=800)

#####################
st.header('Factors and How They Influenced The Past 2 Decades 📊')
st.header('Population 🧑🏻‍🤝‍🧑🏾')
colm1,colm2 = st.columns((3,4))
colm1.write('''
The U.S. population increased by 10 percent between 2000 and 2010 and is projected to increase by 8 percent between 2010 and 2020, from 309 million to 333 million. An 8 percent gain would be the smallest percentage increase in the U.S. population between censuses since the 1930s.
\nThe population-housing relationship is a two-way street. On the one hand, population growth causes a shift in housing demand. Population growth, and especially an increase in the number of households, leads to an increase in housing demand.
\nPopulation decline might lead to a decrease in housing demand. This will, however, only happen in the long run, after not only the number of people but also the number of households has started to decline. The danger of population decline is greatest in remote rural areas and in areas with lower-quality housing.
At the same time, the supply of housing influences the opportunities for population increase through migration.

''')



df = pd.read_csv('./data/cleaned/population_q_cleaned.csv')
df.rename(columns = {'POPTHM':'Population'}, inplace = True)
fig = px.line(df, x='DATE', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)

col1,col2 = st.columns((3,4))
df = pd.read_csv('./data/cleaned/pops.csv')
df.rename(columns = {'CNP16OV_TTLHH':'No. of members in a household'}, inplace = True)
fig = px.line(df, x='Date', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
with col2:
    st.plotly_chart(fig)

with col1:
    st.write('**Poplulation level/Total household** 🧑🏻‍🤝‍🧑🏾/🏠')
    st.write('''
    The graph shows that the number of people in each household has decreased in the longer time period. So the number of households in the US has increased faster than population, which means that any measure divided by population grows faster than one divided by number of households.
    ''')


#####################
st.header('Unemployment')
colm1,colm2 = st.columns((3,4))
df = pd.read_csv('./data/cleaned/unemp.csv')
df.rename(columns = {'UNRATE':'Unemployment Rate in %'}, inplace = True)
fig = px.line(df, x='DATE', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)

with colm1:
    components.iframe("https://d3fy651gv2fhd3.cloudfront.net/embed/?s=usurtot&v=202203041337V20200908&d1=19970314&type=type=line&title=false&url2=/united-states/case-shiller-home-price-index&h=300&w=600",width=600, height=300, scrolling=False)
    st.write("Unemployment tracks the business cycle. Recessions are part of that cycle and can cause high unemployment. Businesses often lay off workers and, without an income, those jobless workers have less money to spend.")


st.write('''
Lower consumer spending reduces business revenue, which forces companies to cut more payroll. This downward cycle can be devastating to individuals and the economy.
When unemployment is rising, fewer people will be able to afford a house. But, even the fear of unemployment may discourage people from entering the property market.
An increase in jobs, employees and wages consequently results in an increase in income for all workers in a country. With that, an increase in income also increases the demand for affordable housing.
\nDuring the Great Recession, unemployment reached 10% in October 2009. 
In 2020, it reached double digits again at 14.7% in April when the U.S. was dealing with a pandemic and recession.
The US unemployment rate edged down to 3.8 percent in February of 2022 from 4 percent in the previous month, a new pandemic low and below market expectations of 3.9 percent. The number of unemployed persons edged down by 243 thousand to 6.270 million.

''')
############################
st.header('Income 💵')
colm1,colm2 = st.columns((3,4))
colm1.write('''
The shortfall in household income is attributable in part to two recessions since 2000. The first recession, lasting from March 2001 to November 2001, was relatively short-lived.7 Yet household incomes were slow to recover from the 2001 recession and it was not until 2007 that the median income was restored to about its level in 2000.

\nBut 2007 also marked the onset of the Great Recession, and that delivered another blow to household incomes. This time it took until 2015 for incomes to approach their pre-recession level. Indeed, the median household income in 2015 – $70,200 – was no higher than its level in 2000, marking a 15-year period of stagnation, an episode of unprecedented duration in the past five decades.8

\nMore recent trends in household income suggest that the effects of the Great Recession may finally be in the past. From 2015 to 2018, the median U.S. household income increased from 70,200 to 74,600 dollars, at an annual average rate of 2.1%.
''')

col1,col2 = st.columns((3,4))
with col2:
    img = Image.open("aff.png")
    st.image(img)

with col1:
    st.write('**Affordability of Homes**')
    st.write('''
    
Steady job growth and an increase in the median wage continue to fuel housing demand. Aside from rising wages, another good sign of financial health is spending less disposable income on repaying debts like credit cards, auto loans, and personal loans.

Today, household budgets continue to be the strongest they’ve been in over 40 years and a far cry from 2008, suggesting consumers have more disposable income to buy a home.

    ''')


df = pd.read_csv('./data/cleaned/incomenew.csv')
df.rename(columns = {'MEHOINUSA672N':'Median Income'}, inplace = True)
df.rename(columns = {'HOUSTCB1FQ_HOUSTOB1FQ':'New Privately Owned Homes'}, inplace = True)
fig = px.line(df, x='DATE', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)
###########################

st.header('Mortgage Rate')
colm1,colm2 = st.columns((3,4))
colm1.write('''
Monetary policy affects interest rates, which affect mortgages, which affect housing market decisions. That may be simple to grasp, but the housing statistics may not follow such clear-cut patterns. 

\nThe graph's red line represents the average 30-year fixed-rate mortgage for the last 20 years. For the same time period, the blue line in the graph represents the ratio of house starts built by contractors to housing starts built by owners. 

\nFrom 2000 to 2007, this ratio remained largely steady, hovering around 1.5, meaning that contractors built roughly 60% of new starts. However, during periods of macroeconomic turmoil, the ratio has deviated from its historical average.
\nBut during the Great Recession, this ratio increased sharply, to over 2.0, peaking at 2.6 in 2016, which implies contractors built 72% of housing starts. In both cases, GDP declined and unemployment rose, but this housing measure behaved differently.
''')

st.write('''
A clear difference between these two episodes is the level of mortgage rates: Rates were much higher in the Great Recession. As mortgage rates go up, the ratio goes down and vice versa.
A potential reason is that, as the price of mortgages increases, the cost of purchasing a new home from a contractor increases relative to the cost of building one’s own home. And, if the costs are basically the same, 
many would-be homeowners might choose to build their own home rather than purchase one that someone else built. 
''')

df = pd.read_csv('./data/cleaned/dd.csv')
df.rename(columns = {'MORTGAGE30US':'Mortgage Rate'}, inplace = True)
df.rename(columns = {'HOUSTCB1FQ_HOUSTOB1FQ':'New Privately Owned Homes'}, inplace = True)
fig = px.line(df, x='DATE', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)

#####################

st.header('Household Debt')
colm1,colm2 = st.columns((3,4))
colm1.write('''
There are many types of debt, including household debt, and many specific types of household debt as well. 
\nThe graph on the right shows Mortgage Debt Service Payments as a Percent of Disposable Personal Income. 
\nThe financial burdens from mortgages debt vary quite a bit. Let’s consider two reasons for this: The larger 
the debt, the larger the burden, as households need to pay more interest on a larger principal. And changes 
in interest rates obviously influence how much is paid to service loans.\n The mortgage debt increased from the early 1990s until the past recession, 
when it decreased. This decrease is the result of the combination of the two effects noted above: the amount of debt and interest rates. 
With one exception (in the fourth quarter of 2012), total debt obligations are at the lowest they’ve been since these data were first 
collected. And this is especially true of mortgage debt.

''')

df = pd.read_csv('./data/cleaned/debt_inc.csv')
fig = px.line(df, x='DATE', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)

labels = ['Mortgage','Student','Others']
values = [10.44, 1.58, 3.22]
# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])

col1,col2 = st.columns((1,2))
with col2:
    st.plotly_chart(fig)

with col1:
    st.write('**Mortgage debt as a fraction of total household debt**')
    st.write('''
    Mortgage Debt Service Payments as a Percent of Disposable Personal Income was 3.81% in April of 2021, according to the United States Federal Reserve.\nHistorically, United States - Mortgage Debt Service Payments as a Percent of Disposable Personal Income reached a record high of 7.18 in October of 2007 and a record low of 3.51 in January of 2021. 
    By the end of 2021, a record level of household debt was reached. Mortgage being the biggest contributor to it being 68.5% at 10.44 Trillion Dollars. Student debt was the second highest contributor with 21.1% at 1.58 Trillion Dollars.

    ''')

##############################

st.header('New Single Family Unit Permits 📋')
colm1,colm2 = st.columns((3,4))
colm1.write('''
\nSingle-family housing starts were pridicted to total 1 million in 2020, the highest since 2007. However, 
There were only approximately 978,000 building permits for single-family housing units granted in the United States in 2020, which is 
an increase of around 116,000 on the previous year. Units have steadily increased since 2011, but the numbers remain considerably 
lower than the 1.68 million authorized by building permits in 2005.
\nThat was about 3 years prior to the housing market meltdown that spurred a global financial rout. 
\nThe rising cost of land, labor, building materials, and regulations, are some of the reasons why we can see significantly more blue (people who may need homes) in the graph below, than orange (total homes built) since 2008. You can also see that few of the new homes built were “starter homes” focused on first-time buyers.
''')

df = pd.read_csv('./data/cleaned/permit.csv')
df.rename(columns = {'PERMIT1':'No. of permits issued in thousands'}, inplace = True)
df.rename(columns = {'HSN1F':'No. of one family homes sold in thousands'}, inplace = True)
fig = px.line(df, x='DATE', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)
col1,col2 = st.columns((1,1))
img = Image.open('new_perms.png')
with col1:
    st.image(img)

with col2:
    st.write('''
    \n Even though the new homes built by 2020 were the fastest rate since 2007, Single-family home construction is running at the slowest pace since 1995.
    \nThe U.S. is short 5.24 million homes, an increase of 1.4 million from the 2019 gap of 3.84 million.
    \nSingle-family home construction has suffered from a severe labor shortage that began well before the pandemic but was then exacerbated by it. Supply chain disruptions in the past year have pushed prices for building materials higher, and as pandemic-induced demand soared, prices for land increased as well. While new household formation is actually slower than it was before the pandemic, homebuilders would have to double their recent new home production pace to close the gap in five to six years. A new household can be either owner-occupied or rented.
    ''')

################################


st.header('Existing Home Sales')
colm1,colm2 = st.columns((3,4))
colm1.write('''
The steady rise in sales after the sharp drop in 2008 is indicative of the general consensus that the housing market is recovering. Construction is showing positive signs, consumers are growing in confidence and are becoming freer with their spending and the market is entering new periods of growth. 
\n
This is a far cry from the dire situation in the not too distant past, in the run up to the bursting of the U.S. housing bubble. Interest rates were very low at that time, making credit cheap and abundantly available. Banks and lending institutions led people to believe that it was okay to buy multiple properties with little money and that real estate was just about the safest investment anyone could make. More and more people decided to take the risk and invest in the market. This coupled with the increased number of people descending on the market caused prices to soar; it seemed like an easy way to make cash fast. But this is how the bubble formed and it was this bubble, upon bursting, that would set into motion a chain of events that would bring the global economy to its knees; plunging the world into an economic depression of which it has not seen the likes since the Great Depression of the 1930s.
''')

df = pd.read_csv('./data/cleaned/existinghomessold.csv')
fig = px.line(df, x='Year', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)
col1,col2 = st.columns((2,1))

labels = ['Exisiting Homes Sold','New Homes Sold']
values = [5640000, 822000]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
col1.plotly_chart(fig)

with col2:
    st.write('''
    **U.S. existing home sales 2005-2023**
    \nIn 2021, the U.S. home sales in the United States surged, reaching the highest value observed since 2006. A total of 6.1 million housing transactions were completed in that year, up from 5.6 million in 2020. According to the forecast, sales activity is expected to slow down slightly in 2022 and increase again in 2023. 
    ''')


##################################

st.header('Foreclosures 🏦')
colm1,colm2 = st.columns((3,4))
colm1.write('''
Despite a deep recession, the U.S. housing market in 2020 set a record for the fewest foreclosures ever.

Just 214,323 properties were in some stage of foreclosure last year, well below the previous low set in 2019, according to ATTOM Data Solutions. Properties with foreclosure filings in 2020 represented a scant 0.16 percent of all U.S. homes, down from a foreclosure rate of 0.36 percent in 2019. The record high was 2.23 percent, in 2010.

In a separate study released Friday, mortgage data firm Black Knight said foreclosure starts plunged by 67 percent from 2019, while foreclosure sales dropped by 70 percent compared to the previous year.

However, the data isn’t all rosy. Fully 2.15 million American homeowners were 90 days past due on their mortgages, a number that rose by 1.7 million during the year of the coronavirus pandemic, Black Knight said.

Foreclosures fell not because all was well economically, but because lenders essentially stopped taking back properties in 2020. After the coronavirus pandemic struck in March, federal and state officials hit the pause button on default filings by lenders. And the CARES Act called for mortgage forbearance plans designed to keep struggling workers in their homes.
''')

df = pd.read_csv('./data/cleaned/foreclosures.csv')
fig = px.line(df, x='Year', y=df.columns)
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(step="all")
        ])
    )
)
colm2.plotly_chart(fig)
##
col1, col2 = st.columns((2,1))

img = Image.open('subprime_mort.png')
with col1:
    st.image(img)

col2.write('''
    \n The mortgage delinquency rate is the share of the total number of mortgaged home loans in the U.S. where payment is overdue by 30 days or more. Many borrowers are eventually able to service their loan though, with foreclosure rates being generally 50-75 percent lower than delinquency rates. Total home mortgage debt in the U.S. stood at 10.94 trillion U.S. dollars in 2020. 
    \n ‘Subprime’ loans, being targeted at high-risk borrowers and generally coupled with higher interest rates to compensate for the risk, have far higher delinquency rates than conventional loans. Defaulting on such loans was one of the triggers for the 2007-2010 financial crisis, with subprime delinquency rates reaching almost 26 percent around this time. These higher delinquency rates translate into higher foreclosure rates, which peaked at just under 15 percent of all subprime mortgages in 2011.
    ''')
st.write("In the second quarter of 2020, under the effects of the coronavirus crisis, the mortgage delinquency rate in the United States spiked at 8.22 percent, just one percent down from its peak of 9.3 percent during the subprime mortgage crisis of 2007-2010. Following the drastic increase directly after the outbreak of the pandemic, delinquency rates started gradually declining and reached 4.65 percent as of the fourth quarter of 2021. ")

##############################
st.header('Determining the most influencial factor')
st.write('''
To Determine the most influencial factor of all the forementioned factors, 
all the data for the factors were resampled to a similar time intervals and combined into a single dataframe:
''')
df = pd.read_csv('finalcombined.csv')
st.dataframe(df)

st.write('Here CUSUSHPISA is the S&P CoreLogic Case-Shiller U.S. National Home Price NSA Index')

desc = df.describe()
st.dataframe(desc)



corr = df.corr()
corr_inf = pd.DataFrame(corr.CSUSHPISA)

st.header("Correlation Analysis")
col1,col2 = st.columns((1,1))
col1.write('''

''')
col1.dataframe(corr_inf,  height=700)

# Generate a mask for the upper triangle
mask = np.triu(np.ones_like(corr, dtype=bool))

# Set up the matplotlib figure
f, ax = plt.subplots(figsize=(11, 9))

# Generate a custom diverging colormap
cmap = sns.diverging_palette(230, 20, as_cmap=True)

# Draw the heatmap with the mask and correct aspect ratio
fig = plt.subplots()

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=.5, cbar_kws={"shrink": .5})
plt.savefig('corr_dia1.png')
img = Image.open('corr_dia1.png')
col2.image(img)

col11,col12 = st.columns((2,1))
corr_inf_new = corr_inf.head(10)
fig = px.bar(corr_inf_new)
col11.plotly_chart(fig)
col12.title("_")
col12.write('''
This analysis shows how the factors are correlated with the index and amongst themselves. Higher the bars in the graph 
(in magnitude) on the left, the more correlated the factors are with the index. 
\n For all the plots above the 0 value, there is a positive correlation and vice-versa.
''')

col1, col2 = st.columns((2,1))
col1.write('''
The absolute values indicate the level of correlation and the sign shows the relation, i.e either positive or negative correlation.
\n The most correlated factors(in order) are:
''')
data = abs(corr_inf_new)
sorted_data = data.sort_values(by=['CSUSHPISA'], ascending=False)
sorted_data_new = corr_inf_new.sort_values(by=['CSUSHPISA'], ascending=False)
col2.dataframe(sorted_data, height=700)
top_5 = sorted_data.head(5)

st.header("Explanatory Regression Analysis")

st.write('''
Next, a multiple regression analysis was performed on the cleaned and combined data. Given in the case, in which we would like to predict the prices
of the index, a multiple regression model would have been created and only the factor(s) influencing it the most would be chosen. Here, only the analysis 
is performed in order to examine whether:\n 1) Is it better to take all the factors into consideration?
\n2) Is it better to take only the top 5 highest correlated data into consideration? 
\n 3) Is it better to just take one factor into consideration?
\n Each of the cases is examined and the output is explained below.
''')
##
col1,col2 = st.columns((1,1))

col1.write('''
Case 1) Building a multiple regression model taking all the factors into consideration:
''')

col1.dataframe(corr_inf_new, height=700)

img_mlr_2 = Image.open('MLR_1.png')
col2.image(img_mlr_2)
##
col1.write('''
Case 2) The asbolute values of the correlation table have been sorted and the 5 factors with the highest correlation are represented in the table
below. When these factors(only) are taken into consideration:
''')


col1.dataframe(top_5)

img_mlr_2 = Image.open('MLR_5.png')
col2.image(img_mlr_2)
##
col1.write('''
Case 3) Only the most correlated factor i.e. the population was taken into consideration:
''')

data = abs(corr_inf_new)
sorted_data = data.sort_values(by=['CSUSHPISA'], ascending=False)
top_1 = sorted_data.head(1)
col1.dataframe(top_1)

img_mlr_2 = Image.open('MLR_O.png')
col2.image(img_mlr_2)


##
st.header("Conclusion")
st.write('''
It is known that for a regression model the R-Squared value always increases and never decres incase the number of variables are increased.
To make up for this, the Adjusted R-Squared penalises the R-Squared based on the number of variables. A very low Adjusted R-Square may indicate that some
of the variables are not contributing. And as we take more variables the R-Squared value rises, which is represented in the above cases. 
However, in the case 1, the Adjusted R-Squared value is very low, indicating that there is no variable that is not contributing at all. 
\n The probablistic F-Static value for case 3 is lesser than that of case 1, indicating that the most correlated field, "Population", 
does have great influence on the index. This also allows us to conclude, that the results of the correlation analysis are true and are proven here.
Thus, we can say that the most import factors in order influencing the *S&P CoreLogic Case-Shiller U.S. National Home Price NSA Index* are the most 
correlated factors. And that Multiple regression analysis is only useful in quantifying relationships in factors when there is a need to do predective
modelling and not singling out one most important variable out of multiple variables.
''')

##############################
st.header('Biblography 📚')
html_string = '''<html>
    <head>
        <title> Biblography </title>
    </head>
    <body>
        <table style="border-width: 1;">
            <th style="background-color:lightgray;"> Refernces</th>
            <tr>
                <td>
                    <a href="http://fred.stlouisfed.org">fred.stlouisfed.org</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="https://www.statista.com">statista.com</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="www.opendoor.com">opendoor.com</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="http://nar.realtor">nar.realtor</a>
                </td>
            </tr>     
            <tr>
                <td>
                    <a href="https://tradingeconomics.com/">tradingeconomics.com</a>
                </td>
            </tr>  
            <tr>
                <td>
                    <a href="https://data.worldbank.org">data.worldbank.org</a>
                </td>
            </tr>
            <tr>
                <td>
                    <a href="https://www.cnbc.com">cnbc.com</a>
                </td>
            </tr>         
        </table>
    </body>
</html>'''
st.markdown(html_string, unsafe_allow_html=True)
