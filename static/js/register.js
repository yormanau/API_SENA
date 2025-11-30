// Escuchar el evento "submit" del formulario de registro
document.getElementById("registerForm").addEventListener("submit", async function(e) {

    e.preventDefault(); 
    // Evita que la página recargue al enviar el formulario

    const formData = new FormData(this);
    // Obtiene todos los datos del formulario y los empaqueta en un FormData

    try {
        // Enviar petición al backend /api/register
        const response = await fetch("/api/register", {
            method: "POST",
            body: formData
        });

        // Convertimos la respuesta del servidor a JSON
        const data = await response.json();

        // Si el registro fue exitoso
        if (data.success) {
            // Mostrar alerta tipo toast
            showToast("success", data.title, data.message);

            // Esperar 3 segundos para mostrar el toast y luego redirigir al login
            setTimeout(() => {
                window.location.href = "/login";
            }, 3000);

        } else {
            // Mostrar errores debajo del formulario
            showToast("danger", data.title, data.message);
        }

    } catch (error) {
        // Si ocurre un error de red, servidor caído, etc.
        console.error("Error en la petición:", error);
    }
});
