import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# 1
# Import the data from medical_examination.csv and assign it to the df variable.
df = pd.read_csv('medical_examination.csv')
# len(df)
# df.columns
# df.head()
# df.shape

# 2
# Add an overweight column to the data. To determine if a person is overweight, 
# first calculate their BMI by dividing their weight in kilograms by the square of their height in meters.
# If that value is > 25 then the person is overweight. Use the value 0 for NOT overweight and the value 1 for overweight.
df['overweight'] = df['weight'] / (df['height']/100)**2 >25
# df.head()
# df.shape
# df['overweight'].value_counts()
df['overweight'] = df['overweight'].astype(int)
# df.head()

# 3
# Normalize data by making 0 always good and 1 always bad.
# If the value of cholesterol or gluc is 1, set the value to 0. If the value is more than 1, set the value to 1.
# 1 >> 0  ||  +1 >> 1
columns = ['cholesterol', 'gluc']
for col in columns:
    # print(df[col].value_counts())
    df[col] = df[col].replace({1: 0, 2: 1, 3: 1})
    # print(df[col].value_counts())
# df.head()

# df.shape

# 4
# Draw the Categorical Plot in the draw_cat_plot function.
def draw_cat_plot():
    
    # 5
# Create a DataFrame for the cat plot using pd.melt with values from cholesterol, gluc, smoke, alco, active, and overweight in the df_cat variable.
    df_cat = pd.melt(df,id_vars=['id', 'age', 'sex', 'height', 'weight', 'cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'] )

    # 6
    # Group and reformat the data in df_cat to split it by cardio. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    
    # 7
# Convert the data into long format and create a chart that shows the value counts of the categorical features using the following method provided by the seaborn library import: sns.catplot().
    g = sns.catplot(data=df_cat, x='variable', y='total' ,col='cardio', hue='value', legend=True, kind='bar')
    # iterate through axes
    for ax in g.axes.ravel():
        # add annotations
        for c in ax.containers:
            labels = [f'{(v.get_height() ):.0f}' for v in c]
            ax.bar_label(c, labels=labels, label_type='edge')
        ax.margins(y=0.2)


    # 8
#     Get the figure for the output and store it in the fig variable.
    fig = g.fig


    # 9
#     Do not modify the next two lines.
    fig.savefig('catplot.png')
    return fig




# 10
# Draw the Heat Map in the draw_heat_map function.
def draw_heat_map():
    # 11
#     Clean the data in the df_heat variable by filtering out the following patient segments that represent incorrect data:
#     diastolic pressure is higher than systolic (Keep the correct data with (df['ap_lo'] <= df['ap_hi']))
#     height is less than the 2.5th percentile (Keep the correct data with (df['height'] >= df['height'].quantile(0.025)))
#     height is more than the 97.5th percentile
#     weight is less than the 2.5th percentile
#     weight is more than the 97.5th percentile

    df_heat = df.loc[(df['ap_lo'] <= df['ap_hi']) & 
                (df['height'] >= df['height'].quantile(0.025)) & 
                (df['height'] <= df['height'].quantile(0.975)) & 
                (df['weight'] >= df['weight'].quantile(0.025)) & 
                (df['weight'] <= df['weight'].quantile(0.975))] 

    # 12
#     Calculate the correlation matrix and store it in the corr variable.
    corr = df_heat.corr() # type: ignore

    # 13
#     Generate a mask for the upper triangle and store it in the mask variable.
    mask = np.triu(corr)



    # 14
#     Set up the matplotlib figure.
    fig, ax =  plt.subplots(figsize=(12, 9))

    # 15
#     Plot the correlation matrix using the method provided by the seaborn library import: sns.heatmap().
    sns.heatmap(data=corr, mask=mask, annot=True, fmt='.1f', ax=ax, square=True, linewidths=0.5, cbar_kws={"shrink": .8})


    # 16
#     Do not modify the next two lines.
    fig.savefig('heatmap.png')
    return fig

# draw_cat_plot()
# plt.show()
# draw_heat_map()
# plt.show()
