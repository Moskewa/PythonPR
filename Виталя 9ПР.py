from enum import Enum


class State(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6


class StateMachine:
    state = State.A

    def brake(self):
        return self.update({
            State.A: [State.B, 0],
            State.B: [State.C, 1],
            State.C: [State.G, 4],
            State.D: [State.E, 6],
        })

    def chain(self):
        return self.update({
            State.C: [State.E, 5],
        })

    def spin(self):
        return self.update({
            State.C: [State.D, 2],
            State.E: [State.F, 7],
            State.F: [State.G, 9],
        })

    def order(self):
        return self.update({
            State.C: [State.C, 3],
            State.E: [State.E, 8],
        })

    def update(self, transitions):
        self.state, signal = transitions[self.state]
        return signal


def main():
    return StateMachine()