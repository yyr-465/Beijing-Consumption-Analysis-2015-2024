def Engel_coefficient(df):
    df['E_coefficient'] = df['Food、tobacco and alcohol'] / df['Per capita consumption expenditure']
    print("In the calculation of Engel's coeffient")
    year = int(input('To view the data,press enter the year:\n'))
    if year not in df.index:
        print("Input error\n"
              "Please enter the year in 2015-2024\n"
              'Please rerun the function')
        return 0
    else:
        print(df['E_coefficient'][year])
        return df['E_coefficient'][year]
def POSC(df1,df2):
    df1['POSC'] = (df1['Traffic Communication']
                  + df1['Education, Culture and Entertainment'] + df1['Heath care']) / df1[
                     'Per capita consumption expenditure']
    df2['POSC'] = (df2['Traffic Communication']
                  + df2['Education, Culture and Entertainment'] + df2['Heath care']) / df2[
                     'Per capita consumption expenditure']
    return df1['POSC'], df2['POSC']
def proportion_of_service_consumption_for_year(df):
    print("In the calculation of proportion of service consumption")
    year = int(input('To view the data,press enter the year:\n'))
    if year not in df.index:
        print("Input error\n"
              "Please enter the year in 2015-2024\n"
              'Please rerun the function')
        return 0
    else:
        print(df['POSC'][year])
        return df['POSC'][year]

