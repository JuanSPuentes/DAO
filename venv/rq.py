from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI ()

class requerimiento(BaseModel):

    nombre: str
    apellido: str
    edad: int
    estadoCivil: Optional[str]

@app. get ("/")
def index():
    return {"message":"Requerimientos"}

@app. get ("/requerimientos/(id}")
def mostrar_requerimiento(id: int):
    return {"data": id}

@app. post ("/requerimientos")
def insertar_requerimiento(requerimiento: requerimiento):
    return {"message": f"requerimiento {requerimiento. nombre} insertado"}