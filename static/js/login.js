document.getElementById("loginForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const form = e.target;
    const formData = new FormData(form);

    const response = await fetch("/api/login", {
        method: "POST",
        body: formData
    });

    const data = await response.json();

    const errorBox = document.getElementById("errorMessage");
    if (data.success) {
        window.location.href = "/success-login";
    } else {
        errorBox.style.display = "block";
        errorBox.textContent = data.message;
    }

})