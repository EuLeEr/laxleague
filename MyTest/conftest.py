from random import choice, randint

import pytest

from laxleague.games import Game
from laxleague.players import Player
from laxleague.teams import Team

@pytest.fixture
def game_type():
    return Game
