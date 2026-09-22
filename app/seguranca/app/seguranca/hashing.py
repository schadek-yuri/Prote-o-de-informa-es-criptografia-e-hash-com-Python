import hashlib


class Hashing:
    """Responsável pela geração e verificação de hashes."""

    @staticmethod
    def gerar_sha256(texto: str) -> str:
        """
        Gera o hash SHA-256 de um texto.
        """
        return hashlib.sha256(
            texto.encode("utf-8")
        ).hexdigest()

    @staticmethod
    def verificar_sha256(
        texto: str,
        hash_original: str
    ) -> bool:
        """
        Verifica se o texto corresponde ao hash informado.
        """
        hash_atual = Hashing.gerar_sha256(texto)

        return hash_atual == hash_original
