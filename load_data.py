"""
Eu gostao de usar o speasy para carregar dados de magntometro da Cassini (E outras sondas tbm).
https://speasy.readthedocs.io/en/latest/examples/index.html

https://github.com/SciQLop/speasy

Tem varios exemplos na documentação.


Para carregar os dados, uso o seguinte cdigo:

O Speasy  possui uma estrutura de inventrio de dados, que pode ser acessada atravs do comando:
import speasy as spz
spz.inventories.tree    

Ele usa diversas fontes de dados, como a AMDA (CDPP), CDAWeb (NASA) e VESPA (CDPP).

Uma maneira de visualizar os dados rápida pode ser tambem com https://amda.irap.omp.eu/desktop.php
É uma ferramenta web que permite carregar e visualizar dados de diversas missões espaciais, incluindo a Cassini.

"""

#%%
import speasy as spz
from speasy.core.inventory import *
import matplotlib.pyplot as plt
import pandas as pd
# %%
amda_tree = spz.inventories.tree.amda
# %%
product = [amda_tree.Parameters.Cassini.MAG.orbit_saturn.cass_mag_orb1]
# %%
# Carregando os dados do magntometro da Cassini resolução de 1 segundo
# Perodo de 1 dia em setembro de 2012
# 14 de setembro de 2012 10:31 a 15 de setembro de 2012 10:31
time_interval = [[f"2012-09-14T10:31",f"2012-09-15T10:31"]]
mag = spz.get_data(product,time_interval)


"""
Um problema é encontrar as variaveis que voc quer. Pra isso eu uso o sistema do 
repositori AMDA https://amda.irap.omp.eu/desktop.php. Pode acessar com o acesso publico mesmo
e ver quais variaveis estao disponiveis. No caso do magntometro da Cassini, as variaveis
"""

# %%
# Visualizando os dados
mag[0][0]['b_ksm'].plot()
#%%
plt.plot(mag[0][0]['b_ksm'].values)
# %%
