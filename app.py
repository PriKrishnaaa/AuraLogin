 # AuraLogin - Starter Flask Website (app.py)

from flask import Flask, render_template, request, redirect, jsonify
import json
import csv
import uuid

app = Flask(__name__)

# Route: Home page to collect user info
@app.route('/')
def home():
    return render_template('index.html')

# Route: Handle form submission and return anime alter ego (mocked)
@app.route('/submit_form', methods=['POST'])
def submit_form():
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']

    # Generate mock anime identity
    alter_ego = {
        "anime_name": f"{name}-kun" if gender.lower() == 'male' else f"{name}-chan",
        "vibe_color": "Violet Blaze",
        "star_element": "Water"
    }
    return render_template('mood.html', alter_ego=alter_ego)

# Route: Mood-based recommendations
@app.route('/mood', methods=['POST'])
def mood():
    mood = request.form['mood']
    mood_data = {
        "happy": {
            "quote": "You radiate like the sun.",
            "slang": "Slay Queen",
            "outfit": "Bright crop top with cargo pants",
            "playlist": ["Happy Vibes", "Feel Good Hits"]
        },
        "sad": {
            "quote": "Your softness is your superpower.",
            "slang": "No cap, you got this",
            "outfit": "Oversized hoodie and warm socks",
            "playlist": ["Soft Rain", "Chill Therapy"]
        }
        # Add more moods as needed
    }
    return render_template('distraction.html', mood_data=mood_data.get(mood, {}))

# Route: Distraction page content
@app.route('/distraction')
def distraction():
    with open('data/affirmations.json') as f:
        affirmations = json.load(f)
    with open('data/books.json') as f:
        books = json.load(f)
    return jsonify({
        "affirmation": affirmations[0],
        "books": books[:3]
    })

# Route: Handle journal post
@app.route('/journal', methods=['POST'])
def journal():
    entry = request.form['entry']
    with open('data/journals.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([str(uuid.uuid4()), entry])
    return redirect('/')

# Route: View journal wall
@app.route('/journals')
def journals():
    entries = []
    try:
        with open('data/journals.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                entries.append(row[1])
    except FileNotFoundError:
        pass
    return render_template('journal.html', entries=entries)

if __name__ == '__main__':
    app.run(debug=True)

