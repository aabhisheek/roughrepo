import numpy as np
import pandas as pd

# Data dictionary
dict1 = {
    "name": ['harry', 'rohan', 'skillf', 'shubh'],
    "marks": [92, 34, 24, 17],
    "city": ['rampur', 'kolkata', 'bareilly', 'antartica']
}

# Creating the DataFrame from the dictionary
df = pd.DataFrame(dict1)

# Print the DataFrame
print(df)

# Message
print("happy world")

# Save the DataFrame to a CSV file without the index column
df.to_csv('friends.csv', index=False)

# Uncomment the line below if you want to save with index included
df.to_csv('friends_index_true.csv', index=True)
