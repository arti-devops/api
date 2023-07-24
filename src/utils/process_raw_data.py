import pandas as pd

def filter_raw_log_data(rw, filter) -> pd.DataFrame: 
    """Reads csv file"""

    # Read Data Sources
    df_rw = pd.read_csv(rw, encoding="latin-1")  
    df_filter = pd.read_csv(filter, encoding="latin-1") 

    noms_a = df_filter["noms"].tolist()  
    matricules_a = df_filter["MATRICULE"].tolist()  

    df_rw = df_rw[df_rw["Name"].isin(noms_a)]  

    df_rw["Matricule"] = df_rw["Name"].map(dict(zip(noms_a, matricules_a)))

    # Enregistrer le résultat dans un nouveau fichier Excel
    #df_rw.to_csv("fichier_b_filtre.csv", index=False) 
    return df_rw

def filter_raw_log_data_remake(rw, filter): 
    """Reads csv file"""
    colnames = ["matricule","base","rh"]
    # Read Data Sources
    df_rw = pd.read_csv(rw, encoding="latin-1")  
    df_rw.rename(columns={"Name":"base"}, inplace=True)
    df_filter = pd.read_csv(filter, encoding="latin-1")
    df_filter.columns = colnames
    
    noms_a = df_filter["base"].tolist()  
    matricules_a = df_filter["matricule"].tolist()  

    df_rw = df_rw[df_rw["base"].isin(noms_a)]  

    df_rw["matricule"] = df_rw["base"].map(dict(zip(noms_a, matricules_a)))

    return [df_rw, df_filter]