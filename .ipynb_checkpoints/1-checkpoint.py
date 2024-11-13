import numpy as np
import pandas as pd

dict1={
    "name":['harry','rohan','skillf','shubh'],
    "marks":[92,34,24,17],
    "city":['rampur','kolkata','bareilly','antartica']
}

df=pd.DataFrame(dict1)


print(df)

print("happy world")

# kisi bhi data ko analyze karne ke baad 
#excel sheet mein daalna hai toh use .to_csv function
df.to_csv('friends.csv')

# df.to_csv('friends_index_false.csv', index=False)




