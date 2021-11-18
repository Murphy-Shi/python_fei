import time
from pathlib import Path
from nb_log import LogManager

log = LogManager('Common').get_logger_and_add_handlers(log_filename="log",
                                                       log_path=Path(__file__).absolute().parent.parent / Path(
                                                           "configure", "pythonlogs"))

if __name__ == '__main__':
    LOG_PATH = Path(__file__).absolute().parent.parent / Path("configure", "pythonlogs")
    log.debug(time.strftime('%Y_%m_%d'))
