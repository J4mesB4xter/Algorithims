const prompt = require('prompt-sync')()

function isEven(n) {
  return n % 2 == 0;
}

function isOdd(n) {
  return Math.abs(n % 2) == 1;
}

let input = prompt("Please Provide an Integer: ")


const errors = {
  inputNaNError: {error: "value provided is not a number"},
  notAnIntegerError: {error: "value provided is not an integer"}
}

function returnStepCount(n) {
  let iteration = 0
  n = Number(n)
  console.log(n)

  if (isNaN(n)) {console.log(errors.inputNaNError); return}
  if (!Number.isInteger(n)) {console.log(errors.notAnIntegerError); return}

  do {
    if (isOdd(n)) {
      n = (3*n + 1);
      iteration++;
      console.log(`Iteration = ${iteration}; Current Value = ${n}`);
    };
    if (isEven(n)) {
      n = (n/2);
      iteration++;
      console.log("Iteration = " + iteration + "; Current Value = " + n);
    };
  } while (n !== 1)
  console.log(`Iterations when number equals 1: ${iteration}`);
  return
};


returnStepCount(input)

