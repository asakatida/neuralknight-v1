from ..models import BaseBoard


class MockBoard(BaseBoard):
    def __init__(self, testapp):
        self.testapp = testapp
        self.args = {}
        self.kwargs = {}
        super().__init__([[[[0 for i in range(8)] for j in range(8)]]])

    def slice_cursor_v1(self, *args, **kwargs):
        self.args['slice_cursor_v1'] = args
        self.kwargs['slice_cursor_v1'] = kwargs
        return {
            'cursor': None,
            'boards': self.board
        }

    def add_player_v1(self, *args, **kwargs):
        self.args['add_player_v1'] = args
        self.kwargs['add_player_v1'] = kwargs
        player = args[1]
        if self.player1:
            self.player2 = player
        else:
            self.player1 = player
        self.poke_player(False)
        return {}

    def update_state_v1(self, *args, **kwargs):
        self.args['update_state_v1'] = args
        self.kwargs['update_state_v1'] = kwargs
        return {'end': True}


def test_make_move(testapp):
    mockboard = MockBoard(testapp)
    player1 = testapp.post_json('/issue-agent', {'id': mockboard.id}).json
    player2 = testapp.post_json('/issue-agent', {'id': mockboard.id, 'player': 2}).json

    assert player1
    assert player2
