from boggle import Boggle
from flask import Flask, render_template, session, redirect
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)


boggle_game = Boggle()


@app.route('/')
def make_and_show_board():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template('show_board.html')


@app.route('/check_word', methods=["POST"])
def check_for_valid_word():
    return redirect("/")
