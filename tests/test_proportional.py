#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2014-17 Richard Hull and contributors
# See LICENSE.rst for details.


from luma.core.legacy.font import proportional, CP437_FONT


def test_narrow_char():
    font = proportional(CP437_FONT)
    assert font[ord('!')] == [6, 95, 95, 6, 0]


def test_wide_char():
    font = proportional(CP437_FONT)
    assert font[ord('W')] == CP437_FONT[ord('W')]


def test_space_char():
    font = proportional(CP437_FONT)
    assert font[ord(' ')] == [0] * 4


def test_doublequote_char():
    font = proportional(CP437_FONT)
    assert font[ord('"')] == [7, 7, 0, 7, 7, 0]


def test_trim_not_nonzero():
    font = proportional(CP437_FONT)
    assert font._trim([0, 0, 0, 0]) == []
