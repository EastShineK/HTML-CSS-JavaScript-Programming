#!/usr/bin/env node

//console.log(process.argv);
const lib = require("./lib");

if(process.argv.length < 4){
    console.log("Insufficient parameter!");
    process.exit(1);
}

let command = process.argv[2];
let numbers = process.argv.slice(3, process.argv.length);//.map((n) => parseFloat(n));
//console.log(numbers);
let len = numbers.length;

for(let i = 0; i < numbers.length; i++){
    //if(numbers[i].some((n) => includes('@'))){
    if(numbers[i].includes('@')){
        let arr = numbers[i].split('@');
        if(arr[1] == 0){
            console.log("Invalid repeat!");
            process.exit(1);
        }
        numbers[i] = arr[0];
        for(let j = 0; j < arr[1] - 1; j++){
            numbers[len] = arr[0];
            len ++;
        }
    }
}
numbers = numbers.map((n) => parseFloat(n));

/*for(let k = 0; k < numbers.length; k++){
    console.log(numbers[k]);
}*/

if(numbers.some((n) => isNaN(n))){
    console.log("Some arguments are not numbers!");
    process.exit(1);
}

let result;
//console.log(command);

switch (command) {
    case "sum":
        result = lib.sum(numbers);
        break;
    case "avg":
        result = lib.avg(numbers);
        break;
    case "max":
        result = lib.max(numbers);
        break;
    case "min":
        result = lib.min(numbers);
        break;
    case "med":
        result = lib.med(numbers);
        break;
    default:
        console.log("Wrong command!");
        process.exit(1);
}

console.log(result);