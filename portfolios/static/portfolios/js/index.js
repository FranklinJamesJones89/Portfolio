/* javascript */

const displayDate = () => {
	const currentYear = new Date().getFullYear();
	document.querySelector('.date').innerHTML = 'Copyright ' + currentYear;
}

displayDate();
setInterval(displayDate, 1000);
