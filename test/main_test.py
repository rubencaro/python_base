
# simple meaningless test
def test_truth():
  assert 1 == 1

# test init function
def test_init():
  from python_base import main
  assert main.init(as_main=True)
