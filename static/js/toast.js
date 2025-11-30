/**
 * Muestra un toast flotante con estilos dinámicos según el tipo.
 *
 * @param {string} type    - success | danger | warning | info
 * @param {string} title   - Título del toast
 * @param {string} message - Mensaje del toast
 */
function showToast(type, title, message) {

    const toast = document.getElementById("toast");
    const toastTitle = document.getElementById("toastTitle");
    const toastMessage = document.getElementById("toastMessage");

    // Eliminar clases previas (por si se muestran varios)
    toast.classList.remove("toast-success", "toast-danger");

    // Agregar clase según el tipo
    toast.classList.add(`toast-${type}`);

    // Insertar contenido
    toastTitle.textContent = title;
    toastMessage.textContent = message;

    // Mostrar animación
    toast.classList.add("show");

    // Ocultar después de 3 segundos
    setTimeout(() => {
        toast.classList.remove("show");
    }, 3000);
}
