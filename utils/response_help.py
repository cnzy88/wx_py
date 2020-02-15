class ResponseHelp(object):

    @staticmethod
    def success_simplify():
        return {
            'code': 0
        }

    @staticmethod
    def success(data):
        return {
            'code': 0,
            'data': data
        }

    @staticmethod
    def failed_simplify(msg):
        return {
            'code': 1,
            'msg': msg
        }

    @staticmethod
    def failed(code, msg):
        return {
            'code': code,
            'msg': msg
        }

    @staticmethod
    def success_with_pagination(data, pagination):
        return {
            'code': 0,
            'data': data,
            'pagination': pagination
        }