# Created by euleer at 10/16/18
Feature: Games
  Вродем здесь описание всего

  Scenario: Определить победителя
    Given Домашняя команда в Голубом
    And Команда гостей в Красном
    And Игра идет между ними
    When Счет 5 у Голубом и 4 у Красном
    Then Голубом победители