// Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
// MASALAN countLetter("e", "engineer") 3ni return qiladi.

console.log("Solution");

function mitTask(letter, word) {
  const splitWord = word.split("");
  const filterWord = splitWord.filter((ele) => {
    return ele === letter;
  });
  return filterWord.length;
}

console.log(mitTask("o", "toyota"));
