# triagem-de-pacientes-Simulador do Protocolo de Manchester 

Este projeto é uma implementação em Python de um sistema de triagem de pacientes baseado no Protocolo de Manchester. Foi desenvolvido como parte da Segunda Avaliação da Fatec Rio Claro.



Descrição
O sistema classifica pacientes por nível de urgência usando uma árvore de decisão. Cada paciente, após responder às perguntas de triagem , é classificado com uma cor (Vermelho, Laranja, Amarelo, Verde ou Azul) e inserido em uma fila de prioridade correspondente.




As filas funcionam no formato FIFO (First-In, First-Out).

Funcionalidades 

O sistema opera através de um menu em loop  que permite as seguintes operações:


Cadastrar paciente: O programa faz as perguntas da árvore de triagem e insere o paciente na fila de sua respectiva cor.


Chamar paciente: Remove e exibe o próximo paciente da fila mais urgente disponível. A ordem de prioridade é: Vermelho > Laranja > Amarelo > Verde > Azul.


Mostrar status: Exibe o tamanho (número de pacientes) de cada fila.


Sair: Encerra o programa.
