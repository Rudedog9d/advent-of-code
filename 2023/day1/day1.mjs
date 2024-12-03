import {readFileSync} from 'fs';

let data;

try {
  data = readFileSync('./input.txt', 'utf8').split("\n").map((line) => line.trim());
} catch (err) {
  console.error(err);
}

// data = [
//   // '1abc2',
//   // 'pqr3stu8vwx',
//   // 'a1b2c3d4e5f',
  'oneight' // 1ight -> 11
// ]

function getPartOne() {
  const total = data.map((str) => {
    let newStr = str.replace(/\D/g, "");
    const newDigit = newStr[0] + newStr[newStr.length - 1];
    return parseInt(newDigit);
  });
  console.log(
    total.reduce(function (x, y) {
      return x + y;
    }, 0)
  );
}

function getPartTwo() {
  const numberKey = {
    one: 1,
    two: 2,
    three: 3,
    four: 4,
    five: 5,
    six: 6,
    seven: 7,
    eight: 8,
    nine: 9,
    1:1,
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9
  };

  const pattern = new RegExp(Object.keys(numberKey).join("|"), "g");
  console.log(pattern)
  const total = data.map((str) => {
    // Use a callback function to replace each matched word with its numeric value
    // const result = str.replace(
    //   pattern,
    //   (match) => numberKey[match.toLowerCase()]
    // );
    const matches = str.match(pattern);
    console.log('matches', matches)
    const first = matches[0].replace()
    const last = matches[matches.length - 1]
    // const newStr = result.replace(/\D/g, "");
    // console.log('newStr', newStr)
    // const newDigit = newStr[0] + newStr[newStr.length - 1];
    // console.log('newDigit', newDigit);

    return parseInt(first + last);
  });
  const sum = total.reduce(
    (accumulator, currentValue) => accumulator + currentValue,
    0
  );

  console.log(sum);
}

getPartOne();
getPartTwo();