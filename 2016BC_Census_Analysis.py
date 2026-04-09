import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv("/Users/marianaramirez/Downloads/Project2/BC Census 2016 data.csv") #WARNING: For this code to work in your computer dont forget to change the name of the folder it is located in. 

df_clean = df.dropna(subset=['income_total_median', 'shelt_rent_30plus_rate', 'shelt_rent_mo_cost_mean'])

pha_rent = df_clean.groupby('pha')['shelt_rent_mo_cost_mean'].mean().sort_values()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
plt.style.use('seaborn-v0_8-whitegrid')


ax1.scatter(df_clean['income_total_median'], df_clean['shelt_rent_30plus_rate'], 
            alpha=0.6, color='teal', edgecolor='black', s=50)

z = np.polyfit(df_clean['income_total_median'], df_clean['shelt_rent_30plus_rate'], 1)
p = np.poly1d(z)
ax1.plot(df_clean['income_total_median'], p(df_clean['income_total_median']), "r--", linewidth=2, label='Trendline')

ax1.set_title("Income vs. Housing Burden (by Community)", fontsize=14)
ax1.set_xlabel("Median Total Income ($)")
ax1.set_ylabel("% of Renters Spending >30% of Income on Rent")
ax1.legend()

bars = ax2.bar(pha_rent.index, pha_rent.values, color='coral', edgecolor='black', alpha=0.8)
ax2.set_title("Average Monthly Rent by Region (PHA)", fontsize=14)
ax2.set_ylabel("Average Monthly Rent ($)")


ax2.tick_params(axis='x', rotation=15)

for bar in bars:
    yval = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2, yval + 15, f'${int(yval)}', ha='center', va='bottom', fontweight='bold')


plt.suptitle("BC Housing Affordability Analysis (2016 Census)", fontsize=18, fontweight='bold')
plt.tight_layout()

plt.show()
