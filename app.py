from flask import Flask, request

app = Flask(__name__)

# =========================================================
# CLASSMATES
# =========================================================

classmates = [
{"name":"Adamah","boy":1,"glasses":0,"football":1,"quiet":0,"like_math":0,"chess":1,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":1,"ml":0,"kpop":0,"technology":1},
{"name":"Saif","boy":1,"glasses":1,"football":0,"quiet":1,"like_math":0,"chess":0,"artist":1,"talktive":0,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Yusuf","boy":1,"glasses":0,"football":0,"quiet":1,"like_math":1,"chess":1,"artist":0,"talktive":0,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":1,"ml":0,"kpop":0,"technology":1},
{"name":"Izzat","boy":1,"glasses":1,"football":0,"quiet":0,"like_math":0,"chess":1,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":0,"photography":0,"coding":0,"ml":1,"kpop":0,"technology":0},
{"name":"Ar Rayyan","boy":1,"glasses":1,"football":1,"quiet":0,"like_math":0,"chess":1,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":1,"photography":1,"coding":0,"ml":0,"kpop":0,"technology":1},
{"name":"Sarvyss","boy":1,"glasses":1,"football":0,"quiet":0,"like_math":1,"chess":1,"artist":0,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":1,"photography":0,"coding":1,"ml":0,"kpop":0,"technology":1},
{"name":"Shaffy","boy":1,"glasses":0,"football":1,"quiet":0,"like_math":0,"chess":1,"artist":0,"talktive":1,"foodie":1,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":1,"photography":1,"coding":0,"ml":1,"kpop":0,"technology":0},
{"name":"Ahmad Rayyan","boy":1,"glasses":0,"football":1,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":1,"energetic":1,"ship":1,"pengawas":0,"photography":1,"coding":0,"ml":1,"kpop":0,"technology":0},
{"name":"Manan","boy":1,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":0,"sporty":1,"energetic":1,"ship":0,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Ashraf","boy":1,"glasses":1,"football":0,"quiet":1,"like_math":0,"chess":1,"artist":0,"talktive":0,"foodie":0,"books":0,"melayu":0,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":0,"technology":1},

{"name":"Arissa S","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":1,"chess":1,"artist":0,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":1,"ml":0,"kpop":1,"technology":0},
{"name":"Arissa Z","boy":0,"glasses":0,"football":0,"quiet":1,"like_math":1,"chess":0,"artist":1,"talktive":0,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":1,"ml":0,"kpop":1,"technology":1},
{"name":"Adelia","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Wan Hana","boy":0,"glasses":0,"football":0,"quiet":1,"like_math":1,"chess":0,"artist":0,"talktive":0,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":0,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Hannah","boy":0,"glasses":1,"football":0,"quiet":0,"like_math":0,"chess":1,"artist":1,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Zulaikha","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":1,"energetic":1,"ship":0,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Qaisara","boy":0,"glasses":1,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":1,"energetic":1,"ship":0,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Orked","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":1,"artist":1,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Attiyah","boy":0,"glasses":0,"football":0,"quiet":1,"like_math":0,"chess":0,"artist":1,"talktive":0,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":1,"technology":1},
{"name":"Najihah","boy":0,"glasses":1,"football":0,"quiet":1,"like_math":0,"chess":0,"artist":1,"talktive":0,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Fatehah","boy":0,"glasses":1,"football":0,"quiet":1,"like_math":0,"chess":0,"artist":1,"talktive":0,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Iris","boy":0,"glasses":1,"football":0,"quiet":0,"like_math":1,"chess":0,"artist":1,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":1,"photography":1,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Irdina","boy":0,"glasses":1,"football":0,"quiet":0,"like_math":1,"chess":0,"artist":1,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":0,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Qistina","boy":0,"glasses":1,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Qaireen","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":1,"energetic":1,"ship":1,"pengawas":1,"photography":0,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Liza","boy":0,"glasses":1,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":1,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":1,"photography":0,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Aina","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":1,"photography":1,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Fitri","boy":1,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":1,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":0,"pengawas":0,"photography":1,"coding":0,"ml":0,"kpop":0,"technology":0},
{"name":"Aishah","boy":0,"glasses":0,"football":0,"quiet":0,"like_math":0,"chess":0,"artist":1,"talktive":1,"foodie":0,"books":1,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":1,"photography":0,"coding":0,"ml":0,"kpop":1,"technology":0},
{"name":"Kamil","boy":1,"glasses":0,"football":1,"quiet":0,"like_math":0,"chess":0,"artist":0,"talktive":1,"foodie":0,"books":0,"melayu":1,"sporty":0,"energetic":1,"ship":1,"pengawas":1,"photography":0,"coding":0,"ml":1,"kpop":0,"technology":0}
]

# =========================================================
# QUESTIONS
# =========================================================

questions = [
("boy","Is the person a boy?"),
("glasses","Do they wear glasses?"),
("football","Do they play football?"),
("quiet","Are they quiet?"),
("like_math","Do they like math?"),
("chess","Do they know how to play chess?"),
("artist","Are they good at drawing?"),
("talktive","Are they talkative?"),
("foodie","Do they really like food?"),
("books","Do they like reading books?"),
("melayu","Can they speak Melayu?"),
("sporty","Do they join many sport activities?"),
("energetic","Are they always energetic?"),
("ship","Do they have a ship name with someone?"),
("pengawas","Are they a school prefect?"),
("photography","Do they like taking photos?"),
("coding","Do they like coding?"),
("ml","Do they know how to play Mobile Legends?"),
("kpop","Do they listen to K-pop?"),
("technology","Are they interested in technology?")
]

# =========================================================
# DESIGN
# =========================================================

CSS = """
<style>
*{box-sizing:border-box}
body{
font-family:Arial;
text-align:center;
background:linear-gradient(135deg,#eef2ff,#fff);
padding:20px;
color:#222
}
.box{
max-width:650px;
margin:auto;
background:white;
padding:25px;
border-radius:25px;
box-shadow:0 5px 20px #bbb
}
h1{font-size:40px}
.q{font-size:28px;font-weight:bold;margin:30px 0}
button{
font-size:25px;
font-weight:bold;
padding:20px 50px;
margin:10px;
border:3px solid #222;
border-radius:15px;
background:white;
box-shadow:0 5px #222
}
button:active{
transform:translateY(5px);
box-shadow:none
}
.yes{background:#d8ffd8}
.no{background:#ffd8d8}
.restart{background:#eee}
.face{font-size:100px;margin:10px}

@media(max-width:600px){
h1{font-size:32px}
.q{font-size:23px}
button{
display:block;
width:90%;
margin:15px auto;
font-size:27px
}
}
</style>
"""

def page(content):
    return f"""
    <html>
    <head>
    <meta name="viewport" content="width=device-width,initial-scale=1">
    {CSS}
    </head>
    <body>
    <div class="box">
    {content}
    </div>
    </body>
    </html>
    """

# =========================================================
# GAME
# =========================================================

@app.route("/", methods=["GET","POST"])
def home():

    remaining = classmates[:]
    answers = {}
    qnum = 0

    if request.method == "POST":

        qnum = int(request.form["qnum"])

        # Load previous answers
        for k,v in request.form.items():
            if k.startswith("a_"):
                answers[k[2:]] = v == "1"

        # Save current answer
        attr = request.form["attr"]
        answers[attr] = request.form["answer"] == "1"

        qnum += 1

        # Filter classmates
        for attr, answer in answers.items():
            remaining = [
                person for person in remaining
                if person.get(attr) == answer
            ]

    # =====================================================
    # 0 PEOPLE
    # =====================================================

    if len(remaining) == 0:

        return page("""
        <h1>🤔 I CAN'T GUESS!</h1>

        <div class="face">😵‍💫</div>

        <h2>I can't guess who it is!</h2>

        <p>None of the classmates match your answers.</p>

        <a href="/restart">
        <button class="restart">🔄 TRY AGAIN</button>
        </a>
        """)

    # =====================================================
    # 1 PERSON → GUESS IMMEDIATELY
    # =====================================================

    if len(remaining) == 1:

        return page(f"""
        <h1>🎯 I KNOW WHO IT IS!</h1>

        <div class="face">😎</div>

        <h2>{remaining[0]["name"]}</h2>

        <p>Was I right?</p>

        <a href="/restart">
        <button class="yes">YES!</button>
        </a>

        <a href="/restart">
        <button class="no">NO</button>
        </a>

        <br>

        <a href="/restart">
        <button class="restart">🔄 PLAY AGAIN</button>
        </a>
        """)

    # =====================================================
    # MORE THAN 1 → NEXT QUESTION
    # =====================================================

    if qnum < len(questions):

        attr, text = questions[qnum]

        hidden = ""

        for k,v in answers.items():
            hidden += f"""
            <input type="hidden"
                   name="a_{k}"
                   value="{int(v)}">
            """

        return page(f"""
        <h1>PERMATA AKINATOR</h1>

        <div class="face">🧑‍💻</div>

        <div class="q">{text}</div>

        <form method="POST">

        {hidden}

        <input type="hidden"
               name="qnum"
               value="{qnum}">

        <input type="hidden"
               name="attr"
               value="{attr}">

        <button class="yes"
                name="answer"
                value="1">
        YES
        </button>

        <button class="no"
                name="answer"
                value="0">
        NO
        </button>

        </form>

        <p>
        Question {qnum + 1} / {len(questions)}
        <br>
        Possible people: {len(remaining)}
        </p>

        <a href="/restart">
        <button class="restart">
        🔄 RESTART
        </button>
        </a>
        """)

    # =====================================================
    # STILL MULTIPLE AFTER ALL QUESTIONS
    # =====================================================

    names = "<br>".join(
        person["name"] for person in remaining
    )

    return page(f"""
    <h1>🤔 NOT SURE</h1>

    <div class="face">🧐</div>

    <h2>It could be:</h2>

    <p style="font-size:22px">
    {names}
    </p>

    <a href="/restart">
    <button class="restart">
    🔄 PLAY AGAIN
    </button>
    </a>
    """)

# =========================================================
# RESTART
# =========================================================

@app.route("/restart")
def restart():
    return home()

# =========================================================

app.run(host="0.0.0.0", port=5000)
