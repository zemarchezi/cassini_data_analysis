# Análise de Dados da Sonda Cassini com Speasy

Este repositório mostra como carregar e visualizar dados do magnetômetro (e também de elétrons) da sonda Cassini usando a biblioteca [Speasy](https://speasy.readthedocs.io/en/latest/). O objetivo é ser um guia didático para quem está começando a trabalhar com dados de missões espaciais.

## O que é o Speasy?

O [Speasy](https://github.com/SciQLop/speasy) é uma biblioteca Python que facilita o acesso a dados de diversas missões espaciais, incluindo a Cassini. Ele integra diferentes fontes de dados, como:

- [AMDA (CDPP)](https://amda.irap.omp.eu/)
- [CDAWeb (NASA)](https://cdaweb.gsfc.nasa.gov/)
- [VESPA (CDPP)](https://vespa.obspm.fr/)

A documentação oficial traz vários exemplos:  
https://speasy.readthedocs.io/en/latest/examples/index.html

## Instalação

Recomenda-se instalar o Speasy via pip:

```bash
pip install speasy
```

Você também vai precisar do `matplotlib` e `pandas` para visualização e manipulação dos dados:

```bash
pip install matplotlib pandas
```

## Carregando Dados do Magnetômetro da Cassini

O Speasy possui um inventário de dados que pode ser explorado para encontrar os produtos disponíveis:

```python
import speasy as spz

# Visualizar o inventário de dados
print(spz.inventories.tree)
```

Para acessar os dados do magnetômetro da Cassini, por exemplo:

```python
import speasy as spz
from speasy.core.inventory import *
import matplotlib.pyplot as plt

# Acessando o inventário AMDA
amda_tree = spz.inventories.tree.amda

# Selecionando o produto do magnetômetro da Cassini
product = [amda_tree.Parameters.Cassini.MAG.orbit_saturn.cass_mag_orb1]

# Definindo o intervalo de tempo (exemplo: 1 dia em setembro de 2012)
time_interval = [["2012-09-14T10:31", "2012-09-15T10:31"]]

# Baixando os dados
mag = spz.get_data(product, time_interval)
```

## Visualizando os Dados

Você pode visualizar rapidamente os dados usando o próprio pandas ou matplotlib:

```python
# Usando pandas para plotar diretamente
mag[0][0]['b_ksm'].plot()

# Ou usando matplotlib
plt.plot(mag[0][0]['b_ksm'].values)
plt.title('Componente B_KSM do Magnetômetro da Cassini')
plt.xlabel('Tempo')
plt.ylabel('B_KSM (nT)')
plt.show()
```

## Como Encontrar as Variáveis Disponíveis

Um dos desafios é descobrir quais variáveis estão disponíveis para cada missão. Para isso, recomendo usar o [AMDA Desktop](https://amda.irap.omp.eu/desktop.php), que permite explorar os produtos e variáveis de forma visual, sem necessidade de login.

Por exemplo, para o magnetômetro da Cassini, você pode procurar por variáveis como `b_ksm`, `b_rtp`, etc.

## Outras Dicas e Ferramentas

- O [AMDA Desktop](https://amda.irap.omp.eu/desktop.php) é uma ótima ferramenta web para explorar e visualizar dados de várias missões espaciais, incluindo a Cassini.
- O repositório [SciQLop](https://github.com/SciQLop/SciQLop) também traz exemplos e ferramentas para análise de dados espaciais.

## Exemplos e Documentação

- [Exemplos na documentação do Speasy](https://speasy.readthedocs.io/en/latest/examples/index.html)
- [AMDA Desktop](https://amda.irap.omp.eu/desktop.php)
- [Repositório SciQLop](https://github.com/SciQLop/SciQLop)

---

## Resumo

1. Instale o Speasy e dependências.
2. Explore o inventário de dados para encontrar o produto desejado.
3. Carregue os dados usando `spz.get_data`.
4. Visualize os dados com pandas ou matplotlib.
5. Use o AMDA Desktop para descobrir variáveis e explorar os dados.

Se tiver dúvidas ou quiser expandir para outros instrumentos (como elétrons), basta adaptar o caminho do inventário para o produto desejado.

---
