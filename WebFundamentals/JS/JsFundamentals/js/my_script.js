function turnOff(element) {
    console.log(element)
    element.innerText = "Off";
    element.classList.add('darkMode')
}
var isLogout = true
function authenticate(element){

    if (isLogout == true){
        element.innerText = 'Login'
        isLogout=false
    }
    else{
        element.innerText = 'Logout'
        isLogout=true
    }

}