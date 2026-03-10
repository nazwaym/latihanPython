import pandas as pd

# membaca dataset
data = pd.read_csv("tips.csv")

# menampilkan 10 baris pertama
print(data.head(10))