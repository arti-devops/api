import pandas as pd
from datetime import datetime

def convert_and_save_data(input_rw, input_filter):
    """Reads csv file"""
    colnames = ["matricule","base","rh"]
    # Read Data Sources
    df_rw = pd.read_csv(input_rw, encoding="latin-1")  
    df_rw.rename(columns={"Name":"base"}, inplace=True)
    df_filter = pd.read_csv(input_filter, encoding="latin-1")
    df_filter.columns = colnames
    
    noms_a = df_filter["base"].tolist()  
    matricules_a = df_filter["matricule"].tolist()  

    df_rw = df_rw[df_rw["base"].isin(noms_a)]  

    df_rw["matricule"] = df_rw["base"].map(dict(zip(noms_a, matricules_a)))

    return [df_rw, df_filter]

# Appel de la fonction en utilisant les fichiers d'entrée et de sortie

def process_attendance_data(original_file, personnel_file):
    # Charger le fichier Excel
    #df = pd.read_excel(original_file)
    df = original_file

    # Charger le fichier Excel contenant les matricules
    #df_matricules = pd.read_excel(personnel_file)
    df_matricules = personnel_file

    matricule_mapping = df_matricules.set_index('base')['matricule'].to_dict()
    mom_mapping = df_matricules.set_index('base')['rh'].to_dict()

    # Convertir la colonne 'Time' en format de date/heure
    df['Time'] = pd.to_datetime(df['Time'], format='%Y-%m-%d %H:%M:%S')

    # Parcourir chaque date unique
    dates = df['Time'].dt.date.unique()

    # Créer une liste pour stocker les données
    data = []

    # Parcourir chaque date
    for date in dates:
        # Filtrer les données pour la date donnée
        date_data = df[df['Time'].dt.date == date]

        # Parcourir chaque personne unique pour la date donnée
        for personne in date_data['base'].unique():
            
            # Filtrer les données pour la personne donnée
            personne_data = date_data[date_data['base'] == personne]

            # Récupérer l'Attendance Check Point correspondante pour la personne donnée
            premiere_attendance = "CENTRALE 1 ARTI_Porte1_Lecteur de carte d''entrée1"
            derniere_attendance = "CENTRALE 1 ARTI_Porte1_Lecteur de carte de sortie2"

            # Vérifier la première heure de badge
            premiere_heure_badge_data = personne_data[personne_data['Attendance Check Point'] == premiere_attendance]['Time']
            premiere_heure_badge = premiere_heure_badge_data.min().to_pydatetime().time() if not premiere_heure_badge_data.isna().all() else datetime.strptime("00:00:00", "%H:%M:%S").time()

            # Vérifier la dernière heure de badge
            derniere_heure_badge_data = personne_data[personne_data['Attendance Check Point'] == derniere_attendance]['Time']
            derniere_heure_badge = derniere_heure_badge_data.max().to_pydatetime().time() if not derniere_heure_badge_data.isna().all() else datetime.strptime("00:00:00", "%H:%M:%S").time()

            # Convertir les heures en objets datetime pour le formatage
            premiere_heure_badge = datetime.combine(datetime.min.date(), premiere_heure_badge)
            derniere_heure_badge = datetime.combine(datetime.min.date(), derniere_heure_badge)

            # Afficher le type des variables

            # Compter le nombre de fois où la personne a badgé
            nombre_badges = personne_data.shape[0]

            # Diviser le nom en last name et first name
            nom = personne.split(" ")[0]

            # Vérifier si position_id est différent de "N/A" pour effectuer l'ajout dans la liste de données

            matricule = matricule_mapping.get(personne, "N/A")
            personne_name = mom_mapping.get(personne, "N/A")  # Corrected this line

            data.append([date, premiere_heure_badge.strftime('%H:%M:%S'), derniere_heure_badge.strftime('%H:%M:%S'), matricule, personne_name, nombre_badges])

    # Créer un DataFrame à partir de la liste de données
    df_output = pd.DataFrame(data, columns=['log_date', 'log_checkin', 'log_checkout', 'log_member_id', 'log_member_name', 'log_count'])

    # Écrire le DataFrame dans un fichier CSV avec encodage UTF-8
    #df_output.to_csv('sortie.csv', index=False, encoding='utf-8-sig')
    return df_output

# Usage example:
#input_file1 = 'personnel.xlsx'
#input_file2 = 'Original Records Report_jAN2023_à_JUIN 2023.xlsx'
#output_file = 'fichier_mongo.xlsx'

#convert_and_save_data(input_file1, input_file2, output_file)
#process_attendance_data(output_file, input_file1)
