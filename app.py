from flask import Flask, render_template,request
from flask_debugtoolbar import DebugToolbarExtension
from stories import stories


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"
debug = DebugToolbarExtension(app)

@app.route("/")
def choose_text():
    """Chooses a text to use"""

    return render_template("choose.html", stories = stories.values())


@app.route("/form")
def input_words():
    """Inputs words for the text """

    story = stories[request.args["story_id"]]
  
    return render_template("form.html", story_id = request.args["story_id"], prompts = story.prompts)


@app.route("/story")
def show_story():
    """Shows the created text"""
    print(request.args)
    story_id = request.args["story_id"]
    story = stories[story_id]
    text = story.generate(request.args)

    return render_template("story.html",text = text)
