from pytest_bdd import scenario, given, when, then

from laxleague.teams import Team
from laxleague.games import Game

@scenario('myGherkin.feature', 'Определить победителя')
def test_games_feature():
    pass


@given("Домашняя команда в Голубом")
def blue():
    return Team("Голубом")
#def step_impl():
#    raise NotImplementedError(u'STEP: Given Домашняя команда в Голубом')


@given("Команда гостей в Красном")
def red():
    return Team("Красном")


@given('Игра идет между ними')
def game_red_blue(game_type, blue, red):
    return game_type(home_team=blue, visitor_team=red)


@when('Счет 5 у Голубом и 4 у Красном')
def record_score(game_red_blue):
    game_red_blue.record_score(5, 4)


@then('Голубом победители')
def winner(game_red_blue):
    assert "Голубом" == game_red_blue.winner.name