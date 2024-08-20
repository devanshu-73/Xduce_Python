import pandas as pd 
import numpy as np
 
# # Creating empty series 
ser = pd.Series()
print("Pandas Series: ", ser) 
 
# # simple array 
data = np.array(['d','e','v']) 
ser = pd.Series(data) 
# breakpoint() 
print("Pandas Series : ", ser)


