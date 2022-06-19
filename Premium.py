from .. import loader
from telethon.tl.types import Message
from telethon.tl.functions.messages import ForwardMessagesRequest


@loader.tds
class PremiumStickMod(loader.Module):
    """Sends Telegram Premium sticker"""

    strings = {"name": "PremiumStick"}

    async def client_ready(self, client, db):
        self._client = client

    async def dancecmd(self, message: Message):
        """Send a sticker"""
        async for msg in self._client.iter_messages("@hikka_fs_stickers"):
            if getattr(msg, "sticker", False):
                await message.delete()
                await self._client(
                    ForwardMessagesRequest(
                        from_peer="@hikka_fs_stickers",
                        to_peer=message.peer_id,
                        id=[msg.id],
                        drop_author=True,
                    )
                )
