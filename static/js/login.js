// Agregar un listener al formulario de login cuando se envía
document.getElementById("loginForm").addEventListener("submit", async (e) => {
    
    e.preventDefault();  
    // Evita que el formulario recargue la página

    const form = e.target;            
    // Obtiene el formulario que disparó el evento

    const formData = new FormData(form);
    // Convierte los datos del formulario en un objeto FormData
    // útil para enviarlo directamente al backend

    // Enviar datos al backend /api/login
    const response = await fetch("/api/login", {
        method: "POST",
        body: formData
    });

    // Convertimos respuesta a JSON
    const data = await response.json();

    // Si el login fue correcto
    if (data.success) {
        // Redirige al usuario a la página de home
        showToast("success", "", data.message)
        // Esperar 3 segundos para mostrar el toast y luego redirigir al login
            setTimeout(() => {
                window.location.href = "/home";
            }, 3000);
        
    } else {
        // Mostrar mensaje de error
       
        showToast("danger", data.title, data.message)
    }

});
