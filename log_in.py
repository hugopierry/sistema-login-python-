import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

from time import sleep

from  pwinput import pwinput # type: ignore



class Criar_acesso_usuario:
    
    def __init__(self):
        print("----------------------")
        print("📝 CRIAR USUÁRIO E SENHA:")
        self.criar_usuario = input("\n👤 Crie um usuário: ")
        self.criar_senha = pwinput("🔐 Crie uma senha: ").strip()
        self.confirmar_senha = pwinput("🔁 Confirmar senha: ").strip()
        
        print("\n👤 Criando usuário...")
        sleep(2)
        


    # validação # usar time

        while self.confirmar_senha != self.criar_senha:
                
                print("\n🔎 Analisando cadastro...")
                sleep(2)
                print("\n❌ A senha criada não é igual a senha confirmada.")
                print("Tente novamente.")
                self.criar_senha = pwinput("\nCrie uma senha: ").strip()
                self.confirmar_senha = pwinput("Confirmar senha: ").strip()
               
                print("👤 Criando usuário...")
                sleep(2)
        print(f"\n✅ Usuário '{self.criar_usuario}' criado com sucesso!")

                

cadastro = Criar_acesso_usuario()

print("-"*60)

class Acesso_suario:
    
    def __init__(self,cadastro):
        print("\n🔐 USUÁRIO E SENHA:")
        self.usuario = input("\n👤 Usuário: ").strip()
        self.senha = pwinput("🔑 Senha: ").strip()
        sleep(2)

        while self.usuario != cadastro.criar_usuario or self.senha != cadastro.criar_senha:
            print("\n❌ Usuário ou senha incorretos.")
            print("Tente novamente.")
            self.usuario = input("\n👤 Usuário: ").strip()
            self.senha = pwinput("🔑 Senha: ").strip()
        print(f"\n🖥️ Bem- vindo ao sistema!")


usuario_cadastrado = Acesso_suario(cadastro)


input("\n\nPressione ENTER para sair.")




















# usuario = "hugopierry"
# senha = "123456"

# usuario = input("Digite o usuário: ").strip()
# senha = int(input("Digite a senha: ").strip())


# if usuario == "hugopierry" and senha == 123456:
#     print("Usuário encontrado,Acesso permitido")
# else:
#     print(f"{usuario} não encontrado, acesso negado")

