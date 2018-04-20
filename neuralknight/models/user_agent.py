from .base_agent import BaseAgent


class UserAgent(BaseAgent):
    '''Human Agent'''

    def __init__(self, game_id, player):
        super().__init__(game_id, player)

    def play_round(self, move):
        if move is None:
            return
        proposal = self.get_state()
        if isinstance(proposal, dict):
            return
        proposal = list(map(list, map(bytes.fromhex, proposal)))
        proposal[move[1][0]][move[1][1]] = proposal[move[0][0]][move[0][1]]
        proposal[move[0][0]][move[0][1]] = 0
        return self.put_board(tuple(map(bytes, proposal)))
