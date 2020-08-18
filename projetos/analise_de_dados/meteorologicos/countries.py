from pygal_maps_world import i18n

def get_country(country):
    for chave, valor in i18n.COUNTRIES.items():
        if valor == country:
            return chave