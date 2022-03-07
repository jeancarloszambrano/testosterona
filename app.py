import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


paginas = ['Home', 'Treinamento','Modelo']

st.sidebar.subheader('Páginas')
pagina = st.sidebar.selectbox('Menu', paginas)

if pagina == 'Home':
	image = Image.open('logo.jpg')
	st.image(image, use_column_width=True, use_column_height=True)
	st.title('APP PARA PREVER DEFICIÊNCIA DE TESTOSTERONA')
	st.markdown('---')
	st.write('A testosterona é o hormônio sexual mais importante entre os homens e afeta significativamente'+
		 'o bem-estar físico e psicológico dos homens. Pacientes com Síndrome de Deficiência de Testosterona (TDS)'+
		 'podem apresentar hipogonadismo, uma condição definida por baixos níveis séricos de testosterona combinado'+
		 'com sintomas clínicos. Esta condição está associada a diversas comorbidades, como síndrome metabólica, '+
		 'doenças cardiovasculares, disfunção erétil, aterosclerose, problemas respiratórios, depressão e outras '+
		 'complicações que reduzem os indicadores gerais de saúde.'+
		 'A análise preditiva usando algoritmos de Inteligência Artificial (IA) é de grande interesse para quem'+
		 'trabalha em diagnóstico médico, pois fornece recursos indispensáveis para análise de dados. As regras'+
		 'de predição clínica combinam vários preditores com base nos pesos atribuídos a cada preditor, obtendo '+
		 'um risco ou probabilidade. A probabilidade de ter ou não a doença, que pode ser usada para solicitar '+
		 'encaminhamento urológico para testes adicionais com base no risco de uma condição de saúde particular'+
		 '(NOVAES et al., 2021).'+
		 'Pensando na democratização da ciência e retorno dos resultados das pesquisas, no grupo de pesquisa'+
		 'em Urologia (Uros) da Universidade Estadual de Feira de Santana, desenvolvemos um aplicativo que permite'+
		 'prever a deficiência de testosterona em homens entre 45 – 85 anos utilizando técnicas de Machine Learning (ML)')
	
	st.write('**Referencias')
	
	st.write('NOVAES, Monique Tonani et al. Prediction of secondary testosterone deficiency using machine learning:'+
		 'A comparative analysis of ensemble and base classifiers, probability calibration, and sampling strategies'+
		 'in a slightly imbalanced dataset. Informatics in Medicine Unlocked, v. 23, p. 100538, 2021. Disponível em:'+
		 '<https://linkinghub.elsevier.com/retrieve/pii/S2352914821000289>. Acesso em: 4 mar. 2022.')

 
