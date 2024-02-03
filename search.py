import pandas as pd
from sentence_transformers import SentenceTransformer, util
import os
import csv
import time
import torch
import streamlit as st

df = pd.read_csv(r'./New_Commerce_Registry.csv')

paper_texts = df['en_ar_merge'].to_list()

# Check if cuda is available
cuda_available = torch.cuda.is_available()

# Set the torch device to cuda or cpu
torch_device = torch.device("cuda" if cuda_available else "cpu")

# Load the Transformer model
modelPath = r"./model"
model = SentenceTransformer(modelPath)
## model = SentenceTransformer('LaBSE')

# Load the embeddings from a file
## corpus_embeddings = model.encode(paper_texts, show_progress_bar=True, convert_to_tensor=True)
corpus_embeddings = torch.load(r"./corpus_embeddings.pt", map_location=torch.device(torch_device))




# Function that searches the corpus and prints the results
def search(inp_question):
    start_time = time.time()
    question_embedding = model.encode(inp_question, convert_to_tensor=True)
    hits = util.semantic_search(question_embedding, corpus_embeddings)
    end_time = time.time()
    hits = hits[0]  #Get the hits for the first query

    # print("Input question:", inp_question)
    st.write("Input question:", inp_question)

    # print("Results (after {:.3f} seconds):".format(end_time-start_time))
    st.write("Results (after {:.3f} seconds):".format(end_time-start_time))
    for hit in hits[0:10]:
        # print("\t{:.3f}\t{}".format(hit['score'], paper_texts[hit['corpus_id']]))
        st.write("{}".format(paper_texts[hit['corpus_id']]))

