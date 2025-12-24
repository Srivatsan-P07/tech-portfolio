const heading = document.querySelector('.title')
const button = document.getElementById('changeTitleBtn')

button.addEventListener('click', () => {
    heading.textContent = 'Title Changed!';
    heading.style.color = 'blue';
});