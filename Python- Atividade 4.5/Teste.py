import xarray as xr
import numpy as np
import geopandas as gpd
from PIL import Image

import matplotlib.pyplot as plt
from cartopy import crs as ccrs, feature as cfeature
import matplotlib.gridspec as gridspec

estados = gpd.read_file('/mnt/c/INPE/Semana 30102023-01112023/Atividade3.2.MalhaComTodasUFsDoBrasil/BR_UF_2022.shp')

# print(estados.head())

# # # Extraindo as dimensões
dset = xr.open_dataset('/mnt/c/INPE/Semana 30102023-01112023/Atividade3.2.MalhaComTodasUFsDoBrasil/arquivoClimatologia_1991_2020.nc')
# print(dset)

# Extrai as coordenadas de latitude e longitude do arquivo de dados
lat = dset.lat.values
lon = dset.lon.values

# Seleciona a variável 'precip' do arquivo de dados
var = dset['precip']

## Este arquivo da NASA tem apenas o período de 1 mes.
# ds = xr.open_dataset('/mnt/c/INPE/Semana 30102023-01112023/Atividade3.2.MalhaComTodasUFsDoBrasil/GPCPMON_L3_202303_V3.2.nc4')


# # Defina o intervalo de datas desejado
# start_date = '2023-03-01'
# end_date = '2023-03-31'

# # Selecione a variável "sat_gauge_precip" e o intervalo de datas
# sat_gauge_precip = ds['sat_gauge_precip'].sel(time=slice(start_date, end_date))

# # Agora, sat_gauge_precip contém os dados de precipitação combinada de satélite e pluviômetros no intervalo de datas

# # Você pode plotar os dados para verificar se o recorte está correto
# sat_gauge_precip.plot()
# plt.title('Precipitação Combinada de Satélite e Pluviômetros (Março de 2023)')
# plt.show()

# Calcula a média anual dos dados de precipitação
clim = np.mean(var, axis=0)
# print(clim.coords)

# Calcula a média sazonal dos dados de precipitação
sclim = var.groupby('time.season').mean('time')

# print(sclim)
# print(sclim['season'].values)

#-------------------------------------------------------------------------#
# 3 - Plots

# ax = plt.axes(projection=ccrs.PlateCarree())
# ax.set_extent((-90.0,-30.0,-60.0,15.0))
# ax.coastlines(resolution='110m', color='black')
# ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black')

# gl=ax.gridlines(draw_labels=True)
# gl.xlines = False
# gl.ylines = False
# gl.right_labels = False
# gl.top_labels = False

# levels = np.linspace(0.0, 10.0, 11)
# cnplot = ax.contourf(clim.lon, clim.lat, clim, levels=levels, cmap='YlGnBu', extend='max')
# cbar = plt.colorbar(cnplot, orientation='horizontal', pad=0.07, shrink=0.6)
# cbar.set_label('precipitation (mm/day) \n 2022dez')
# ax.set_title(' (matplotlib)')

# estados.plot(ax =ax, color = 'none', edgecolor = 'black')

# plt.savefig('s1-matplot.png', dpi=300)

# plt.show()

def create_plot(ax, nrow, ncol, data, tlon, season=''):
    ax = plt.subplot(gs[nrow, ncol], projection=ccrs.PlateCarree())
    ax.set_extent((-90.0,-30.0,-60.0,15.0))
    ax.coastlines(resolution='110m', color='black')
    ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='black')

    gl=ax.gridlines(draw_labels=True)
    gl.xlines = False
    gl.ylines = False
    gl.right_labels = False
    gl.top_labels = False

    cnplot = ax.contourf(data.lon, data.lat, data.sel(season=season), levels=levels, cmap='YlGnBu', extend='max')
    ax.text(tlon,-55,season,bbox=dict(facecolor='white',alpha=0.7))

    levels = np.linspace(0.0, 10.0, 11)

    fig = plt.figure()

    gs = fig.add_gridspec(nrows=2, ncols=2, hspace=0.12, wspace=0.00)

    create_plot(ax, 0, 0, sclim, -44, season='DJF')
    create_plot(ax, 0, 1, sclim, -48.5, season='MAM')
    create_plot(ax, 1, 0, sclim, -41.5, season='JJA')
    create_plot(ax, 1, 1, sclim, -47, season='SON')

    plt.subplots_adjust(bottom=0.2, top=0.95)
    plt.figtext(0.6, 0.97, '(matplotlib)', ha='right', fontsize=12)

    cax = plt.axes([0.2, 0.065, 0.6, 0.069]) # left, bottom, right, top
    plt.colorbar(cnplot, cax=cax, orientation='horizontal', pad=0.4)

    plt.savefig('s2-matplot.png', dpi=300)
    plt.show()

# # Abre as imagens salvas
# img = Image.open("s1-matplot.png")
# img1 = Image.open("s2-matplot.png")

# # Redimensiona as imagens
# img_size = img.resize((670, 1024))
# img1_size = img1.resize((670, 1024))

# # Cria uma nova imagem branca
# img2 = Image.new("RGB", (1340, 1024), "white")

# # Cola as imagens na nova imagem
# img2.paste(img_size, (0, 0))
# img2.paste(img1_size, (670, 0))

# # Salva a nova imagem
# img2.save('s1-medias-anual-sazonal.png')