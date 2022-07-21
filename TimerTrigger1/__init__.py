import datetime
import logging

import azure.functions as func


def main(mytimer: func.TimerRequest) -> None:
    print("I'm drinking coffee rn.")
    logging.info("I'm drinking coffee rn.")
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    #if mytimer.past_due:
    #    logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)

main(None)