const btn = document.getElementById('myButton');

function handleClick(event) {
    console.log('Button clicked!', event);
}

btn.addEventListener('click', (e) => {
    handleClick(e);
});