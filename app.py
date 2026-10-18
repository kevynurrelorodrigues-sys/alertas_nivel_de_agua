from colorama import Fore, Style #<<< importa a biblioteca colorama para colorir o texto no terminal

def status_nivel_do_reservatorio(nivel):#<<< cria uma função que recebe o nível de água como parâmetro

    match nivel:#<<< transforma a mensagem de cada nivel de água em uma cor diferente
        case "nivel1":
            print(Fore.RED + "Atenção: nível de água muito baixo.")
        case "nivel2":
            print(Fore.YELLOW + "Atenção: nível de água baixo.")
        case "nivel3":
            print(Fore.GREEN + "Nível de água normal.")
        case "nivel4":
           print(Fore.CYAN + "Nível de água alto.")
        case "nivel5":
           print(Fore.BLUE + "Nível de água extremamente alto.")
        case _:
            print("Nível desconhecido.")
#faz uma lista com os niveis de agua começando de 0 a 4, e atribui o nivel atual como nivel5, que é o último da lista
nivel_agua = ["nivel1", "nivel2", "nivel3", "nivel4", "nivel5"]
nivel_atual = nivel_agua[0]#<<< atribui o nível atual como o último da lista, que é "nivel5" mude o índice para 0, 1, 2, 3 ou 4 para testar os outros níveis de água
print(nivel_atual)
#imprime  a situação atual com o nivel  de agua  com a mensagem colorida de acordo com o nível de água 
print(f"Situação atual: {nivel_atual}")
status_nivel_do_reservatorio(nivel_atual)
print(Style.RESET_ALL, end="")