import pandas as pd
import matplotlib.pyplot as plt

def cargar_informacion(nombre_archivo:str):
    covid_dpto=pd.read_excel(nombre_archivo)
    columnas_de_interes=["fecha reporte web","Nombre municipio","Edad","Unidad de medida de edad","Sexo","Tipo de contagio","Fecha de muerte"]
    covid_dpto=covid_dpto[columnas_de_interes]
    return covid_dpto

def filtrar_por_municipio(df_completo,municipio:str):
    df_municipio=df_completo[df_completo["Nombre municipio"]==municipio]
    return df_municipio

def agrupar_por_fecha(df_completo):
    df_agrupado=df_completo.groupby("fecha reporte web")["Edad"].agg(contagios="count").reset_index()
 
    return df_agrupado

def obtener_lista_municipios(df_completo):
    lista_municipios=df_completo['Nombre municipio'].unique().tolist()
    lista_municipios=sorted(lista_municipios)
    return lista_municipios

def graficar(fig,df_completo,var_x:str,var_y:str,titulo:str,x_label:str,y_label:str):
    plano=fig.gca()
    plano.plot(df_completo[var_x],df_completo[var_y])
    plano.set_title(titulo, fontsize = 12)
    plano.set_xlabel(x_label, fontsize = 12)
    plano.set_ylabel(y_label, color = 'blue', fontsize = 12)
    plano.grid(True)
    return(fig)
    

    
    
