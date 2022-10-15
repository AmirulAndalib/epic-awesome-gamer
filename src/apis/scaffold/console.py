# -*- coding: utf-8 -*-
# Time       : 2022/7/4 23:03
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import os.path
import subprocess
import sys
import typing

from services.settings import DIR_LOG


def get_logger(start: typing.Optional[bool] = False):
    path_runtime_log = os.path.join(DIR_LOG, "runtime.log")
    log_mapping = {
        "path_log_runtime": path_runtime_log,
        "path_log_error": os.path.join(DIR_LOG, "error.log"),
        "dir_screenshot": os.path.join(os.path.dirname(DIR_LOG), "challenge_result"),
    }

    # Automatically open the log directory
    if start is True:
        if sys.platform == "win32":
            os.startfile(DIR_LOG)
        elif sys.platform == "darwin":
            subprocess.call(["open", DIR_LOG])
        elif sys.platform == "linux":
            for name, path_ in log_mapping.items():
                print(f"{name} --> {path_}")
        return

    # Echo log sequence
    _session = []

    # Segmentation of logs based on start cmd's
    # Get the log of the last Scaffold command
    with open(path_runtime_log, "r", encoding="utf8") as file:
        data = file.readlines()
    for i in data[::-1]:
        _session.append(i.strip())
        if ">> STARTUP [AwesomeScheduler]" in i:
            break

    # Print back the logs
    for i in _session[::-1]:
        print(i)


if __name__ == "__main__":
    get_logger()
