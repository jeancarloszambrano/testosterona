import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pycaret.classification import load_model, predict_model


Menu = ['Home', 'Modelo', 'Modelagem']

from PIL import Image
LOGO = Image.open('UEFS.png')
st.sidebar.image(LOGO, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="png")
st.sidebar.subheader('Universidade Estadual de Feira de Santana')
st.sidebar.subheader('Grupo de pesquisa em Urológia')

pagina = st.sidebar.selectbox('Navegação', Menu)

st.sidebar.write('')

st.sidebar.write('*Monique Tonani Novais*')
st.sidebar.write('*Anna Paloma Martins Rocha Ribeiro*')
st.sidebar.write('*Caroline Santos Silva*')
st.sidebar.write('*Jean Carlos Zambrano Contreras*')
st.sidebar.write('*José de Bessa Júnior*')

if pagina == 'Home':
	from PIL import Image
	image = Image.open('logo.jpg')
	st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="JPEG")
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
		 '(NOVAES et al., 2021).')
	
	st.write('Pensando na democratização da ciência e retorno dos resultados das pesquisas, no grupo de pesquisa'+
		 'em Urologia (Uros) da Universidade Estadual de Feira de Santana, desenvolvemos um aplicativo que permite'+
		 'prever a deficiência de testosterona em homens utilizando parâmetros simples com técnicas de Machine Learning (ML)')
	
	st.write('**Dr. José de Bessa Júnior**')
	
	

if pagina == 'Modelo':
	
	from PIL import Image
	image = Image.open('logo.jpg')
	st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="JPEG")
	st.title('MODELO PARA PREVER DEFICIÊNCIA DE TESTOSTERONA')
	#st.markdown('---')
	st.write('Por favor, inserir os dados solicitados, tenha em consideração que o modelo esta desenvolvido para homens entre 20 e 85 anos.')
	
	# função para carregar o modelo
	modelo1 = load_model('Final_Model')

	def predict(modelo1, dados):
		predictiones_df = predict_model(estimator=modelo1, data=dados)
		predic = predictiones_df['Label'][0]
		return predictions


	# função para carregar o dataset
	@st.cache(allow_output_mutation=True)
	def get_data():
    		return pd.read_csv('testost2.csv')

	Idade = st.slider('Idade', min_value=21, max_value=97, value=60)
	GLI = st.slider("Glicemia: (em mg/dl)", min_value=10, max_value=384, value=70)
	TGL = st.slider("Triglicerídeos: (em mg/dl)", min_value=1, max_value=980, value=150)
	HDL = st.slider("Colesterol HDL:(em mg/dl)", min_value=9, max_value=116, value=40)
	CA = st.slider("Circunferência de cintura: (em cm)", min_value=43, max_value=198, value=94)
	COL = st.slider("Colesterol total: (em mg/dl)", min_value=16, max_value=363, value=190)
	LDL = st.slider("Colesterol LDL: (em mg/dl)", min_value=10, max_value=832, value=130)
	HAS = st.selectbox("Hipertenso:", ["Sim", "Não"])

	
	HAS = 1.0 if HAS == 'Sim' else 0.0
	
	
	dados0 = {'Age':[Idade], 'GLI':[GLI], 'TGL':[TGL], 'HDL':[HDL], 'CA':[CA], 'COL':[COL], 'LDL':[LDL], 'HAS':[HAS]}
	dados = pd.DataFrame(dados0)
	
		
	#st.markdown('---')

	if st.button('REALIZAR PREDIÇÃO'):
		pred = float(predict_model(modelo1, data = dados)['Label'].round(0))
		saida = '{:.0f}'.format(pred)
		st.subheader(saida)
		saida2 = '{:.0f}'.format(pred)
		st.subheader('NEGATIVO PARA DEFICIÊNCIA DE TESTOSTERONA') if saida == '0' else st.subheader('POSITIVO PARA DEFICIÊNCIA DE TESTOSTERONA')
		st.write('Glicemia baixa ou hipoglicemia.') 
			elif GLI < 70 
		st.write('Glicemia normal.') 
			elif (GLI >= 70) and (GLI < 100) 
		st.write('Glicemia alterada.') 
			elif (GLI >= 100) and (GLI <= 125) 
			else st.write('Diabético ou alta propensão pra desenvolver diabetes.') 
		
		
if pagina == 'Modelagem':
	from PIL import Image
	image = Image.open('logo.jpg')
	st.image(image, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="JPEG")
	st.title('MODELAGEM DOS DADOS')
	st.markdown('---')
	
	st.write('Aprendizado de Máquina (ou Machine Learning) é uma das técnicas utilizadas'+
		 'na Inteligência Artificial que usa algoritmos baseados em matemática e'+
		 'algoritmos com a finalidade de extrair informações de dados brutos e representá-los'+
		 'por meio de algum tipo de modelo matemático e fazer predições a partir de'+
		 'de extrair informações de dados brutos e representá-los'+
		 'por meio de algum tipo de modelo matemático e fazer'+
		 'novos conjuntos de dados.')
		 
	st.write('Para a modelagem dos dados, foram coletadas informações sob idade, glicemia'+
		 'em jejum (mg/dl), triglicerídeos (mg/dl), colesterol total (mg/dl), HDL (mg/dl) e'+
		 'LDL (mg/dl), circunferência de cintura (cm), hipertensão arterial (Sim - Não) e'+
		 'nível de testosterona de 4258 homens com idade entre 20-90 anos da Região'+
		 'Metropolitana de Feira de Santana.')
	
	st.write('Nós, testamos diferentes algoritmos de Aprendizado de Máquina para prever a'+
		 'deficiência de testosterona (testosterona <300 ng/dl) com algoritmos de'+
		 'aprendizado supervisionado do tipo classificação. A proporção de homens com'+
		 'deficiência de testosterona na amostra foi de 23,5%, pelo que aplicamos técnicas'+
		 'oversampling para lidar com os dados desequilibrados (técnica SMOTE).')
	
	st.write('Dividimos a amostra em amostra de teste (1278 casos) e amostra de treino'+
		 '(2980 casos), rodamos diferentes algoritmos, e selecionamos os algoritmos que'+
		 'apresentaram o maior Recall (Sensibilidade), situação em que os Falsos'+
		 'Negativos são considerados mais prejudiciais que os Falsos Positivos. Os'+
		 'resultados são apresentados na tabela 1.')
	
	st.write('**Tabela 1. Algoritmos de aprendizado de maquina**')
	from PIL import Image	 
	tabela1 = Image.open('tabela1.png')
	st.image(tabela1, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="png")
		 
	st.write('Treinamos os modelos utilizando o método de validação cruzada (k-fold = 10),'+
		 'otimizamos o recall com 1000 interações. A regressão logística mostrou o'+
		 'melhor desempenho no recall e representamos graficamente AUC (figura 1). O'+
		 'AUC representa o grau ou medida de discriminação, quanto maior a AUC'+
		 'melhor o modelo, o seja distingue melhor entre pacientes com deficiência de'+
		 'testosterona e pacientes sem deficiência (AUC = 0.79).')
		 
	st.write('**Figura 1. AUC regressão logística**')
	from PIL import Image
	AUC = Image.open('AUC.png')
	st.image(AUC, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="png")
	
	st.write('Outra métrica bastante utilizada para problemas de classificação é a matriz de'+
		 'confusão, que oferece um detalhamento do desempenho do modelo de'+
		 'classificação, mostrando, para cada classe, o número de classificações corretas'+
		 'em relação ao número de classificações preditas pelo modelo. A matriz de'+
		 'confusão pode ser usada para calcular outras métricas, tais como o número de'+
		 'Falsos Positivos (quando o resultado esperado é negativo, mas o modelo'+
		 'resulta em positivo), Falsos Negativos (quando o resultado esperado é positivo,'+
		 'mas o modelo resulta em negativo), Verdadeiros Positivos (quando o resultado'+
		 'esperado é positivo e o modelo resulta em positivo) e Verdadeiros Negativos'+
		 '(quando o resultado esperado é negativo e o modelo resulta em negativo).')
		 
	st.write('**Tabela 2. Matriz de confusão**')
	Matrix = Image.open('MatrixConf.png')
	st.image(Matrix, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="png")
	
	st.write('Sensibilidade é a proporção de participantes que têm a doença e o modelo os'+
		 'classificou com deficiência de testosterona. Nosso modelo apresenta uma'+
		 'sensibilidade de 92,9% e especificidade de 35,8% isto porque selecionamos e'+
		 'otimizamos algoritmos com o maior Recall.')
	 		 
	st.write('**Fig 2. Recall**')
	from PIL import Image
	Recall = Image.open('recall.png')
	st.image(Recall, caption=None, width=None, use_column_width=None, clamp=False, channels="RGB", output_format="png")
	
	st.write('**Referencias**')
	st.write('')
	st.write('NOVAES, Monique Tonani et al. Prediction of secondary testosterone deficiency using machine learning:'+
		 'A comparative analysis of ensemble and base classifiers, probability calibration, and sampling strategies'+
		 'in a slightly imbalanced dataset. Informatics in Medicine Unlocked, v. 23, p. 100538, 2021. Disponível em:'+
		 '<https://linkinghub.elsevier.com/retrieve/pii/S2352914821000289>. Acesso em: 4 mar. 2022.')	
