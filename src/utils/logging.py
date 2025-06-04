import sys
import logging
from pathlib import Path
from loguru import logger

class InterceptHandler(logging.Handler):
    def emit(self, record):
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = record.levelno
        
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = frame.f_back
            depth += 1
        
        logger.opt(depth=depth, exception=record.exc_info).log(level, record.getMessage())

def setup_logging(log_dir: str = "logs", rotation: str = "1 day", retention: str = "31 days"):
    log_path = Path(log_dir)
    log_path.mkdir(exist_ok=True)
    
    logger.remove()
    
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="INFO",
        colorize=True
    )
    
    logger.add(
        f"{log_dir}/{{time:YYYY-MM-DD}}.log",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG",
        rotation=rotation,
        retention=retention,
        compression="zip"
    )
    
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    
    for logger_name in ("aiogram", "tortoise", "asyncio"):
        mod_logger = logging.getLogger(logger_name)
        mod_logger.handlers = [InterceptHandler()]
        mod_logger.propagate = False
    
    logger.success("Logging configured succesfuly.")
    return logger
