import datetime
from dateutil.relativedelta import relativedelta

def hello(event, context):
    today = datetime.date.today()
    yesterday = today + relativedelta(days=-1)

    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event,
        "dates": {
            "today": f'{today: %Y-%m-%d}',
            "yesterday": f'{yesterday: %Y-%m-%d}'
        }
    }
