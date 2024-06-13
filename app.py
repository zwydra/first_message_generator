import random
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)

# Define arrays of words and phrases
sals1 = ["Unsatisfied", "Naughty", "Dear", "Dearest", "Sweet"]
sals2 = ["Master", "Sir", "Girl", "Slut", "You", "Y/N", "Sweetheart"]
adjs = ["tight", "hot", "wet", "naughty", "thick", "sensitive", "plump", "rough", "fucking", "deep", "shaky", "intense", "smooth", "massive", "hard", "passionate", "sexy", "seductive", "sweet", "dirty", "soft", "unsatisfied", "hoarse", "powerful"]
nouns = ["cock", "pussy", "cum", "bed", "mouth", "skin", "orgasm", "finger", "craving", "desire", "voice", "tongue", "ass", "balls", "body", "throat", "pleasure", "heart", "seed", "breast", "chest", "face", "love", "lust", "passion", "breath", "head", "thirst", "pillow"]
advs = ["deeply", "quickly", "intensely", "senselessly", "slowly", "hoarsely", "roughly", "desperately", "nicely", "impatiently", "thoroughly", "lovingly", "passionately", "seductively", "shakily", "softly","tightly","sloppily","shamelessly"]
verbs = ["cums for", "fucks", "moans for", "kisses", "sucks", "drives into", "thrusts into", "whispers", "lusts after", "pants for", "coos for", "licks", "strokes", "thirsts for", "teases", "begs for", "woos"]

# Function to select a random element from an array, ensuring no repetition
def rel(arr, used):
    word = random.choice(arr)
    while word in used:
        word = random.choice(arr)
    used.append(word)
    return word

# Function to generate a love letter
def generate_love_letter():
    used_words = []
    ll = f"<p>{rel(sals1, used_words)} {rel(sals2, used_words)},</p>\n<p>     "
    last = None
    for i in range(5):
        if random.randint(0, 9) < 5:
            # LONG
            optadj1 = '' if random.randint(0, 9) < 5 else rel(adjs, used_words)
            noun1 = rel(nouns, used_words)
            optadv = '' if random.randint(0, 9) < 5 else rel(advs, used_words)
            verb = rel(verbs, used_words)
            optadj2 = '' if random.randint(0, 9) < 5 else rel(adjs, used_words)
            noun2 = rel(nouns, used_words)

            concat = ". " if last is not None else ""
            ll += f"{concat}My {optadj1} {noun1} {optadv} {verb} your {optadj2} {noun2}"
            last = "LONG"

        else:
            # SHORT
            adj = rel(adjs, used_words)
            noun = rel(nouns, used_words)
            if last == "SHORT":
                concat = ", "
            elif last == "LONG":
                concat = ". You are"
            else:
                concat = "You are "
            ll += f"{concat} my {adj} {noun}"
            
        ##
            
            last = "SHORT"

    adv = rel(advs, used_words)
    ll += f".</p>\n<p>     Yours {adv},</p>\n<p>     Z.</p>"
    return ll

# Define the route for the main page
@app.route('/')
def home():
    love_letter = generate_love_letter()
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dating apps: First Message Generator</title>
        <style>
            body {{
                font-family: Trebuchet MS, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #ECC1C1;
                display: flex;
                flex-direction: column;
                min-height: 100vh;
            }}
            .container {{
                text-align: center;
                flex: 1;
                padding: 40px;
            }}
            h1 {{
                font-size: 2.5em;
                margin-bottom: 0.5em;
            }}
            h2 {{
                font-size: 1.5em;
                margin-bottom: 1em;
            }}
            .letter-frame {{
                border: 2px solid #ccc;
                padding: 20px;
                background-color: #fff;
                margin-top: 20px;
                display: inline-block;
                text-align: left;
                width: 60%;
            }}
            p {{
                margin: 20px 0;
            }}
            .note {{
                font-size: 0.8em;
                color: #888;
                margin-top: 10px;
            }}
            .button-container {{
                text-align: center;
                margin-top: 20px;
            }}
            button {{
                padding: 10px 20px;
                font-size: 1em;
                cursor: pointer;
            }}
            .about {{
                font-size: 0.8em;
                color: #888;
                width: 80%;
                max-width: 500px;
                margin: 20px auto;
                text-align: left;
            }}
            footer {{
                text-align: center;
                padding: 20px;
                background-color: #f0f0f0;
            }}
        </style>
        <script>
            async function generateNewLetter() {{
                const response = await fetch('/generate');
                const data = await response.json();
                document.querySelector('.letter-frame').innerHTML = data.letter;
            }}
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Dating apps: First Message Generator</h1>
            <h2>Your guarantee for an interaction*</h2>
            <div class="letter-frame">
                {love_letter}
            </div>
            <div class="button-container">
                <button onclick="generateNewLetter()">Generate New Message</button>
            </div>
            <p class="note">*Please note, that the other person’s reaction might vary. Being blocked can also be considered an interaction!</p>
        </div>
        <footer>
            <div class="about">
                <p><strong>About the project</strong></p>
                <p>This project is a modern take on the 1952 program “Loveletters” by Christopher Strachey which is often considered to be one of the first creative algorithms. The list of words used as variables was adjusted to the language used by creators of erotic fanfiction on the platform Archive of Our Own (AO3). The fanfictions for this project were chosen based on their popularity in the “Smut” tag on the AO3 platform. The specific words used for this project were chosen based on the frequency with which they appear in the sources. Certain words were used over ten times in the sources. The results produced by this reformed algorithm are sexual in nature and can often be considered obscene. This can be considered as a case study for the evolution of the language of human desires.</p>
                <p>The title and subtitle of the project are a playful commentary on communication on dating apps which tends to skip the phase of polite courtship to go straight into crude sexual, suggestions and remarks.</p>
                <p>Sources:</p>
                <p><a href="https://www.gingerbeardman.com/loveletter/" target="_blank">https://www.gingerbeardman.com/loveletter/</a></p>
                <p><a href="https://archiveofourown.org/works/5076781/chapters/11674075?view_adult=true" target="_blank">@megamatt09 on AO3 - “The Breeding Ground”</a></p>
                <p><a href="https://archiveofourown.org/works/23032696/chapters/55079845" target="_blank">@Zabeck on AO3 - “The Hero Rises”</a></p>
                <p><a href="https://archiveofourown.org/works/21651097/chapters/51629176" target="_blank">@guardianangelcas on AO3 - “A Rough Day”</a></p>
                <p>Project created with the help of ChatGPT 3.5</p>
            </div>
        </footer>
    </body>
    </html>
    """
    return render_template_string(html_content)

# Define the route for generating a new love letter
@app.route('/generate')
def generate():
    new_love_letter = generate_love_letter()
    return jsonify({'letter': new_love_letter})

if __name__ == '__main__':
    app.run(debug=True)
