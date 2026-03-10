# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# membaca dataset
data = pd.read_csv("tips.csv")

# %%
# menghitung jumlah laki-laki dan perempuan
gender_count = data['sex'].value_counts()

# %%
# membuat pie chart persentase
plt.figure(figsize=(6,6))
plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title("Persentase Laki-laki dan Perempuan yang Memberikan Tips")
plt.show()