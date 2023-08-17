console.log('123');

setInterval(() => {
    document.querySelector('#box').innerText = new Date();
}, 1000);
document.querySelector('#url').innerText = window.location.href;
