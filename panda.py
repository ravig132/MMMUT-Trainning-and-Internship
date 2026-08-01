import pandas as pd 

df = {
    'cars':["Thar","Scorpio","Bolero"],
    'type':["Diesel","Petrol","Diesel"]
}

myVar = pd.DataFrame(df)
print(myVar)