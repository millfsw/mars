from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/<title>")
@app.route("/index/<title>")
def prepare_for_permission(title=""):
    return render_template("base.html", title=title)


@app.route("/training/<prof>")
def traning(prof):
    if "инженер" in prof or "строитель" in prof:
        profession = "инженерные тренажеры"
    else:
        profession = "научные симуляторы"
    return render_template("training.html", profession=profession)


@app.route("/list_prof/<list>")
def list_of_professions(list):
    profs = [
        "инженер-исследователь",
        "пилот",
        "строитель",
        "экзобиолог",
        "врач",
        "инженер по терраформированию",
        "климатолог",
        "специалист по радиоционной защите",
        "астрогеолог",
        "гляциолог",
        "инженер жизнеобеспечения",
        "метеоролог",
        "оператор марсохода",
        "киберинженер",
        "штурман",
        "пилот дронов",
    ]
    return render_template("list_of_professions.html", list=list, profs=profs)

