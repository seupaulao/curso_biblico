# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "Bem-vindo a este Curso Bíblico"

    e "Nosso intuito aqui é te apresentar esse grande livro"

    e "A Bíblia é um livro de relacionamento."

    e "O Relacionamento alvo da Bíblia é : entre Deus e você"

    e "Você, eu e todos os seres humanos"

    e "Isso mesmo : você é personagem da história da Bíblia"

    e "A bíblia é um livro de história. Histórias reais, baseado em pessoas reais. E um Deus real, que quer se relacionar conosco."

    e "A bíblia é composto de vários livros : 66 livros."

    e "A bíblia tem como objetivo te apresentar Deus e vai mostrar também como Ele se relaciona conosco"

    e "A partir daqui começamos nossa jornada!"


    # This ends the game.

    return
