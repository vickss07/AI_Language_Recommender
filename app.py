from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load the programming languages data from the JSON file
with open('data/languages.json', 'r') as json_file:
    languages_data = json.load(json_file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_criteria = request.get_json()
    experience_level = user_criteria.get('experience-level')
    project_type = user_criteria.get('project-type')

    recommended_languages = []

    for language in languages_data:
        if (
            language['experienceLevel'] == experience_level
            and language['projectType'] == project_type
        ):
            recommended_languages.append(language)

    return jsonify(recommended_languages)

if __name__ == '__main__':
    app.run(debug=True)
