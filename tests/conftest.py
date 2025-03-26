import sys

from src.wse.config.config import PROJECT_PATH

import_path = str(PROJECT_PATH / 'src')
sys.path.insert(0, import_path)
