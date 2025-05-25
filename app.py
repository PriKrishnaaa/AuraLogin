from flask import Flask, render_template, request, redirect, url_for 
import csv
import uuid
from datetime import datetime
import requests
import random

# Initialize Flask app with static folder path
app = Flask(__name__, static_folder='static')

# Krishna Bhagavad Gita Quote API

def get_live_quote(name, dob, mood):
    fallback_quotes = [
        "You have the right to work, but never to the fruit of work.",
        "Be steadfast in yoga, O Arjuna. Perform your duty and abandon all attachment to success or failure.",
        "Change is the law of the universe. You can be a millionaire, or a pauper in an instant.",
        "There is neither this world, nor the world beyond. Nor happiness for the one who doubts.",
        "A person can rise through the efforts of their own mind; or draw themselves down, in the same manner."
    ]
    try:
        random.seed(hash(name + dob + mood))
        max_shloks = {
            1: 47, 2: 72, 3: 43, 4: 42, 5: 29, 6: 47, 7: 30, 8: 28, 9: 34,
            10: 42, 11: 55, 12: 20, 13: 35, 14: 27, 15: 20, 16: 24, 17: 28, 18: 78
        }
        chapter = random.randint(1, 18)
        slok = random.randint(1, max_shloks[chapter])
        url = f"https://bhagavadgitaapi.in/slok/{chapter}/{slok}/?api_key=demo"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return f"{data['slok']} — {data['tej']['ht'][:150]}..."
    except:
        pass
    return random.choice(fallback_quotes)

def get_element(dob, gender):
    year = int(dob.split('-')[0])
    month = int(dob.split('-')[1])
    base = (year + month + len(gender)) % 4
    return ["Fire", "Water", "Earth", "Air"][base]

def get_affirmation_by_date():
    url = "https://www.affirmations.dev"
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json().get("affirmation", "I am strong and capable.")
    except:
        return "I radiate calm and peaceful energy."

def get_book_recommendations_detailed():
    try:
        url = "https://openlibrary.org/subjects/biography.json?limit=10"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            books = data.get("works", [])
            recommendations = []
            for book in books[:3]:
                title = book.get("title", "Unknown")
                authors = book.get("authors", [])
                author = authors[0].get("name", "Unknown") if authors else "Unknown"
                cover_id = book.get("cover_id", "")
                key = book.get("key", "")
                cover_url = f"https://covers.openlibrary.org/b/id/{cover_id}-M.jpg" if cover_id else "https://via.placeholder.com/80x120?text=No+Cover"
                link = f"https://openlibrary.org{key}"
                recommendations.append({"title": title, "author": author, "cover": cover_url, "link": link})
            return recommendations
    except:
        pass
    return [{
        "title": "The Story of My Life",
        "author": "Helen Keller",
        "cover": "https://covers.openlibrary.org/b/id/8235116-M.jpg",
        "link": "https://openlibrary.org/works/OL27448W"
    }]

def get_anime_character(name, mood, gender):
    naruto_chars = [
        {"name": "Naruto Uzumaki", "desc": "The chaos in his heart holds a sun-like warmth."},
        {"name": "Sasuke Uchiha", "desc": "Darkness shaped him, but resolve defines him."},
        {"name": "Kakashi Hatake", "desc": "Masked calm, mind like a hidden blade."},
        {"name": "Itachi Uchiha", "desc": "A silent sorrow carrying a nation’s weight."},
        {"name": "Hinata Hyuga", "desc": "Shy strength blooming like lavender snow."},
        {"name": "Sakura Haruno", "desc": "Soft cherry blossoms punch through stone."}
    ]

    demon_slayer_chars = [
        {"name": "Tanjiro Kamado", "desc": "Smells grief, but breathes hope."},
        {"name": "Nezuko Kamado", "desc": "A silent flame with eyes of dusk."},
        {"name": "Zenitsu Agatsuma", "desc": "Fear-struck lightning strikes hardest."},
        {"name": "Inosuke Hashibira", "desc": "Untamed heart with a beast’s pride."},
        {"name": "Shinobu Kocho", "desc": "She poisons pain with smiles and butterflies."},
        {"name": "Mitsuri Kanroji", "desc": "Love is her blade and blush her shield."}
    ]

    jjk_chars = [
        {"name": "Yuji Itadori", "desc": "Carries death lightly and friends dearly."},
        {"name": "Megumi Fushiguro", "desc": "Shadowed grace with a clenched core."},
        {"name": "Satoru Gojo", "desc": "He blinds with brilliance, laughs with chaos."},
        {"name": "Nobara Kugisaki", "desc": "Beauty with a hammer, rebellion in her grin."},
        {"name": "Toji Fushiguro", "desc": "A ghost of blood and impossible silence."},
        {"name": "Maki Zenin", "desc": "Powerless by curse, powerful by choice."}
    ]

    poetic_originals = [
        {"name": "Aiko Hoshino", "desc": "A stargazer with dreams woven in silver light."},
        {"name": "Ren Takashi", "desc": "Walks in shadows, but glows from within."},
        {"name": "Yuna Mizuki", "desc": "Carries a soft rebellion in every glance."},
        {"name": "Takumi Yoru", "desc": "Storm-tamer with an artist's soul."},
        {"name": "Sayaka Fuji", "desc": "Shimmers like sakura in rainfall."},
        {"name": "Hikaru Enzo", "desc": "Speaks silence in the language of stars."}
    ]

    all_characters = naruto_chars + demon_slayer_chars + jjk_chars + poetic_originals

    # Mood-based aura color mapping
    mood_colors = {
        "anxiety": ["Misty Blue", "Ash Lilac", "Fog White"],
        "peaceful": ["Cloud White", "Sakura Pink", "Sky Mist"],
        "sad": ["Grey Pearl", "Rain Blue", "Dusky Lavender"],
        "happy": ["Peach Bloom", "Citrus Gold", "Sunlight Amber"],
        "excited": ["Electric Rose", "Bold Plum", "Aurora Flame"],
        "creative": ["Indigo Spark", "Mint Teal", "Neon Orchid"]
    }

    try:
        # Identity-based seeding
        seed_input = f"{name.lower()}_{mood.lower()}_{gender.lower()}"
        identity_seed = hash(seed_input)
        random.seed(identity_seed)

        # Optional: gender filter
        gender = gender.lower()
        if gender == "male":
            filtered = [c for c in all_characters if c["name"].split()[-1] not in ["Haruno", "Hyuga", "Nezuko", "Shinobu", "Mitsuri", "Nobara", "Sayaka", "Yuna", "Aiko"]]
        elif gender == "female":
            filtered = [c for c in all_characters if c["name"].split()[-1] in ["Haruno", "Hyuga", "Nezuko", "Shinobu", "Mitsuri", "Nobara", "Sayaka", "Yuna", "Aiko"]]
        else:
            filtered = all_characters

        character = random.choice(filtered or all_characters)
        aura_color = random.choice(mood_colors.get(mood.lower(), ["Twilight Grey"]))

        return {
            "name": character["name"],
            "aura_color": aura_color,
            "description": character["desc"]
        }

    except:
        # Final fallback (Animechan optional)
        return {
            "name": "Yuki Haruno",
            "aura_color": "Twilight Grey",
            "description": "A soul wrapped in stories and soft resilience."
        }


def get_playlist_url(mood):
    playlists = {
        "anxiety": "https://www.youtube.com/embed/videoseries?list=PLPu9yLLnWBe1GPlWgHoGFFZwD6VaPUxuE",
        "peaceful": "https://open.spotify.com/embed/playlist/37i9dQZF1DX3rxVfibe1L0",
        "happy": "https://open.spotify.com/embed/playlist/37i9dQZF1DX0XUsuxWHRQd",
        "sad": "https://open.spotify.com/embed/playlist/37i9dQZF1DWSqBruwoIXkA"
    }
    return playlists.get(mood, "")

def get_lifestyle_tip(mood):
    tips = {
        "anxiety": ["Drink water and ground yourself.", "Take a mindful walk outside."],
        "sad": ["Write down what you're feeling.", "Listen to calming music."],
        "peaceful": ["Make tea and journal in a quiet spot.", "Sit with a plant or garden in silence."]
    }
    return random.choice(tips.get(mood, tips.get("anxiety", [])))

def get_genz_slang(mood):
    slangs = {
        "anxiety": [
            ("It’s giving... breathe 🌬️", "Take a deep breath and calm down"),
            ("Main character reboot 🔁", "Resetting your mindset")
        ],
        "sad": [
            ("Soft-resetting 💔", "Letting emotions reboot you gently"),
            ("Blue vibes but still cute 💙", "Acknowledging sadness with grace")
        ],
        "peaceful": [
            ("Lowkey vibin' 🌸", "Feeling gentle and quietly confident"),
            ("Zen-core unlocked 🧘", "Radiating peace like a calm monk")
        ]
    }
    mood_slangs = slangs.get(mood, slangs.get("anxiety", []))
    sample_size = min(2, len(mood_slangs))  # Use 2 to avoid errors
    sampled = random.sample(mood_slangs, sample_size)

    # Safely convert to dictionary
    slang_dict = {}
    for pair in sampled:
        if isinstance(pair, (list, tuple)) and len(pair) == 2:
            slang_dict[pair[0]] = pair[1]
    return slang_dict

def get_random_hug():
    hugs = []
    try:
        with open('data/hugs.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if len(row) >= 2:
                    hugs.append(row[1])
    except FileNotFoundError:
        pass
    return [random.choice(hugs)] if hugs else []

def generate_user_aura(name, dob, gender, mood):
    quote = get_live_quote(name, dob, mood)
    tip = get_lifestyle_tip(mood)
    slang_list = get_genz_slang(mood)
    character = get_anime_character(name, mood, gender)
    playlist = get_playlist_url(mood)
    zodiac_element = get_element(dob, gender)
    books = get_book_recommendations_detailed()
    affirmation = get_affirmation_by_date()
    hug_sample = get_random_hug()

    gratitude_entries = []
    try:
        with open('data/gratitude_log.csv', newline='', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 6 and row[1] == name and row[4] == mood:
                    gratitude_entries.append(row[5])
    except FileNotFoundError:
        pass

    return {
        "quote": quote,
        "tip": tip,
        "slang": slang_list,
        "anime_name": character["name"],
        "aura_color": character["aura_color"],
        "star_element": zodiac_element,
        "description": character["description"],
        "playlist": playlist,
        "latest_gratitudes": gratitude_entries[-3:],
        "affirmation": affirmation,
        "fashion": "",
        "books": books,
        "hugs": hug_sample,
        "latest_journals": [],
        "hugs": hug_sample
    }

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def handle_index_form():
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    return render_template('mood.html', name=name, dob=dob, gender=gender)
@app.route('/mood', methods=['POST'])
def mood_page():
    try:
        name = request.form.get('name')
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        mood = request.form.get('mood', '').lower()

        if not all([name, dob, gender, mood]):
            return "<h3>Error: Missing name, date of birth, gender or mood.</h3>", 400

        aura_data = generate_user_aura(name, dob, gender, mood)

        peaceful_moods = ['peaceful', 'happy', 'excited']
        anxious_moods = ['angry', 'anxiety', 'depression']
        sad_moods = ['sad', 'feeling numb']

        if mood in peaceful_moods:
            template = 'peaceful.html'
        elif mood in anxious_moods:
            template = 'anxiety.html'
        elif mood in sad_moods:
            template = 'sad.html'
        else:
            template = 'mood.html'

        return render_template(template, aura=aura_data, name=name, dob=dob, gender=gender)

    except Exception as e:
        return f"<h3>Something went wrong: {str(e)}</h3>", 500

@app.route('/journals', methods=['POST'])
def save_journal():
    entry = request.form['entry']
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    mood = request.form['redirect']

    with open('data/gratitude_log.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([str(uuid.uuid4()), name, dob, gender, mood, entry, datetime.now().strftime('%Y-%m-%d %H:%M')])

    return redirect(url_for('mood_page'))

@app.route('/sendhug', methods=['POST'])
def send_hug():
    note = request.form['hug_note']
    name = request.form.get('name')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    mood = request.form.get('redirect')

    try:
        with open('data/hugs.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([str(uuid.uuid4()), note, datetime.now().strftime('%Y-%m-%d %H:%M')])
    except FileNotFoundError:
        with open('data/hugs.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'note', 'timestamp'])
            writer.writerow([str(uuid.uuid4()), note, datetime.now().strftime('%Y-%m-%d %H:%M')])

    aura_data = generate_user_aura(name, dob, gender, mood)
    return render_template(f"{mood}.html", aura=aura_data, name=name, dob=dob, gender=gender)


@app.route('/saveletter', methods=['POST'])
def save_letter():
    letter = request.form['future_letter']
    name = request.form.get('name')
    dob = request.form.get('dob')
    gender = request.form.get('gender')
    mood = request.form.get('mood')  # ✅ Fix: use the correct key "mood"

    try:
        with open('data/future_letters.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([str(uuid.uuid4()), letter, datetime.now().strftime('%Y-%m-%d %H:%M')])
    except FileNotFoundError:
        with open('data/future_letters.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'letter', 'timestamp'])
            writer.writerow([str(uuid.uuid4()), letter, datetime.now().strftime('%Y-%m-%d %H:%M')])

    aura_data = generate_user_aura(name, dob, gender, mood)
    return render_template(f"{mood}.html", aura=aura_data, name=name, dob=dob, gender=gender)


@app.route('/log_aura_message', methods=['POST'])
def log_aura_message():
    msg = request.form.get('message')
    try:
        with open('data/aura_messages.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([str(uuid.uuid4()), msg, datetime.now().strftime('%Y-%m-%d %H:%M')])
    except FileNotFoundError:
        with open('data/aura_messages.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'message', 'timestamp'])
            writer.writerow([str(uuid.uuid4()), msg, datetime.now().strftime('%Y-%m-%d %H:%M')])
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)
