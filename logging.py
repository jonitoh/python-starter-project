# -*- coding: utf-8 -*-
"""Code to manage logging of the starter project base """
# IMPORT ALL THE REQUIRED LIBRARIES
import os
import json
import logging
import logging.config

__all__ = ['setup_logging']


# REQUIRED FUNCTIONS FOR THE WHOLE PACKAGE
def setup_logging(default_path='logging.json', default_level=logging.INFO,
    env_key='LOG_CFG'):
    """Configure the logging """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


setup_logging()
LOG = logging.getLogger(__name__)
