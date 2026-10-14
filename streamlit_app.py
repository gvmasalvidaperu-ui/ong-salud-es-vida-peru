
import streamlit as st
import datetime
st.set_page_config(page_title="MAS VIDA PERU",layout="centered")
st.title("ONG SALUD ES VIDA PERU")
st.header("FICHA MAS VIDA - SEDE PERU")
st.success("App Oficial - Programa Preventivo")
nombre=st.text_input("Nombre Completo")
dni=st.text_input("DNI")
edad=st.number_input("Edad",0,110,1)
peso=st.number_input("Peso kg",0.0,300.0,1.0)
talla=st.number_input("Talla m",0.0,3.0,0.01)
imc=0
if peso>0 and talla>0:
    imc=peso/(talla*talla)
    st.metric("IMC",f"{imc:.2f}")
fecha=st.date_input("Fecha",datetime.date.today())
obs=st.text_area("Observaciones")
if st.button("GENERAR FICHA"):
    st.balloons()
    st.success(f"Ficha {nombre} DNI {dni}")
    st.write(f"IMC {imc:.2f} Fecha {fecha}")
    st.write(obs)
