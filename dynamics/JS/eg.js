let a = Array(1, 23, 14);
let max = 0, i;
a.forEach((element) => {
    if(max<element){
        max = element;
    }
});
console.log(max);