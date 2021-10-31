import sys

class LoggerConfig:
    format = '[<green>{time:DD-MMM-YY}</green> | <green>{time:HH:mm:ss}</green>] | <lvl>{level: <8}</lvl> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <lvl>{message}</lvl>'
    config_handlers = {
        'handlers': [
            {'sink': 'log/log.log', 'rotation': '5 MB', 'compression': 'zip', 'format': format},
            {'sink': sys.stdout, 'format': format}
        ]
    }
