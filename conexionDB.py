from typing import Optional, List
from sqlmodel import Field, SQLModel, Relationship,create_engine,Session,select
from envparse import Env
import mysql.connector

pathEnv = "config/.env"
env = Env()
env.read_envfile(pathEnv)


host = env.str("host")
database = env.str("database")
userDB = env.str("user")
password = env.str("password")

urlBD = f"mysql+mysqlconnector://{userDB}:{password}@{host}/{database}"

engine = create_engine(url=urlBD,echo=True)


class Usuarios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    cargo_empresa: Optional[str] = None
    nivel_permisos: Optional[int] = None
    dni: str
    contraseña: str

class Perfil_usuarios(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    gmail: Optional[str] = None
    telefono: Optional[str] = None
    telefono_auxiliar: Optional[str] = None
    redes_sociales: Optional[str] = None



def get_user(id:int):
    with Session(engine) as session:
        selection = select(Usuarios).where(Usuarios.id == id)
        user = session.exec(selection).first()
        if user is None:
            return None
        else:
            return user.dict()


def get_infoUser(id:int):
    with Session(engine) as session:
        selection = select(Perfil_usuarios).where(Perfil_usuarios.id == id)
        user = session.exec(selection).first()
        if user is None:
            return None
        else:
            return user.dict()


def verify_user(user_dni):
    with Session(engine) as session:
        date = session.exec(select(Usuarios.id).where(Usuarios.dni == user_dni)).first()

    if date:
        raise HTTPException(status_code=406,
                        detail="USUARIO YA CREADO.",
                        headers={"ERROR":"NOT ACCEPTABLE"})


def post_user(user):
    verify_user(user_dni=user.dni)
    with Session(engine) as session:
        user_post = Usuarios(nombre=user.nombre,dni=user.dni,contraseña=user.contraseña)
        session.add(user_post)
        session.commit()
        
        



# Prueba
# with Session(engine) as session:
#     selection = select(Usuarios,Perfil_usuarios).join(Perfil_usuarios,
#     Perfil_usuarios.usuario_id == Usuarios.id)
#     user = session.exec(selection)
#     print("----------------------------------------")
#     print("----------------------------------------")
#     print(user)
#     print("----------------------------------------")
#     print("----------------------------------------")






#     session.add(user)
#     session.add(infoUser)
#     session.commit()   





