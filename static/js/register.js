document.getElementById("registerForm").addEventListener("submit", async function(e) {
    e.preventDefault();

    const formData = new FormData(this);

    try {
        const response = await fetch("/api/register", {
            method: "POST",
            body: formData
        });

        const data = await response.json();
        console.log(data)
        const errorBox = document.getElementById("errorMessage");

        if (data.success) {
            showToast(data.title, data.message);
            setTimeout(() => {
                window.location.href = "/login";
            }, 3000);
        } else {
            errorBox.style.display = "block";
            errorBox.textContent = data.message;
        }

    } catch (error) {
        console.error("Error en la petición:", error);
    }
});