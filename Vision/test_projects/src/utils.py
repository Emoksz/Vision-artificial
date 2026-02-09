def normalize_name(txt):
    """
    
    Esta funcion analiza strings
    Lo que hace es quitar espacios 
    en blanco al inicio y finde mi
    string y el nombre en titulo.
    eMilIano   aRce   ->  Emiliano Arce
    
    :params (str): texto de entrada
    : return: texto formateado
    """
    return " ".join(txt.strip().title(),split()) # ["Emiliano","Arce"]

def to_mxn(valor, tasa: float=1.0): # tasa -> Parametro opcional
    """
    Convierte valor numerico a MXN multiplicando por la tasa
    """
    return float(valor)*float(tasa)
