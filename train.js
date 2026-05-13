/*
L-TASK
Shunday function yozing, u string qabul qilsin va
string ichidagi hamma sozlarni chappasiga yozib,
sozlar ketma-ketligini buzmasdan stringni qaytarsin.

MASALAN:
reverseSentence("we like coding!") => "ew ekil !gnidoc"
*/
console.log("Solution");

function reverseSentence(str) {
  const splitWords = str.split(" ");

  const reversedWords = splitWords.map((word) => {
    return word.split("").reverse().join("");
  });

  return reversedWords.join(" ");
}

console.log(reverseSentence("we like coding!"));

/*
J-TASK (NodeJS)

Shunday function yozing, u parametridagi array ichida eng kop takrorlangan raqamni topib qaytarsin.
MASALAN: majorityElement([1,2,3,4,5,4,3,4]) return 4
*/
/* J-TASK */

// function majorityElement(arr) {
//   let maxCount = 0;
//   let result = arr[0];

//   for (let num of arr) {
//     let count = arr.filter((ele) => ele === num).length;

//     if (count > maxCount) {
//       maxCount = count;
//       result = num;
//     }
//   }

//   return result;
// }

// console.log(majorityElement([1, 2, 3, 4, 5, 4, 3, 4]));

/* H-TASK (NodeJS)
shunday function tuzing, u integerlardan iborat arrayni argument sifatida qabul qilib,
faqat positive qiymatlarni olib string holatda return qilsin
MASALAN: getPositive([1, -4, 2]) return qiladi "12"

*/
// function hTask(arr) {
//   let result = [];
//   for (let i = 0; i < arr.length; i++) {
//     if (arr[i] > 0) {
//       result.push(arr[i]);
//     }
//   }
//   return result.join(",");
// }

// console.log(hTask([1, 4, 23, 3, 2, 3, -12, -21, 0]));

/*
F-TASK (NodeJS)

Shunday findDoublers function tuzing, unga faqat bitta string argument pass bolib, agar stringda bir hil harf qatnashgan bolsa true, qatnashmasa false qaytarishi kerak.
MASALAN: getReverse("hello") return true return qiladi
*/
// Masalaning yechimi

// function findDoublers(str) {
//   const splitStr = str.split("");

//   const hasDouble = splitStr.some((ele) => {
//     const count = splitStr.filter((ch) => ch === ele).length;
//     return count > 1;
//   });

//   return hasDouble;
// }
// console.log(findDoublers("helllo"));

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

// console.log("=== Solution ===");

// function getReverse(a) {
//   const result = a.split("").reverse().join("");
//   return result;
// }
// console.log(getReverse("hello"));

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
