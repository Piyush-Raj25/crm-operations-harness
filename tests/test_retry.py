import sys

sys.path.append("src")

from tools.retry import Retry


count = 0


def test():

    global count

    count += 1

    print(f"Attempt {count}")

    if count < 3:
        raise Exception("Failed")

    return "Success"


print(Retry.run(test))