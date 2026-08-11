from flask import Flask, request

app = Flask(__name__)

# =========================
# YOUR CLASSMATES
# =========================

classmates = [
    {"name": "Adamah", "boy": True, "glasses": False, "football": True, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": True, "ml": False, "kpop": False, "technology": True},
    {"name": "Saif", "boy": True, "glasses": True, "football": False, "quiet": True, "like_math": False, "chess": False, "artist": True, "talktive": False, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Yusuf", "boy": True, "glasses": False, "football": False, "quiet": True, "like_math": True, "chess": True, "artist": False, "talktive": False, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": False, "coding": True, "ml": False, "kpop": False, "technology": True},
    {"name": "Izzat", "boy": True, "glasses": True, "football": False, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": False, "photography": False, "coding": False, "ml": True, "kpok": False, "technology": False},
    {"name": "Ar Rayyan", "boy": True, "glasses": True, "football": True, "quiet": False, "like_math": False, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": True, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": True},
    {"name": "Sarvyss", "boy": True, "glasses": True, "football": False, "quiet": False, "like_math": True, "chess": True, "artist": False, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": True, "photography": False, "coding": True, "ml": False, "kpok": False, "technology": True},
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
    {"name": "Aina", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess":False, "artist": False, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Fitri", "boy": True, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": False, "pengawas": False, "photography": True, "coding": False, "ml": False, "kpop": False, "technology": False},
    {"name": "Aishah ", "boy": False, "glasses": False, "football": False, "quiet": False, "like_math": False, "chess": False, "artist": True, "talktive": True, "foodie": False, "books": True, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": False, "coding": False, "ml": False, "kpop": True, "technology": False},
    {"name": "Kamil", "boy": True, "glasses": False, "football": True, "quiet": False, "like_math": False, "chess": False, "artist": False, "talktive": True, "foodie": False, "books": False, "melayu": True, "sporty": False, "energetic": True, "ship": True, "pengawas": True, "photography": False, "coding": False, "ml": True, "kpop": False, "technology": False}
]


# =========================
# QUESTIONS
# =========================

questions = [
  {
    ("boy", "Is the person a boy?"),
    ("glasses", "Does the person wear glasses?"),
    ("football", "Does the person play football?"),
    ("quiet", "Is the person quiet?"),
    ("like_math", "Does this person like math"),
    ("chess", "Does this person know how to play chess?"),
    ("artist", "Are they good at drawing"),
    ("talktive", "are they talktive"),
    ("foodie", "Do they really like food"),
    ("books", "Do they like reading books"),
    ("melayu", "Can they speak Melayu"),
    ("sporty", "Do you think this person Join so many sport Activities"),
    ("energetic", "Are they always energetic"),
    ("ship", "Does this person has their own ship name with someone -our class only-"),
    ("pengawas", "Does this person hold the position of school prefect/Pengawas sekolah"),
    ("photography", "Does this person like to take photos"),
    ("coding", "Does this person love to Coding"),
    ("ml", "Does this person really know how to play Mobile legends"),
    ("kpop", "Does this person listen to K-pop"),
    ("technology", "Does this person interested in technology")
  }
]


# =========================
# WEBSITE
# =========================

@app.route("/", methods=["GET", "POST"])
def home():

    # Start with everyone
    remaining = classmates.copy()

    question_number = 0
    answers = {}

    if request.method == "POST":

        # Get previous information
        question_number = int(request.form["question_number"])

        # Get all previous answers
        for key, value in request.form.items():

            if key.startswith("answer_"):
                attribute = key.replace("answer_", "")
                answers[attribute] = value == "yes"

        # Get the answer to the current question
        current_attribute = request.form["current_attribute"]
        current_answer = request.form["answer"]

        answers[current_attribute] = current_answer == "yes"

        # Filter classmates
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
        </head>

        <body>

        <h1>CLASS AKINATOR</h1>

        <h2>🎯 I KNOW WHO IT IS!</h2>

        <h1>{remaining[0]["name"]}</h1>

        <p>Was I right?</p>

        <button>YES!</button>
        <button>NO</button>

        </body>
        </html>
        """

    # No one matches
    if len(remaining) == 0:

        return """
        <html>
        <head>
            <title>Class Akinator</title>
        </head>

        <body>

        <h1>CLASS AKINATOR</h1>

        <h2>🤔 Hmm...</h2>

        <p>I couldn't find anyone who matches those answers.</p>

        </body>
        </html>
        """

    # Finished questions
    if question_number >= len(questions):

        names = ""

        for person in remaining:
            names += f"<li>{person['name']}</li>"

        return f"""
        <html>
        <head>
            <title>Class Akinator</title>
        </head>

        <body>

        <h1>CLASS AKINATOR</h1>

        <h2>🤔 I'm not completely sure...</h2>

        <p>It could be:</p>

        <ul>
            {names}
        </ul>

        </body>
        </html>
        """

    # =========================
    # SHOW QUESTION
    # =========================

    attribute, question = questions[question_number]

    # Hidden fields preserve previous answers
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
    </head>

    <body>

    <h1>CLASS AKINATOR</h1>

    <p>Think of someone in your class!</p>

    <h2>{question}</h2>

    <form method="POST">

        {hidden_answers}

        <input type="hidden"
               name="question_number"
               value="{question_number}">

        <input type="hidden"
               name="current_attribute"
               value="{attribute}">

        <button name="answer" value="yes">
            YES
        </button>

        <button name="answer" value="no">
            NO
        </button>

    </form>

    <p>
        Possible people: {len(remaining)}
    </p>

    <p>
        Question {question_number + 1} of {len(questions)}
    </p>

    </body>

    </html>
    """


app.run(host="0.0.0.0", port=5000)
