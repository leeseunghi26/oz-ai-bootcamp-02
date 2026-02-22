// Timer API = 시간을 다루는 API 기능
// setTimeOut() = 일정 시간이 지난 다음에 함수를 실행하는 기능
// setTimeout(함수, 시간(ms))

// setTimeout(
   // () => console.log("시간이 만료되었습니다."),5000); 5000은 5초 , 3000은 3초/ 함수로 전달해야한다.
    const timeOutReturn = setTimeout(() => { return 1}, 5000);
    console.log(timeOutReturn); //반환값

    //setInterval(함수, 시간(ms))-> 일정 시간마다 함수를 반복 실행
    //const intervalReturn = setInterval(() => console.log("1초마다 실행"),1000)
    
    const intervalReturn = setInterval(() => {},1000)
    console.log(intervalReturn);


    // 함수 실행 시키는 방법 : '힘수이름(인자)'
    // setTime
    // 웹_API_함수(화살표_함수, 시간);
    // '웹_API_함수'는 언제 실행될까요? '힘수이름(인자)'가 실행되는 즉시 
    // '화살표_함수'는 언제 실행될까요? 특정 조건을 만족한 순간에 

    // inputTag 값을 preview에 보여주기
    //   inputTag.addEventListner<-겉에 있는 함수("input", function (){
    //       divTag.tectContent = inputTag.value;});<- 안에 있는 함수(input 조건을 만족하면 그 안에 있는 함수를 실행)
    웹_API_함수(화살표_함수, 시간);
    setTimeout(() => {console.log("5초 경과")}, 5000);
    const timerId = setInterval(() => console.log("1초마다 실행"), 1000);
    setTimeout(() => clearInterval(timerId), 5000);

    clearInterval(timerId);