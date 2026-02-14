
from geobr import read_state

from geobr import read_municipality

# Municípios do Pará (UF = "PA"); escolha o ano disponível (ex.: 2020)
mun_pa = read_municipality(code_muni="PA", year=2020)  # GeoDataFrame

# Exportar como shapefile
mun_pa.to_file("municipios_PA.shp")  # cria .shp + arquivos auxiliares
