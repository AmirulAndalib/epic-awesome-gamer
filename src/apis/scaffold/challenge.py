# -*- coding: utf-8 -*-
# Time       : 2022/1/16 0:25
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import typing

from loguru import logger

from services.bricklayer.game import GameClaimer
from services.settings import PATH_USR_COOKIES, config
from services.utils.toolbox import ToolBox

bricklayer = GameClaimer(email=config.epic_email, password=config.epic_password)


def run(silence: typing.Optional[bool] = None):
    """Refreshing identity tokens"""
    logger.info("STARTUP [ScaffoldChallenge] Updating identity token")
    if bricklayer.cookie_manager.refresh_ctx_cookies(silence=silence):
        ctx_cookies = bricklayer.cookie_manager.load_ctx_cookies()
        with open(PATH_USR_COOKIES, "w", encoding="utf8") as file:
            file.write(ToolBox.transfer_cookies(ctx_cookies))
    logger.success(f"GET [ChallengeRunner] Mission Accomplished!! - path={PATH_USR_COOKIES}")
