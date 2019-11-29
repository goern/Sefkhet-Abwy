#!/usr/bin/env python3
# sesheta-actions
# Copyright(C) 2019 Christoph Görn
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Sesheta's actions Tests."""


import typing
import pytest

from aicoe.sesheta.utils import extract_url_from_text


class TestURLExtraction:
    def test_extract_no_url(self):
        assert extract_url_from_text("lame test text") == []

    @pytest.mark.parametrize(
        "input_text, expected_urls, expected_urls_total",
        [
            ("lame https://test.com and https://text.net", ["https://test.com", "https://text.net"], 2),
            ("lame https://test.com text", ["https://test.com text"], 1),
        ],
    )
    def test_extract_urls(self, input_text, expected_urls: typing.List[str], expected_urls_total: int):
        urls = extract_url_from_text(input_text)

        assert urls is not None
        assert type(urls) is list
        assert len(urls) == expected_urls_total
