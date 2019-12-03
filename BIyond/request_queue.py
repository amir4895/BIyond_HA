class RequestQueueObject:

    """
    class to describe a request in the request queue that analyze timeout requests
    """

    def __init__(self, fut_ps, data):
        self.future_ps = fut_ps
        self.data = data
