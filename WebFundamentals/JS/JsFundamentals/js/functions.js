function addTwoNumbers(num1, num2){
    if (typeof(num1)=='string' || typeof(num2)=='string') {
        return 'I only expect numbers, i dont know how to add by text!'
    }
    return num1+num2;
}

function substractTwoNumbers(num1,num2){
    return num1-num2
}

function sayMyName(name){
    console.log('My name is '+ name)
}

sayMyName('Endi')

var shuma=addTwoNumbers('sdsd',3)

var shuma2=substractTwoNumbers(30.3,10)

console.log(shuma)
console.log(shuma2)
