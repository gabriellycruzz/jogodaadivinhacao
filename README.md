# Jogo da Forca

## Descrição
Este é um jogo de adivinhação simples de "Jogo da Forca" implementado em Python. O objetivo do jogo é adivinhar uma palavra secreta, escolhendo letras uma por uma, dentro de um número limitado de tentativas.

## Funcionalidades
- O jogador pode escolher o número de tentativas, que pode variar entre 1 e 25.
- O jogador também define o tamanho mínimo das palavras, que deve estar entre 4 e 10 caracteres.
- A palavra secreta é escolhida aleatoriamente a partir de um arquivo de palavras.
- O jogo permite que o jogador jogue várias rodadas até escolher a opção de sair.

## Tecnologias
- Python 3.7.0
- A biblioteca unicodedata para remover acentos e caracteres especiais.
- Arquivo de palavras para o jogo: palavras_forca.txt (O arquivo deve estar na mesma pasta que o script).
