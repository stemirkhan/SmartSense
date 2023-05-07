const closedF = document.querySelector('.input-icon.eye.first')
const openedF = document.querySelector('.input-icon.eye.first.opened')
const inputF = document.getElementById('password')

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