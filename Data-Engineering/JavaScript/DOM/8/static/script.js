async function updatePage () {
    const response = await fetch('/get_data');
    const data = await response.json();

    document.getElementById('main-title').innerText = data.title;

    document.getElementById('description-area').innerHTML = `Updated at: <u>${new Date().toLocaleTimeString()}</u>`;

    const imgElement = document.getElementById('feature-image');
    imgElement.src = data.image_url;

    const linkElement = document.getElementById('action-link');
    linkElement.href = data.link;
    linkElement.innerText = "visit new link";

    document.body.style.backgroundColor = data.color;
    document.getElementById('content-box').style.borderColor = "white";
    document.getElementById('content-box').style.backgroundColor = "rgba(0, 0, 0, 1)";
    }