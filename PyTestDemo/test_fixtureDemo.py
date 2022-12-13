import pytest


# Fixtures are used for setup & tear down methods for test cases - conftest file to generalize
# fixture and make it available to all test cases
# Data-Driven and Parameterization can be done with return statements in tuple format
# when you define fixture scope to class only, it will run once before class is initiated and at the end

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute fixture demo method1")

    def test_fixtureDemo2(self):
        print("I will execute fixture demo method2")

    def test_fixtureDemo3(self):
        print("I will execute fixture demo method3")


    def test_fixtureDemo4(self):
        print("I will execute fixture demo method4")
