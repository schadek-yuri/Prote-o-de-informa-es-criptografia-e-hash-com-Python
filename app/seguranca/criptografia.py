from cryptography.fernet import Fernet, InvalidToken


class Criptografia:
    """Responsável por criptografar e descriptografar informações."""

    @staticmethod
    def gerar_chave() -> bytes:
        """Gera uma nova chave de criptografia."""
        return Fernet.generate_key()

    @staticmethod
    def criptografar(mensagem: str, chave: bytes) -> str:
        """
        Criptografa uma mensagem utilizando Fernet.

        Args:
            mensagem: Texto que será criptografado.
            chave: Chave Fernet válida.

        Returns:
            Mensagem criptografada em formato de texto.
        """
        fernet = Fernet(chave)
        mensagem_criptografada = fernet.encrypt(
            mensagem.encode("utf-8")
        )

        return mensagem_criptografada.decode("utf-8")

    @staticmethod
    def descriptografar(
        mensagem: str,
        chave: bytes
    ) -> str:
        """
        Descriptografa uma mensagem.

        Raises:
            ValueError: Caso a chave ou mensagem seja inválida.
        """
        try:
            fernet = Fernet(chave)

            mensagem_original = fernet.decrypt(
                mensagem.encode("utf-8")
            )

            return mensagem_original.decode("utf-8")

        except (InvalidToken, ValueError):
            raise ValueError(
                "Não foi possível descriptografar a mensagem."
