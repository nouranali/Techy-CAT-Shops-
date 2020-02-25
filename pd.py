import pandas as pd

#pandas is a python pckage for data manipulation
# has 2 data structures Series and data frame

#DataFrames a table 
test=pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})

#series sequence of data values >> list
S=pd.Series(["A","B","C","D"])
#reading data files
#pandas can read many types of data files like
# csvs,excel,flatfiles,tables,json,sql...
#CSVS most common

df=pd.read_csv("IRIS.csv")
#print first&last 5 rows
print(df.head())
print(df.tail())
print(df.head(12))
print(df.shape)

#indexing 
print(df.columns)
print(df.species)
#or
print(df['species'])
#index_based selection iloc:
# selection based on numerical position
#select 3rd row
print(df.iloc[2])
#all rows, first column , we can manipulate the slicing methods
print(df.iloc[:,0])
# label based selection loc
df.loc[1,'species']
#we can change the index of the df by
#df.set_index(column_name)

#conditional selection
res=df.species=='Iris-virginica'
print(res)

print(df.loc[df.species=='Iris-virginica'])

print(df.loc[(df.species=='Iris-virginica')& (df.petal_length<=6.0)])

print(df.loc[df.species.isin(["Iris-virginica","Iris-setosa"])])

# getting summaries about dataframe

#describe: description of a column... mean,count...
#string data is difference from numeric data
df.species.describe()

df.petal_length.describe()

df.sepal_width.mean()
df.sepal_width.unique()
df.sepal_width.value_counts()

#grouping

df.groupby('sepal_length').sepal_length.count()
df.groupby(['species']).petal_length.agg([max,min])
#sorting
#we can sort with multiple values or 1 
df.sort_values(by='sepal_length',ascending=False)
df.sort_index()

#with pandas we can change the datatypes of columns by astype()

#missing data nan,null
df[pd.isnull(df.sepal_width)]
df.sepal_width.fillna("NaN")
# we can replace values
df.petal_length.replace(2.9,3)

# rename columns
df.rename(columns={'species':'types'})
#join or combine data with concat and pass a list of of datsets