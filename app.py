from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import conexionDB as c




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
async def page(id,request:Request):
    user = c.get_user(id)
    if user is None:
        return templates.TemplateResponse("msgerror.html",{"request":request,"number_error":404})
    else:
        user["request"] = request
        return templates.TemplateResponse("index.html",user)
        

@app.get("/user/contact",response_class=HTMLResponse)
async def contact(request:Request):
    return templates.TemplateResponse("contact.html",information)


@app.get("/user/sesion",response_class=HTMLResponse)
async def sesion(request:Request):
    return templates.TemplateResponse("iniciosesion.html",{"request":request})



