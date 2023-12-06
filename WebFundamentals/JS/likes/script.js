function likePost(idjaPostit){
    var numriLikeve = parseInt(document.getElementById(idjaPostit).innerText)
    document.getElementById(idjaPostit).innerText = numriLikeve+1
}

