function test() {
  console.log("working");
}


async function checkIfValidWord(evt) {
  evt.preventDefault()
  console.log('working')
  res = await axios.post("/check-word" , {
    data: {
      guess: $("#guess").val()
    }
  });
}
$("#guessForm").on("submit", checkIfValidWord)
