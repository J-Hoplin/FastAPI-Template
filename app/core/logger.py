import logging

"""
Inject logger to request handler
"""
def get_logger():
    logger = logging.getLogger("uvicorn")
    return logger