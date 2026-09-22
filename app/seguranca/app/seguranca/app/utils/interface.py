import os


class Interface:
    """Responsável pela interface do terminal."""

    AZUL = "\033[94m"
    VERDE = "\033[92m"
    AMARELO = "\033[93m"
    VERMELHO = "\033[91m"
    CIANO = "\033[96m"
    RESET = "\033[0m"

    @staticmethod
    def limpar_tela():
        """Limpa o terminal."""
        os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def titulo():
        """Exibe o título principal."""

        print(
            f"""
{Interface.CIANO}
╔══════════════════════════════════════════════╗
║                                              ║
║       🔐 PROTEÇÃO DE INFORMAÇÕES 🔐         ║
║                                              ║
║          Criptografia + Hash em Python       ║
║                                              ║
╚══════════════════════════════════════════════╝
{Interface.RESET}
"""
        )

    @staticmethod
    def menu():
        """Exibe o menu principal."""

        print(f"""
{Interface.AZUL}┌──────────────────────────────────────────────┐
│                  MENU PRINCIPAL               │
├──────────────────────────────────────────────┤
│                                              │
│  [1] 🔐 Criptografar mensagem                │
│  [2] 🔓 Descriptografar mensagem             │
│  [3] #️⃣  Gerar Hash SHA-256                 │
│  [4] 🔎 Verificar Hash                       │
│  [0] 🚪 Sair                                 │
│                                              │
└──────────────────────────────────────────────┘{Interface.RESET}
""")

    @staticmethod
    def sucesso(mensagem: str):
        print(
            f"\n{Interface.VERDE}✅ {mensagem}{Interface.RESET}"
        )

    @staticmethod
    def erro(mensagem: str):
        print(
            f"\n{Interface.VERMELHO}❌ {mensagem}{Interface.RESET}"
        )

    @staticmethod
    def informacao(mensagem: str):
        print(
            f"\n{Interface.AMARELO}ℹ️ {mensagem}{Interface.RESET}"
        )

    @staticmethod
    def pausar():
        input("\nPressione ENTER para continuar...")
