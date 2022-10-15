# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:25
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import typing

from loguru import logger

from services.deploy import ClaimerScheduler


@logger.catch()
def deploy(unreal: typing.Optional[bool] = False):
    """Deploy in tiny containers `claim` Scheduled tasks"""
    ClaimerScheduler(silence=True, unreal=unreal).deploy_on_vps()


@logger.catch()
def run(
    silence: typing.Optional[bool] = None,
    log_ignore: typing.Optional[bool] = None,
    unreal: typing.Optional[bool] = False,
):
    """Running `claim` Single-step sub-task, claiming weekly free games"""
    ClaimerScheduler(silence=silence, unreal=unreal).job_loop_claim(log_ignore)
