import sys
from collections import deque

class Fila:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class NodoArvore:
    def __init__(self, pergunta=None, classificacao=None, filho_sim=None, filho_nao=None):
        self.pergunta = pergunta
        self.classificacao = classificacao
        self.filho_sim = filho_sim
        self.filho_nao = filho_nao

    def is_folha(self):
        return self.classificacao is not None

def montar_arvore():
    
    folha_vermelho = NodoArvore(classificacao={'cor': 'Vermelho', 'desc': 'Emergência (atendimento imediato)'})
    folha_laranja = NodoArvore(classificacao={'cor': 'Laranja', 'desc': 'Muito urgente'})
    folha_amarelo = NodoArvore(classificacao={'cor': 'Amarelo', 'desc': 'Urgente'})
    folha_verde = NodoArvore(classificacao={'cor': 'Verde', 'desc': 'Pouco urgente'})
    
    no_dor = NodoArvore(pergunta="Está com dor intensa? (s/n):",
                        filho_sim=folha_amarelo,
                        filho_nao=folha_verde)

    no_consciente = NodoArvore(pergunta="Está consciente? (s/n):",
                               filho_sim=no_dor,
                               filho_nao=folha_laranja)

    raiz = NodoArvore(pergunta="O paciente está respirando? (s/n):",
                      filho_sim=no_consciente,
                      filho_nao=folha_vermelho)

    return raiz

def triagem(nodo_atual):
    while not nodo_atual.is_folha():
        resposta = ''
        while resposta not in ['s', 'n']:
            resposta = input(f"  {nodo_atual.pergunta} ").strip().lower()
            if resposta not in ['s', 'n']:
                print("  Resposta inválida. Por favor, digite 's' (sim) ou 'n' (não).")
        
        if resposta == 's':
            nodo_atual = nodo_atual.filho_sim
        else:
            nodo_atual = nodo_atual.filho_nao
            
    return nodo_atual.classificacao

def mostrar_menu():
    print("\n" + "="*35)
    print(" === SISTEMA DE TRIAGEM MANCHESTER ===")
    print("="*35)
    print(" 1 - Cadastrar paciente")
    print(" 2 - Chamar paciente")
    print(" 3 - Mostrar status das filas")
    print(" 0 - Sair")
    print("="*35)

def cadastrar_paciente(arvore_raiz, filas):
    print("\n--- Cadastro de Paciente ---")
    nome = input("  Nome do paciente: ")
    
    classificacao = triagem(arvore_raiz)
    cor = classificacao['cor']
    desc = classificacao['desc']
    
    filas[cor].enqueue(nome)
    
    print(f"  Cor atribuída: {cor} ({desc})")
    print(f"  Paciente {nome} adicionado à fila {cor.lower()}.")

def chamar_paciente(filas):
    print("\n--- Chamada de Paciente ---")
    
    ordem_prioridade = ['Vermelho', 'Laranja', 'Amarelo', 'Verde', 'Azul']
    
    paciente_chamado = False
    for cor in ordem_prioridade:
        if not filas[cor].is_empty():
            paciente = filas[cor].dequeue()
            print(f"  Chamando paciente da fila {cor}: {paciente}")
            paciente_chamado = True
            break
            
    if not paciente_chamado:
        print("  Nenhum paciente aguardando nas filas.")

def mostrar_status(filas):
    print("\n--- Status das Filas ---")
    for cor, fila in filas.items():
        print(f"  Fila {cor}: {fila.size()} paciente(s)")

def main():
    
    arvore_raiz = montar_arvore()
    
    filas = {
        'Vermelho': Fila(),
        'Laranja': Fila(),
        'Amarelo': Fila(),
        'Verde': Fila(),
        'Azul': Fila()
    }
    
    while True:
        mostrar_menu()
        escolha = input("  Escolha: ").strip()
        
        if escolha == '1':
            cadastrar_paciente(arvore_raiz, filas)
        elif escolha == '2':
            chamar_paciente(filas)
        elif escolha == '3':
            mostrar_status(filas)
        elif escolha == '0':
            print("Encerrando o sistema...")
            sys.exit(0)
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()