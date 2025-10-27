from flask import Flask, request, jsonify
import pymorphy2

app = Flask(__name__)
morph = pymorphy2.MorphAnalyzer(lang='uk')

@app.route('/')
def home():
    return jsonify({"message": "Ukrainian Name Normalizer API active"})

@app.route('/normalize_names', methods=['POST'])
def normalize_names():
    try:
        data = request.get_json(force=True)
        names = data.get('names', [])
        normalized = []

        for name in names:
            parsed = morph.parse(name)
            if parsed:
                normalized.append(parsed[0].normal_form.capitalize())
            else:
                normalized.append(name)

        return jsonify({'normalized': normalized})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
