/*
E-TASK (NodeJS)

Shunday function tuzing, u bitta string argumentni qabul qilib osha stringni teskari qilib return qilsin.
MASALAN: getReverse("hello") return qilsin "olleh"
*/
/*                                                         Quick notes
Strings in JavaScript are immutable and do not have a native .reverse() method.
To reverse a string, you typically convert it to an array, reverse it, and join it back
*/
// Masalaninig yechimi

console.log("=== Solution ===");

function getReverse(a) {
  const result = a.split("").reverse().join("");
  return result;
}
console.log(getReverse("hello"));

/*
D-TASK (NodeJS)

Shunday function tuzingki unga integerlardan iborat array pass bolsin va function bizga osha arrayning eng katta qiymatiga tegishli birinchi indexni qaytarsin.
MASALAN: getHighestIndex([5, 21, 12, 21, 8]) return qiladi 1 sonini.
 */
// Masalaning yechimi
// console.log("Solution");

// function highIndex(arr) {
//   const max = Math.max(...arr);
//   return arr.indexOf(max);
// }
// console.log(highIndex([5, 21, 12, 201, 8]));

/*   C-TASK (NodeJS)

Shunday function tuzing, u 2ta string parametr ega bolsin, hamda agar har ikkala string bir hil harflardan iborat bolsa true aks holda false qaytarsin
MASALAN checkContent("mitgroup", "gmtiprou") return qiladi true;
*/

// Masalaning yechimi
// console.log("Solution");

// function checkContent(str, str1) {
//   const arr = str.split("").sort();
//   const arr1 = str1.split("").sort();

//   const joined = arr.join("");
//   const joined1 = arr1.join("");

//   return joined === joined1;
// }

// console.log(checkContent("hello", "olleh"));

/* B-TASK (NodeJS)

Savol: Shunday function tuzing, u 1ta string parametrga ega bolsin, hamda osha stringda qatnashgan raqamlarni sonini bizga return qilsin.
MASALAN countDigits("ad2a54y79wet0sfgb9") 7ni return qiladi.
*/

// Masalaning yechimi
// console.log("Solutuion2");

// function countDigits(str) {
//   const splitStr = str.split("");
//   const filterDigits = splitStr.filter((ele) => {
//     return ele >= "0" && ele <= "9";
//   });
//   return filterDigits.length;
// }

// console.log(countDigits("jfw923983sdf238dfh83r2"));

// ===================================================

/* A-TASK
Savol: Shunday 2 parametrli function tuzing, hamda birinchi parametrdagi letterni ikkinchi parametrdagi sozdan qatnashga sonini return qilishi kerak boladi.
 MASALAN countLetter("e", "engineer") 3ni return qiladi.
*/

/*    Masalaning yechimi

console.log("Solution");

function mitTaskA(letter, word) {
  const splitWord = word.split("");
  const filterWord = splitWord.filter((ele) => {
    return ele === letter;
  });
  return filterWord.length;
}

console.log(mitTaskA("o", "toyota")); 
*/
