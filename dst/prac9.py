import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel(r'C:\Users\comp\Desktop\html css course\dst\dstdataset.xlsx')

type_counts = df['Type'].value_counts()

colors = ['skyblue', 'orange', 'lightgreen', 'pink', 'purple']

plt.figure(figsize=(7, 5))
bars = plt.bar(type_counts.index, type_counts.values, color=colors[:len(type_counts)], edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 100, f'{yval:,}', ha='center', va='bottom')

plt.title('Product Type Distribution')
plt.xlabel('Product Type')
plt.ylabel('Count')

plt.tight_layout()
plt.show()