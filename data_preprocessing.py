import pandas as pd
def data_preprocessing(df):
    #print(df.head(10))
    new_header = df.iloc[2]
    new_header.name = None
    df = df[3:]
    df.columns = new_header
    df.dropna(how='all', axis=0, inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.rename(columns={df.columns[0]:"年份"},inplace=True)
    df['年份'] = df['年份'].astype(str).str.replace(r'\s+', '', regex=True)
    target_list = ['人均可支配收入', '人均消费支出', '食品烟酒', '衣着', '居住',
                   '生活用品及服务', '交通通信', '教育文化娱乐', '医疗保健', '其他用品及服务']
    df_final = df[df['年份'].isin(target_list)].copy()
    df_t = df_final.set_index('年份').T
    df_t = df_t[:-1]
    df_t.index = df_t.index.astype(int)
    #print(df_t)
    df_t.columns = ['Per capita disposable','Per capita consumption expenditure','Food、tobacco and alcohol','Clothing','Live','Daily necessities and services',
              'Traffic Communication','Education, Culture and Entertainment','Heath care',
              'Other supplies and services']
    return df_t

if __name__ == '__main__':
    df_urban = pd.read_excel(r"data/C0507_copy.xls")
    a = data_preprocessing(df_urban)
    print(a)

