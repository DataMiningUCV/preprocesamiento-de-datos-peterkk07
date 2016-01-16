# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal
"""


# PEDRO FLORES  CI:20050936
import csv as csv
import os
import pandas as pd
from pandas import DataFrame
from pandas import read_csv
import datetime
import pandas.io.data
import numpy as np
import re
import datetime
import time
from datetime import datetime,date
import matplotlib.pyplot as plt


os.getcwd() # obtener dir
os.chdir("/home/pedro/Descargas") # cambiarlo

#Funciones para extraer los datos numeros de expresiones alfanumericas    
def extraer_numero(str):
    if str is None or str=='':
        return 0

    out_number=''
    out_number2=''
    for ele in (str):
        if ele.isdigit():
            out_number+=ele
        
        else:
            
            for ele2 in (out_number):
                if ele2.isdigit():
                    out_number2+=ele2
            
            return float(out_number2)
       
        
    return float(out_number)
    

def extraer_numero_2(str2):
    if str2 is None or str=='':
        return 0
    
    out_number=''
    for ele in (str2):
        if ele.isdigit():
            out_number+=ele
        
        
    return float(out_number)


df= pd.read_csv('data.csv')

#Se eliminan las siguientes columnas:
#La primera, la cual tenia informaccion irrelevante
#Edad
#Se encuentra usted realizando una actividad que le genere ingresos
#En caso afirmativo, indique el tipo de actividad y frecuencia

df.pop(df.columns[0])
df.pop(df.columns[3])
df.pop(df.columns[30])
df.pop(df.columns[30])


#renombramos las columnas para mejor compresion y manejo de variables en python

df.rename(columns={'Indique.el.Período.Académico.a.renovar':'Periodo_Academico_a_Renovar','Cédula.de.Identidad': 'CI','Fecha.de.Nacimiento..colocar.sólo.datos.numéricos.': 'Fecha_de_nacimiento_colocar_solo_datos_numericos','Estado.Civil': 'Estado_Civil','Año.de.Ingreso.a.la.UCV': 'Anio_de_Ingreso_a_la_UCV','Modalidad.de.Ingreso.a.la.UCV': 'Modalidad_de_Ingreso_a_la_UCV','Semestre.que.cursa': 'Semestre_que_cursa','Ha.cambiado.usted.de.dirección.': 'Ha_cambiado_de_direccion','De.ser.afirmativo..indique.el.motivo': 'De_ser_afirmativo_indique_el_motivo', 'Número.de.materias.inscritas.en.el.semestre.o.año.anterior':'Numero_de_materias_inscritas_en_el_semestre_o_anio_anterior','Número.de.materias.aprobadas.en.el.semestre.o.año.anterior': 'Numero_de_materias_aprobadas_en_el_semestre_o_anio_anterior','Número.de.materias.retiradas.en.el.semestre.o.año.anterior': 'Numero_de_materias_retiradas_en_el_semestre_o_anio_anterior', 'Número.de.materias.reprobadas.en.el.semestre.o.año.anterior': 'Numero_de_materias_reprobadas_en_el_semestre_o_anio_anterior','Promedio.ponderado.aprobado': 'Promedio_ponderado_aprobado','Si.reprobó.una.o.más.materias.indique.el.motivo': 'Si_reprobo_una_o_mas_materias_indique_el_motivo','Número.de.materias.inscritas.en.el.semestre.en.curso': 'Numero_de_materias_inscritas_en_el_semestre_en_curso','X.Estás.realizado.tesis...trabajo.de.grado.o.pasantías.de.grado.': 'Esta_realizando_tesis_trabajo_de_grado_o_pasantias_de_grado','Tesis...trabajo.de.grado.o.pasantías.de.grado': 'Tesis_trabajo_de_grado_o_pasantias_de_grado','Lugar.donde.reside.mientras.estudia.en.el.Universidad': 'Lugar_donde_reside_mientras_estudia_en_la_universidad','Personas.con.las.cuales.usted.vive..mientras.estudia.en.la.universidad.': 'Personas_con_quien_vive_mientras_estudia_en_la_universidad','Tipo.de.vivienda.donde.reside.mientras.estudia.en.la.universidad': 'Tipo_de_vivienda_donde_reside_mientras_estudia_en_la_universidad', 'En.caso.de.vivir.en.habitación.alquilada.o.residencia.estudiantil..indique.el.monto.mensual.': 'En_caso_de_vivir_en_habitacion_alquilada_o_residencia_estudiantil_indique_el_monto','Dirección.donde.se.encuentra.ubicada.la.residencia.o.habitación.alquilada': 'Direccion_de_residencia_o_habitacion_alquilada','X.Contrajo.Matrimonio.': 'Contrajo_matrimonio','X.Ha.solicitado.algún.otro.beneficio.a.la.Universidad.u.otra.Institución.': 'Ha_solicitado_beneficio_a_la_universidad_u_otra_institucion', 'En.caso.afirmativo.señale..año.de.la.solicitud..institución.y.motivo': 'En_caso_afirmativo_indique_anio_de_solicitud_institucion_y_motivo','X.Se.encuentra.usted..realizando.alguna.actividad.que.le.genere.ingresos.': 'Se_encuentra_usted_realizando_alguna_atividad_que_le_genere_ingresos','En.caso.de.ser.afirmativo..indique.tipo.de.actividad.y.su.frecuencia': 'En_caso_de_ser_afirmativo_indique_tipo_de_actividad_y_frecuencia', 'Monto.mensual.de.la.beca': 'Monto_mensual_de_la_beca', 'Aporte.mensual.que.le.brinda.su.responsable.económico': 'Aporte_mensual_que_le_brinda_su_responsable_economico','Aporte.mensual.que.recibe.de.familiares.o.amigos': 'Aporte_mensual_que_recibe_de_familiares_o_amigos','Ingreso.mensual.que.recibe.por.actividades.a.destajo.o.por.horas': 'Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas','Ingreso.mensual.total': 'Ingreso_mensual_total_propio','Alimentación':'Alimentacion_propio', 'Transporte.público': 'Transporte_publico_propio','Gastos.médicos': 'Gastos_medicos_propio', 'Gastos.odontológicos': 'Gastos_odontologicos_propio', 'Gastos.personales': 'Gastos_personales_propio', 'Residencia.o.habitación.alquilada': 'Residencia_o_habitacion_alquilada','Materiales.de.estudio': 'Materiales_de_estudio_','Recreación': 'Recreacion','Otros.gastos': 'Otros_gastos','Total.egresos': 'Total_egresos_propio', 'Indique.quién.es.su.responsable.económico': 'Indique_quien_es_su_responsable_economico', 'Carga.familiar': 'Carga_familiar', 'Ingreso.mensual.de.su.responsable.económico': 'Ingreso_mensual_de_su_responsable_economico','Otros.ingresos': 'Otros_ingresos', 'Total.de.ingresos': 'Total_de_ingresos', 'Alimentación.1': 'Alimentacion_representante', 'Gastos.médicos.1': 'Gastos_medicos_representante', 'Gastos.odontológicos.': 'Gastos_odontologicos_representante', 'Gastos.educativos': 'Gastos_educativos','Servicios.públicos.de.agua..luz..teléfono.y.gas': 'Servicios_publicos_agua_luz_telefono_gas','Otros.gastos.1': 'Otros_gastos_representante','Total.de.egresos': 'Total_de_egresos_representante','Deseamos.conocer.la.opinión.de.nuestros.usuarios..para.mejorar.la.calidad.de.los.servicios.ofrecidos.por.el.Dpto..de.Trabajo.Social.OBE': 'opinion_para_mejorar_obe','Sugerencias.y.recomendaciones.para.mejorar.nuestra.atención': 'sugerencias_y_recomendaciones_para_mejorar_nuestra_atencion'},inplace=True)


#me aseguro de que solo hayan valores numericos
df.Otros_ingresos=df.Otros_ingresos.fillna('0')

for i in range(len(df.Otros_ingresos)):
    if not(df.Otros_ingresos[i].isdigit()):
        df.Otros_ingresos[i]=0
    

#aplico la funcion extraer numero para obtener numeros de columnas donde hay strings con expresiones numericas y caracteres (24bs)

df.Numero_de_materias_aprobadas_en_el_semestre_o_anio_anterior=df.Numero_de_materias_aprobadas_en_el_semestre_o_anio_anterior.apply(extraer_numero_2)
df.Servicios_publicos_agua_luz_telefono_gas=df.Servicios_publicos_agua_luz_telefono_gas.fillna('0')
df.Servicios_publicos_agua_luz_telefono_gas=df.Servicios_publicos_agua_luz_telefono_gas.apply(extraer_numero)
df.Condominio=df.Condominio.fillna('0')
df.Condominio=df.Condominio.apply(extraer_numero)
df.Alimentacion_representante=df.Alimentacion_representante.apply(extraer_numero)


#sustituyo strings y valores nulos por ceros
df.Vivienda=df.Vivienda.fillna('0')
for i,row in enumerate(df.Vivienda.values):
    
    if df.Vivienda[i].isalpha():
        df.Vivienda[i]=0


df.Gastos_medicos_representante=df.Gastos_medicos_representante.fillna('0')
for i,row in enumerate(df.Gastos_medicos_representante.values):
    if df.Gastos_medicos_representante[i].isalpha():
         df.Gastos_medicos_representante[i]=0
    

#descarto las columnas en las que no coincide el numero de materias inscritas, con la suma de las aprobadas, retiradas y reprobadas

df=df[df.Numero_de_materias_inscritas_en_el_semestre_o_anio_anterior==df.Numero_de_materias_aprobadas_en_el_semestre_o_anio_anterior+df.Numero_de_materias_retiradas_en_el_semestre_o_anio_anterior+df.Numero_de_materias_reprobadas_en_el_semestre_o_anio_anterior]
df=df.reset_index(drop=True)

#Se unifica el formato de fechas y se descartan las que no cumplan un formato valido
a='/'
b='-'

for i,row in enumerate(df.Fecha_de_nacimiento_colocar_solo_datos_numericos.values):
    if(df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i].find(a)==-1 or df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i].find(b)==0):
        df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i]=0

df=df[df.Fecha_de_nacimiento_colocar_solo_datos_numericos!=0]

#reseteo los indices cada vez q filtro algo
df=df.reset_index(drop=True)


#reemplazo - por / para que todas tengan el mismo formato
c='-'
d='/'
for i,row in enumerate(df.Fecha_de_nacimiento_colocar_solo_datos_numericos.values):
    df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i]=df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i].replace(d,c)


#llevo todo al mismo formato dd mm aaaa

df.Fecha_de_nacimiento_colocar_solo_datos_numericos

formater_string='%d-%m-%y'
formater_string2='%d-%m-%Y'

for i,row in enumerate(df.Fecha_de_nacimiento_colocar_solo_datos_numericos.values):
    
    if len(df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i])==8:
        
        date_time_object=datetime.strptime(df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i],formater_string)
        date_object=date_time_object.date()
        y=date_object.strftime('%d-%m-%Y')
        df.Fecha_de_nacimiento_colocar_solo_datos_numericos[i]=y
        
        #acomodo los periodos a renovar

for i,row in enumerate(df.Periodo_Academico_a_Renovar.values):
    df.Periodo_Academico_a_Renovar[i]=df.Periodo_Academico_a_Renovar[i].lower()


s1='I-2014'
s2='II-2014'
s3='I-2015'
s4='II-2015'

for i,row in enumerate(df.Periodo_Academico_a_Renovar.values):
    
    if (df.Periodo_Academico_a_Renovar[i].find('pri')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2014')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s1
        
    elif(df.Periodo_Academico_a_Renovar[i].find('seg')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2014')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s2
        
    elif(df.Periodo_Academico_a_Renovar[i].find('pri')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2015')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s3
        
    elif(df.Periodo_Academico_a_Renovar[i].find('seg')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2015')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s4
        
    elif(df.Periodo_Academico_a_Renovar[i].find('01s')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2014')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s1
        
    elif(df.Periodo_Academico_a_Renovar[i].find('02s')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2014')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s2
        
    elif(df.Periodo_Academico_a_Renovar[i].find('01s')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2015')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s3
        
    elif(df.Periodo_Academico_a_Renovar[i].find('02s')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2015')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s4
        
    elif(df.Periodo_Academico_a_Renovar[i].find('I-')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2014')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s1
        
    elif(df.Periodo_Academico_a_Renovar[i].find('I-')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2015')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s3
        
    elif(df.Periodo_Academico_a_Renovar[i].find('II')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2014')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s2
        
    elif(df.Periodo_Academico_a_Renovar[i].find('II')!=-1 and df.Periodo_Academico_a_Renovar[i].find('2015')!=-1):
        df.Periodo_Academico_a_Renovar[i]=s1
        
    else:
        df.Periodo_Academico_a_Renovar[i]=0
        
#elimino las filas con formato invalido    y se resetean los indices     
df=df[df.Periodo_Academico_a_Renovar!=0]   

df=df.reset_index(drop=True) 
        
      
#acomodo los promedios para que tengan el mismo formato

for i,row in enumerate(df.Promedio_ponderado_aprobado.values):
    if df.Promedio_ponderado_aprobado[i]>20 and df.Promedio_ponderado_aprobado[i]<20000:
        df.Promedio_ponderado_aprobado[i]=df.Promedio_ponderado_aprobado[i]/1000
    
    elif df.Promedio_ponderado_aprobado[i]>20000:
        df.Promedio_ponderado_aprobado[i]=df.Promedio_ponderado_aprobado[i]/10000     

#acomodo la eficiencia para que tengan el mismo formato

for j,row in enumerate(df.Eficiencia.values):
    
    if df.Eficiencia[j]>1 and df.Eficiencia[j]<=1000:
        df.Eficiencia[j]=df.Eficiencia[j]/1000
        
    elif df.Eficiencia[j]>1000 and df.Eficiencia[j]<10000:
        df.Eficiencia[j]=df.Eficiencia[j]/10000
        
    elif df.Eficiencia[j]>10000 and df.Eficiencia[j]<100000:
        df.Eficiencia[j]=df.Eficiencia[j]/100000
        
         
#Imputar zeros a los siguientes campos de gastos del estudiante que contengan Nan

df.Aporte_mensual_que_le_brinda_su_responsable_economico=df.Aporte_mensual_que_le_brinda_su_responsable_economico.fillna(0)
df.Aporte_mensual_que_recibe_de_familiares_o_amigos=df.Aporte_mensual_que_recibe_de_familiares_o_amigos.fillna(0)
df.Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas=df.Ingreso_mensual_que_recibe_por_actividades_a_destajo_o_por_horas.fillna(0)
df.Gastos_odontologicos_propio=df.Gastos_odontologicos_propio.fillna(0)
df.Residencia_o_habitacion_alquilada=df.Residencia_o_habitacion_alquilada.fillna(0)
df.Transporte_publico_propio=df.Transporte_publico_propio.fillna(0)

#Imputar Zeros a los siguientes campos de gastos del representante economico que contengan Nan

df.Ingreso_mensual_de_su_responsable_economico=df.Ingreso_mensual_de_su_responsable_economico.fillna(0)
df.Otros_ingresos=df.Otros_ingresos.fillna(0)
df.Transporte=df.Transporte.fillna(0)
df.Gastos_odontologicos_representante=df.Gastos_odontologicos_representante.fillna(0)
df.Gastos_educativos=df.Gastos_educativos.fillna(0)
df.Condominio=df.Condominio.fillna(0)
df.Otros_gastos_representante=df.Otros_gastos_representante.fillna(0)


#Imputar la media a los siguientes campos pertenecientes a gastos del estudiante que contengan valores NaN

df.Alimentacion_propio=df.Alimentacion_propio.fillna(round(df.Alimentacion_propio.median(),2))
df.Gastos_medicos_propio=df.Gastos_medicos_propio.fillna(round(df.Gastos_medicos_propio.median(),2))
df.Gastos_personales_propio=df.Gastos_personales_propio.fillna(round(df.Gastos_personales_propio.median(),2))
df.Recreacion=df.Recreacion.fillna(round(df.Recreacion.median(),2))
df.Otros_gastos=df.Otros_gastos.fillna(round(df.Otros_gastos.median(),2))


#Imputar la media a los siguientes campos pertenecientes a gastos de responsable economico

df.Alimentacion_representante=df.Alimentacion_representante.fillna(round(df.Alimentacion_representante.mean(),2))


#Se llevan a un  mismo formato los gastos
x1='bs'
x2=''
for j,row in enumerate(df.Ingreso_mensual_de_su_responsable_economico.values):
    if df.Ingreso_mensual_de_su_responsable_economico[j].find('bs')!=-1:
        df.Ingreso_mensual_de_su_responsable_economico[j]=df.Ingreso_mensual_de_su_responsable_economico[j].replace(x1,x2)
        
for j,row in enumerate(df.Total_de_ingresos.values):
    if df.Total_de_ingresos[j].find('bs')!=-1:
        df.Total_de_ingresos[j]=df.Total_de_ingresos[j].replace(x1,x2)

for j,row in enumerate(df.Transporte.values):
    if df.Transporte[j].find('bs')!=-1:
        df.Transporte[j]=df.Transporte[j].replace(x1,x2)    
    

for j,row in enumerate(df.Gastos_medicos_representante.values):
    if df.Gastos_medicos_representante[j].find('bs')!=-1:
        df.Gastos_medicos_representante[j]=df.Gastos_medicos_representante[j].replace(x1,x2)  
        

for j,row in enumerate(df.Total_de_egresos_representante.values):
    if df.Total_de_egresos_representante[j].find('bs')!=-1:
        df.Total_de_egresos_representante[j]=df.Total_de_egresos_representante[j].replace(x1,x2) 



for j,row in enumerate(df.Estado_Civil.values):
    if df.Estado_Civil[j].find('Casado')==-1 and df.Estado_Civil[j].find('Soltero')==-1:
        df.Estado_Civil[j]='Soltero (a)'
        
#Se sustiyen las opciones con valores numericos

for j,row in enumerate(df.Estado_Civil.values):
    if df.Estado_Civil[j].find('Casado')!=-1:
        df.Estado_Civil[j]=1
        
    elif df.Estado_Civil[j].find('Soltero')!=-1:
        df.Estado_Civil[j]=0


for j,row in enumerate(df.Sexo.values):
    if df.Sexo[j].find('Femenino')!=-1:
        df.Sexo[j]=1
        
    elif df.Sexo[j].find('Masculino')!=-1:
        df.Sexo[j]=0


for j,row in enumerate(df.Escuela.values):
    if df.Escuela[j].find('Enfermería')!=-1:
        df.Escuela[j]=1
        
    elif df.Escuela[j].find('Bioanálisis')!=-1:
        df.Escuela[j]=0



for j,row in enumerate(df.Modalidad_de_Ingreso_a_la_UCV.values):
    if df.Modalidad_de_Ingreso_a_la_UCV[j].find('Prueba Interna y/o propedéutico')!=-1:
        df.Modalidad_de_Ingreso_a_la_UCV[j]=0
        
    elif df.Modalidad_de_Ingreso_a_la_UCV[j].find('Asignado OPSU')!=-1:
        df.Modalidad_de_Ingreso_a_la_UCV[j]=1

         
    elif df.Modalidad_de_Ingreso_a_la_UCV[j].find('Convenios Internos')!=-1:
        df.Modalidad_de_Ingreso_a_la_UCV[j]=2



for j,row in enumerate(df.Ha_cambiado_de_direccion.values):
    if df.Ha_cambiado_de_direccion[j].find('No')!=-1:
        df.Ha_cambiado_de_direccion[j]=0
        
    elif df.Ha_cambiado_de_direccion[j].find('Si')!=-1:
        df.Ha_cambiado_de_direccion[j]=1



for j,row in enumerate(df.Esta_realizando_tesis_trabajo_de_grado_o_pasantias_de_grado.values):
    if df.Esta_realizando_tesis_trabajo_de_grado_o_pasantias_de_grado[j].find('No')!=-1:
        df.Esta_realizando_tesis_trabajo_de_grado_o_pasantias_de_grado[j]=0
        
    elif df.Esta_realizando_tesis_trabajo_de_grado_o_pasantias_de_grado[j].find('Si')!=-1:
        df.Esta_realizando_tesis_trabajo_de_grado_o_pasantias_de_grado[j]=1


for j,row in enumerate(df.Contrajo_matrimonio.values):
    if df.Contrajo_matrimonio[j].find('No')!=-1:
        df.Contrajo_matrimonio[j]=0
        
    elif df.Contrajo_matrimonio[j].find('Si')!=-1:
        df.Contrajo_matrimonio[j]=1


for j,row in enumerate(df.Ha_solicitado_beneficio_a_la_universidad_u_otra_institucion.values):
    if df.Ha_solicitado_beneficio_a_la_universidad_u_otra_institucion[j].find('No')!=-1:
        df.Ha_solicitado_beneficio_a_la_universidad_u_otra_institucion[j]=0
        
    elif df.Ha_solicitado_beneficio_a_la_universidad_u_otra_institucion[j].find('Si')!=-1:
        df.Ha_solicitado_beneficio_a_la_universidad_u_otra_institucion[j]=1



df.to_csv('minable.csv')

   