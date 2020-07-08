from flask import Flask,render_template,url_for,request
import re
import pandas as pd
import spacy
from spacy import displacy
#nlp = spacy.load('pt_core_news_sm')
nlp = spacy.load("custom_ner_model")

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/process',methods=["POST"])
def process():
	if request.method == 'POST':
		choice = request.form['taskoption']
		rawtext = request.form['rawtext']
		doc = nlp(rawtext)
		d = []
		for ent in doc.ents:
			d.append((ent.label_, ent.text))
			df = pd.DataFrame(d, columns=('named entity', 'output'))
			pessoa_named_entity = df.loc[df['named entity'] == 'pessoa']['output']
			matricula_named_entity = df.loc[df['named entity'] == 'matrícula']['output']
			acao_named_entity = df.loc[df['named entity'] == 'ação']['output']
		if choice == 'matricula':
			results = matricula_named_entity
			num_of_results = len(results)
		elif choice == 'pessoa':
			results = pessoa_named_entity
			num_of_results = len(results)
		elif choice == 'acao':
			results = acao_named_entity
			num_of_results = len(results)
		
	
	return render_template("index.html",results=results,num_of_results = num_of_results)


if __name__ == '__main__':
	app.run(debug=True)