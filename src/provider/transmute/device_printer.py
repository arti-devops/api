import requests, re, json
from bs4 import BeautifulSoup

# Liste des noms des cartouches à rechercher
CARTRIDGES = ['Cartouche Jaune', 'Cartouche noir', 'Cartouche Cyan', 'Cartouche Magenta']
CARTRIDGES_MAP = dict({'Cartouche Jaune':'yello',
                       'Cartouche noir':'black',
                       'Cartouche Cyan':'cyan',
                       'Cartouche Magenta':'magneta'})

def get_printer_status(printer_ip):
    printer_url = f'http://{printer_ip}' #/info_suppliesStatus.html?tab=Home&menu=SupplyStatus'
    printer_info_url = f'http://{printer_ip}/info_suppliesStatus.html?tab=Home&menu=SupplyStatus'
    res = {"status":"offline","content":None}
    try:
        # Effectuer une requête GET à l'URL
        response = requests.get(printer_url, timeout=0.1)
        response.raise_for_status()  # Vérifier si la requête a réussi
        #return {"status":"oneline","content":response.content}
        res["status"] = "online"
        try:
            # Effectuer une requête GET à l'URL
            response = requests.get(printer_info_url, timeout=0.1)
            response.raise_for_status()  # Vérifier si la requête a réussi
            return {"status":"online","content":response.content}
        except requests.exceptions.RequestException as e:
            #print(f"La requête pour l'imprimante {printer_ip} a échoué:", e)
            return res
    except requests.exceptions.RequestException as e:
        #print(f"La requête pour l'imprimante {printer_ip} a échoué:", e)
        return res
    
def parse_printer_status(content):
    if content is None:
        return None

    try:
        soup = BeautifulSoup(content, 'html.parser')

        cartridges_found = False
        cartridge_status = dict({
            'black':0,
            'yello':0,
            'magenta':0,
            'cyan':0
        })

        # Trouver tous les éléments <td> avec la classe CSS "SupplyName width65"
        td_elements = soup.find_all('td', {'class': 'SupplyName width65'})
        for td_element in td_elements:
            nom_cartouche = td_element.contents[0].strip()
            if nom_cartouche in CARTRIDGES:
                # Trouver le prochain élément <td> avec la classe CSS "SupplyName width35 alignRight"
                td_status = td_element.find_next('td', {'class': 'SupplyName width35 alignRight'})
                if td_status:
                    etat_texte = td_status.get_text(strip=True)
                    etat_texte = etat_texte.replace('*', '')

                    # Remove special characters
                    etat_texte = ''.join(c for c in etat_texte if c.isalnum() or c.isspace())
                    etat_texte = re.sub(r'[\s\\n]+', '', etat_texte)
                    etat_texte = re.findall(r'\d+', etat_texte)

                    # Ajouter l'état de la cartouche à la liste
                    cartridge_status[CARTRIDGES_MAP[nom_cartouche]] = int(etat_texte[0])

                cartridges_found = True

        if not cartridges_found:
            return []

        return cartridge_status
    except Exception as e:
        print("Une erreur s'est produite lors de l'analyse de la page:", e)
        return None
    
# SECTION - Function to call
def printer_status(PRINTER_IPS):
    printer_statuses = []

    # Parcourir les adresses IP de l'imprimante
    for printer_ip in PRINTER_IPS:
        # Obtenir l'état de l'imprimante
        response_content = get_printer_status(printer_ip)

        # Analyser l'état de l'imprimante

        if response_content["status"] == "online" and response_content['content']:
            parsed_levels = parse_printer_status(response_content["content"])
            printer_statuses.append({
                'ip': printer_ip,
                'status': response_content["status"],
                'levels': parsed_levels
            })
        else:
            printer_statuses.append({
                'ip': printer_ip,
                'status': response_content["status"]
            })

    # Remove white spaces and special characters from the data
    data_json = json.dumps(printer_statuses, separators=(',', ':'), ensure_ascii=False)
    return json.loads(data_json)
# !SECTION