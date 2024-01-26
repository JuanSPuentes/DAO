from typing import List
from fastapi import FastAPI
from fastapi.params import Depends
from starlette.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import models,schemas
from Conexion import SessionLocal,engine
from sqlalchemy.orm import Session

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://angel.mipagina.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

@app.get('/clientes/',response_model=List[schemas.Client])
def show_clientes(db:Session=Depends(get_db)):
    cliente = db.query(models.Client).all()
    return cliente

@app.post('/clientes/',response_model=schemas.Client)
def create_clientes(entrada:schemas.Client,db:Session=Depends(get_db)):
    usuario = models.Client(pais=entrada.pais,
nitorfc=entrada.nitorfc,
nombre=entrada.nombre,
estado=entrada.estado,
razonsocial=entrada.razonsocial,
direcciónfiscal=entrada.direcciónfiscal,
comercialcuenta=entrada.comercialcuenta,
servicios=entrada.servicios,
notas=entrada.notas,

nombrec=entrada.nombrec,
correoc=entrada.correoc,
celularc=entrada.celularc,
cargoc=entrada.cargoc,
departamentoc=entrada.departamentoc,
margenc=entrada.margenc,
notasc=entrada.	notasc,
ciudadc	=entrada.ciudadc,
direccionoficinac=entrada.direccionoficinac,
modalidadentrevistasc=entrada.modalidadentrevistasc,
notasentrevistasc=entrada.notasentrevistasc,

nombrec1=entrada.nombrec1,
correoc1=entrada.correoc1,
celularc1=entrada.celularc1,
cargoc1=entrada.cargoc1,
departamentoc1=entrada.departamentoc1,
margenc1=entrada.margenc1,
notasc1=entrada.notasc1,
ciudadc1=entrada.ciudadc1,
direccionoficinac1=entrada.direccionoficinac1,
modalidadentrevistasc1=entrada.modalidadentrevistasc1,
notasentrevistasc1=entrada.notasentrevistasc1,

    nombrec2 = entrada.nombrec2,
    correoc2 = entrada.correoc2,
    celularc2 = entrada.celularc2,
    cargoc2 = entrada.cargoc2,
    departamentoc2 = entrada.departamentoc2,
    margenc2 = entrada.margenc2,
    notasc2 = entrada.notasc2,
    ciudadc2 = entrada.ciudadc2,
    direccionoficinac2 = entrada.direccionoficinac2,
    modalidadentrevistasc2 = entrada.modalidadentrevistasc2,
    notasentrevistasc2 = entrada.notasentrevistasc2)
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@app.put('/clientes/{cliente_id}',response_model=schemas.Client)
def update_clientes(usuario_id:int,entrada:schemas.UserUpdate,db:Session=Depends(get_db)):
    usuario = db.query(models.Client).filter_by(id=usuario_id).first()
    usuario.nombre=entrada.nombre
    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete('/cliente/{usuario_id}',response_model=schemas.Respuesta)
def delete_cliente(usuario_id:int,db:Session=Depends(get_db)):
    usuario = db.query(models.Client).filter_by(id=usuario_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta

@app.get('/rqs/',response_model=List[schemas.User])
def ver_requerimientos(db:Session=Depends(get_db)):
    usuarios = db.query(models.User).all()
    return usuarios

@app.post('/rqs/',response_model=schemas.User)
def create_requerimientos(entrada:schemas.User,db:Session=Depends(get_db)):
    usuario = models.User(nombre=entrada.nombre,
comercialasignado=entrada.comercialasignado,
cliente=entrada.cliente,
contacto=entrada.contacto,
pais=entrada.pais,
estado=entrada.estado,
prioridad=entrada.prioridad,
dificultad=entrada.dificultad,
                          formatoperfilamiento=entrada.formatoperfilamiento,
                          tiposervicio=entrada.tiposervicio,
                          duracionasignacion=entrada.duracionasignacion,
                          numerovacantes=entrada.numerovacantes,
                          cantidadcandidatosvacantes=entrada.cantidadcandidatosvacantes,
                          fechaingreso=entrada.fechaingreso,
                          jornadalaboral=entrada.jornadalaboral,
                          tipoasignacion=entrada.tipoasignacion,
                          ciudad=entrada.ciudad,
                          direccion=entrada.direccion,
                          equipodecomputo=entrada.equipodecomputo,
                          carrerabase=entrada.carrerabase,
                          niveldeformacion=entrada.niveldeformacion,
                          pruebatecnica=entrada.pruebatecnica,
                          detalleprueba=entrada.detalleprueba,
                          pruebapsicotecnica=entrada.pruebapsicotecnica,
                          otroidioma=entrada.otroidioma,
                          certificaciones=entrada.certificaciones,
                          requieretarjetaprofesional=entrada.requieretarjetaprofesional,
                          conocimientostecnicos=entrada.conocimientostecnicos,
                          detalleperfil=entrada.detalleperfil,
                          conocimientosrequeridos=entrada.conocimientosrequeridos,
                          aosexperiencia=entrada.aosexperiencia,
                          habilidadesblandas=entrada.habilidadesblandas,
                          umbraltarifario=entrada.umbraltarifario,
                          prestacionservicios=entrada.prestacionservicios,
                          nominaobraolabor=entrada.nominaobraolabor,
                          tarifamargen=entrada.tarifamargen,
                          notascomerciales=entrada.notascomerciales,
                          notasgenerales=entrada.notasgenerales,

                          numerovacantesh=entrada.numerovacantesh,
                          candidatosvacantesh=entrada.candidatosvacantesh,
                          fechaingresoh=entrada.fechaingresoh,
                          jornadalaboralh=entrada.jornadalaboralh,
                          tipoasignacionh=entrada.tipoasignacionh,
                          ciudadh=entrada.ciudadh,
                          direccionasignacionh=entrada.direccionasignacionh,
                          equipocomputoh=entrada.equipocomputoh,
                          formacionprofesionalh=entrada.formacionprofesionalh,
                          carrerabaseh=entrada.carrerabaseh,
                          nivelformacionh=entrada.nivelformacionh,
                          pruebatecnicah=entrada.pruebatecnicah,
                          detallepruebah=entrada.detallepruebah,
                          pruebapsicotecnicah=entrada.pruebapsicotecnicah,
                          otroidiomah=entrada.otroidiomah,
                          certificacionesh=entrada.certificacionesh,
                          tarjetaprofesionalh=entrada.tarjetaprofesionalh,
                          conocimientostecnicosh=entrada.conocimientostecnicosh,
                          detalleperfilh=entrada.detalleperfilh,
                          conocimientosrequeridosh=entrada.conocimientosrequeridosh,
                          aosexperienciah=entrada.aosexperienciah,
                          habilidadesblandash=entrada.habilidadesblandash,
                          salariocandidatoh=entrada.salariocandidatoh,
                          tipocontratoh=entrada.tipocontratoh,
                          porcentajefeeh=entrada.porcentajefeeh,
                          notascomercialesh=entrada.notascomercialesh,
                          notasgeneralesh=entrada.notasgeneralesh

                          )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario

@app.put('/rqs/{rq_id}',response_model=schemas.User)
def update_requerimientos(usuario_id:int,entrada:schemas.UserUpdate,db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=usuario_id).first()
    usuario.nombre=entrada.nombre
    db.commit()
    db.refresh(usuario)
    return usuario

@app.delete('/usuarios/{usuario_id}',response_model=schemas.Respuesta)
def delete_requerimientos(usuario_id:int,db:Session=Depends(get_db)):
    usuario = db.query(models.User).filter_by(id=usuario_id).first()
    db.delete(usuario)
    db.commit()
    respuesta = schemas.Respuesta(mensaje="Eliminado exitosamente")
    return respuesta