import streamlit as st
import pickle
import numpy as np
import pandas as pd
import sklearn

pickle_in = open("classifier.pkl", "rb")

classificator = pickle.load(pickle_in)  # our model


def result_stars(Temperature, Luminosity, Radius, Absolute_magnitude,  Star_color, Spectral_Class):
    prediction = classificator.predict(
        [[Temperature, Luminosity, Radius, Absolute_magnitude, Star_color, Spectral_Class]])
    print(prediction)
    return prediction


def main():

    st.title("Classificació d'estrelles amb machine learning")
    st.text("Treball de recerca Pau Iznardo")

    int_Temperature = st.text_input("Temperature")
    int_Luminosity = st.text_input("Luminosity")
    int_Radius = st.text_input("Radius")
    int_Absolute_magnitude = st.text_input("Absolute magnitude")
    int_Star_color = st.text_input("Star color")
    int_Spectral_Class = st.text_input("Spectral Class")

    result = ""
    if st.button("predict"):
        result = result_stars(int_Temperature, int_Luminosity, int_Radius,
                              int_Absolute_magnitude, int_Star_color, int_Spectral_Class)
    if result >= 0 and result <= 0.499:
        st.success("EL TIPUS D'ESTRELLA ÉS NANA MARRO {}".format(result))
    if result >= 0.5 and result <= 1.499:
        st.success("EL TIPUS D'ESTRELLA ÉS NANA VERMELLA {}".format(result))
    if result >= 1.5 and result <= 2.499:
        st.success("EL TIPUS D'ESTRELLA ÉS NANA BLANCA {}".format(result))
    if result >= 2.5 and result <= 3.499:
        st.success(
            "EL TIPUS D'ESTRELLA ÉS  SEQÜÈNCIA PRINCIPAL {}".format(result))
    if result >= 3.5 and result <= 4.499:
        st.success("EL TIPUS D'ESTRELLA ÉS SUPERGEGANT {}".format(result))
    if result >= 4.5 and result <= 5:
        st.success("EL TIPUS D'ESTRELLA ÉS HIPERGEGANT {}".format(result))


if __name__ == '__main__':
    main()
