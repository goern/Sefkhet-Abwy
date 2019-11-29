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

from aicoe.sesheta.chatbot import get_intent


class TestChatbot:
    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "user_text, issue_url, github_username",
        [
            (
                "assign https://github.com/thoth-station/core/issues/23 to fridex",
                "https://github.com/thoth-station/core/issues/23",
                "fridex",
            ),
        ],
    )
    async def test_get_intent(self, user_text, issue_url, github_username):
        (s, p, o) = await get_intent(user_text)

        assert s == github_username
        assert p == "assign"
        assert o == issue_url

