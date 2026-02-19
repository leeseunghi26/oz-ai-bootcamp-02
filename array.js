// 배열(array)
let numbers = [10,20,30];

console.log(numbers[0]);
console.log(numbers[1]);
console.log(numbers[2]);

let numbers = [10, "two", 30];
for (let i = 0; i < numbers.length; i++) {
    console.log(numbers[i]);
}

for(const [i,num] of numbers.entries()) {
    console.log(i+"번 index 값; "+num);
}

// enumerate() = entries