function test() {
  console.log("working");
}

$('#guessForm').on("submit", checkIfValidWord)

async function checkIfValidWord(evt) {
  evt.preventDefault()
  console.log('working')
  res = await axios.post("/check_word" , {
    data: FormData($(evt.target))
  });
  return res
}
