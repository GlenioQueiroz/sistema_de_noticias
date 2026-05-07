"""Interface de linha de comando do Sistema de Notícias."""

from sistema_noticias.servico import (
    adicionar_noticia,
    analisar_noticia,
    listar_noticias,
)


OPCOES_MENU = {
    "1": "Adicionar notícia manualmente",
    "2": "Adicionar notícia automaticamente",
    "3": "Listar notícias",
    "4": "Sair",
}


def exibir_menu() -> None:
    """Exibe as opções disponíveis no menu principal."""
    print("\nSistema de Monitoramento de Fake News")
    for codigo, descricao in OPCOES_MENU.items():
        print(f"{codigo} - {descricao}")


def ler_texto_noticia() -> str:
    """Solicita o texto da notícia ao usuário."""
    return input("Digite o texto: ")


def adicionar_noticia_manual() -> None:
    """Cadastra uma notícia usando a classificação digitada pelo usuário."""
    texto = ler_texto_noticia()
    classificacao = input("Digite a classificação (confiavel, duvidosa ou falsa): ")

    try:
        adicionar_noticia(texto, classificacao)
        print("Notícia cadastrada com sucesso.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def adicionar_noticia_automatica() -> None:
    """Cadastra uma notícia com classificação calculada automaticamente."""
    texto = ler_texto_noticia()

    try:
        classificacao = analisar_noticia(texto)
        adicionar_noticia(texto, classificacao.value)
        print(f"Notícia cadastrada como: {classificacao.value}.")
    except ValueError as erro:
        print(f"Erro: {erro}")


def exibir_noticias() -> None:
    """Mostra todas as notícias cadastradas."""
    noticias = listar_noticias()

    if not noticias:
        print("Nenhuma notícia cadastrada.")
        return

    for noticia in noticias:
        print("Texto:", noticia.texto)
        print("Classificação:", noticia.classificacao.value)
        print("-------------------")


def executar_menu() -> None:
    """Executa o menu principal até que o usuário escolha sair."""
    while True:
        exibir_menu()
        opcao = input("Opção: ").strip()

        if opcao == "1":
            adicionar_noticia_manual()
        elif opcao == "2":
            adicionar_noticia_automatica()
        elif opcao == "3":
            exibir_noticias()
        elif opcao == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Escolha uma opção entre 1 e 4.")
