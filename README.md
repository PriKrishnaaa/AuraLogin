# 🌌 AuraLogin: Mood-Based Aura Experience

**AuraLogin** is an immersive emotion-based interaction platform built using Flask, HTML, CSS, and JavaScript. This project creates a serene and playful Gen Z–inspired experience that responds to your mood with anime alter egos, poetic quotes, spiritual affirmations, breathing animations, fashion suggestions, and playlists.

---

## ✨ May 2025 Highlights

* 🌿 **Peaceful Mood Page**

  * Alps forest aesthetic background with poetic Krishna quotes
  * Curated peaceful playlist and aura lifestyle suggestions

* 🧘‍♂️ **Anxious Mood Page**

  * Breathwork animation (triangle breathing toggle)
  * Devotional Krishna & Shiva playlist
  * Anime alter ego, calming affirmations, and mountainous visuals

* 😔 **Sad Mood Page**

  * Hug Wall (anonymous comfort messages)
  * Letter to Future Self module
  * Mask Dropper animation
  * Vibe and fashion cards for emotional support

* 🎨 **Dynamic Mood Data Integration**

  * Quotes, anime identities, fashion styles, aura colors and affirmations are fetched dynamically from JSON files

* 🎧 **Mood-Based Music**

  * YouTube playlists mixed with Kannada, English, and Hindi
  * Fallback interaction prompts if autoplay fails

---

## 🌐 Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python Flask
* **Assets:** JSON (for quotes, anime data), YouTube embeds
* **Tools:** Git, VS Code, Postman, Google Fonts

---

## 🚀 Getting Started

### Prerequisites

* Python 3.x
* Flask

### Setup

```bash
# Clone the repository
git clone https://github.com/your-username/AuraLogin.git
cd AuraLogin

# Install Flask
pip install Flask

# Run the app
python app.py
```

### Project Structure

```
AuraLogin/
├── static/
│   ├── images/           # Backgrounds (Alps, Sakura, Rain, etc.)
│   ├── css/              # Style files
│   └── js/               # Animations, breath toggle, etc.
├── templates/
│   ├── index.html
│   ├── mood.html
│   ├── peaceful.html
│   ├── anxious.html
│   └── sad.html
├── data/
│   ├── quotes.json       # Mood-based Krishna quotes
│   ├── anime_characters.json
│   └── lifestyle_tips.json
├── app.py                # Flask routes and logic
└── README.md
```

---

## 🧪 Features

* 🧠 Unique quote per user-session (based on name + DOB + mood)
* 🎭 Mood selector redirect logic

  * Peaceful/Excited → `peaceful.html`
  * Anxious/Angry/Overwhelmed → `anxious.html`
  * Sad/Numb → `sad.html`
* 🌟 Anime alter ego card with elemental identity
* 🎨 Mood-to-aesthetic fashion cards (student + office modes)
* 🧘‍♀️ Triangle breathwork animation toggle (CSS + JS)
* 🫶 Hug Wall: Anonymous user comfort messages
* 📖 Daily journaling and mood tracking (optional enhancement)

---

## 📸 Screenshots

Add your own screenshots here:

```
static/screenshots/
├── peaceful.png
├── anxious.png
└── sad.png
```

---

## 🙌 Credits

* Krishna quotes and affirmations inspired by the Bhagavad Gita
* UI backgrounds sourced from [Unsplash](https://unsplash.com) and anime scenery
* Fonts from [Google Fonts](https://fonts.google.com)
* Built with ❤️ by Priyanka Ramanna Shobha

---

## 📬 Contact

Want to collaborate or provide feedback?

* GitHub: [@priyankaramanna](https://github.com/your-username)
* Email: [priyankaramanna@example.com](mailto:priyankaramanna@example.com)

---

> "Reveal your aura, rewrite your story."
 
