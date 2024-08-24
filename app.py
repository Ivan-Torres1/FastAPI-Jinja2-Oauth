from fastapi import FastAPI,Request,HTTPException, Depends
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



# -------------------------------REGISTER USERS-----------------------------------

@app.get("/register-1", response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("register_login/registerP1.html",{"request":request})


@app.get("/register-2", response_class=HTMLResponse)
async def register(request:Request):
    return templates.TemplateResponse("register_login/registerP2.html",{"request":request})

# ----------
@app.post("/register/user_complete")
async def form_1(user_complete : dict):
    print(user_complete)
    return {"sucess": True,"First Section": "Complete"}
    






# PROBAR CON MANEJARLO DESDE EL JS