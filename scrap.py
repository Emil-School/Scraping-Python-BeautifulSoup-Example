import requests
from bs4 import BeautifulSoup
import pandas as pd

# Le site visé est Studyrama

'''
Documentation des librairies :

Requests : https://docs.python-requests.org/en/latest/
BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Pandas pour save en csv : https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
'''


# ------- ETAPE 0 ------- : faire la recherche à la main et voir comment automatiser
URL_SCRAP = 'https://www.studyrama.com/formations/annuaire-des-formations/?btnRechercherEcoles=Rechercher&currentPage=1&cboDominante=38&cboEtablissementType=ingenieur'




# ------- ETAPE 1 ------- : récupérer le nom des écoles et le lien de leur fiche Studyrama
nom_ecole = []
lien_fiche_ecole = []

# Il y a 8 pages à scraper
for num_page in range(1,9):

    # On requête la page
    r = requests.get('https://www.studyrama.com/formations/annuaire-des-formations/?btnRechercherEcoles=Rechercher&currentPage='+str(num_page)+'&cboDominante=38&cboEtablissementType=ingenieur')

    # On initialise le BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')

    # On récupère l'élément qui nous intéresse, ici une balise <a></a>
    # qui contient la class "trackingElement"
    # Trouver à la main ces informations
    a = soup.find_all("a",class_="trackingElement")

    # On va analyser chaque block
    for block in a:

        # On récupère le nom de l'école
        nom_ecole.append(block.find("h3",class_="center").string)

        # On récupère le lien vers la fiche de l'école sur studyrama
        lien_fiche_ecole.append(block.get("href"))




# ------- ETAPE 2 ------- : clean les données, notamment le nom des écoles
nom_ecole_clean = []
for n in nom_ecole:
    n = n.replace("\t",'')
    n = n.replace("\n",'')
    n = n.replace("\r",'')
    nom_ecole_clean.append(n)




# ------- ETAPE 3 ------- : visiter chaque fiche école et extraire les informations
mails = []
prive_public = []
site = []

url_studyrama = "https://www.studyrama.com"

for lien in lien_fiche_ecole:

    # On requête le lien de la fiche école
    r = requests.get(url_studyrama + lien)
    soup = BeautifulSoup(r.content, 'html.parser')

    # L'élément qui nous intéresse est une balise span qui contient la
    # class front-child-right
    a = soup.find_all('span','front-child-right')

    # Si jalais l'information est bien présente, on l'ajoute
    if len(a) != 0:
        prive_public.append(a[-1].string)
    else:
        prive_public.append('Inconnu')

    # Les mails sont dans une balise <a></a> avec la class email trackingElement
    a = soup.find_all("a",class_="email trackingElement")

    # On extrait les mails
    m = []
    for i in a:
        m.append(i.string)
    # On récupère deux fois chaque mail donc on n'en garde que la moitié
    m = m[:len(m)//2]

    # On nettoie les mails
    m_clean = []
    for mail in m:
        mail = mail.replace(" at ","@")
        mail = mail.replace(" dot ",".")
        m_clean.append(mail)
    mails.append(m_clean)

    # On récupère le site
    a = soup.find_all("a",class_="website-link")
    site.append(a[0].get("href"))





# ------- ETAPE 4 ------- : encore du cleaner, dans l'optique de save dans un csv
url_studyrama = "https://www.studyrama.com"
lien_fiche_ecole_complet = []

for lien in lien_fiche_ecole:
    lien_fiche_ecole_complet.append(url_studyrama+lien)




# ------- ETAPE 5 ------- : On save dans un csv, en passant par un Dataframe
d = {'Nom': nom_ecole_clean, 'Site': site, 'Fiche_Studyrama':lien_fiche_ecole_complet, 'Mails':mails, 'Public/Privé': prive_public }

df = pd.DataFrame(data=d)
df.to_csv(r'out.csv', index=False,encoding='utf-8')


