import requests
import time
import logging
logger = logging.getLogger(__name__)


def retry(func):
    def inner(*args, **kwargs):
        """
        retry is a decorator which retries HTTP calls
        for maximum of 5 times
        it waits for 10 seconds after each unsuccessful call
        """
        init_retry_count = 0
        max_retry_count = 5
        retry_interval_btw_two_calls = 10
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
        raise requests.RequestException("problem in making HTTP call please check logs")
    return inner


@retry
def make_http_call(url, method):
    return requests.request(method, url, verify=False)


if __name__ == "__main__":
    make_http_call("https://lokesh1729.free.beeceptor.com/abc/", "GET")
