import logging
import colorlog

def get_logger(name: str, level: str = 'DEBUG') -> logging.Logger:
    level_str = level.upper()
    levels = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    logger = logging.getLogger(name)
    logger.setLevel(levels.get(level_str, logging.INFO))
    # Create color formatter
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(levelname)s:%(reset)s %(asctime)s - %(name)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        reset=True,
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bold_red',
        }
    )
    # Console handler
    ch = logging.StreamHandler()
    ch.setLevel(levels.get(level_str, logging.INFO))
    ch.setFormatter(color_formatter)
    logger.addHandler(ch)
    return logger
