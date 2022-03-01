let sum = 0;
for(let i = 1; i < 1001; i++){
    if(i % 4 == 0){
        sum = sum + i;
    }
}

console.log(sum);