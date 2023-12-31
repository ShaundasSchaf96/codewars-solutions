/*
DESCRIPTION:
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
*/

function findShort(s){
  const stringArray = s.split(" ");
  const orderedArray = stringArray.sort((a, b) => {
    return a.length - b.length;
  })
  return orderedArray[0].length
}