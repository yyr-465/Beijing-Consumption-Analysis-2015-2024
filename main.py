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