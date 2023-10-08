import pandas as pd
import matplotlib.pyplot as plt

weather = pd.read_csv("local_weather.csv", index_col="DATE")

# print(weather)

# print(wheather.apply(pd.isnull).sum()/wheather.shape[0])

core_weather = weather[["PRCP", "SNOW", "SNWD", "TMAX", "TMIN"]].copy()
core_weather.columns = ["precip", "snow", "snow_depth", "temp_max", "temp_min"]

## calcula a proporção de valores nulos em cada coluna do DataFrame
# print(core_weather.apply(pd.isnull).sum()/core_weather.shape[0])

# print(core_weather["snow"].value_counts())

# print(core_weather["snow_depth"].value_counts())

#Aqui eu removo as colunas snow e snow_depth
del core_weather["snow"]
del core_weather["snow_depth"]

#Ve todo conteudo dentro dentro da tabela 
# print(core_weather)

##aqui eu seleciono apenas os campos nulos
#print(core_weather[pd.isnull(core_weather["precip"])])

##aqui eu vejo os dados de dois dias diferentes
# print(core_weather.loc["1983-10-20":"1983-11-05"])

##pude observar que a maioria dos dias n tem precipitação e outros tem muita 
#print(core_weather["precip"].value_counts())

##Aqui eu passo valor 0 para os valores nulos na coluna precip
# core_weather["precip"] = core_weather["precip"].fillna(0)
# print(core_weather["precip"])
 

##Para ver a coluna e analisar quais dados são nulos
# print(core_weather[pd.isnull(core_weather["temp_max"])])
# print(core_weather[pd.isnull(core_weather["temp_min"])])

# core_weather = core_weather.fillna(method="ffill")

## Agora ele me retorna as colunas (temp_max e temp_min) sem valores nulos
core_weather.apply(pd.isnull).sum()/core_weather.shape[0]


## Nesse bloco eu vejo alguns dados do arquivo
# print(core_weather.dtypes)
core_weather.index = pd.to_datetime(core_weather.index) 
# print(core_weather.index)
# print(core_weather.index.year)

## Somente para confirmar se há algum dado com valor muito alto
# print(core_weather.apply(lambda x: (x == 9999).sum()))

## Demonstração da tela
# core_weather[["temp_max", "temp_min"]].plot()
# plt.show()

## Mostra a quantidade de dias que pegou durante cada ano ex: ano:1960 dias:366
# print(core_weather.index.year.value_counts().sort_index())


# ## Demonstração da tela
# core_weather["precip"].plot()                   '''Para as funções que chamam index.year funcionarem é necessario que descomente a linha 53'''       
# plt.show()


# core_weather.groupby(core_weather.index.year).apply(lambda x: x["precip"].sum()).plot()
# plt.show()

core_weather ["target"] = core_weather.shift(-1)["temp_max"]

print(core_weather["temp_min", "target"])
