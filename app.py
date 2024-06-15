mport random
from flask import Flask, render_template, jsonify

app = Flask(_name_)

sals1 = ["Unsatisfied", "Naughty", "Dear", "Dearest", "Sweet"]
sals2 = ["Master", "Sir", "Girl", "Slut", "You", "Y/N", "Sweetheart"]
adjs = ["tight", "hot", "wet", "naughty", "thick", "sensitive", "plump", "rough", "fucking", "deep", "shaky", "intense", "smooth", "massive", "hard", "passionate", "sexy", "seductive", "sweet", "dirty", "soft", "unsatisfied", "hoarse", "powerful"]
nouns = ["cock", "pussy", "cum", "bed", "mouth", "skin", "orgasm", "finger", "craving", "desire", "voice", "tongue", "ass", "balls", "body", "throat", "pleasure", "heart", "seed", "breast", "chest", "face", "love", "lust", "passion", "breath", "head", "thirst", "pillow"]
advs = ["deeply", "quickly", "intensely", "senselessly", "slowly", "hoarsely", "roughly", "desperately", "nicely", "impatiently", "thoroughly", "lovingly", "passionately", "seductively", "shakily", "softly","tightly","sloppily","shamelessly"]
verbs = ["cums for", "fucks", "moans for", "kisses", "sucks", "drives into", "thrusts into", "whispers", "lusts after", "pants for", "coos for", "licks", "strokes", "thirsts for", "teases", "begs for", "woos"]


def rel(arr, used):
    word = random.choice(arr)
    while word in used:
        word = random.choice(arr)
    used.append(word)
    return word


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


@app.route('/')
def home():
    love_letter = generate_love_letter()
    return render_template('index.html', love_letter=love_letter)


@app.route('/generate')
def generate():
    new_love_letter = generate_love_letter()
    return jsonify({'letter': new_love_letter})

if _name_ == '_main_':
    app.run(debug=True)
