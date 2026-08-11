from flask import Flask, request

app = Flask(__name__)

# =========================
# YOUR CLASSMATES
# =========================

classmates = [
    {"name": "Adamah", "boy": True, "glasses": False, "football": True, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": True, "ml": False, "kpop": False, "technology": True},
    {"name": "Saif", "boy": True, "glasses": True, "football": False, "quiet": True, "like_math": False, "chess": False, "artist": True, "talktive": False, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Yusuf", "boy": True, "glasses": False, "football": False, "quiet": True, "like_math": True, "chess": True, "artist": False, "talktive": False, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": True, "ml": False, "kpop": False, "technology": True},
    {"name": "Izzat", "boy": True, "glasses": True, "football": False, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": False, "photography": False, "coding": False, "ml": True, "kpop": False, "technology": False},
    {"name": "Ar Rayyan", "boy": True, "glasses": True, "football": True, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": True, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": True},
    {"name": "Sarvyss", "boy": True, "glasses": True, "football": False, "quiet": False, "like_math": True, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": True, "photography": False, "coding": True, "ml": False, "kpop": False, "technology": True},
    {"name": "Shaffy", "boy": True, "glasses": False, "football": True, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": True, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": True, "coding": False, "ml": True, "kpop": False, "technology": False},
    {"name": "Ahmad Rayyan", "boy": True, "glasses": False, "football": True, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": True, "energetic": True, "ship": True, "pengawas": False, "photography": True, "coding": False, "ml": True, "kpop": False, "technology": False},
    {"name": "Manan", "boy": True, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": False, "sporty": True, "energetic": True, "ship": False, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Ashraf", "boy": True, "glasses": True, "football": False, "quiet": True, "like_math": False, "chess": True, "artist": False, "talktive": False, "foodie": False, "books": False, "melayu": False, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": True},
    {"name": "Arissa S", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": True, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": True, "ml": False, "kpop": True, "technology": False},
    {"name": "Arissa Z", "boy": False, "glasses": False, "football": False, "quiet": True, "like_math": True, "chess": False, "artist": True, "talktive": False, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": True, "ml": False, "kpop": True, "technology": True},
    {"name": "Adelia", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Wan Hana", "boy": False, "glasses": False, "football": False, "quiet": True, "like_math": True, "chess": False, "artist": False, "talktive": False, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": False, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Hannah", "boy": False, "glasses": True, "football": False, "quiet": False, "like_math": False, "chess": True, "artist": True, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Zulaikha", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": True, "energetic": True, "ship": False, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Qaisara", "boy": False, "glasses": True, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": True, "energetic": True, "ship": False, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Orked", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": True, "artist": True, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Attiyah", "boy": False, "glasses": False, "football": False, "quiet": True, "like_math": False, "chess": False, "artist": True, "talktive": False, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": True, "technology": True},
    {"name": "Najihah", "boy": False, "glasses": True, "football": False, "quiet": True, "like_math": False, "chess": False, "artist": True, "talktive": False, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Fatehah", "boy": False, "glasses": True, "football": False, "quiet": True, "like_math": False, "chess": False, "artist": True, "talktive": False, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Iris", "boy": False, "glasses": True, "football": False, "quiet": False, "like_math": True, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": True, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Irdina", "boy": False, "glasses": True, "football": False, "quiet": False, "like_math": True, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Qistina", "boy": False, "glasses": True, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Qaireen", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": True, "energetic": True, "ship": True, "pengawas": True, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Liza", "boy": False, "glasses": True, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": True, "photography": False, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Aina", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Fitri", "boy": True, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Aishah", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": False, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Kamil", "boy": True, "glasses": False, "football": True, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": False, "coding": False, "ml": True, "kpop": False, "technology": False}
]


# =========================
# QUESTIONS
# =========================

questions = [
    ("boy", "Is the person a boy?"),
    ("glasses", "Does the person wear glasses?"),
    ("football", "Does the person play football?"),
    ("quiet", "Is the person quiet?"),
    ("like_math", "Does this person like math?"),
    ("chess", "Does this person know how to play chess?"),
    ("artist", "Are they good at drawing?"),
    ("talktive", "Are they talkative?"),
    ("foodie", "Do they really like food?"),
    ("books", "Do they like reading books?"),
    ("melayu", "Can they speak Melayu?"),
    ("sporty", "Do you think this person joins many sport activities?"),
    ("energetic", "Are they always energetic?"),
    ("ship", "Does this person have a ship name with someone in our class?"),
    ("pengawas", "Does this person hold the position of school prefect/Pengawas sekolah?"),
    ("photography", "Does this person like taking photos?"),
    ("coding", "Does this person like coding?"),
    ("ml", "Does this person know how to play Mobile Legends?"),
    ("kpop", "Does this person listen to K-pop?"),
    ("technology", "Is this person interested in technology?")
]


# =========================
# SHARED CSS
# =========================

def page_style():
    return """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            text-align: center;
            background: linear-gradient(135deg, #eef2ff, #ffffff);
            color: #222;
            padding: 25px 15px;
        }

        .container {
            max-width: 700px;
            margin: auto;
        }

        .title {
            font-size: 42px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        .subtitle {
            font-size: 20px;
            margin-bottom: 25px;
        }

        /* =====================
           CARTOON CHARACTER
           ===================== */

        .character {
            width: 190px;
            height: 210px;
            margin: 20px auto 30px;
            position: relative;
        }

        .head {
            width: 170px;
            height: 160px;
            background: #f5cfa0;
            border: 5px solid #222;
            border-radius: 50% 50% 45% 45%;
            position: absolute;
            left: 10px;
            top: 15px;
            overflow: hidden;
        }

        .hair {
            position: absolute;
            width: 175px;
            height: 65px;
            background: #222;
            top: -10px;
            left: -7px;
            border-radius: 50% 50% 20% 20%;
        }

        .eye {
            position: absolute;
            width: 25px;
            height: 25px;
            background: white;
            border: 4px solid #222;
            border-radius: 50%;
            top: 67px;
        }

        .eye::after {
            content: "";
            width: 8px;
            height: 8px;
            background: #222;
            border-radius: 50%;
            position: absolute;
            top: 5px;
            left: 5px;
        }

        .eye.left {
            left: 38px;
        }

        .eye.right {
            right: 38px;
        }

        .nose {
            position: absolute;
            top: 92px;
            left: 75px;
            font-size: 24px;
        }

        .mouth {
            position: absolute;
            top: 120px;
            left: 58px;
            width: 55px;
            height: 20px;
            border-bottom: 5px solid #222;
            border-radius: 50%;
        }

        .body {
            position: absolute;
            width: 120px;
            height: 75px;
            background: #555;
            left: 35px;
            top: 150px;
            border: 5px solid #222;
            border-radius: 35px 35px 10px 10px;
        }

        .tie {
            position: absolute;
            width: 20px;
            height: 45px;
            background: #222;
            left: 85px;
            top: 160px;
            clip-path: polygon(50% 0%, 100% 30%, 70% 100%, 50% 80%, 30% 100%, 0% 30%);
        }

        /* =====================
           QUESTION BOX
           ===================== */

        .question-box {
            background: white;
            border: 4px solid #222;
            border-radius: 20px;
            padding: 25px;
            margin: 20px auto;
            max-width: 650px;
            box-shadow: 0 6px 0 #222;
        }

        .question {
            font-size: 29px;
            font-weight: bold;
        }

        /* =====================
           BUTTONS
           ===================== */

        button {
            font-size: 25px;
            font-weight: bold;
            padding: 18px 45px;
            margin: 10px;
            border-radius: 15px;
            border: 3px solid #222;
            background: white;
            cursor: pointer;
            box-shadow: 0 5px 0 #222;
            transition: transform 0.1s;
        }

        button:active {
            transform: translateY(5px);
            box-shadow: 0 0 0 #222;
        }

        .yes {
            background: #d9ffd9;
        }

        .no {
            background: #ffd9d9;
        }

        .restart {
            background: #eeeeee;
        }

        .stats {
            font-size: 18px;
            margin-top: 25px;
        }

        a {
            text-decoration: none;
        }

        .result-name {
            font-size: 48px;
            font-weight: bold;
        }

        @media (max-width: 600px) {

            body {
                padding: 20px 10px;
            }

            .title {
                font-size: 32px;
            }

            .subtitle {
                font-size: 18px;
            }

            .character {
                transform: scale(0.85);
                margin: 5px auto 10px;
            }

            .question-box {
                padding: 20px 12px;
            }

            .question {
                font-size: 24px;
            }

            button {
                width: 90%;
                font-size: 26px;
                padding: 20px;
                margin: 10px auto;
                display: block;
            }

            .result-name {
                font-size: 38px;
            }
        }
    </style>
    """


# =========================
# WEBSITE
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    remaining = classmates.copy()

    question_number = 0
    answers = {}

    if request.method == "POST":

        question_number = int(request.form["question_number"])

        for key, value in request.form.items():

            if key.startswith("answer_"):
                attribute = key.replace("answer_", "")
                answers[attribute] = value == "yes"

        current_attribute = request.form["current_attribute"]
        current_answer = request.form["answer"]

        answers[current_attribute] = current_answer == "yes"

        for attribute, answer in answers.items():

            remaining = [
                person for person in remaining
                if person[attribute] == answer
            ]

        question_number += 1

    # =========================
    # GUESS
    # =========================

    if len(remaining) == 1:

        return f"""
        <html>

        <head>
            <title>Class Akinator</title>
            {page_style()}
        </head>

        <body>

        <div class="container">

        <div class="title">CLASS AKINATOR</div>

        <div class="character">

            <div class="head">
                <div class="hair"></div>

                <div class="eye left"></div>
                <div class="eye right"></div>

                <div class="nose">▼</div>
                <div class="mouth"></div>
            </div>

            <div class="body"></div>
            <div class="tie"></div>

        </div>

        <div class="question-box">

            <h2>🎯 I KNOW WHO IT IS!</h2>

            <div class="result-name">
                {remaining[0]["name"]}
            </div>

            <p class="subtitle">
                Was I right?
            </p>

        </div>

        <button class="yes">YES!</button>
        <button class="no">NO</button>

        <br>

        <a href="/restart">
            <button class="restart">🔄 START AGAIN</button>
        </a>

        </div>

        </body>
        </html>
        """

    # =========================
    # NO MATCH
    # =========================

    if len(remaining) == 0:

        return f"""
        <html>

        <head>
            <title>Class Akinator</title>
            {page_style()}
        </head>

        <body>

        <div class="container">

        <div class="title">CLASS AKINATOR</div>

        <div class="character">

            <div class="head">
                <div class="hair"></div>

                <div class="eye left"></div>
                <div class="eye right"></div>

                <div class="nose">▼</div>
                <div class="mouth"></div>
            </div>

            <div class="body"></div>
            <div class="tie"></div>

        </div>

        <div class="question-box">

            <h2>🤔 Hmm...</h2>

            <p class="question">
                I couldn't find anyone who matches those answers.
            </p>

        </div>

        <a href="/restart">
            <button class="restart">🔄 START AGAIN</button>
        </a>

        </div>

        </body>
        </html>
        """

    # =========================
    # FINISHED QUESTIONS
    # =========================

    if question_number >= len(questions):

        names = ""

        for person in remaining:
            names += f"<li>{person['name']}</li>"

        return f"""
        <html>

        <head>
            <title>Class Akinator</title>
            {page_style()}
        </head>

        <body>

        <div class="container">

        <div class="title">CLASS AKINATOR</div>

        <div class="character">

            <div class="head">
                <div class="hair"></div>

                <div class="eye left"></div>
                <div class="eye right"></div>

                <div class="nose">▼</div>
                <div class="mouth"></div>
            </div>

            <div class="body"></div>
            <div class="tie"></div>

        </div>

        <div class="question-box">

            <h2>🤔 I'm not completely sure...</h2>

            <p class="question">
                It could be:
            </p>

            <ul style="font-size: 22px; text-align: left;">
                {names}
            </ul>

        </div>

        <a href="/restart">
            <button class="restart">🔄 START AGAIN</button>
        </a>

        </div>

        </body>
        </html>
        """

    # =========================
    # SHOW QUESTION
    # =========================

    attribute, question = questions[question_number]

    hidden_answers = ""

    for key, value in answers.items():

        hidden_answers += f"""
        <input type="hidden"
               name="answer_{key}"
               value="{"yes" if value else "no"}">
        """

    return f"""
    <html>

    <head>
        <title>Class Akinator</title>
        {page_style()}
    </head>

    <body>

    <div class="container">

        <div class="title">
            CLASS AKINATOR
        </div>

        <div class="subtitle">
            Think of someone in your class!
        </div>

        <!-- CARTOON CHARACTER -->

        <div class="character">

            <div class="head">

                <div class="hair"></div>

                <div class="eye left"></div>
                <div class="eye right"></div>

                <div class="nose">▼</div>

                <div class="mouth"></div>

            </div>

            <div class="body"></div>
            <div class="tie"></div>

        </div>

        <!-- QUESTION -->

        <div class="question-box">

            <div class="question">
                {question}
            </div>

        </div>

        <!-- ANSWERS -->

        <form method="POST">

            {hidden_answers}

            <input type="hidden"
                   name="question_number"
                   value="{question_number}">

            <input type="hidden"
                   name="current_attribute"
                   value="{attribute}">

            <button class="yes"
                    name="answer"
                    value="yes">
                YES
            </button>

            <button class="no"
                    name="answer"
                    value="no">
                NO
            </button>

        </form>

        <div class="stats">

            Possible people: {len(remaining)}

            <br><br>

            Question {question_number + 1} of {len(questions)}

        </div>

        <br>

        <a href="/restart">
            <button class="restart">
                🔄 START AGAIN
            </button>
        </a>

    </div>

    </body>

    </html>
    """


# =========================
# RESTART
# =========================

@app.route("/restart")
def restart():
    return home()


# =========================
# START SERVER
# =========================

app.run(host="0.0.0.0", port=5000)
