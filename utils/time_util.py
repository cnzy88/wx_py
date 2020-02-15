import time
import datetime

class TimeHelper(object):

    @staticmethod
    def get_current_time():
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    @staticmethod
    def get_current_date():
        return time.strftime('%Y-%m-%d', time.localtime(time.time()))

    @staticmethod
    def current_date_plus_day(days):
        return str((datetime.datetime.now() + datetime.timedelta(days=days)).strftime('%Y-%m-%d'))