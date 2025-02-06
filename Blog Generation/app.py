import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

# function to get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    # LLama2 model
    llm = CTransformers(model=r'C:\Users\username\projects\LLM\models', 
                        model_type='llama',
                        config={'max_new_tokens':256,
                               'temperature':0.01})
    # prompt template
    template = """
    Write a blog for {style} job profile for topic {text} within {n_words} 
    """
    prompt = PromptTemplate(input_variables=["style", "text", "n_words"],
                           template=template)
    # generate response
    response = llm.invoke(prompt.format(style=blog_style, text=input_text, n_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                  page_icon='🤖',
                  initial_sidebar_state='collapsed')
st.header("Generate Blogs 🤖")
input_text = st.text_input("Enter the blog topic")
col1, col2 = st.columns([5,5])
with col1:
    no_words = st.text_input('No. of words')
with col2:
    blog_style = st.selectbox('Writing the blog for', 
                              ('Researchers', 'Data Scientists', 'Common People'), index=0)
submit = st.button('Generate')

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))