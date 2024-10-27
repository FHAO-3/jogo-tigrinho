from abc import ABC, abstractmethod
import itertools

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


class CassaNiquel:

    def __init__(self):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F976',
            'alien': '1F47D',
            'hearth_of_fire': '2764',
            'coliston': '1F4A5'
        }

    def _gen_permutation(self):
        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        print(permutations)


machine1 = CassaNiquel()
machine1._gen_permutation()