# python3

from collections import namedtuple
from typing import List

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


def process_buffer(buffer_size: int, requests: List[Request]) -> List[Response]:
    """
    >>> process_buffer(1, [])
    []

    >>> process_buffer(1, [Request(0, 1), Request(0, 1)])
    [Response(was_dropped=False, started_at=0), Response(was_dropped=True, started_at=-1)]

    >>> process_buffer(1, [Request(0, 1), Request(1, 1)])
    [Response(was_dropped=False, started_at=0), Response(was_dropped=False, started_at=1)]
    """
    requests = sorted(requests, key=lambda x: x.arrived_at)

    finish_times = []
    response_list = []

    for request in requests:

        while finish_times:
            if request.arrived_at < finish_times[0]:
                break
            else:
                finish_times.pop(0)

        if len(finish_times) < buffer_size:
            if finish_times:
                response_list.append(Response(False, finish_times[-1]))
                finish_times.append(finish_times[-1] + request.time_to_process)
            else:
                response_list.append(Response(False, request.arrived_at))
                finish_times.append(request.arrived_at + request.time_to_process)
        else:
            response_list.append(Response(True, -1))

    return response_list


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    responses = process_buffer(buffer_size, requests)

    for response in responses:
        print(response.started_at)


if __name__ == "__main__":
    main()
