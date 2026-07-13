import time


class Retry:
    """
    Executes a function with retry support.
    """

    @staticmethod
    def run(
        function,
        retries=3,
        delay=1,
        on_retry=None,
    ):

        last_exception = None

        for attempt in range(1, retries + 1):

            try:
                return function()

            except Exception as e:

                last_exception = e

                if on_retry:
                    on_retry(attempt, e)

                if attempt < retries:
                    time.sleep(delay)

        raise last_exception