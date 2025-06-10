# %% [markdown]
# # Unemployment rate Over Time Analysis

# %% [markdown]
# ## Libraries and Data Import Testing

# %%
import pandas as pd
import matplotlib.pyplot as plt
print("Assignment 1: Fatima Zahra Manzah")
print("\nPart 4: Development Workflow with Jupyter and VSCode")
print("\n-Testing Part:")
print(" All packages imported successfully!")
print(f" Pandas version: {pd.__version__}")
# Test loading the data file
df = pd.read_csv('UNRATE.csv')
print(f" Data loaded successfully! Shape: {df.shape}")

# %% [markdown]
# ## Part 1: Data Loading and Exploration

# %%
import pandas as pd
import matplotlib.pyplot as plt
# Load the provided unemployment data
df = pd.read_csv('UNRATE.csv')
df['observation_date'] = pd.to_datetime(df['observation_date'])
print("1-Data Loading and Exploration:")
print(" Dataset shape:", df.shape)
print(f" Data types:\n{df.dtypes}")
print(f" First 5 rows:\n{df.head()}")

# %% [markdown]
# **Unrate & Observation date Statistics**

# %%
print("-Basic statistics:")
# Unrate statistics
print(f"\n Unrate data:\n {df['UNRATE'].describe()}")
# Now let's Check the range of Observation Date:
print(f"\n Observation date data:\n{df['observation_date'].describe()}")

# %% [markdown]
# **Unrate Statistics Summary:** "We assume that the unrate is a percentage"
# 
# The unemployment rate in the dataset ranges from 2.5% to 14.8%, with an average of 5.68% and a median of 5.5%, indicating a relatively moderate central tendency but with some high outliers.

# %% [markdown]
# **Observation date Statistics Summary:**
# 
# We can see that the dataset contains monthly unemployment data spanning from January 1948 to April 2025, with a median observation date around August 1986.

# %% [markdown]
# ## Part 2: Statistical Analysis (15 points)

# %%
print("\n2-Statistical Analysis (15 points)")

# %% [markdown]
# ### **Overall average Unemployment rate**

# %%
# Calculate the overall average unemployment rate
average_unrate = df['UNRATE'].mean()
# We will use 2 decimal precision
print(f"\n Overall average unemployment rate: {average_unrate:.2f}%")

# %% [markdown]
# ### **Minimum & Maximum Unemployment rates with their dates**

# %%
# Minimum Unemployment rate
print(f"\n Minimum unemployment rate:\n{df[df['UNRATE'] == df['UNRATE'].min()]}")
# Maximum Unemployment rate
print(f"\n Maximum unemployment rate:\n{df[df['UNRATE'] == df['UNRATE'].max()]}")

# %% [markdown]
# ### **Unemployment statistics by decade (1950s, 1960s, etc.)**

# %%
# Create a column decade:
df['decade'] = (df['observation_date'].dt.year // 10) * 10
# Group by decade and calculate statistics
decade_stats = df.groupby('decade')['UNRATE'].agg(['mean', 'min', 'max', 'std', 'count']).round(2)
print(f"\n Unemployment statistics by decade:\n{decade_stats}")

# %% [markdown]
# ### **Year with the highest average unemployment rate**

# %%
# Creating a column year 
df['year'] = df['observation_date'].dt.year
# Extract the average per year
average_by_year = df.groupby('year')['UNRATE'].mean()
# Extract the year of the highest average
max_year = average_by_year.idxmax()
# Extract the highest average
max_value = average_by_year.max()
print(f"\n The highest average unemployment rate was {max_value:.2f}% in {max_year}.")

# %% [markdown]
# ## Part 3: Business Questions to Answer (10 points)

# %%
print("\n3-Business Questions to Answer (10 points)")

# %% [markdown]
# ### **What was the unemployment rate during major economic events (2008 financial crisis, COVID-19 pandemic)?**

# %% [markdown]
# #### The 2008 Financial Crisis
# 
# Wikipedia: "The 2008 financial crisis, also known as the global financial crisis (GFC), was a major worldwide financial crisis centered in the United States. The causes of the 2008 crisis included excessive speculation on housing values by both homeowners and financial institutions that led to the 2000s United States housing bubble, exacerbated by predatory lending for subprime mortgages and deficiencies in regulation. Cash out refinancings had fueled an increase in consumption that could no longer be sustained when home prices declined. The first phase of the crisis was the subprime mortgage crisis, which began in early 2007, as mortgage-backed securities (MBS) tied to U.S. real estate, and a vast web of derivatives linked to those MBS, collapsed in value. A liquidity crisis spread to global institutions by mid-2007 and climaxed with the bankruptcy of Lehman Brothers in September 2008, which triggered a stock market crash and bank runs in several countries.The crisis exacerbated the Great Recession, a global recession that began in mid-2007, as well as the United States bear market of 2007–2009. It was also a contributor to the 2008–2011 Icelandic financial crisis and the euro area crisis."
# 
# Check out the links below for more information: 
# - [2008 financial crisis](https://en.wikipedia.org/wiki/2008_financial_crisis)
# - [BLS SPOTLIGHT ON STATISTICSTHE RECESSION OF 2007–2009](https://www.bls.gov/spotlight/2012/recession/pdf/recession_bls_spotlight.pdf)
# 
# **We will now discover the trend of the period between January 2006 and December 2009, to see how the unemployment rate evolved during the 2008 financial crisis.**
# 

# %%
# Filter the data for the period 
fcrisis_period = df[(df['observation_date'] >= '2006-01-01') & (df['observation_date'] <= '2009-12-31')]
# Calculate average unemployment rate during this period
avg_unrate = fcrisis_period['UNRATE'].mean()

# Find the peak in this period
peak_row = fcrisis_period[fcrisis_period['UNRATE'] == fcrisis_period['UNRATE'].max()]
peak_date = peak_row['observation_date'].values[0]
peak_value = peak_row['UNRATE'].values[0]

# Plot with peak annotation
print("\nWhat was the unemployment rate during major economic events (2008 financial crisis, COVID-19 pandemic)?")
plt.figure(num='Figure 1: 2008 Fiancial crisis Trend & Peak', figsize=(10, 5))
plt.plot(fcrisis_period['observation_date'], fcrisis_period['UNRATE'], label='Unemployment Rate', color='purple')
plt.scatter(peak_date, peak_value, color='black', zorder=5)
# Use of chatgpt to plot the peak in the graph :
plt.text(peak_date, peak_value + 0.3, f'Peak: {peak_value:.1f}%\n({pd.to_datetime(peak_date).strftime("%b %Y")})',
         ha='center', va='bottom', fontsize=9, backgroundcolor='white')
plt.title('Unemployment Rate (Jan 2006 - Dec 2009)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
# Convert peak_date to Timestamp before formatting
peak_date = pd.to_datetime(peak_date)
print("\n What was the unemployment rate during the 2008 financial crisis?")
print(" NB: We consider The period 'January 2006 to December 2009' for the 2008 Financial crisis")
print(f"\n  The peak unemployment rate was {peak_value:.2f}% in {peak_date.strftime('%B %Y')}.")
print(f"  The average unemployment rate during that period was {avg_unrate:.2f}%")
plt.show()


# %% [markdown]
# **The plot shows a sharp rise in unemployment between mid-2008 and mid-2009, reaching nearly 10%, clearly reflecting the impact of the 2008 financial crisis. The unemployment rate reached its peak of 10.0% in October 2009, marking the height of the 2008 financial crisis's impact on the job market.**

# %% [markdown]
# #### Covid-19 Pandemic
# 
# **Pew Research Center:** "The COVID-19 outbreak and the economic downturn it engendered swelled the ranks of unemployed Americans by more than 14 million, from 6.2 million in February to 20.5 million in May 2020. As a result, the U.S. unemployment rate shot up from 3.8% in February, among the lowest on record in the post-World War II era to 13.0% in May. That rate was the era’s second highest, trailing only the level reached in April (14.4%).
# The rise in the number of unemployed workers due to COVID-19 is substantially greater than the increase due to the Great Recession, when the number unemployed increased by 8.8 million from the end of 2007 to the beginning of 2010. The Great Recession, which officially lasted from December 2007 to June 2009, pushed the unemployment rate to a peak of 10.6% in January 2010, considerably less than the rate currently, according to a new Pew Research Center analysis of government data."
# 
# Check out the link for more information: [Unemployment rose higher in three months of COVID-19 than it did in two years of the Great Recession](https://www.pewresearch.org/short-reads/2020/06/11/unemployment-rose-higher-in-three-months-of-covid-19-than-it-did-in-two-years-of-the-great-recession/)
# 
# **Further analysis of the COVID-19 period will be done. We will focus on the years 2020, 2021, 2022 and 2023 (Since The WHO ended the public health emergency of international concern (PHEIC) on 5 May 2023) to identify when the unemployment rate reached its peak.**

# %%
# COVID-19 period (2020 – May 2023)
covid_period = df[(df['observation_date'] >= '2020-01-01') & (df['observation_date'] <= '2023-05-03')]

# Find the peak in this period
peak_row = covid_period[covid_period['UNRATE'] == covid_period['UNRATE'].max()]
peak_date = peak_row['observation_date'].values[0]
peak_value = peak_row['UNRATE'].values[0]
# Calculate average unemployment rate during this period
avg_unrate = covid_period['UNRATE'].mean()

# Plot
plt.figure( num='Figure 2: COVID-19 Unemployment rate Trend & Peak', figsize=(10, 5))
plt.plot(covid_period['observation_date'], covid_period['UNRATE'], label='Unemployment Rate', color='darkred')
plt.scatter(peak_date, peak_value, color='black', zorder=5)
# Use of chatgpt in this part to plot the peak on the graph :
plt.text(peak_date, peak_value + 0.5, f'Peak: {peak_value:.1f}%\n({pd.to_datetime(peak_date).strftime("%b %Y")})', 
         ha='center', va='bottom', fontsize=9, backgroundcolor='white')
plt.title('Unemployment Rate (2020 - 5 May 2023)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
# Convert peak_date to Timestamp before formatting
peak_date = pd.to_datetime(peak_date)
print("\n What was the unemployment rate during COVID-19?")
print(""" NB: The Covid-19 Perido in this analysis is considered from 2020 to 5 May 2023 since 
    The WHO ended the public health emergency of international concern (PHEIC) on 5 May 2023 """)
print(f"\n  The peak unemployment rate was {peak_value:.2f}% in {peak_date.strftime('%B %Y')}.")
print(f"  Average unemployment rate (2020 - May 2023): {avg_unrate:.2f}%")
plt.show()

# %% [markdown]
# **Covid-19 analysis summary:** The unemployment rate peaked at 14.8% in April 2020, marking the highest point during the COVID-19 pandemic

# %% [markdown]
# ### **Which decade had the most stable unemployment rates (lowest standard deviation)?**

# %%
print("\n Which decade had the most stable unemployment rates (lowest standard deviation)?")

# Calculate standard deviation by decade (since we already added the column decade in the part 2 )
decade_std = df.groupby('decade')['UNRATE'].std()

# Get the decade with the lowest standard deviation
most_stable_decade = decade_std.idxmin()
lowest_std = decade_std.min()
print(f"  The most stable decade was the {most_stable_decade}s with a standard deviation of {lowest_std:.2f}.")


# %% [markdown]
# ### **What’s the trend in unemployment over the last 10 years?**

# %%
# Since we already added the column year we will Filter for the last 10 years
last_10_years = df[df['year'] >= df['year'].max() - 10]
# Plot
print("\n Look at the figure 3 to see the trend in unemployment over the last 10 years")
plt.figure(num='figure 3: The trend in unemployment over the last 10 years',figsize=(12, 5))
plt.plot(last_10_years['observation_date'], last_10_years['UNRATE'], label='Unemployment Rate')
# Chatgpt help for that part of fixing the unique years in the x-axis
# Set x-axis ticks by year
years_to_show = sorted(last_10_years['year'].unique())
plt.xticks(
    ticks=[last_10_years[last_10_years['year'] == y]['observation_date'].iloc[0] for y in years_to_show],
    labels=years_to_show,
    rotation=45)
plt.title('Unemployment Rate (Last 10 Years)')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
# Create simple table
simple_table = last_10_years[['observation_date', 'UNRATE']].copy()
simple_table.columns = ['Date', 'Unemployment Rate']
simple_table = simple_table.round(2)
# Display
# Show all rows in output (help Chatgpt to see all the ouput)
pd.set_option('display.max_rows', None)
print(f"\n The trend in unemployment over the last 10 years:\n{simple_table}")
plt.show()

# %% [markdown]
# ## Part 4: Data Visualization (10 points)

# %%
print("\n4-Data Visualization (10 points)")

# %% [markdown]
# ### **Unemployment rate over time**

# %%
# Plot Unemployement rate Over Time
print(" Look at the figure 4 to see the plot of the Unemployement rate Over Time")
plt.figure(num='Figure 4: Unemployment Rate Over Time', figsize=(14, 6))
plt.plot(df['observation_date'], df['UNRATE'], label='Unemployment Rate', color='blue')
plt.title('Unemployment Rate Over Time')
plt.xlabel('Years')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig('Unemployement_rate_Over_Time.png', dpi=300)  # dpi=300 for high resolution
plt.show()

# %% [markdown]
# ### **Average unemployment by decade**

# %%
# Calculate average unemployment rate by decade
decade_avg = df.groupby('decade')['UNRATE'].mean().round(2)
print(" Look at the figure 5 to see the plot of Average unemployment by decade")
# Plot bar chart : chatgpt help
plt.figure(num='figure 5: Average unemployment by decade', figsize=(10, 5))
plt.bar(decade_avg.index.astype(str), decade_avg.values, color='gray')
plt.title('Average Unemployment Rate by Decade')
plt.xlabel('Decade')
plt.ylabel('Average Unemployment Rate (%)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
# Save as PNG
plt.savefig('Unemployment_By_Decade.png', dpi=300)  # dpi=300 for high resolution
plt.show()

# %% [markdown]
# ### **Analysis Summary:** 

# %%
print("""
    Analysis Summary: The unemployment rate has followed a clear cycle over the years, rising and falling with the economy. 
    We see big spikes during tough times, like the early 1980s, the 2008 financial crisis, 
    and most sharply in 2020 when the pandemic hit and unemployment soared to nearly 15%. 
    Thankfully, that surge didn’t last long, as the job market bounced back fairly quickly. 
    Looking at the bigger picture, unemployment has generally stayed lower in recent decades, 
    especially during the stable period from 2010 to 2020 before COVID-19 disrupted the trend.
    To get a better understanding of how unemployment has changed during tough economic times, 
    we took a closer look at three major periods that are marked by a sharp rise in unemployment: 
    - The early 1980s recession
    - The 2008 financial crisis
    - The COVID-19 pandemic
      """)

# %% [markdown]
# ## Additional Analysis

# %%
print("\n5-Further Analysis: 'The 1980s recession crisis' ")

# %% [markdown]
# **Early 1980s Recession**
# 
# The early 1980s recession was a severe economic recession that affected much of the world between approximately the start of 1980 and 1982. Long-term effects of the early 1980s recession contributed to the Latin American debt crisis, long-lasting slowdowns in the Caribbean and Sub-Saharan African countries,the US savings and loan crisis, and a general adoption of neoliberal economic policies throughout the 1990s. It is widely considered to have been the most severe recession since World War II.
# 
# Check out the link for more information: [Early 1980s recession](https://en.wikipedia.org/wiki/Early_1980s_recession)
# 
# Based on information from Wikipedia, we will focus first on the period from March 1973 to February 1993 to see if our data reflects similar trends as shown i  the picture below, and then narrow in on 1980 to 1982 to identify the peak in unemployment during that time.
# 
# ![US unemployment rate](https://upload.wikimedia.org/wikipedia/commons/d/d3/US_1980s_unemployment.png)
# 

# %% [markdown]
# ##### 1. Plot from March 1973 to February 1993

# %%
period1 = df[(df['observation_date'] >= '1973-03-01') & (df['observation_date'] <= '1993-02-28')]
print(" Look at the figure 6 to see the plot of the Early 1980s Recession Trend")
plt.figure(num='Figure 6: Early 1980s Recession Trend', figsize=(12, 5))
plt.plot(period1['observation_date'], period1['UNRATE'], label='Unemployment Rate')
plt.title('Unemployment Rate (Mar 1973 - Feb 1993)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# %% [markdown]
# ##### 2. Plot from 1980 to 1982 & Early 1980s recession Peak 

# %%
period2 = df[(df['observation_date'] >= '1980-01-01') & (df['observation_date'] <= '1982-12-31')]

# Find the peak unemployment rate during this period
peak_row = period2[period2['UNRATE'] == period2['UNRATE'].max()]
peak_date = peak_row['observation_date'].values[0]
peak_value = peak_row['UNRATE'].values[0]

# Plot the data and annotate the peak
print(" Look at the figure 7 to see the plot of the Early 1980s Recession Peak")
plt.figure(num='Figure 7: Early 1980s Recession Peak', figsize=(10, 4))
plt.plot(period2['observation_date'], period2['UNRATE'], label='Unemployment Rate', color='orange')
plt.scatter(peak_date, peak_value, color='black', zorder=5)
# Use of chatgpt to plot the peak correctly in the graph
plt.text(peak_date, peak_value + 0.3, f'Peak: {peak_value:.1f}%\n({pd.to_datetime(peak_date).strftime("%b %Y")})',
         ha='center', va='bottom', fontsize=9, backgroundcolor='white')

plt.title('Unemployment Rate (1980-1982)')
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# %% [markdown]
# **Between 1980 and 1982, the unemployment rate showed a steady upward trend, rising from around 6% to nearly 11%. This sharp increase reflects the severity of the early 1980s recession, confirming a prolonged period of economic struggle during these years. The unemployment rate peaked at 10.8% in both November and December 1982, marking the highest point of the early 1980s recession. We can see a clear rise in unemployment during this time, which matches what is known about the early recession crisis and helps confirm that the data reflects the economic challenges of that period.**

# %%
print("""\n
     Between 1980 and 1982, the unemployment rate showed a steady upward trend, 
     rising from around 6% to nearly 11%. This sharp increase reflects the severity of the early 1980s recession, 
     confirming a prolonged period of economic struggle during these years. 
     The unemployment rate peaked at 10.8% in both November and December 1982, marking the highest point of the early 1980s recession. 
     We can see a clear rise in unemployment during this time, which matches what is known about the early recession crisis and helps 
     confirm that the data reflects the economic challenges of that period.""")


