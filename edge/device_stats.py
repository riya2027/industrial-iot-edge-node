from datetime import datetime

START_TIME = datetime.now()


def get_uptime():

    return datetime.now() - START_TIME