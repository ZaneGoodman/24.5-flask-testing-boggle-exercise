async function checkIfValidWord(evt) {
  evt.preventDefault();
  console.log("working");

  res = await axios.get("/check-word", {
    data: {
      guess: $("#guess").val(),
    },
  });
  if (res.data === "not-word") {
    showMessage("not a word");
  }
}

$("#guessForm").on("submit", checkIfValidWord);

function showMessage(msg) {
  $(".msg").text(msg);
}

// why can I not affect the dom with messages?
