// FOR FIRST INPUT

const closedF = document.querySelector('.input-icon.eye.first')
const openedF = document.querySelector('.input-icon.eye.first.opened')
const inputF = document.getElementById('initPassword')

closedF.addEventListener('click', ()=>{
    closedF.classList.toggle('active')
    openedF.classList.toggle('active')
    inputF.type = 'text'

})

openedF.addEventListener('click', ()=>{
    closedF.classList.toggle('active')
    openedF.classList.toggle('active')
    inputF.type = 'password'
})

// FOR SECOND INPUT

const closedS = document.querySelector('.input-icon.eye.second')
const openedS = document.querySelector('.input-icon.eye.second.opened')
const inputS = document.getElementById('secondPassword')

closedS.addEventListener('click', ()=>{
    closedS.classList.toggle('active')
    openedS.classList.toggle('active')
    inputS.type = 'text'

})

openedS.addEventListener('click', ()=>{
    closedS.classList.toggle('active')
    openedS.classList.toggle('active')
    inputS.type = 'password'
})