const editar = document.querySelectorAll('.editar');
const modal = document.querySelectorAll('dialog');
const fechar = document.querySelectorAll('.modal-close');

editar.forEach((btn, i) => {
	btn.addEventListener('click', () => {
		modal[i].showModal();
	});
	fechar[i].addEventListener('click', () => {
		modal[i].close();
	});
});

modal.forEach((el) => {
	el.addEventListener('click', (e) => {
		let rect = el.getBoundingClientRect();
		let isInDialog = rect.top <= e.clientY && e.clientY <= rect.top + rect.height && rect.left <= e.clientX && e.clientX <= rect.left + rect.width;
		if (!isInDialog) {
			el.close();
		}
	});
});
