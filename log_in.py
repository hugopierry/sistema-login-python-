from time import sleep


class Criar_acesso_usuario:
    print("----------------------")
    print("CRIAR USUÁRIO E SENHA:")
    def __init__(self):
        
        self.criar_usuario = input("\nCrie um usuário: ")
        self.criar_senha = input("Crie uma senha: ")
        self.confirmar_senha = input("Confirmar senha: ")
        


    # validação # usar time

        while self.confirmar_senha != self.criar_senha:
                
                print("🔎 Analisando cadastro...")
                sleep(2)
                print("\n❌ A senha criada não é igual a senha confirmada.")
                print("Tente novamente.")
                self.criar_senha = input("Crie uma senha: ")
                self.confirmar_senha = input("Confirmar senha: ")
        print(f"✅ Usuário '{self.criar_usuario}' criado com sucesso!")

                

cadastro = Criar_acesso_usuario()

print("-"*60)

class Acesso_suario:
    print("\n🔐 USUÁRIO E SENHA:")
    def __init__(self,cadastro):
        self.usuario = input("\n👤 Usuário: ")
        self.senha = input("🔑 Senha: ")

        if self.usuario == cadastro.criar_usuario and self.senha == cadastro.criar_senha:
            print("✅ Acesso permitido!")
        else:
            print("⛔ Usuário e senha incorretos")


usuario_cadastrado = Acesso_suario(cadastro)




















# usuario = "hugopierry"
# senha = "123456"

# usuario = input("Digite o usuário: ").strip()
# senha = int(input("Digite a senha: ").strip())


# if usuario == "hugopierry" and senha == 123456:
#     print("Usuário encontrado,Acesso permitido")
# else:
#     print(f"{usuario} não encontrado, acesso negado")

