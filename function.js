// 함수(function)

function add(num1,num2) {
    // 반환(return) =호출부로 값을 되돌려주는 것
    return num1 + num2
}

//반환(return)
//=호출부로 값을 되돌려주는 것 
//출력(output)
//console.log(add(1, 2));
//호출부(호출하는 곳)-> 함수호출 -> add 함수 실핼 -> 결과값이 반환
//console.log(add(1,2));
//let result = add(1,2);

console.log(add);

//let my_fuction = add;
//console.log(myFuntion);

//function wrapper(func) {
//    const result = func(1,2);
//    console.log(result);

//let my_fuction = add;
//console.log(add(10, 20);

//1번: add라는 함수를 1,2라는 인자값을 전달해서 add라는 함수를 "호출=실행"
add(1, 2)

// 2번: add라는 함수 자체
add
console.log(add);//출력하는 코드
// add 함수를 myFunction 변수에 할당 (함수 자체를 할당)
let myFuction = add;
//console.log(myFuction);
myFuction(10,20);

let a = 10;

a + 20

const myFuction = add;

const result = myFuction(10,20)

console.log(result);
