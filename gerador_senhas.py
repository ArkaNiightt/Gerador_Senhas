import random
import string
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Gerador de Senhas Seguras", page_icon="🔐", layout="centered"
)

# Custom CSS
st.markdown(
    """
    <style>
    .main {
        padding: 2rem;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    .password-box {
        color: #323440
        padding: 1rem;
        background-color: #f0f2f6;
        border-radius: 5px;
        text-align: center;
    
        .password-box-h2 {
            color: #323440
        }
    }
    </style>
""",
    unsafe_allow_html=True,
)


def gerar_senha(tamanho, qtd_especiais, use_lower, use_upper, use_digits):
    caracteres = ""
    especiais = r"""!@#"""

    if use_lower:
        caracteres += string.ascii_lowercase
    if use_upper:
        caracteres += string.ascii_uppercase
    if use_digits:
        caracteres += string.digits

    if caracteres == "" and qtd_especiais == 0:
        st.error("⚠️ Selecione pelo menos uma opção de caracteres!")
        return ""

    senha_normal = "".join(
        random.choice(caracteres) for _ in range(tamanho - qtd_especiais)
    )
    senha_especial = "".join(random.choice(especiais) for _ in range(qtd_especiais))
    senha = list(senha_normal + senha_especial)
    random.shuffle(senha)
    return "".join(senha)


# Interface principal
st.title("🔐 Gerador de Senhas Seguras")
st.markdown("---")

# Criar duas colunas para organizar os controles
col1, col2 = st.columns(2)

with col1:
    st.subheader("Tipos de Caracteres")
    use_lower = st.checkbox("📝 Letras minúsculas (abc)", value=True)
    use_upper = st.checkbox("📝 Letras maiúsculas (ABC)", value=True)
    use_digits = st.checkbox("🔢 Números (123)", value=True)

with col2:
    st.subheader("Configurações")
    tamanho_senha = st.slider(
        "📏 Comprimento da senha", min_value=4, max_value=32, value=12
    )
    qtd_especiais = st.slider(
        "🔑 Caracteres especiais", min_value=0, max_value=tamanho_senha, value=2
    )

st.markdown("---")

# Centralizar o botão
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("🎲 Gerar Senha"):
        senha_gerada = gerar_senha(
            tamanho_senha, qtd_especiais, use_lower, use_upper, use_digits
        )
        if senha_gerada:
            st.markdown("### Sua senha gerada:")
            st.markdown(
                f"""
            <div class="password-box">
                <h2 class="password-box-h2">{senha_gerada}</h2>
            </div>
            """,
                unsafe_allow_html=True,
            )

            # Adicionar métricas de força da senha
            st.markdown("### Força da senha:")
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Comprimento", f"{len(senha_gerada)} caracteres")
            with col2:
                st.metric("Caracteres especiais", f"{qtd_especiais}")
            with col3:
                tipos_chars = sum([use_lower, use_upper, use_digits, qtd_especiais > 0])
                st.metric("Complexidade", f"{tipos_chars}/4")
