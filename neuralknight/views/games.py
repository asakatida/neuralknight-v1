from cornice import Service
from pyramid.httpexceptions import HTTPBadRequest

from ..models import Board

games = Service(
    name='games',
    path='/v1.0/games',
    description='Create game')
game_states = Service(
    name='game_states',
    path='/v1.0/games/{game}/states',
    description='Game states')
game_interaction = Service(
    name='game_interaction',
    path='/v1.0/games/{game}',
    description='Game interaction')
game_info = Service(
    name='game_info',
    path='/v1.0/games/{game}/info',
    description='Game info')


def get_game(request):
    """
    Retrieve board for request.
    """
    return Board.get_game(request.matchdict['game'])


@games.get()
def get_games(request):
    """
    Retrieve all game ids.
    """
    return {'ids': list(Board.GAMES.keys())}


@games.post()
def post_game(request):
    """
    Create a new game and provide an id for interacting.
    """
    return {'id': Board().id}


@game_states.get()
def get_states(request):
    """
    Start or continue a cursor of next board states.
    """
    return get_game(request).slice_cursor_v1(**request.GET)


@game_interaction.get()
def get_state(request):
    """
    Provide current state on the board.
    """
    return get_game(request).current_state_v1()


@game_interaction.post()
def join_game(request):
    """
    Add player to board.
    """
    try:
        user_id = request.json['id']
    except KeyError:
        raise HTTPBadRequest
    return get_game(request).add_player_v1(request.dbsession, user_id)


@game_interaction.put()
def put_state(request):
    """
    Make a move to a new state on the board.
    """
    return get_game(request).update_state_v1(request.dbsession, **request.json)


@game_info.get()
def get_info(request):
    """
    Provide current state on the board.
    """
    return {'print': str(get_game(request))}
