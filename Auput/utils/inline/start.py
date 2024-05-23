from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO, SUPPORT_CHANNEL, SUPPORT_GROUP
from Auput import app


def start_pannel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"],
                url=f"https://t.me/{app.username}?start=help",
            ),
            InlineKeyboardButton(
                text=_["S_B_2"], callback_data="settings_helper"
            ),
        ],
    ]
    if SUPPORT_CHANNEL and SUPPORT_GROUP:
        buttons.append(
            [
                InlineKeyboardButton(
                    text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                ),
                InlineKeyboardButton(
                    text=_["S_B_3"], url=f"{SUPPORT_GROUP}"
                ),
            ]
        )
    else:
        if SUPPORT_CHANNEL:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_4"], url=f"{SUPPORT_CHANNEL}"
                    )
                ]
            )
        
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(text=_["S_B_8"], callback_data="settings_back_helper"),
            InlineKeyboardButton(text="CH", url=f"https://t.me/fakeSupportt"),
            InlineKeyboardButton(text="OWNER", url="https://t.me/malespakeidd"),
        ]
    ]
    buttons.append(
        [
            InlineKeyboardButton(
                text=_["S_B_5"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ]
    )
    if GITHUB_REPO:
        buttons.append(
            [
                
                InlineKeyboardButton(
                    text=_["S_B_6"], url=f"https://github.com/"
                ),
            ]
        )
    else:
        if GITHUB_REPO:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text=_["S_B_6"], url=f"https://github.com/"
                    ),
                ]
            )
    buttons.append(
        [
            InlineKeyboardButton(text=_["ST_B_6"], callback_data="LG"),
            InlineKeyboardButton(
                text="Donate", url="https://telegra.ph//file/ab858687bea52e9dde445.jpg"
            ),
        ]
                  )
    return buttons
