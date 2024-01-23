from typing import Optional
from pydantic import BaseModel

class Client(BaseModel):
    id:Optional[int]
    estado:Optional[int]
    pais:Optional[str]
    nitorfc:Optional[str]
    nombre:Optional[str]
    razonsocial:Optional[str]
    direcciónfiscal:Optional[str]
    comercialcuenta:Optional[str]
    servicios:Optional[str]
    notas:Optional[str]

    nombrec:Optional[str]
    correoc:Optional[str]
    celularc:Optional[str]
    cargoc:Optional[str]
    departamentoc:Optional[str]
    margenc:Optional[str]
    notasc:Optional[str]
    ciudadc:Optional[str]
    direccionoficinac:Optional[str]
    modalidadentrevistasc:Optional[str]
    notasentrevistasc:Optional[str]

    nombrec1:Optional[str]
    correoc1:Optional[str]
    celularc1:Optional[str]
    cargoc1:Optional[str]
    departamentoc1:Optional[str]
    margenc1:Optional[str]
    notasc1:Optional[str]
    ciudadc1:Optional[str]
    direccionoficinac1:Optional[str]
    modalidadentrevistasc1:Optional[str]
    notasentrevistasc1:Optional[str]

    nombrec2:Optional[str]
    correoc2:Optional[str]
    celularc2:Optional[str]
    cargoc2:Optional[str]
    departamentoc2:Optional[str]
    margenc2:Optional[str]
    notasc2:Optional[str]
    ciudadc2:Optional[str]
    direccionoficinac2:Optional[str]
    modalidadentrevistasc2:Optional[str]
    notasentrevistasc2:Optional[str]



    class Config:
        orm_mode =True

class User(BaseModel):
    id:Optional[int]
    nombre:str
    comercialasignado:str
    cliente:str
    contacto:str
    pais:str
    estado:int
    prioridad:str
    dificultad:str
    formatoperfilamiento:str
    tiposervicio:str
    duracionasignacion:str
    numerovacantes:str
    cantidadcandidatosvacantes:str
    fechaingreso:str
    jornadalaboral:str
    tipoasignacion:str
    ciudad:str
    direccion:str
    equipodecomputo:str
    carrerabase:str
    niveldeformacion:str
    pruebatecnica:str
    detalleprueba:str
    pruebapsicotecnica:str
    otroidioma:str
    certificaciones:str
    requieretarjetaprofesional:str
    conocimientostecnicos:str
    detalleperfil:str
    conocimientosrequeridos:str
    aosexperiencia:str
    habilidadesblandas:str
    umbraltarifario:str
    prestacionservicios:str
    nominaobraolabor:str
    tarifamargen:str
    notascomerciales:str
    notasgenerales:str

    numerovacantesh:str
    candidatosvacantesh:str
    fechaingresoh:str
    jornadalaboralh:str
    tipoasignacionh:str
    ciudadh:str
    direccionasignacionh:str
    equipocomputoh:str
    formacionprofesionalh:str
    carrerabaseh:str
    nivelformacionh:str
    pruebatecnicah:str
    detallepruebah:str
    pruebapsicotecnicah:str
    otroidiomah:str
    certificacionesh:str
    tarjetaprofesionalh:str
    conocimientostecnicosh:str
    detalleperfilh:str
    conocimientosrequeridosh:str
    aosexperienciah:str
    habilidadesblandash:str
    salariocandidatoh:str
    tipocontratoh:str
    porcentajefeeh:str
    notascomercialesh:str
    notasgeneralesh:str

    class Config:
        orm_mode =True

class UserUpdate(BaseModel):
    nombre:str


    class Config:
        orm_mode =True

class Respuesta(BaseModel):
    mensaje:str



