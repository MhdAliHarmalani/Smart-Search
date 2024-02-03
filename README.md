# Smart Search

## Description
This project is a web app that allows users to search for company names in Arabic, English, and other languages using a sentence transformer model called "LaBSE".
The app uses Streamlit a Python library for creating data apps, and PyTorch, a deep learning library.

![Logo](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/logo.png?raw=true)

The data for this project is from the Dubai Pulse Open Data Portal, which provides a centralized register of companies in Dubai.
The data file is called commerce_registry.csv and contains information such as company name, legal type, nationality, activities, and status.
Can get the data file from this [link](https://www.dubaipulse.gov.ae/dataset/42a06aca-0aa6-4db9-a406-71ae95c2cc88/resource/47c7d04e-8aec-46ed-baf8-059e471750d7/download/commerce_registry.csv)

## Streamlit App Features
The app has the following features:
1. A home page that displays a logo and a title
2. A text input where users can type anything to search for related company names
3. A warning message if the input is empty or the model encounters a problem
4. A table that shows the top 10 results with their similarity scores and company names in Arabic and English
5. A Text that displays the amount of time it took for the algorithm to return search results

## App Screenshots

![Screenshot1](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot1.PNG?raw=true) ![Screenshot2](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot2.PNG?raw=true) 
![Screenshot3](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot3.PNG?raw=true) ![Screenshot4](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot4.PNG?raw=true) 
![Screenshot5](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot5.PNG?raw=true) ![Screenshot6](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot6.PNG?raw=true) 
![Screenshot7](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/pic/Screenshot7.PNG?raw=true) 

## Colab Notebook
This project also includes a Colab notebook that shows how to preprocess and encode the original data using the LaBSE model to get the corpus_embeddings.pt
[Smart_Search.ipynb](https://github.com/MhdAliHarmalani/Smart-Search/blob/main/Smart_Search.ipynb)

## Installation and Usage
To run this project locally, you need to have Python 3.6 or higher and the following packages installed:
1. streamlit
2. torch
3. sentence-transformers
4. pandas
   
You can install them using pip.
Then, you need to download the data file and save it in the same folder as the main.py file.

To run the app, use the following command:
streamlit run main.py
This will open a browser window where you can interact with the app.

## More information:
1. Language-agnostic BERT Sentence Encoder (LaBSE) is a BERT-based model trained for sentence embedding for 109 languages. 
The pre-training process combines masked language modeling with translation language modeling. 
The model is useful for getting multilingual sentence embeddings and for bi-text retrieval.
2. Streamlit is an open-source Python framework that lets you create web apps from data scripts in pure Python.
3. PyTorch is an open-source machine learning framework that accelerates the path from research prototyping to production deployment. 
It supports a wide range of applications, such as computer vision, natural language processing, and generative models.
4. Dubai Pulse is the digital backbone powering the Smart City, to help spread happiness among all Dubai residents and visitors. 
It provides open and shared data for individuals and public and private sectors.
