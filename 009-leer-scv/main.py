# import pandas as pd


# dicVanguardParidad = {}

# df = pd.read_csv('tabla.csv', sep=',', encoding='utf-8')

# for i in range(len(df)):
#     # print(df.iloc[i,0] , ' ' , df.iloc[i,1], ' ' , df.iloc[i,2], ' ' , df.iloc[i,3])
#     dicVanguardParidad[df.iloc[i,1]] = df.iloc[i,2]

# print(dicVanguardParidad[90102])

dicVanguardParidad = {
"102":"CMED",
"106":"OTROS",
"109":"OTROS",
"207":"OTROS",
"302":"OTROS",
"303":"OTROS",
"403":"OTROS",
"602":"CC3",
"902":"CC3",
"50101":"OTROS",
"501":"OTROS",
"50201":"OTROS",
"90103":"OTROS",
"20502":"OTROS",
"90102":"OTROS"
}

print(dicVanguardParidad[90102])


