# Sistema de Monitoramento de Fake News

Projeto refatorado para a disciplina **DIM0501 - Boas Práticas de Programação**.

## Descrição

O sistema permite cadastrar textos de notícias, classificá-los como `confiavel`, `duvidosa` ou `falsa` e listar as notícias cadastradas. A classificação pode ser informada manualmente ou calculada automaticamente com base em critérios simples:

- ausência da palavra `FONTE`;
- presença de linguagem sensacionalista, como `!!!` ou `URGENTE`;
- texto com menos de 10 caracteres.

## Estrutura do projeto

```text
sistema_noticias_refatorado/
├── main.py
├── README.md
├── docs/
│   └── relatorio_tecnico_simplificado.pdf
└── sistema_noticias/
    ├── __init__.py
    ├── modelo.py
    ├── servico.py
    └── interface.py
```

## Como executar

Na raiz do projeto, execute:

```bash
python main.py
```
- Remoção de comentários redundantes.
- Inclusão de docstrings e documentação básica do projeto.

## Observação

O sistema preserva o comportamento principal do código original, mas organiza a implementação para facilitar manutenção e evolução.
