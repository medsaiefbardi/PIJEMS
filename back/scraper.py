import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_esprit():
    url = "https://esprit-tn.com" 
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Exemple de scraping : récupérer les filières et modules
    filieres = []
    for filiere in soup.find_all("div", class_="filiere"):
        nom = filiere.find("h2").text
        modules = [module.text for module in filiere.find_all("li", class_="module")]
        filieres.append({"filiere": nom, "modules": modules})
    
    df = pd.DataFrame(filieres)
    df.to_csv("data/raw/esprit_filieres.csv", index=False)
    return df

if __name__ == "__main__":
    scrape_esprit()