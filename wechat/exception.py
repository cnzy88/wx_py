class NotAccessTokenException(Exception):
    pass

class WeixinPayError(Exception):

    def __init__(self, msg):
        super(WeixinPayError, self).__init__(msg)