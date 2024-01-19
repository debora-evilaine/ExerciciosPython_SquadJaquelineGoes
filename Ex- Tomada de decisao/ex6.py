"""
Crieumprogramaquesoliciteaousuárioumlogineumasenha.
Oprogramadevepermitiroacessoapenasseousuáriofor"admin"
easenhafor"admin123",casocontrárioimprimaumamensagemdeerro.
"""

login = input("Entre com o seu login: ")

senha = input("Entre com sua senha: ")

if login == 'admin' and senha == 'admin123':
    print("Você foi logado no sistema!")

else:
    print("Login ou senha inválidos.")