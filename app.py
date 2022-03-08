import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pycaret.classification import load_model, predict_model

modelo1 = load_model('FinalLRCModel')

Menu = ['Home', 'Modelo', 'Treinamento']

st.sidebar.subheader('Páginas')
pagina = st.sidebar.selectbox('Menu', Menu)
st.sidebar.subheader('Grupo de pesquisa em Urológia')

if pagina == 'Home':
	image = Image.open('logo')
	st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
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
	
	st.write('**Referencias**')
	
	st.write('NOVAES, Monique Tonani et al. Prediction of secondary testosterone deficiency using machine learning:'+
		 'A comparative analysis of ensemble and base classifiers, probability calibration, and sampling strategies'+
		 'in a slightly imbalanced dataset. Informatics in Medicine Unlocked, v. 23, p. 100538, 2021. Disponível em:'+
		 '<https://linkinghub.elsevier.com/retrieve/pii/S2352914821000289>. Acesso em: 4 mar. 2022.')

if pagina == 'Modelo':
	st.title('MODELO PARA PREVER DEFICIÊNCIA DE TESTOSTERONA')
	st.markdown('---')
	st.write('Por favor, inserir os dados solicitados, tenha em consideração que o modelo esta desenvolvido para homens entre 20 e 85 anos.')
	
	Idade = st.number_input('Idade', min_value=45, max_value=85, step=1)
	GLI = st.number_input("Glicemia: (em mg/dl)", min_value=12, max_value=383)
	TGL = st.number_input("Triglicerídeos: (em mg/dl)", min_value=23, max_value=980)
	HDL = st.number_input("Colesterol HDL:(em mg/dl)", min_value=13, max_value=115)
	CA = st.number_input("Circunferência de cintura: (em cm)", min_value=43, max_value=198)
	COL = st.number_input("Colesterol total: (em mg/dl)", min_value=50, max_value=363)
	LDL = st.number_input("Colesterol LDL: (em mg/dl)", min_value=15, max_value=600)
	HAS = st.selectbox("Hipertenso:", ["Sim", "Não"])

	
	values = [Idade, GLI, TGL, HDL, CA, COL, LDL, HAS]
	column_names = ['Age','GLI', 'TGL', 'HDL', 'CA', 'COL', 'LDL', 'HAS']
	dados0 = pd.DataFrame(values, column_names)
	if   dados0[0][1] == 'Sim': dados0[0][1] = 1
	elif dados0[0][1]  == 'Não': dados0[0][1] = 0

	st.markdown('---')

	if st.button('REALIZAR PREDIÇÃO'):
		pred = float(predict_model(modelo1, data = dados0)['Label'].round(0))
		saida = 'Se o valor for 1, é muito provável que você tenha deficiência de testosterona, o valor predito é de {:.0f}'.format(pred)
		st.subheader(saida)
