import os
import sys
import importlib.util

config = None

def load_config():
    global config
    if config is None:
        base_dir = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(__file__)
        config_path = os.path.join(base_dir, "config.py")

        if os.path.exists(config_path):
            spec = importlib.util.spec_from_file_location("config", config_path)
            config = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(config)
        else:
            raise FileNotFoundError("Config file not found at path: ", config_path)
    return config