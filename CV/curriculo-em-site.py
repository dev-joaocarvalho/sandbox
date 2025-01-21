import streamlit as st
import time

# Configuração da página
st.set_page_config(
    page_title="João Carvalho",
    page_icon="😁",
    layout="centered",
    initial_sidebar_state="auto"
)

# Estilo personalizado
st.markdown(
    """
    <style>
    .main-title { color: #2C3E50; font-size: 32px; font-weight: bold; text-align: center; }
    .section-title { color: #3498DB; font-size: 24px; margin-top: 20px; }
    .profile-pic { display: block; margin: 0 auto 10px; border-radius: 50%; }
    </style>
    """,
    unsafe_allow_html=True
)

# Tabulação
tab1, tab2 = st.tabs(["Currículo", "Outros Conteúdos"])

with tab1:
    # Colunas dentro da aba 1
    col1, col2 = st.columns([4, 1])

    with col1:
        st.markdown('<h1 class="main-title">João Marcos Santos e Carvalho</h1>', unsafe_allow_html=True)
        st.write("Estudante de Engenharia de Software. Interesse em Ciência de Dados e Inteligência Artificial.")

        st.image("fotodeperfil.png", caption="João Carvalho", width=150, use_column_width="auto", output_format="auto")

        st.divider()
        st.markdown('<h2 class="section-title">EXPERIÊNCIA PROFISSIONAL</h2>', unsafe_allow_html=True)
        st.write("Em construção. Aguardando oportunidade de estágio em TI.")

        st.divider()
        st.markdown('<h2 class="section-title">PROJETOS</h2>', unsafe_allow_html=True)
        st.write("**[Projeto Currículo](https://(colocar ainda).streamlit.app)**")
        st.caption("Criação de um currículo interativo usando Streamlit.")

        st.divider()
        st.markdown('<h2 class="section-title">FORMAÇÃO</h2>', unsafe_allow_html=True)

        st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
        st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")

        st.write("Universidade de Brasília (UnB), Gama, DF")
        st.caption("Bacharelado em Engenharia de Software - Primeiro semestre, com previsão de formatura em 2029.")

        st.divider()
        st.markdown('<h2 class="section-title">REDES</h2>', unsafe_allow_html=True)

        button_col1, button_col2 = st.columns([1, 1])

        with button_col1:
            st.button("🐱 GitHub", key="github_button")

        with button_col2:
            st.button("🔗 LinkedIn", key="linkedin_button")

    with col2:
        st.caption("Grande Colorado, DF, 73105-905")
        st.caption("**☎️ +55 61 08199-4401**")
        st.caption("**dev.joaocarvalho@gmail.com**")

        st.divider()
        st.write("**:blue[COMPETÊNCIAS]**")
        st.caption("Programação: Java, Python, C.")
        st.caption("Análise de Dados: Excel, Python (Pandas, NumPy), SQL.")
        st.caption("Desenvolvimento Web: HTML, CSS, Streamlit.")
        st.caption("Ferramentas: Eclipse, Visual Studio Code.")
        st.caption("Gestão de Projetos: Scrum, Kanban, Microsoft Project, Trello.")
        st.caption("Pacote Office: Word, Excel, PowerPoint.")
        st.caption("Sistemas Operacionais: Linux, Windows.")

        st.divider()
        st.write("**:blue[IDIOMAS]**")
        st.caption("Inglês.")

st.divider()

# URL do arquivo PDF no GitHub
pdf_url = "https://raw.githubusercontent.com/CraraMaria/Testes_Curr%C3%ADculo/main/Curr%C3%ADculo_JoaoCarvalho.pdf"  # Atualize com o link correto

# Cria o botão de download
st.markdown(f'<a href="{pdf_url}" download="Currículo_JoaoCarvalho.pdf">Baixar em PDF</a>', unsafe_allow_html=True)

with tab2:
    # Conteúdo para a aba 2
    st.markdown('<h2 class="main-title">PÁGINA EM CONSTRUÇÃO 🛠👩‍🚒</h2>', unsafe_allow_html=True)
    st.write("Mais sobre mim")
    st.image("fotodeperfil.png", caption="João Carvalho", width=200)

    st.markdown('<h2 class="section-title">Sobre Mim</h2>', unsafe_allow_html=True)
    st.write(
        """Sou João Marcos Santos e Carvalho, um estudante de tecnologia sempre em busca de aprender algo novo. 
Meu objetivo é me tornar um desenvolvedor de destaque, com interesse especial em Ciência de Dados, Inteligência Artificial e Desenvolvimento Full Stack."""
    )

    st.markdown('<h2 class="section-title">Projetos</h2>', unsafe_allow_html=True)
    st.write(
        """**Projeto Currículo**
Este é um projeto feito com Streamlit, onde criei um currículo interativo para treinar minhas habilidades de desenvolvimento web. 
[Veja o código no GitHub](https://github.com/dev-joaocarvalho/curriculo-em-site)"""
    )

    st.markdown('<h2 class="section-title">Contato</h2>', unsafe_allow_html=True)
    with st.form(key='contact_form'):
        name = st.text_input("Nome")
        email = st.text_input("Email")
        message = st.text_area("Mensagem")
        submit = st.form_submit_button("Enviar")
        if submit:
            with st.spinner("Enviando sua mensagem..."):
                time.sleep(2)
                st.success("Mensagem enviada com sucesso!")

    

