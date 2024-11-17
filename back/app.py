from flask import Flask, jsonify
from scraper import scrape_esprit
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/scrape/esprit', methods=['GET'])
def get_esprit_data():
    data = scrape_esprit()
    return jsonify(data.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(debug=True)
