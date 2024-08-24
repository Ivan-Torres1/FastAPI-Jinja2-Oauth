document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formUser");

    form.addEventListener("submit", async function(event) {
        event.preventDefault(); 
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        localStorage.setItem("formUser", JSON.stringify(data));
        
        window.location.href = "/register-2";

    });
});

