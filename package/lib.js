function sum(numbers){
    /*let s = 0;
    for(let i = 0; i < numbers.length; i++) s += numbers[i];
    return s;*/
    return numbers.reduce((prev, curr) => prev + curr, 0);
} 

function avg(numbers){
    return sum(numbers) / numbers.length;
} 

function max(numbers){
    return numbers.reduce((max, curr) => (max > curr ? max : curr), numbers[0]);
} 

function min(numbers){
    return numbers.reduce((min, curr) => (min < curr ? min : curr), numbers[0]);
}

function med(numbers){
    let l = numbers.length;
    let s = numbers[0];
    for(let i = 0; i < l - 1; i++){
        for(let j = i + 1; j < l; j++){
            if(numbers[i] > numbers[j]){
                let temp = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = temp;
            }
        }
    }
    if(numbers.length % 2 != 0)
        s = numbers[(l+1)/2-1];
    else
        s = (numbers[l/2-1] + numbers[l/2])/2;
    
        return s;
}

exports.sum = sum;
exports.avg = avg;
exports.max = max;
exports.min = min;
exports.med = med;