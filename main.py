import streamlit as st
import os
import getpass

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

# Verificar se a chave de API está disponível
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")

# Cache do LLM para evitar reinicializar a cada clique
@st.cache_resource
def get_llm():
    return ChatOpenAI(
        model="gpt-4o-mini", 
        base_url=os.environ.get("OPENROUTER_BASE_URL")
    )

# Configuração da interface do Streamlit
st.title("AI chat using LangChain")
st.write("Ask a question and receive an answer from the AI!")

# Área de texto para a pergunta
prompt = st.text_area("Type your question for the AI:", height=100)

# Botão para enviar
if st.button("Send", type="primary"):
    if prompt.strip():
        try:
            with st.spinner("Processing your question..."):
                llm = get_llm()
                resposta = llm.invoke(prompt)
                st.success("Response received!")
                st.write("**AI response:**")
                st.write(resposta.content)
        except Exception as e:
            st.error(f"Error processing the question: {str(e)}")
    else:
        st.warning("Please enter a question before sending.")
