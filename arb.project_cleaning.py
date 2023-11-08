import pandas as pd
df = pd.read_excel('arb.project_data.xlsx', sheet_name='sheet -> I')
print(df)

for i in range (0,len(df["rooms"])-1):
    if df["rooms"][i] == " ":
        df["rooms"][i] = df["bedrooms"][i]
df["rooms"]=df["rooms"].astype(int)

for x in df.index:
  if df.loc[x, "price"] < 10000 or df.loc[x, "price_m2"] == 0 or df.loc[x, "price_m2"] > 10000:
    df.drop(x, inplace = True)
df.to_excel('arb.project_clean_data.xlsx',sheet_name='sheet -> I', index=False)
print(df.info())


