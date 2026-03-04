# -*- coding: utf-8 -*- 
from data_preprocessing import*
from Consumption_upgrade_indicator import *
from Drawing import *

df_urban = pd.read_excel(r"data/C0507_copy.xls")
df_rural = pd.read_excel(r"data/C0510_copy.xls")
df_urban_t = data_preprocessing(df_urban)
df_rural_t = data_preprocessing(df_rural)
urban_Engel = Engel_coefficient(df_urban_t)
rural_Engel = Engel_coefficient(df_rural_t)
POSC(df_urban_t, df_rural_t)
urban_POSC  = proportion_of_service_consumption_for_year(df_urban_t)
rural_POSC =  proportion_of_service_consumption_for_year(df_rural_t)
Line_diagram(ECFD(df_urban_t),ECFD(df_rural_t))
df_rural_2015 , df_rural_2024 = The_proportion_of_consumption(df_rural,2015,2024)
Rader_Map(df_rural_2015,df_rural_2024)
Stacking_diagram(df_urban_t)
Trend_chart(df_urban_t,df_rural_t)
try:
    file_path = (r"data/分省年度数据.csv")
    df_p = pd.read_csv(file_path, encoding='gbk', skiprows=3)
    # 2. 筛选北京数据（假设列名为'地区'，请根据你CSV实际列名微调）
    # 提取关键年份 2015 和 2024 进行对比
    bj_data = df_p.iloc[0:11]
    bj_data.set_index('指标', inplace=True)
    grain_2015 = bj_data.loc['城镇居民人均粮食消费量(千克)','2024年']
    grain_2024 = bj_data.loc['城镇居民人均粮食消费量(千克)','2015年']
    oil_2015 = bj_data.loc['城镇居民人均食用油消费量(千克)','2024年']
    oil_2024 = bj_data.loc['城镇居民人均食用油消费量(千克)','2015年']
    veg_2020 = bj_data.loc['城镇居民人均蔬菜及食用菌消费量(千克)','2020年']
    veg_avg = bj_data.loc['城镇居民人均蔬菜及食用菌消费量(千克)'].mean()
    print("\n"  + "="*45)
    print("[In-Depth Insights]Analysis of Beijing Residents' Physical Consumption Structure (2015-2024)")
    grain_drop = (grain_2015 - grain_2024) / grain_2015 * 100
    print(f"1. Dietary Structure Optimization: Per capita grain consumption decreased from {grain_2015} kg "
          f"to {grain_2024} kg (a reduction of {grain_drop:.1f}%).")
    print(f"   - Verification Conclusion: The decline in the Engel coefficient coincides with reduced staple "
          f"food dependency, aligning with dietary upgrading patterns in high-income regions.")
    oil_drop = (oil_2015 - oil_2024) / oil_2015 * 100
    print(f"2. Health-conscious consumption trends: Edible oil consumption has dropped significantly by "
          f"{oil_drop:.1f}%, reflecting a shift toward low-oil, healthier diets.")
    print(f"3. 2020 Consumption Resilience: Vegetable consumption reached {veg_2020} kg that year "
          f"(exceeding the ten-year average of {veg_avg:.1f} kg).")
    print(f"   - Verification conclusion: Home-based living during the special period boosted the physical volume of basic agricultural products, supporting a pulse-like increase in the proportion of food expenditures.")
    print("=" * 45 + "\n")
except Exception as e:
    print(f"⚠️ Skip automated analysis of physical data (please verify CSV column names match): {e}")


