from teeko import Board, Match, Player, Cell


class State:
    def __init__(self):
        self.utility = None

    def utility_function(self, state):
        #cantidad de movimientos que tomo llegar a la victoria
        return False


    def terminal_test(self, player):
        #verificar si el juego ya llego a un estado terminal
        return False



class IA:
    # black=max red=min
    def __init__(self, initialState):
        self.initialState = initialState

    def min_max_desicion(self, state, player):
        if (player.playerColor == "black"):
            #retorna un estado? como obtenerlo?
            max = self.min_value(state, player)
            return max
        else:
            min = self.max_value(state, player)
            return min

    def min_value(self, state):
        if (state.terminal_test(state)):
            return state.utility_function(state)
        v = 1000

        #entender que es Result(S,a)
        #actions deberia ser un metodo que expande el estado mostrando sus acciones

        for a in Actions(state):
            v = Min(v, self.max_value(Result(S,a)))

        #ver como retornar un estado y no un valor
        return v

    def max_value(self, state):
        if (state.terminal_test(state)):
            return state.utility_function(state)
        min = -1000

        for a in Actions(state):
            v = Max(v, self.min_value(Result(S, a)))
        return v