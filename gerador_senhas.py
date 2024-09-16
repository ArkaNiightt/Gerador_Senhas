import random
import string
import streamlit as st

# Função para gerar a senha
def gerar_senha(tamanho, qtd_especiais, use_lower, use_upper, use_digits):
    caracteres = ""
    especiais = string.punctuation
    
    if use_lower:
        caracteres += string.ascii_lowercase
    if use_upper:
        caracteres += string.ascii_uppercase
    if use_digits:
        caracteres += string.digits

    if caracteres == "" and qtd_especiais == 0:
        st.error("Selecione pelo menos uma opção de caracteres!")
        return ""

    # Gera a parte da senha sem os caracteres especiais
    senha_normal = ''.join(random.choice(caracteres) for _ in range(tamanho - qtd_especiais))
    
    # Gera a parte da senha com os caracteres especiais
    senha_especial = ''.join(random.choice(especiais) for _ in range(qtd_especiais))

    # Combina ambas as partes e embaralha
    senha = list(senha_normal + senha_especial)
    random.shuffle(senha)
    return ''.join(senha)

# Interface Streamlit
st.title("Gerador de Senhas")

st.write("Selecione as opções para gerar a senha:")

# Opções de configuração da senha
use_lower = st.checkbox('Incluir letras minúsculas (abc)')
use_upper = st.checkbox('Incluir letras maiúsculas (ABC)')
use_digits = st.checkbox('Incluir números (123)')

# Slider para escolher o comprimento da senha
tamanho_senha = st.slider('Comprimento da senha', min_value=4, max_value=32, value=12)

# Slider para escolher a quantidade de caracteres especiais
qtd_especiais = st.slider('Quantidade de caracteres especiais', min_value=0, max_value=tamanho_senha, value=2)

# Botão para gerar senha
if st.button('Gerar Senha'):
    senha_gerada = gerar_senha(tamanho_senha, qtd_especiais, use_lower, use_upper, use_digits)
    if senha_gerada:
        st.success(f"Sua senha gerada: {senha_gerada}")
