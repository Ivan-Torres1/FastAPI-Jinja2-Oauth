document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formUser");

    form.addEventListener("submit", async function(event) {
        event.preventDefault(); 
        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch("/register/user", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                const result = await response.json();
                alert("Errors: " + result.detail.map(error => `${error.loc[0]}: ${error.msg}`).join("\n"));
            } else {
                const result = await response.json();
                window.location.href = "/register-2";
            }
        } catch (error) {
            console.error("Error:", error);
        }
    });
});

