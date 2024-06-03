document.addEventListener('DOMContentLoaded', () => {
	const signUpButton = document.getElementById('signUp');
	const signInButton = document.getElementById('signIn');
	const container = document.getElementById('container');
    const activeForm = container.getAttribute('data-active-form');
	
	if (activeForm === 'Register') {
		console.log(activeForm)
        container.classList.add("right-panel-active");
    } else {
        container.classList.remove("right-panel-active");
    }

	signUpButton.addEventListener('click', () => {
		container.classList.add("right-panel-active");
	});
	
	signInButton.addEventListener('click', () => {
		container.classList.remove("right-panel-active");
	});
});