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
