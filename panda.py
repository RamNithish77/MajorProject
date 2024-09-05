import pandas as pd

#-------------------------Reading File---------------0
df=pd.read_csv("data.csv")
dt = pd.DataFrame(df)
# print(dt)

#---------------Data------------------------
# print(dt.head(5))
# print(dt[:10])
# print(dt[["Country Name","Country Code"]])
# for i in dt.iterrows():
#     print(i)

#-------------------loc data----------------------
# print(dt.loc[0])
# print(dt.loc[1,["Country Name","Country Code"]])
# # print(dt.loc[0:9])
# print(dt.loc[0:9,["Country Name","Country Code"]])

#--------------iloc data-----------------------
# print(dt.iloc[:8])
# print(dt.iloc[1,[0,1]])
# print(dt.iloc[:,[0,2]])
# print(dt.iloc[0:5,1])

#-----------------Sorting data----------------------
# print(dt.sort_values("Name"))

#----------------Manupulating Data------------------
# dt["height"]=dt["Mobile"]+dt["FatherMo"]
# dt["height"]=dt["Mobile"]>9000000000
# dt=dt.drop(columns=["Photo","height"])

#-----------------Dulicate data---------------------
# print(dt.duplicated())


#----------------------data filtering and Conditional Changes----------------
print(dt.loc[dt["Name"].str.startswith("S")])
#---------------dictionary ti pandas-------------------
# di={
#     "Name":["Naruto","luffy","Goku","ichigo"],
#     "power":["5k","4.7k","199k","45k"],
#     "Wife":["Hinata","Boa hancock","chichi","Orihime"],
#     "Age":[16,19,38,15]
# }
# dt=pd.DataFrame(di)
# print(dt)