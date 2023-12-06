function editName(emri){
    document.getElementById(emri).innerHTML = prompt('Shkruaj emrin')
}
function removePerson(personi){
    document.getElementById(personi).remove()
    var numriRequestave = parseInt(document.getElementById('requestsNumber').innerText)

    document.getElementById('requestsNumber').innerText = numriRequestave - 1
}