#script by Tara Zakizadeh to calculate dipole moment value 
# May 8,2025 _ Tabriz university of Technologe
import pandas as pd
import math as mt

In=r"C:\Users\Ahoura\Downloads\my_code\new_out_dipole.txt"
out= r"C:\Users\Ahoura\Downloads\my_code\new_out_dipole_1.txt"
A=[]
x= pd.read_csv(In , sep=r"\s*,\s*", engine="python", header=None)
x = x.apply(pd.to_numeric, errors='coerce')

for i in range(len(x.dropna())):
   a,b,c=x.iloc[i]
   y=mt.sqrt(mt.pow(a,2)+mt.pow(b ,2)+mt.pow(c, 2))
   y = round(y, 15)
   A.append(y)
pd.DataFrame(A).to_csv(out , index=False, header= False)
print(f'dipole moment value saved')


