#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2017 Richard Hull and contributors
# See LICENSE.rst for details.

"""
Tests for the deprecated :py:mod:`luma.core.serial` module.
"""

import pytest


def test_module_deprecated():
    """
    The :py:mod:`luma.core.serial` module is deprecated.
    """
    msg = ("luma.core.serial is deprecated and will be removed in " +
        "v1.0.0: use luma.core.interface.serial instead")

    with pytest.deprecated_call() as c:
        import luma.core.serial  # noqa: F401

        assert str(c.list[0].message) == msg


def test_module_all_equal():
    """
    :py:mod:`luma.core.serial`'s module provides the same ``__all__`` list
    as :py:mod:`luma.core.interface.serial`.
    """
    import luma.core.serial
    from luma.core.interface.serial import __all__

    assert luma.core.serial.__all__ == __all__
