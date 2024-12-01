import sys
import os
import pytest
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from dineable import PeopleDinner, RobotDinner

def test_people_dinner():
    people_dinner = PeopleDinner()
    people_dinner.serveDinner("Car1")
    assert people_dinner.people_served == 1

def test_robot_dinner():
    robot_dinner = RobotDinner()
    robot_dinner.serveDinner("Car2")
    assert robot_dinner.robots_served == 1

# python -m pytest test_dineable.py