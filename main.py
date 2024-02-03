import streamlit as st
from search import search

st.set_page_config(page_title="Smart Search")

# Link the CSS file to your Streamlit application
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css('styles.css')

# Define the home page
def home(search):
    st.image("./pic/logo.png", width=600)
    st.markdown('<h2 class="center">Search for company names</h2>', unsafe_allow_html=True)
    search_query = st.text_input('Type anything to search for related company names ...', value="")
    search_query = str(search_query)

    if not search_query:
        st.warning('ابحث بأي لغة ... ندعم اللغة العربية')
    else:
        try:
            search(search_query)
        except:
            st.warning('Problem With AI Model.')


def main():
    home(search)

if __name__ == '__main__':
    main()
