# Example de scraping avec Python et BeautifulSoup

_Mis à jour le 05/10/2021_ 

## !!! ATTENTION !!!

La législation sur le scraping n'est pas claire. Il est de votre responsabilité de lire les conditions d'utilisations des sites web qui vous intéressent. 

Nous vous conseillons de ne pas scraper des données personnelles et de ne rien divulguer.

## L'objectif est de scraper des informations sur Studyrama.com 

On veut récupérer des informations sur les écoles d'ingénieurs en informatique en France (nom, privée/public, emails, site web). 

On se base sur le site studyrama.com.

La page de recherche se présente comme suit :

![Studyrama](https://user-images.githubusercontent.com/57575311/135997227-7e16d9c2-ecb8-4b75-90ff-e9f560709d18.PNG)

Chaque vignette redirige vers la fiche de l'école. La fiche école contient son site, ses mails et si l'école est privée ou public.
Nous voulons récupérer ces informations. Le script complet est disponible dans le répo.

## Etape 0 : Faire la recherche à la main et voir comment automatiser

Le lien : 'https://www.studyrama.com/formations/annuaire-des-formations/?btnRechercherEcoles=Rechercher&currentPage=1&cboDominante=38&cboEtablissementType=ingenieur'

Nous remarquons qu'il y a 8 pages, il va donc falloir 8 requêtes avec la libraire request.

## Etape 1 : Analyser à la main les éléments qui nous intéressent, pour les récupérer avec BeautifulSoup

Il faut ouvrir l'inspecteur (clic droit inspecter) et regarder ce qui nous intéresse. Pour cela, utilisez l'outil de l'inspecteur présent au haut à gauche et survolez le rectangle bleu. 

![Utile](https://user-images.githubusercontent.com/57575311/135999534-70cd3f26-9f49-439e-8863-7a7374b2788d.PNG)

En regardant le code dans l'inspecteur, nous remarquons que la balise <a> contient l'attribut qui nous intéresse : la redirection vers la fiche école et le nom de l'école. 
Il suffit maintenant de bien utiliser les librairies requests et BeautifulSoup. Voir le code.
  
![Capture1](https://user-images.githubusercontent.com/57575311/136000654-93b04fab-39f2-4c04-bddc-c41c10f49462.PNG)
  
## Les étapes suivantes sont décrites dans le code. Au travail !

**Aussi :** si vous êtes intéressé par la [Data](https://www.emil.school/programmes/data-for-pro), [l'Automatisation](https://www.emil.school/programmes/marketing-and-data-automation), [Python et le machine learning](https://www.emil.school/programmes/python-machine-learning) ou le [Product Analytics](https://www.emil.school/programmes/tracking-product-analytics), je vous invite à jeter un coup d'oeil à nos formations sur le sujet :
  
https://www.emil.school/programmes

