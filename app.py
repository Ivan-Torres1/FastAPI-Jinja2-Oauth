from fastapi import FastAPI,Request,HTTPException
from fastapi.responses import HTMLResponse,JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from conexionDB import *




"""
By Ivan Torres
Hacer una aplicacion donde insertando el ID de un usuario,puedas tener una web con todos sus datos

4/7

"""


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def saludo():
    return "HELLO WORLD"


@app.get("/user/{id}",response_class=HTMLResponse)
async def infoUser(id:int,request:Request):
    user = get_user(id)
    if user is None:
        return templates.TemplateResponse("msgerror.html",{"request":request,"number_error":401})
    else:
        user["request"] = request
        return templates.TemplateResponse("user/infoUser.html",user)
        
 
@app.get("/user/contact/{id}",response_class=HTMLResponse)
async def contact(id,request:Request):
    aditional_info_user = get_infoUser(id)
    if aditional_info_user is None:
        return templates.TemplateResponse("msgerror.html",{"request":request,"number_error":404})
    else:
        aditional_info_user["request"] = request
        return templates.TemplateResponse("user/contact.html",aditional_info_user)


@app.get("/iniciosesion",response_class=HTMLResponse)
async def sesion(request:Request):
    return templates.TemplateResponse("register_login/session.html",{"request":request})



# -----------------------------------

@app.get("/register-1", response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("register_login/registerP1.html",{"request":request})

@app.get("/register-2", response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("register_login/registerP2.html",{"request":request})

# ----------
@app.post("/register/user")
async def form_submit(user: Usuarios):
    print(user)
    # try:
    user = Usuarios(nombre=user.nombre, dni=user.dni,contraseña=user.contraseña)
    post_user(user)
    # except ValidationError as e:

    #     raise HTTPException(status_code=422, detail=e.errors())
    
    return JSONResponse(content={"success": True, "message": "¡User create!"})

