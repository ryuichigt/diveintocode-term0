import pandas as pd
import numpy as np

a = pd.DataFrame([[1,2,3],[1,4,2],[1,1,3],[2,3,3]])

a.columns = ["day_no","class","score1"]

b = pd.DataFrame([[3,4,5,2,3]])

b.columns = ["day_no","class","score15","score25","aa"]

c = pd.merge(a, b, on = "day_no", how = "left")

print(c)
