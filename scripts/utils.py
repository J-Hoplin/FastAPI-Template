import subprocess
from typing import List

def run_script(script:List[str]) -> None:
    return subprocess.run(script)
