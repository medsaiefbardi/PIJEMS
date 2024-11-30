import requests
from bs4 import BeautifulSoup
import os
import pandas as pd

def scrape_program_details(url):
    """Scrape details of a single program."""
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    program_details = {"URL": url}

    # Objectifs
    objectives_section = soup.find('h3', text='Objectifs')
    if objectives_section:
        objectives = objectives_section.find_next('p').get_text(strip=True)
        program_details['Objectifs'] = objectives

    # Compétences
    competences_section = soup.find('h3', text='Compétences')
    if competences_section:
        competences = [li.get_text(strip=True) for li in competences_section.find_next('ul').find_all('li')]
        program_details['Compétences'] = competences

    # Contenu
    contenu_section = soup.find('h3', text='Contenu')
    if contenu_section:
        contenu = contenu_section.find_next('ul').get_text(separator=' ', strip=True)
        program_details['Contenu'] = contenu

    # Métiers
    metiers_section = soup.find('h3', text='Métiers')
    if metiers_section:
        metiers = [li.get_text(strip=True) for li in metiers_section.find_next('ul').find_all('li')]
        program_details['Métiers'] = metiers

    # Secteurs d'activité
    secteurs_section = soup.find('h3', text='Secteurs d’activité')
    if secteurs_section:
        secteurs = [li.get_text(strip=True) for li in secteurs_section.find_next('ul').find_all('li')]
        program_details['Secteurs d’activité'] = secteurs

    return program_details

def scrape_all_programs(url_list):
    """Scrape details for all programs."""
    all_programs = []
    for url in url_list:
        print(f"Scraping {url}...")
        try:
            details = scrape_program_details(url)
            all_programs.append(details)
        except Exception as e:
            print(f"Failed to scrape {url}: {e}")
            continue
    return all_programs

def save_to_csv(data, filename):
    """Save scraped data to a CSV file."""
    df = pd.DataFrame(data)
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")
