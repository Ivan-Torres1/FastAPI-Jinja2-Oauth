document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("formPerfil");

    form.addEventListener("submit", async function(event) {
        event.preventDefault(); 
        const formData = new FormData(form);
        const formPerfil  = Object.fromEntries(formData.entries());

        const formUser = JSON.parse(localStorage.getItem("formUser"));
        
        const weDate = {"user":formUser,"perfil":formPerfil}


        try {
            const response = await fetch("/register/user_complete", {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(weDate)  
            });
        
            if (response.ok) {
                console.log("Datos enviados correctamente");
                localStorage.removeItem("formUser")
                
            } else {
                console.error("Error al enviar los datos");
            }
        } catch (error) {
            console.error("Error en la conexión:", error);
        }}
      

    );
});
