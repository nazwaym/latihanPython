# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
# membaca dataset
data = pd.read_csv("tips.csv")

# %%
# menambahkan judul
plt.title("Scatter Plot")

# %%
# label sumbu
plt.xlabel('Day')
plt.ylabel('Tip')

# %%
# membuat scatter plot
plt.scatter(data['day'], data['tip'])

# %%
plt.show()