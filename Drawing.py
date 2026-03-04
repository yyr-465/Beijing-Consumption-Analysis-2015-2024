import matplotlib.pyplot as plt
import numpy as np
from data_preprocessing import *
def ECFD(df):
    df['E_coefficient'] = df['Food、tobacco and alcohol'] / df['Per capita consumption expenditure']
    return df['E_coefficient']
def Line_diagram(df1,df2):
    plt.figure(figsize = (10,10))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.xlabel('Years', fontsize = 20)
    plt.ylabel('Power Consumption', fontsize = 20)
    plt.ylabel('percent(%)')
    plt.plot(df1.index,df1*100,df2*100,linewidth = 2,marker = '.',
             markersize=10,label = 'E_coefficient')
    for a,b,c in zip(df1.index,df1*100,df2*100):
        plt.text(a,b,f'{b:.2f}',ha = 'center', va = 'bottom' , fontsize = 10)
        plt.text(a,c,f'{c:.2f}',ha = 'center', va = 'bottom' , fontsize = 10)
    plt.legend(['urban_E_coefficient','rural_E_coefficient'])
    plt.title('2015-2024 Urban and Rural Engel Coefficient Double Line Chart',fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.grid(True)
    plt.show()
    return 0
def The_proportion_of_consumption(df,year1,year2):
    df = data_preprocessing(df)
    df_columns_1 = df.columns[2:]
    prop_year1 = df.loc[year1,df_columns_1]/df.loc[year1,'Per capita consumption expenditure']
    prop_year2 = df.loc[year2,df_columns_1]/df.loc[year2,'Per capita consumption expenditure']
    list_year1 = prop_year1.to_numpy()
    list_year2 = prop_year2.to_numpy()
    return list_year1,list_year2
def Rader_Map(df1,df2):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    labels = ['Food、tobacco\n and alcohol','Clothing','Live','Daily necessities\n and services',
              'Traffic Communication','Education, Culture\n and Entertainment','Heath care',
              'Other supplies\n and services']
    value1 = df1*100
    value2 = df2*100
    N = len(labels)
    angles = np.linspace(0,2*np.pi,N,endpoint = False).tolist()
    value1 = np.append(value1,value1[0])
    value2 = np.append(value2,value2[0])
    angles += angles[:1]
    fig , ax = plt.subplots(figsize = (10,10),subplot_kw={'polar':True})
    ax.plot(angles,value1,"o-",color = 'blue',label = '2015')
    ax.fill(angles,value1,color = 'blue',alpha = 0.5)
    ax.plot(angles,value2,"o-",color = 'red',label = '2024')
    ax.fill(angles,value2,color = 'red',alpha = 0.5)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels,fontsize = 10,color = 'black')
    plt.legend(loc = 'upper right',fontsize = 10)
    plt.title('2015 VS 2024 Consumption Composition Radar Chart',fontsize = 20)
    plt.show()
def Stacking_diagram(df):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    labels = ['Food、tobacco and alcohol','Clothing','Live','Daily necessities and services',
              'Traffic Communication','Education, Culture and Entertainment','Heath care',
              'Other supplies and services']
    plot_df = df.loc[2015:2024,labels]
    ax = plot_df.plot(kind = 'bar',stacked = True,figsize = (12,7),colormap = 'Blues',edgecolor = 'black')
    plt.title('2015-2024 Beijing Urban Consumption Structure (Stacked)', fontsize=16)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Annual Expenditure (Yuan)', fontsize=12)
    plt.xticks(rotation=0)  # 让年份横向显示
    plt.legend(title='Consumption Categories', bbox_to_anchor=(1.05, 1), loc='upper left')

    # 4. 在柱子上方标注总支出（可选，增加专业度）
    total_spending = df.loc[2015:2024, 'Per capita consumption expenditure']
    for i, total in enumerate(total_spending):
        plt.text(i, total + 500, f'{int(total)}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    plt.tight_layout()
    plt.show()
def Trend_chart(df1,df2):
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(df1.index,df1['POSC'],label = 'Urban Consumption')
    plt.plot(df1.index,df2['POSC'],label = 'Rural Consumption')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Precent(%)', fontsize=12)
    plt.title('2015-2024 Beijing Urban-Rural Service Consumption Trend', fontsize=16)
    plt.legend(loc = 'upper right',fontsize = 10)
    plt.show()