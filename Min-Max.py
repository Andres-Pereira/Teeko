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
            max = self.min_value(Result(S,a))
            return max
        else:
            min = self.max_value(Result(S,a))
            return min

    def min_value(self, state):
        #retorna un estado con valor utilitario  (objeto con accion y val num)

        if (state.terminal_test(state)):
            return state.utility_function(state)
        v = 1000

        #entender que es Result(S,a)
        #actions deberia ser un metodo que expande el estado mostrando sus acciones disponibles

        for a in Actions(state):
            v = min(v, self.max_value(Result(S,a))

        #funcion Min selecciona el minimo entre v y max_value

        #result es como funcion de trancision segun estado actual y accion

        #ver como retornar un estado y no un valor
        return v

    def max_value(self, state):
        if (state.terminal_test(state)):
            return state.utility_function(state)
        min = -1000

        for a in Actions(state):
            v = max(v, self.min_value(Result(S, a)))
        return v