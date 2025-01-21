import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(
    page_title="João Carvalho",
    page_icon="😁",
    layout="centered",
    initial_sidebar_state="auto"
)

# Tabulação
tab1, tab2 = st.tabs(["Currículo", "Outros Conteúdos"])

with tab1:
    # Colunas dentro da aba 1
    col1, col2 = st.columns([4, 1])
    
    with col1:
        st.title("João Marcos Santos e Caravlho")
        st.write("Estudante de Engenharia de Software. Interesse em Ciência de Dados w Inteligência Artificial.")
        
        st.divider()
        st.subheader(":blue[EXPERIÊNCIA PROFISSIONAL]")


""")

        
        st.divider()
        st.subheader(":blue[PROJETOS]")
        '''st.write("**[Projeto Currículo](https://(colocar ainda).streamlit.app)** — _Projeto Python_")
        st.caption("Criação deste currículo interativo usando Streamlit.")
        st.write("**Projeto Guia do Universitário** — _Projeto Integrador_")
        st.caption("Solução prática para calouros, com dicas sobre a faculdade e contratação de monitores.")'''


        st.divider()
        st.subheader(":blue[FORMAÇÃO]")

        st.write("Instituto de Educação Superior de Brasília (IESB), Asa Sul, DF")
        st.caption("Bacharelado em Ciência da Computação - Quarto semestre, com previsão de formatura em 2026.")
        st.write("Universidade de Brasília (UnB), Gama, DF")
        st.caption("Bacharelado em Engenharia de Software - Primeiro semestre, com previsão de formatura em 2029.")

        st.divider()

        st.subheader(":blue[REDES]")

        button_col1, button_col2, button_col3, button_col4 = st.columns([1, 1, 1, 1])

        with button_col1:
            st.link_button("🐱 Github", "https://github.com/dev-joaocarvalho") 

        with button_col2:
            st.link_button("🔗 LinkedIn", "https://www.linkedin.com/in/joaom-s-carvalho/")



    with col2:
        st.caption("Grande Colorado, DF, 73105-905")
        st.caption("**☎️ +55 61 08199-4401**")
        st.caption("**dev.joaocarvalho@gmail.com**")
        
        st.divider()
        st.write(":blue[COMPETÊNCIAS]")
        st.caption("Programação: Java, Python, C.")
        st.caption("Análise de Dados: Excel, Python (Pandas, NumPy), SQL.")
        st.caption("Desenvolvimento Web: HTML, CSS, Streamlit.")
        st.caption("Ferramentas: Eclipse, Visual Studio Code.")
        st.caption("Gestão de Projetos: Scrum, Kanban, Microsoft Project, Trello.")
        st.caption("Pacote Office: Word, Excel, PowerPoint.")
        st.caption("Sistemas Operacionais: Linux, Windows.")

        st.divider()
        st.write(":blue[PROJETOS VOLUNTÁRIOS]")
        st.caption("Monitoria em Geometria Analítica e Lógica Matemática.")
        st.caption("Apoio na organização e aplicação de provas para o EAD.")
        
        st.divider()
        st.write(":blue[IDIOMAS]")
        st.caption("Inglês.")


st.divider()

# URL do arquivo PDF no GitHub
pdf_url = "https://raw.githubusercontent.com/CraraMaria/Testes_Currículo/main/Currículo_JoaoCarvalho.pdf"  # Atualize com o link correto

# Cria o botão de download
st.markdown(f'<a href="{pdf_url}" download="Currículo_JoaoCarvalho.pdf">Baixar em PDF</a>', unsafe_allow_html=True)

with tab2:
    # Conteúdo para a aba 2
    # tentar colocar foto interativa
    st.write("PÁGINA EM CONSTRUÇÃO 🛠👩‍🚒")
    st.write("Mais sobre mim")
    st.image("fotodeperfil.png", caption="Joao Carvalho", width=200)
    st.title("Sobre Mim")
    st.write("""
Sou João Marcos Santos e Carvalho, um estudante de tecnologia e sempre em busca de aprender algo novo. 
Meu objetivo é me tornar uma desenvolvedor de destaque, com interesse especial em Ciência de Dados, Inteliência Artificial e Desenvolvimento Full Stack. 
""")
    # Além da , .
    st.title("Projetos")
    st.subheader("Projeto Currículo")
    st.write("""Este é um projeto feito com Streamlit, onde criei um currículo interativo para treinar minhas habilidades de desenvolvimento web. 
[Veja o código no GitHub](https://github.com/dev-joaocarvalho/curriculo-em-site)
""")
    st.title("Contato")
with st.form(key='contact_form'):
    name = st.text_input("Nome")
    email = st.text_input("Email")
    message = st.text_area("Mensagem")
    submit = st.form_submit_button("Enviar")
    if submit:
        st.success("Mensagem enviada com sucesso!")
    

