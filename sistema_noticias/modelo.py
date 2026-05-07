"""Modelos de dados do Sistema de Notícias."""

from dataclasses import dataclass
from enum import Enum


class Classificacao(str, Enum):
    """Classificações permitidas para uma notícia."""

    CONFIAVEL = "confiavel"
    DUVIDOSA = "duvidosa"
    FALSA = "falsa"


@dataclass
class Noticia:
    """Representa uma notícia cadastrada no sistema."""

    texto: str
    classificacao: Classificacao
