from flask import Flask, jsonify
from scraper import scrape_all_programs, save_to_csv
from data_processor import clean_data
import os

app = Flask(__name__)

# URLs des programmes
PROGRAM_URLS = [
    # Licences
    "https://www.esb.tn/programmes/licences/sciences-de-gestion/",
    "https://www.esb.tn/programmes/licences/licence-en-business-computing/",
    "https://www.esb.tn/programmes/licences/licence-en-mathematiques-appliquees/",
    # Masters
    "https://www.esb.tn/programmes/masters-professionnels/master-en-management-digital-systemes-dinformation/",
    "https://www.esb.tn/programmes/masters-professionnels/master-en-marketing-digital/",
    "https://www.esb.tn/programmes/masters-professionnels/master-en-business-analytics/",
    "https://www.esb.tn/programmes/masters-professionnels/master-professionnel-de-comptabilite-controle-audit/",
    "https://www.esb.tn/programmes/masters-professionnels/master-professionnel-gamma/",
    "https://www.esb.tn/programmes/masters-professionnels/master-professionnel-en-finance-digitale/",
    # Alternance
    "https://www.esb.tn/programmes/alternance/BA-alternance/",
    # Doubles diplômes
    "https://www.esb.tn/programmes/doubles-diplomes/partenaires-academiques/",
]

RAW_DATA_PATH = "data/raw/programs.csv"
PROCESSED_DATA_PATH = "data/processed/programs_cleaned.csv"

@app.route('/')
def index():
    return jsonify({"message": "Bienvenue à l'API Backend pour le scraping des programmes d'ESB"})

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Pas de contenu pour éviter les erreurs 404 sur /favicon.ico

@app.route('/api/scrape', methods=['GET'])
def scrape_data():
    """Scrape program data and save to raw CSV."""
    data = scrape_all_programs(PROGRAM_URLS)
    save_to_csv(data, RAW_DATA_PATH)
    return jsonify({"message": "Scraping completed and data saved", "data": data})

@app.route('/api/clean', methods=['GET'])
def clean_raw_data():
    """Clean raw data and save to processed CSV."""
    clean_data(RAW_DATA_PATH, PROCESSED_DATA_PATH)
    return jsonify({"message": "Data cleaning completed"})

@app.route('/api/data', methods=['GET'])
def get_cleaned_data():
    """Return cleaned data."""
    if not os.path.exists(PROCESSED_DATA_PATH):
        return jsonify({"error": "Processed data not found. Run /api/clean first."}), 404

    df = pd.read_csv(PROCESSED_DATA_PATH)
    return jsonify(df.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)
