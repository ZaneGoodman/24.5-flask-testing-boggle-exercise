"use strict";
class BoggleGame {
  constructor(boardId, seconds = 60) {
    this.seconds = seconds;
    this.score = 0;
    this.playedWords = new Set();
    this.board = $("#" + boardId);
    this.timer = setInterval(this.countDown.bind(this), 1000);
    $("#guessForm", this.board).on("submit", this.checkIfValidWord.bind(this));
  }
  showScore(word) {
    this.score += word.length;
    $(".score").text(this.score);
  }

  showMessage(msg) {
    $("#msg", this.board).text(msg);
    $("#guess").val("");
  }

  showWord(word) {
    $("#playedWords").append($(`<li>${word}</li>`));
  }

  addPlayedWord(word) {
    this.playedWords.add(word);
    console.log(this.playedWords);
    this.showWord(word);
  }

  async checkIfValidWord(evt) {
    evt.preventDefault();
    let $word = $("#guess").val();
    if (!$word) return;
    if (this.playedWords.has($word)) {
      this.showMessage(`You've already played "${$word}"`);
      return;
    }

    const resp = await axios.get("/check-word", {
      params: { word: $word },
    });
    let res_message = resp["data"]["result"];

    if (res_message === "not-on-board") {
      this.showMessage("Sorry, that word isn't on the board");
    } else if (res_message === "not-word") {
      this.showMessage("Sorry, that isn't a word. Try again!");
    } else {
      this.showMessage("Nice job!, word added!");
      this.showScore($word);
      this.addPlayedWord($word);
    }
  }

  countDown() {
    this.seconds -= 1;
    $(".timer", this.board).text(this.seconds);
    if (this.seconds === 0) {
      clearInterval(this.timer);
      this.highScoreData();
    }
  }

  async highScoreData() {
    $("#guessForm", this.board).hide();
    const resp = await axios.post("/highscore", { score: this.score });

    if (resp.data.broke_record) {
      this.showMessage(`You beat the Highscore!: ${this.score}`);
    } else {
      this.showMessage(`Final score: ${this.score}`);
    }
  }
}
// highscore = session.get("highscore", 0)
// times_played = session.get("times_played", 0)
