from os import system

def obter_lista_de_requerimentos() -> list():
    with open('requeriments.txt') as requerimentos:
        lista_de_requerimentos = list()
        
        for requerimento in requerimentos.readlines():
            lista_de_requerimentos.append(requerimento)
        
        return lista_de_requerimentos

def instalar_dependencias() -> None:
    for requerimento in obter_lista_de_requerimentos():
        system(f"pip install {requerimento}")