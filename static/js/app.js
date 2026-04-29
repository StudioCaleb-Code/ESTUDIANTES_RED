function guardarNombre() {
    const nombre = document.getElementById('nombre').value;
    if (nombre.trim() !== "") {
        localStorage.setItem('nombreAnalista', nombre);
        window.location.href = "/formulario";
    } else {
        alert("¡Por favor, ingresa un nombre!");
    }
}

// Al cargar resultado.html, puedes usar esto para poner el nombre:
document.addEventListener("DOMContentLoaded", () => {
    const titulo = document.getElementById('titulo_resultado');
    const nombre = localStorage.getItem('nombreAnalista');
    if (titulo && nombre) {
        titulo.innerText = `Análisis de: ${nombre}`;
    }
});