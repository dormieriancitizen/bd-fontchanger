from typing import TYPE_CHECKING

from discord import app_commands
from discord.ext import commands

from PIL import ImageFont

from ballsdex.core.image_generator import image_gen

if TYPE_CHECKING:
    from ballsdex.core.bot import BallsDexBot

from ..models import Font, FontType


class FontchangerCog(commands.Cog):
    originals: dict[FontType, ImageFont.FreeTypeFont]

    def __init__(self, bot: "BallsDexBot"):
        self.bot = bot

    async def cog_load(self):
        self.originals = {
            FontType.TITLE: image_gen.title_font,
            FontType.ABILITY_NAME: image_gen.capacity_name_font,
            FontType.ABILITY_DESC: image_gen.capacity_description_font,
            FontType.STATS: image_gen.stats_font,
            FontType.CREDITS: image_gen.credits_font,
        }

        await self.monkeypatch()

    async def monkeypatch(self):
        image_gen.title_font = self.originals[FontType.TITLE]
        image_gen.capacity_name_font = self.originals[FontType.ABILITY_NAME]
        image_gen.capacity_description_font = self.originals[FontType.ABILITY_DESC]
        image_gen.stats_font = self.originals[FontType.STATS]
        image_gen.credits_font = self.originals[FontType.CREDITS]

        async for font in Font.objects.all():
            truetype = ImageFont.truetype(font.file.path, font.size)
            match font.role:
                case FontType.TITLE:
                    image_gen.title_font = truetype
                case FontType.ABILITY_NAME:
                    image_gen.capacity_name_font = truetype
                case FontType.ABILITY_DESC:
                    image_gen.capacity_description_font = truetype
                case FontType.STATS:
                    image_gen.stats_font = truetype
                case FontType.CREDITS:
                    image_gen.credits_font = truetype

    @commands.command()
    async def fontchanger_reloadconf(self, ctx: commands.Context["BallsDexBot"]):
        await self.monkeypatch()
        await ctx.reply("Sucessfully applied fonts!")
