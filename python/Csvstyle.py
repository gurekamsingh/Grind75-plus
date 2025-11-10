# You are given CSV style data:
# name,region,sales
# mark,ca,100
# alicia,us,200
# mark,ca,400
# james,us,150
# alicia,us,50

# Return total sales per region in dict form.
def totalsales(rows):
    result = {}
    for i in range(1, len(rows)):
        name , region , sales = i.split(",")
        sales = int(sales)
        result[region] = result.get(region, 0) + sales
    return result

# print(totalsales(rows))

# pandas version

import pandas as pd

df = pd.read_csv("file.csv")
result = df.groupby("region")["sales"].sum().to_dict()
print(result)