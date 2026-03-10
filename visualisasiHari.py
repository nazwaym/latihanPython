# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# membaca dataset
data = pd.read_csv("tips.csv")

# %%
# menghitung jumlah data berdasarkan hari
day_count = data['day'].value_counts()

# %%
# membuat bar chart
plt.figure(figsize=(8,5))

plt.bar(day_count.index, day_count.values)

# %%
# menambahkan judul dan label
plt.title("Jumlah Pelanggan yang Memberikan Tips Berdasarkan Hari")
plt.xlabel("Hari")
plt.ylabel("Jumlah Pelanggan")

# %%
# menampilkan grafik
plt.show()