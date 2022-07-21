import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    my_message = "I just drank a honey cinnamon latte with oat milk at Caffe Ladro. (with cake)"
    print(my_message)
    logging.info(my_message)
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    #if mytimer.past_due:
    #    logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

main(None)
