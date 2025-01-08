"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""
import pandas as pd
import glob
import os

def load_data(path):
    """
    Carga un archivo csv en un DataFrame de pandas.
    """
    return pd.read_csv(path, sep=";", index_col=0)

def initialize_citizen_commune(df):
    """
    Inicializa la columna 'comuna_ciudadano' como entero.
    """
    df["comuna_ciudadano"] = df["comuna_ciudadano"].astype(int)
    return df

def initialize_loan_amount(df):
    """
    Inicializa la columna 'monto_credito' como float.
    """
    df["monto_del_credito"] = df["monto_del_credito"].str.strip().str.strip("$")
    df["monto_del_credito"] = df["monto_del_credito"].str.replace(".00", "").str.replace(",", "")
    df["monto_del_credito"] = df["monto_del_credito"].astype(int)
    return df

def clean_sex(df):
    """
    Limpia los espacios y capitalización de la columna 'sexo'.
    """
    df['sexo'] = df['sexo'].str.strip().str.lower()
    return df

def clean_type_of_entrepreneurship(df):
    """
    Limpia los espacios y capitalización de la columna 'tipo_de_emprendimiento'.
    """
    df['tipo_de_emprendimiento'] = df['tipo_de_emprendimiento'].str.strip().str.lower()
    return df

def clean_line_of_credit(df):
    """
    Limpia los espacios y capitalización de la columna 'línea_credito'.
    """
    df['línea_credito'] = df['línea_credito'].str.strip().str.lower()
    df["línea_credito"] = df["línea_credito"].str.replace(" ", "")
    df["línea_credito"] = df["línea_credito"].str.translate(str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))
    return df

def clean_date_of_benefit(df):
    """
    Limpia los espacios y capitalización de la columna 'fecha_de_beneficio'.
    """ 
    df['fecha_de_beneficio'] = pd.to_datetime(df['fecha_de_beneficio'], dayfirst=True, format='mixed')
    return df

def clean_idea_of_business(df):
    """
    Limpia los espacios y capitalización de la columna 'idea_negocio'.
    """
    df['idea_negocio'] = df['idea_negocio'].str.strip().str.lower()
    df["idea_negocio"] = df["idea_negocio"].str.replace("á", "a").str.replace("é", "e").str.replace("í", "i").str.replace("ó", "o").str.replace("ú", "u")
    df["idea_negocio"] = df["idea_negocio"].str.replace(" ", "")
    df["idea_negocio"] = df["idea_negocio"].str.translate(str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))
    return df

def clean_neighborhood(df):
    """
    Limpia los espacios y capitalización de la columna 'barrio'.
    """
    df['barrio'] = df['barrio'].str.lower()
    df["barrio"] = df["barrio"].str.replace("_", " ").str.replace("-", " ")
    return df

def clean_missing_data(df):
    """
    Elimina registros con datos faltantes de un DataFrame de pandas.
    """
    return df.dropna()

def clean_duplicates(df):
    """
    Elimina registros duplicados de un DataFrame de pandas.
    """
    df.drop_duplicates(inplace=True)
    return df

def save_data(df, path):
    """
    Guarda un DataFrame de pandas en un archivo csv.
    """
    df.to_csv(path, index=False, sep=";")

def pregunta_01():
    """
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"

    """
    if os.path.exists("files/output/"):
        files = glob.glob(os.path.join("files/output/", "*"))
        for f in files:
            os.remove(f)
    else:
        os.makedirs("files/output/")

    df = load_data("files/input/solicitudes_de_credito.csv")
    df = initialize_citizen_commune(df)
    df = initialize_loan_amount(df)
    df = clean_sex(df)
    df = clean_type_of_entrepreneurship(df)
    df = clean_line_of_credit(df)
    df = clean_date_of_benefit(df)
    df = clean_idea_of_business(df)
    df = clean_neighborhood(df)
    df = clean_missing_data(df)
    df = clean_duplicates(df)
    print(df)
    save_data(df, "files/output/solicitudes_de_credito.csv")

if __name__ == "__main__":
    pregunta_01()
