# -*- coding: utf-8 -*-
# Time       : 2022/1/20 16:16
# Author     : QIN2DIM
# Github     : https://github.com/QIN2DIM
# Description:
import typing

import hcaptcha_challenger as solver

from services.settings import config


def do(yolo_onnx_prefix: typing.Optional[str] = None, upgrade: typing.Optional[bool] = False):
    """Downloading all the dependencies needed to run the project"""
    onnx_prefix = yolo_onnx_prefix or solver.Prefix.YOLOv6n
    solver.set_reverse_proxy(config.HTTPS_CDN)
    solver.install(onnx_prefix=onnx_prefix, upgrade=upgrade)
