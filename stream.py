from redis import Redis


def append(
    stream_name: str,
    data: dict,
    r: Redis,
):
    r.xadd(stream_name, data)
