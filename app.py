from fastapi import FastAPI,Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
"""
By Ivan Torres
Hacer una aplicacion donde insertando el ID de un usuario,puedas tener una web con todos sus datos

"""


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/user/",response_class=HTMLResponse)
async def page(request: Request):
    information = {"request": request,
    "nameUser": "Ivan Torres",
    "cargoUser": "Lider",
    "idUser": "1",
    "permisoLevelUser": "9",
    "userDni": 47103883}
    return templates.TemplateResponse("index.html",information)


@app.get("/user/contact",response_class=HTMLResponse)
async def contact(request:Request):
    information = {"request": request,
    "nameUser": "Ivan Torres",
    "userGmail": "ivantorres2076@gmail.com",
    "numberUser": "341 349 8566",
    "auxNumberUser": "341 386 8750",
    "igUser": "ivan.torres77",
    "idUser": 1}
    return templates.TemplateResponse("contact.html",information)





