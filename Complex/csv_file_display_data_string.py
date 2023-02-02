import pandas as pd
file = pd.read_csv('myfile.csv')
print(file.shape)
print(file.to_string)