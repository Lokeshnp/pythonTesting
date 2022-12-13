import pytest


# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped with method only
# Method name should have sense
# -k stands for method names excution, -s logs in out put, -v stands for more info metadata
# you can run specific file with py.test <filename>
# You can mark (tag) tests @pytest.mark.smoke and then run with -m
# You can skip tests with import pytest @pytest.mark.skip
# @pytest.mark.xfail -> will execute the test case but not reporting whether its pass or fail

# Command for running all the tests from folder -> py.test
# Command for running selected test files -> py.test test_demo2.py -v -s
# Command for running selected tests from multiple files -> py.test -k CreditCard -v -s
# Command for tagging test cases with specific tag like smok, regression, etc -> py.test -m smoke -v -s
# Command for generating html report -> pytest --html=report.html -s


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")


@pytest.mark.xfail
def test_CreditCard():
    print("Good Morning")


def test_CrossBrowser(crossBrowser):
    print(crossBrowser[1])
