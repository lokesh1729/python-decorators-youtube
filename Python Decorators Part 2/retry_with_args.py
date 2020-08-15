import requests
import time
import logging
logger = logging.getLogger(__name__)


def retry(retry_count=5, retry_interval=10):
    def wrapped(func):
        def inner(*args, **kwargs):
            """
            retry is a decorator which retries HTTP calls
            for maximum of 5 times
            it waits for 10 seconds after each unsuccessful call
            """
            init_retry_count = 0
            max_retry_count = retry_count
            retry_interval_btw_two_calls = retry_interval
            response = None
            while init_retry_count < max_retry_count:
                try:
                    response = func(*args, **kwargs)
                    if response.status_code in [200, 201]:
                        return response
                except requests.RequestException:
                    logger.error("error in making call")
                print("request failed, sleeping for %s seconds" % retry_interval_btw_two_calls)
                time.sleep(retry_interval_btw_two_calls)
                init_retry_count += 1
            return response
        return inner
    return wrapped


@retry(retry_count=3, retry_interval=1)
def make_http_call(url, method):
    return requests.request(method, url, verify=False)


if __name__ == "__main__":
    response = make_http_call("https://lokesh1729.free.beeceptor.com/abc/", "GET")
    if response is not None:
        print(response.content)
