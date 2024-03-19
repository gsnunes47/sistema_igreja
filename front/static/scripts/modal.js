const button_editar = document.querySelectorAll('.editar')
const modal = document.querySelectorAll('dialog')
let cont = 0

button_editar.forEach(botao2 => {
    const cont2 = cont
    botao2.addEventListener("click",function(){
        modal[cont2].showModal()
    })
    cont += 1
});

// let cont2 = 0
// const button_sair = document.querySelectorAll('button')

// modal.forEach(pop => {
//     alert(pop.innerHTML)
// })

// button_editar.forEach(pop => {
//     alert(pop.innerHTML)
// })


// button_sair.forEach(botao => {
//     botao.onclick = function(){
//         modal.close()
//         cont2 += 1
//     }
// });

