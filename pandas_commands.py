import pandas as pd

## we will explore useful pandas commands on iris dataset

# =============================================================================
#  Basic Commands
# =============================================================================

# 1.Reading or Loading a datset into a variable 
dataset = pd.read_csv('Iris.csv');

#2.Displaying top 5 rows in dataset
dataset.head()
dataset.head(8) #Displays top 8 rows in the dataset

#3.Display bottom rows in the datset
dataset.tail()
dataset.tail(3) #Displays bottom 3 rows in the dataset
 
#4.Display count of rows and columns in the dataset
dataset.shape
dataset.shape[0] #Display rows count
dataset.shape[1] #Display columns count

#5.Display summary of the Dataset
dataset.info()

#6.Display statistical summary of all columns
dataset.describe() #statistical description of all numerical data columns
dataset.describe(include = ['O'])#statistical description of categorical columns
dataset.describe(include = 'all')#statistical description of all columns

#7.Display datatypes in datset
dataset.dtypes #Datatypes of all columns in the dataset 
dataset.Id.dtype #Datatype of particular column in the dataset
#      (or)
dataset['Id'].dtype

#8.no of uique rows in each column
dataset.nunique() #count of unique rows in all columns
dataset.Id.nunique() #count of unique rows of a particular column
#      (or)
dataset['Id'].nunique()

#9.select row with particular name or row no
dataset.loc[:,'Id'] #select all rows in column Id
dataset.iloc[:,1] #select all rows in column no 1

#10.find rows with duplicate data
sum(dataset.duplicated()) #count of rows with duplicated data
dataset[dataset.duplicated()] #displays the rows with duplicate data.

# 11. drop a column
dataset.drop('Id',axis = 1)

#12.count of unique values in the column
dataset['Species'].value_counts()

# =============================================================================
# Advanced Commands
# =============================================================================

#1. query command
dataset.query('SepalLengthCm < 5') #fetch the rows in dataset which vae speallength less than 5

length = 1.2
dataset.query('PetalLengthCm < @length') # fetch rows with lentgh lessthan 1.2

#2.Get dummie variables
dataset[['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']] = pd.get_dummies(dataset['Species'])

#3.group by
dataset.groupby('Species').count()

#4. order the datset
dataset.sort_values(by = 'Species', inplace = True)

#5.rename the column
dataset.rename(columns = {"Id":"id","Species":"species"},inplace = True) 

dataset.rename(str.lower,axis ='columns', inplace = True)

#6. merge datsets
df1 = dataset[['id','sepallengthcm','sepalwidthcm']]
df2 = dataset[['id','petallengthcm','petalwidthcm','species']]

new_data = pd.merge(df1,df2,on = 'id')
new_data.head()
#7. concat datsets
df1 = dataset.iloc[0:75,:]
df2 = dataset.iloc[75:150,:]

new_data = pd.concat([df1,df2])
new_data.head()

# =============================================================================
# Plotting with pandas 
# =============================================================================

#1. Scatter plot
dataset.plot.scatter('sepallengthcm','petallengthcm');

#2. Histogram plot
dataset['sepalwidthcm'].plot.hist();

#3. Bar plot
dataset['species'].value_counts().plot.bar();

#4. Horizontal bar plot
dataset['species'].value_counts().plot.barh();

#5. box plots
dataset[['sepallengthcm','petallengthcm','sepalwidthcm','petalwidthcm']].plot.box();

#6 pie plots
dataset['species'].value_counts().plot.pie(autopct='%.2f',figsize=(6,6));


