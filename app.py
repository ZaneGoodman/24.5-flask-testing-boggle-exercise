from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify
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


def is_valid_word(word):
    return Boggle.check_valid_word(boggle_game, session["board"], word)


@app.route('/check-word', methods=["POST", "GET"])
def check_if_valid_word():
    user_guess = request.get_json(force=True)['data']['guess']
    result = is_valid_word(user_guess)
    return jsonify(result)
