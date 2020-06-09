#Gerekli Kütüphanelerin yüklenmesi
import pandas as pd
import matplotlib.pyplot as plt
import fbprophet

#verilerin okutulması
df1 = pd.read_csv('tokat.csv')
 
#Kullanılacak kolonların seçilmesi
df = df1[['Tarih','PM10']]
 
#Prophet için ds (Tarih) and y (Değer) kolonlarının seçilmesi
df = df.rename(columns={'Tarih': 'ds', 'PM10': 'y'})
 
#Tarih formatının düzenlenmesi
df['ds'] = pd.to_datetime(df['ds'], format='%d %m %Y')

#Gerçek değerlerin görsellerştirilmesi
fig = plt.figure(figsize=(40,10))
plt.plot(df['ds'], df['y'],'r') # kırmızı renk
plt.title('Tarih ve PM10 Değişimi')
plt.ylabel('PM10')
plt.show()
plt.savefig("Fb_01.png",bbox_inches="tight")

#prophet modelinin hazırlanması ve modelin fit edilmesi
df_prophet = fbprophet.Prophet(changepoint_prior_scale=0.05)    #trend esnekliğinin ayarlanması varsayılan değeri(0.05) kullandım
df_prophet.fit(df)
 
#Tahmin süresinin belirlenmesi t_s=>tahmin süresi
t_s=365
df_forecast = df_prophet.make_future_dataframe(periods= t_s, freq='D')
 
#Tahminlerin gerçekleştirilmesi
df_forecast = df_prophet.predict(df_forecast)
 
#Tahmin sonuçlarının görselleştirilmesi
df_prophet.plot(df_forecast, xlabel = 'Tarih', ylabel = 'PM10 Değeri',figsize=(40,10))
plt.title(f'{t_s} günlük PM10 Tahmin')
plt.title('PM10 Değişimi')
plt.ylabel('PM10')
plt.show()
plt.savefig("Fb_02.png",bbox_inches="tight")

#Tahmin sonuçlarına komponentlerin görselleştirilmesi
df_prophet.plot_components(df_forecast,figsize=(20,25))
plt.show()
plt.savefig("Fb_03.png",bbox_inches="tight")