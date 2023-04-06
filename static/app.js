function test() {
  console.log("working");
}

async function checkIfValidWord() {
  res = await axios.get("/check_word");
}
