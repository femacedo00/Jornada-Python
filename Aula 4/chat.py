# Tela Inicial:
    
    
        
        
        
            #  e na tela inicial irá:
                
                # Carregar o campo de escrever a mensagem com o placeholder ""
                # Botão: Enviar a mensagem
                    # Ao clicar, a mensagem será enviada e campo de escrita da mensagem será esvaziada
import flet as ft

    

# Função principal para rodar o aplicativo
def main(pagina):
    # Título:
    titulo_pagina = ft.Text("Hashzap")
    pagina.add(titulo_pagina)

    def enviar_mensagem_todos(mensagem): # Função a ser executada pelo websocket
        texto = ft.Text(mensagem)
        chat.controls.append(texto) # Adicionando ao chat a mensagem
        pagina.update() # Mostrando na tela

    pagina.pubsub.subscribe(enviar_mensagem_todos) # Mandar a mensagem para todos os usuários ativos no chat via websocket

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value # Pegando o nome do usuário
        texto_campo_msg = campo_enviar_msg.value # Pegando a mensagem do usuário
        mensagem = f"{nome_usuario}: {texto_campo_msg}" # Formatando a mensagem para ser enviada com a info do nome do usuário e a mensgaem
        pagina.pubsub.send_all(mensagem)

        campo_enviar_msg.value = "" # Esvaziando a caixa de enviar a emnsagem para o usuário enviar outra mensagem
        pagina.update() # Mostrando na tela

    campo_enviar_msg = ft.TextField(label="Digite a sua mensagem")
    botao_enviar_msg = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_msg, botao_enviar_msg])

    chat = ft.Column()

    def entrar_chat(evento):
        modal.open = False # Fechando o modal

        pagina.remove(titulo_pagina) # Removendo título da pagina
        pagina.remove(botao) # Removendo botão de abrir o modal

        pagina.add(chat) # Carregar o chat
        pagina.add(linha_enviar) # Carregar o campo e o botão de enviar mensagem ao chat

        # Informar ao chat quem entrou
        nome_usuario = caixa_nome.value # Pegando o nome do usuário
        mensagem = f"{nome_usuario} entrou no chat" # Formatando a mensagem para ser enviada para avisar quem entrou
        pagina.pubsub.send_all(mensagem)

        pagina.update() # Mostrando na tela

    # Titulo do modal:
    titulo_modal = ft.Text("Bem-vindo ao Hashzap")
    # Caixa de texto: 
    caixa_nome = ft.TextField(label="Digite seu nome")
    # Botão:
    botao = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat) # Ao clicar, o modal irá fechar e o usuário irá entrar no chat
    # Visualizando o modal:
    modal = ft.AlertDialog(title=titulo_modal, content=caixa_nome, actions=[botao])
    
    # Função do modal para informar o nome do usuario
    def info_nome(evento):
        pagina.dialog = modal
        modal.open = True
        pagina.update() # Mostrando na tela

    # Botão do modal:
    botao = ft.ElevatedButton("Iniciar Chat", on_click=info_nome) # Ao clicar, irá abrir o modal
    pagina.add(botao)

# Executar a função main com o flet
ft.app(main)