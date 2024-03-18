const floatingLabels = () => {
	const labels = document.querySelectorAll('label'),
		inputs = document.querySelectorAll('.form-input'),
		fields = [...inputs];

	function handleFocus(i) {
		labels[i].classList.add('active');
	}

	function handleBlur(field, i) {
		if (field.value.length === 0) {
			labels[i].classList.remove('active');
		}
	}

	[...fields].forEach((field, index) => {
		if (field.value) handleFocus(index);
		field.addEventListener('focus', () => {
			handleFocus(index);
		});
		field.addEventListener('blur', () => {
			handleBlur(field, index);
		});
	});
};

floatingLabels();
