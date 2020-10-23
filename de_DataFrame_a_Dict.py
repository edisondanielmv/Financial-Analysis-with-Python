# importing pandas module 
import pandas as pd 

# reading csv file from url 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

# dropping null value columns to avoid errors 
data.dropna(inplace = True) 

# converting to dict 
data_dict = data.to_dict('series') 

# printing datatype of first keys value in dict 
print(type(data_dict['Name'])) 

# display 
print(data_dict) 



# importing pandas module 
import pandas as pd 

# reading csv file from url 
data = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv") 

# dropping null value columns to avoid errors 
data.dropna(inplace = True) 

# converting to dict 
data_dict = data.to_dict() 

# display 
print(data_dict) 
