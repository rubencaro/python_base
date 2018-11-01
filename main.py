# Actual entry point
def main():
  print("Hello world!")
  return True

# Execution wrapper
def init(as_main=False):
  if __name__ == "__main__" or as_main:
    return main()

init()