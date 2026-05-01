/*
function findDoublers(str) {
  if (str.length <= 1) return false;
  const seen = new Set();
  for (let i of str) {
    if (seen.has(i)) {
      return true;
    }
    seen.add(i);
  }
  return false;
}
*/

function max(arr) {
  const c = Math.max(...arr);
  return arr.indexOf(c);
}

console.log(getHighestIndex([5, 21, 12, 21, 8]));
