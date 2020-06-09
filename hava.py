#Kütüphanelerin yüklenmesi
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder

#Verilerin okutulması
df = pd.read_csv("tr.csv",encoding='iso-8859-9')

#Veri tiplerinin dönüştürülmesi
df["Tarih"] = pd.to_datetime(df["Tarih"])

#Grafiklerin oluşturulması
df[['PM10', 'Şehir']].groupby(['Şehir']).median().sort_values("PM10", ascending = False).plot.bar()
df[['SO2', 'Şehir']].groupby(['Şehir']).median().sort_values("SO2", ascending = False).plot.bar()
df[['CO', 'Şehir']].groupby(['Şehir']).median().sort_values("CO", ascending = False).plot.bar()
df[['NO2', 'Şehir']].groupby(['Şehir']).median().sort_values("NO2", ascending = False).plot.bar()
df[['NOX', 'Şehir']].groupby(['Şehir']).median().sort_values("NOX", ascending = False).plot.bar()
df[['NO', 'Şehir']].groupby(['Şehir']).median().sort_values("NO", ascending = False).plot.bar()
df[['O3', 'Şehir']].groupby(['Şehir']).median().sort_values("O3", ascending = False).plot.bar()

#Tüm sütunların dağılım grafikleri
sns.set()
cols = ["PM10", 'SO2', 'CO', 'NO2', 'NOX',"NO","O3"]
sns.pairplot(df[cols], size = 2.5)
plt.show()

#Korelasyon matrisi
corrmat = df.corr()
f, ax = plt.subplots(figsize = (15, 10))
sns.heatmap(corrmat, vmax = 1, square = True, annot = True)

#Ay kolonu oluşturma
df['Tarih'] = pd.to_datetime(df['Tarih'], format = '%M/%d/%y')
df['Ay'] = df['Tarih'].dt.month # year
df['Ay'] = df['Ay'].fillna(0.0).astype(int)
df = df[(df['Ay']>0)]

#Şehirler baz alınarak değerlere göre oluşturulan ısı haritaları
f, ax = plt.subplots(figsize = (10,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('PM10'))
sns.heatmap(df.pivot_table('PM10', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("pm10_heatmap.png",bbox_inches="tight")

f, ax = plt.subplots(figsize = (10,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('SO2'))
sns.heatmap(df.pivot_table('SO2', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("so2_heatmap.png",bbox_inches="tight")

f, ax = plt.subplots(figsize = (20,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('CO'))
sns.heatmap(df.pivot_table('CO', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("co_heatmap.png",bbox_inches="tight")

f, ax = plt.subplots(figsize = (10,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('NO2'))
sns.heatmap(df.pivot_table('NO2', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("no2_heatmap.png",bbox_inches="tight")

f, ax = plt.subplots(figsize = (10,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('NOX'))
sns.heatmap(df.pivot_table('NOX', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("nox_heatmap.png",bbox_inches="tight")

f, ax = plt.subplots(figsize = (10,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('NO'))
sns.heatmap(df.pivot_table('NO', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("no_heatmap.png",bbox_inches="tight")

f, ax = plt.subplots(figsize = (10,50))
ax.set_title('{} Şehir Ve Aya Göre'.format('O3'))
sns.heatmap(df.pivot_table('O3', index = 'Şehir',
                columns = ['Ay'], aggfunc = 'median', margins=True),
                annot = True, cmap = 'YlGnBu', linewidths = 1, ax = ax, cbar_kws = {'label': 'Aylık Alınan Ortalama'})
plt.savefig("o3_heatmap.png",bbox_inches="tight")