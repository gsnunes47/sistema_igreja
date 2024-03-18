tds = document.querySelectorAll('.td-nasc');

tds.forEach((td) => {
	let current = td.innerText;
	td.innerText = current.replaceAll('-', '/');
});
