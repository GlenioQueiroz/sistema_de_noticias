"""Regras de negócio do Sistema de Notícias."""

from sistema_noticias.modelo import Classificacao, Noticia

noticias: list[Noticia] = []


PALAVRAS_SENSACIONALISTAS = ("!!!", "URGENTE")
TAMANHO_MINIMO_TEXTO = 10


def normalizar_classificacao(valor: str | None) -> Classificacao:
    """Converte a entrada textual em uma classificação válida.

    Quando a classificação não é informada, mantém o comportamento original:
    a notícia é cadastrada como duvidosa.
    """
    if valor is None or valor.strip() == "":
        return Classificacao.DUVIDOSA

    valor_normalizado = valor.strip().lower()
    for classificacao in Classificacao:
        if valor_normalizado == classificacao.value:
            return classificacao

    raise ValueError(
        "Classificação inválida. Use: confiavel, duvidosa ou falsa."
    )


def adicionar_noticia(texto: str, classificacao: str | None = None) -> None:
    """Adiciona uma notícia à lista, após validar seus dados."""
    texto_limpo = texto.strip()

    if not texto_limpo:
        raise ValueError("O texto da notícia não pode estar vazio.")

    noticia = Noticia(
        texto=texto_limpo,
        classificacao=normalizar_classificacao(classificacao),
    )
    noticias.append(noticia)


def analisar_noticia(texto: str) -> Classificacao:
    """Classifica automaticamente uma notícia com base em critérios simples."""
    texto_limpo = texto.strip()
    pontuacao = 0

    if not texto_limpo:
        raise ValueError("O texto da notícia não pode estar vazio.")

    if "FONTE" not in texto_limpo:
        pontuacao += 1
    if any(palavra in texto_limpo for palavra in PALAVRAS_SENSACIONALISTAS):
        pontuacao += 1
    if len(texto_limpo) < TAMANHO_MINIMO_TEXTO:
        pontuacao += 1

    if pontuacao == 0:
        return Classificacao.CONFIAVEL
    if pontuacao == 1:
        return Classificacao.DUVIDOSA
    return Classificacao.FALSA


def listar_noticias() -> list[Noticia]:
    """Retorna as notícias cadastradas."""
    return noticias.copy()
