from scripts.utils import run_script


def db_up():
    run_script(["docker","compose","up","-d"])


def db_down():
    run_script(["docker","compose","down"])


def db_console():
    run_script(["docker","exec","-it","api-db","psql","-U","postgres"])