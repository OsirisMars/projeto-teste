import streamlit as st

# Título do aplicativo
st.title("Agendamento de Serviços")

# Entradas do usuário
id_cliente = st.text_input("ID")
razao_social_nome_fantasia = st.text_input("Razão Social / Nome Fantasia")
contato = st.text_input("Contato")
os_numero = st.text_input("OS (Número da Ordem de Serviço)")
observacoes = st.text_area("Observações")
dia_agendamento = st.date_input("Dia do Agendamento")
#turno = st.

# Botão para gerar a mensagem
if st.button("Gerar Mensagem"):
    # Mensagem gerada com as informações inseridas
    mensagem = f"""
    Agendamento de Serviço:
    
    ID do Cliente: {id_cliente} \n
    Razão Social / Nome Fantasia: {razao_social_nome_fantasia}\n
    Contato: {contato} \n
    Ordem de Serviço (OS): {os_numero} \n
    Observações: {observacoes} \n
    Data do Agendamento: {dia_agendamento} \n
    """
    
    # Exibindo a mensagem
    st.subheader("Mensagem Gerada:")
    st.write(mensagem)
