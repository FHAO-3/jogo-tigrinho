# Documentação do Código de Cassa Níquel

Este código é um exemplo de implementação de uma máquina cassa níquel em Python. Abaixo está uma descrição detalhada das classes e métodos usados.

## Classes

### BaseMachine (ABC)
Classe base abstrata que define a estrutura para máquinas de jogos. Todos os métodos nela definidos são abstratos e precisam ser implementados nas classes filhas.

### Player
Representa um jogador com um saldo.
- **__init__(balance=0)**: Inicializa o jogador com um saldo padrão de 0.

### CassaNiquel
Representa a máquina de cassa níquel.
- **__init__(level=1, balance=0)**: Inicializa a máquina com um nível especificado e saldo inicial. Também define os símbolos (emojis) a serem usados na máquina.
- **_gen_permutation()**: Gera todas as combinações possíveis dos símbolos e as salva. O nível define o número de combinações específicas adicionadas.
- **_get_final_result()**: Obtém um resultado aleatório da lista de combinações. Se todos os elementos são diferentes, há uma pequena chance de se repetir um elemento.
- **_display(amount_bet, result, time=0.2)**: Anima a máquina e exibe o resultado final, mostrando se o jogador venceu ou perdeu.
- **_emojize(emojis)**: Converte códigos Unicode em emojis.
- **_check_result_user(result)**: Verifica se o jogador venceu. Retorna True se todos os elementos no resultado forem iguais.
- **_update_balance(amount_bet, result, player)**: Atualiza o saldo da máquina e do jogador com base no resultado.
- **play(amount_bet, player)**: Executa o jogo, exibindo o resultado e atualizando os saldos.

## Função Principal

### run_machine()
Função que mantém a máquina funcionando em loop até que o jogador pare o jogo.
- Inicializa a máquina e o jogador, roda o jogo repetidamente, e imprime o saldo ao fim.

```python
from abc import ABC, abstractmethod
from random import choice, randint
from time import sleep
import itertools
import os

# Definindo a classe base abstrata para a máquina
class BaseMachine(ABC):
    @abstractmethod
    def _gen_permutations(self):
        ...
    
    @abstractmethod
    def _gen_final_result(self):
        ...
    
    @abstractmethod
    def _display(self):
        ...
    
    @abstractmethod
    def _check_result_user(self):
        ...
    
    @abstractmethod
    def _update_balance(self):
        ...
    
    @abstractmethod
    def emojize(self):
        ...
    
    @abstractmethod
    def gain(self):
        ...

    @abstractmethod
    def play(self, amount_bet, player):
        ...

# Classe para representar o jogador
class Player:
    def __init__(self, balance=0):
        self.balance = balance

# Classe principal CassaNiquel
class CassaNiquel:
    def __init__(self, level=1, balance = 0):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F976',
            'alien': '1F47D',
            'hearth_of_fire': '2764',
            'coliston': '1F4A5'
        }
        self.level = level
        self.permutation = self._gen_permutation()
        self.balance = balance
        self.initial_balance = self.balance

    def _gen_permutation(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS:
                permutations.append((i, i, i))
        return permutations
    
    def _get_final_result(self):
        if not hasattr(self, 'permutations'):
            self.permutation = self._gen_permutation()
        
        result = list(choice(self.permutation))

        if len(set(result)) == 3 and randint(0, 5) >= 2:
            result[1] = result[0]

        return result

    def _display(self, amount_bet, result, time=0.2):
        
        seconds = 0.1
        
        for i in range(0, int(seconds/time)):
            print(self._emojize(choice(self.permutation)))
            sleep(time)
            os.system('clear')
        print('>', self._emojize(result))
        
        if self._check_result_user(result):
            print(f'Você venceu e recebeu: {amount_bet*3}')
        else:
            print('Foi quase tente novamente')
    
    def _emojize(self, emojis):
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))
    
    def _check_result_user(self, result):
        x = [result[0] == x for x in result]
        return True if all(x) else False

    def _update_balance(self, amount_bet, result, player:Player):
        if self._check_result_user(result):
            self.balance -= (amount_bet * 3)
            player.balance = (amount_bet * 3)
        else: 
            self.balance += amount_bet
            player.balance -= amount_bet

    def play(self, amount_bet, player:Player):
        result = self._get_final_result()
        self._display(amount_bet, result)
        self._update_balance(amount_bet, result, player)

# Função principal que roda a máquina
def run_machine():
    while True:
        machine1 = CassaNiquel(level=4)
        usuer1 = Player()
        machine1.play(10, usuer1)

        next = str(input('Clique agora!'))

        if next != '':
            print('Finalizando ...')
            print('Valor final da maquina: ', machine1.balance)
            print('Valor final da usuario: ', usuer1.balance)
            exit(1)
        
run_machine()
```
