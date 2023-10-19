import PySimpleGUI as sg

# Inclusão de dados no Layout
layout = [
    [sg.Text('usuario')],
    [sg.Input(key='usuario')],
    [sg.Text('senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('',key='mensagem')],
]

# Usuario e senha corretos para validação
senha_correta = '123456'
usuario_correto = 'Lucas'

# Criar a interface de login
window = sg.Window('login', layout=layout)


while True: # Validação de dados
    
    # Criar um evento(variavel) para pegar o valor da Janela
    event, values = window.read()
    
    # Validar se o usuario esta com Janela Fechada
    if event == sg.WIN_CLOSED:
        break
    
    # Se a Janela estiver aberta, valida se os dados de usuario e senha passados estão corretos
    elif event == 'login':
        # Pegar os valores inserido pelo o usuario
        usuario = values['usuario']
        senha = values['senha']
        
        # Se a senha e o usuario estão corretos a janela informa que o login foi feito com sucesso.
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
            
        # Se não a janela informa que o Usuario e senha estão incorretos.   
        else:
            window['mensagem'].update('Usuario ou senha incorreto')
            
# Vamos testar
        