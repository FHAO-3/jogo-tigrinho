from abc import ABC, abstractmethod
from random import choice, randint
from time import sleep
import itertools
import os

def BaseMachine(ABC):
    # usado para indicar quais os metodos que serão implementados melhor dizendo para saber oque vai acontecer por debaixo dos panos

    @abstractmethod
    def _gen_permutations(self):
        # baseado nas imagens aleatorias quais são todas as combinações
        ...
    
    @abstractmethod
    def _gen_final_result(self):
        # decide a combinação final
        ...
    
    @abstractmethod
    def _display(self):
        # realiza a animação da tela e mostrar o resultado final
        ...
    
    @abstractmethod
    def _check_result_user(self):
        # verifica se usuario ganhou ou perdeu
        ...
    
    @abstractmethod
    def _update_balance(self):
        # gerencia o dinheiro- manda para a maquina o usuario perde ou manda para o usuario caso ganhe
        ...
    
    @abstractmethod
    def emojize(self):
        # usado para trabsfomrar o codigo unicade para um emoji
        ...
    
    @abstractmethod
    def gain(self):
        # mostra o lucro de acordo com o saldo de ganhos 
        ...

    @abstractmethod
    def play(self, amount_bet, player):
        # METODO PRINCIPAL - onde ira psaar o valor que sera apostado `amount_bet`e quem que está realizando aposta `player`
        ...


class Player:
    def __init__(self, balance=0):
        self.balance = balance


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