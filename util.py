from pathlib import Path

from config import Config


def prepend_log(p: Path, str: str):
    p.touch(exist_ok=True)
    with p.open('r') as f:
        tmp = f.read()
    with p.open('w') as f:
        if tmp:
            f.write(str + Config.LOG_DELIM + tmp)
        else:
            f.write(str)