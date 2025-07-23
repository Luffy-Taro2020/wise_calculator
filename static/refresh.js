// refresh.js

document.addEventListener("DOMContentLoaded", function () {
    // Autoenvía el formulario cada 60 segundos
    setInterval(() => {
        document.querySelector('form').submit();
    }, 60000);
});
