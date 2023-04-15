from boggle import Boggle
from flask import Flask, render_template, session, redirect, request, jsonify
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.config["SECRET_KEY"] = "4534gdghjk5d#$RGR^HDG"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
toolbar = DebugToolbarExtension(app)
app.debug = True

boggle_game = Boggle()


@app.route('/')
def make_and_show_board():
    board = boggle_game.make_board()
    session["board"] = board
    return render_template('show_board.html')


@app.route('/check-word')
def check_if_valid_word():
    user_guess = request.args["word"]
    board = session["board"]
    response = boggle_game.check_valid_word(board, user_guess)

    return jsonify({'result': response})


@app.route('/highscore', methods=["POST"])
def check_times_played_and_highscore():
    score = request.json["score"]
    highscore = session.get("highscore", 0)
    times_played = session.get("times_played", 0)

    session["times_played"] = times_played + 1
    session["highscore"] = max(score, highscore)

    return jsonify(broke_record=score > highscore)
