var age = 25;
var firstName = 'Endi';
var isMale = true
var isFemale = false
                    // 0    1        2             3



var person = {
    'firstName': 'Endi',
    'lastName': 'Mimini',
    'email': '3ndi.mimini@gmail.com',
    'age': 25,
    'programmingLanguage': ['Python', 'Javascript'],
    'isAdmin': true
}
// console.log(age + 'this is my age ')
// age = 26;


// console.log(person.age)

var users = [
    {
        'emri': 'Endi',
        'mbiemri': 'Mimini',
        'email': 'endimimini@betaplan.al'
    },
    {
        'emri': 'Dikush',
        'mbiemri': 'Tjeter',
        'email': 'dikush@betaplan.al'
    },
    {
        'emri': 'Unknown',
        'mbiemri': 'Unknown',
        'email': 'unknown@betaplan.al'
    }
]



for (var i = 0; i<users.length; i++){
    console.log(`Endi ${users[i].emri}, Mbiemri:, ${users[i].mbiemri} Email-i:${users[i].email}` )
}
var a = 23
var b = 2

if( a>b){
    console.log( a, ' is bigger then ', b)
}
else{
    console.log('third times the charm')
}

