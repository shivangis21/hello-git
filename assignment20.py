import pandas as pd
#q1
data = {'Name':['Sia', 'Sumit'],'Age':[18,24],'mail id':['sia@gmail.com','sumit@gmail.com'],'phone no':['6958398','875450938']}
df = pd.DataFrame(data)
df.loc[2]=['Pia',26,'pia@gmail.com','fjdhfjd']
print(df)

#q2
df=pd.read_csv('weather.csv')
print(df)
print(df.head(5))
print(df.head(10))
print(df['MinTemp'].describe())
print(df['MaxTemp'].describe())
print(df.tail(5))
finaldata=[df['MinTemp'].sum(),
df['MinTemp'].mean(),
df['MinTemp'].median(),
df['MinTemp'].nunique(),
df['MinTemp'].max(),
df['MinTemp'].min()]
print(finaldata)