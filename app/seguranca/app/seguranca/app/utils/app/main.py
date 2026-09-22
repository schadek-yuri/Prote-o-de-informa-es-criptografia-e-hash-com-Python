from getpass import getpass

from seguranca.criptografia import Criptografia
from seguranca.hashing import Hashing
from utils.interface import Interface


class Aplicacao:
    """Controla o funcionamento da aplicação."""

    def __init__(self):
        self.chave = None
        self.mensagem_criptografada = None

    def executar(self):
        """Inicia a aplicação."""

        while True:
            Interface.limpar_tela()
            Interface.titulo()
            Interface.menu()

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.criptografar()

            elif opcao == "2":
                self.descriptografar()

            elif opcao == "3":
                self.gerar_hash()

            elif opcao == "4":
                self.verificar_hash()

            elif opcao == "0":
                self.sair()
                break

            else:
                Interface.erro("Opção inválida.")
                Interface.pausar()

    def criptografar(self):
        """Executa o processo de criptografia."""

        Interface.limpar_tela()

        print("🔐 CRIPTOGRAFIA\n")

        mensagem = input(
            "Digite a mensagem que deseja proteger: "
        )

        if not mensagem:
            Interface.erro("A mensagem não pode estar vazia.")
            Interface.pausar()
            return

        self.chave = Criptografia.gerar_chave()

        self.mensagem_criptografada = (
            Criptografia.criptografar(
                mensagem,
                self.chave
            )
        )

        print("\n" + "─" * 50)

        print(
            f"\n🔑 Chave:\n{self.chave.decode()}"
        )

        print(
            f"\n🔒 Mensagem criptografada:\n"
            f"{self.mensagem_criptografada}"
        )

        Interface.informacao(
            "Guarde a chave! Sem ela, a mensagem não poderá "
            "ser descriptografada."
        )

        Interface.pausar()

    def descriptografar(self):
        """Executa o processo de descriptografia."""

        Interface.limpar_tela()

        print("🔓 DESCRIPTOGRAFIA\n")

        chave = input("Digite a chave Fernet: ").strip()

        mensagem = input(
            "\nDigite a mensagem criptografada: "
        ).strip()

        if not chave or not mensagem:
            Interface.erro(
                "A chave e a mensagem são obrigatórias."
            )
            Interface.pausar()
            return

        try:
            mensagem_original = (
                Criptografia.descriptografar(
                    mensagem,
                    chave.encode()
                )
            )

            print("\n" + "─" * 50)

            print(
                f"\n📄 Mensagem original:\n"
                f"{mensagem_original}"
            )

            Interface.sucesso(
                "Mensagem descriptografada com sucesso!"
            )

        except ValueError as erro:
            Interface.erro(str(erro))

        Interface.pausar()

    def gerar_hash(self):
        """Gera um hash SHA-256."""

        Interface.limpar_tela()

        print("#️⃣ GERADOR DE HASH SHA-256\n")

        texto = getpass(
            "Digite o texto que deseja transformar em hash: "
        )

        if not texto:
            Interface.erro("O texto não pode estar vazio.")
            Interface.pausar()
            return

        hash_gerado = Hashing.gerar_sha256(texto)

        print("\n" + "─" * 50)

        print(f"\n🔑 SHA-256:\n{hash_gerado}")

        Interface.sucesso(
            "Hash gerado com sucesso!"
        )

        Interface.pausar()

    def verificar_hash(self):
        """Verifica um hash SHA-256."""

        Interface.limpar_tela()

        print("🔎 VERIFICAÇÃO DE HASH\n")

        texto = getpass(
            "Digite o texto para verificar: "
        )

        hash_original = input(
            "\nDigite o hash SHA-256: "
        ).strip()

        if not texto or not hash_original:
            Interface.erro(
                "O texto e o hash são obrigatórios."
            )
            Interface.pausar()
            return

        resultado = Hashing.verificar_sha256(
            texto,
            hash_original
        )

        print("\n" + "─" * 50)

        if resultado:
            Interface.sucesso(
                "O texto corresponde ao hash informado."
            )
        else:
            Interface.erro(
                "O texto NÃO corresponde ao hash informado."
            )

        Interface.pausar()

    @staticmethod
    def sair():
        """Finaliza o programa."""

        Interface.limpar_tela()

        print("""
╔══════════════════════════════════════════════╗
║                                              ║
║       🔐 PROGRAMA ENCERRADO 🔐              ║
║                                              ║
║       Obrigado por utilizar o projeto!       ║
║                                              ║
╚══════════════════════════════════════════════╝
""")


if __name__ == "__main__":
    Aplicacao().executar()
