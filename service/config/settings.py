DS_TO_S_KEY_MAPPING = {
    'codi': 'codi',
    'data_fi': 'dataFi',
    'data_inici': 'dataInici',
    'data_fi_aproximada': 'dataFiAprox',
    'denominaci': 'denominacio',
    'descripcio': 'descripcio',
    'descripci': 'descripcio',
    'entrades': 'entrades',
    'horari': 'horari',
    'subt_tol': 'subtitol',
    'nom_organitzador': 'nomOrganitzador',
    'url_organitzador': 'urlOrganitzador',
    'tel_fon_organitzador': 'telefonOrganitzador',
    'email_organitzador': 'emailOrganitzador',
    'tags_mbits': 'tagsAmbits',
    'tags_categor_es': 'tagsCateg',
    'tags_altres_categor_es': 'tagsAltresCateg',
    'enlla_os': 'links',
    'documents': 'documents',
    'imatges': 'imatges',
    'v_deos': 'videos',
    'adre_a': 'adreca',
    'codi_postal': 'codiPostal',
    'comarca_i_municipi': 'comarcaIMunicipi',
    'email': 'email',
    'espai': 'espai',
    'latitud': 'latitud',
    'localitat': 'localitat',
    'longitud': 'longitud',
    'regi_o_pa_s': 'regioOPais',
    'tel_fon': 'telf',
    'url': 'URL',
    'imgapp': 'imgApp',
    'descripcio_html': 'descripcioHtml'
}

GEO_KEYS = ["regioOPais", "espai", "comarcaIMunicipi", "localitat", "adreca"]

REDUNDANT_KEYS = ['descripcioHtml']

PRIMARY_KEY = ['denominacio', 'ubicacio', 'dataInici', 'adreca', 'espai']

DATE_QUERY = '?$limit={}&$where=date_trunc_ymd(data_fi) >= date_trunc_ymd(\'{}\')'

