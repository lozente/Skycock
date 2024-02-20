from datetime import datetime


def get_current_standard_quarter() -> int:
    return (datetime.now().month - 1) // 3 + 1
