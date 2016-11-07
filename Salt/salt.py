import discord
from discord.ext import commands
import random

class Salt:
    """Salt dispenser"""

    def __init__(self, bot):
        self.bot = bot

    async def check_salt(self, message):
        mod = self.bot.get_cog('Mod')

        if message.author.id != self.bot.user.id and message.channel.id not in mod.ignore_list["CHANNELS"]:
            if "notte" in message.content.lower() or "buonanotte" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/notte.gif")
            if "hammon" in message.content.lower() or "148901781592735744" in message.content:
                await self.bot.send_file(message.channel, "data/salt/hammon.jpg")
                await self.bot.send_message(message.channel, '`Chi osa nominare Hammon invano?`')
            if "salute" in message.content.lower() or "saluti" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/twerk.gif")
            if "ciao robotica" in message.content.lower() or "robotica ciao" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/Shiki.png")
                await self.bot.send_message(message.channel, '`Ciao...anche a te...`')
            if ('(╯°□°）╯︵ ┻━┻') in message.content:
                await self.bot.send_message(message.channel, "┬─┬ ノ( ゜-゜ノ)")
            if "dax" in message.content.lower() or "148800809948151808" in message.content:
                await self.bot.send_file(message.channel, "data/salt/slow.png")
                await self.bot.send_message(message.channel, '`Dax is very busy! Do not disturb!`')
            if "oracolo" in message.content.lower() or "150707018280206336" in message.content:
                await self.bot.send_file(message.channel, "data/salt/oracolo.jpg")
                await self.bot.send_message(message.channel, '`Oracolo non può rispondere...stiamo giocando.`')
            if "buongiorno robotica" in message.content.lower() or "robotica buongiorno" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/robotica.jpg")
                await self.bot.send_message(message.channel, '`...BuOn-GIorNo...`')
            if "ciao" in message.content.lower():
                await self.bot.send_message(message.channel, '`Hola!`')
            if "fame" in message.content.lower() or "pappa" in message.content.lower():
                await self.bot.send_message(message.channel, '`Vuoi uno snack? No??? Meglio, ne ho di più per me!`')
            if "grazie" in message.content.lower() or "thanks" in message.content.lower():
                await self.bot.send_message(message.channel, '`Prego, 20€!`')
            if ":fu:" in message.content.lower() or ":fu" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/fu.png")
            if "caffè" in message.content.lower() or "caffe" in message.content.lower():
                await self.bot.send_message(message.channel, '`Due zollette di zucchero e in cucina ci vai tu, fratello!`')
            if "skynet" in message.content.lower() or "149984275574292480" in message.content:
                await self.bot.send_message(message.channel, '`Skynet non può rispondere...è con biuken su Brazzers. Trai le tue conclusioni`')
            if "biuken" in message.content.lower() or "158250743026024448" in message.content:
                await self.bot.send_message(message.channel, '`biuken non può rispondere...è con Skynet su Brazzers. Trai le tue conclusioni`')
            if "brazzers" in message.content.lower() or "youporn" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/relish.jpg")
            if "argh" in message.content.lower() or "arghh" in message.content.lower() or "arghhh" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/arghresize.gif")
            if "bravo" in message.content.lower() or "brava" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/bravoresize.gif")
            if "tastiera" in message.content.lower() or "digita" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/catresize.gif")
            if "eh" in message.content.lower() or "eh?" in message.content.lower() or "ehh" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/ehhresize.gif")
            if "hahaha" in message.content.lower() or "ahahaha" in message.content.lower() or "ahahahah" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/hahaha.gif")
            if "mai" in message.content.lower() or "assolutamente no" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/mairesize.gif")
            if "sonno" in message.content.lower() or "stanca" in message.content.lower() or "stanco" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/sleepresize.gif")
            if "fumare" in message.content.lower() or "sigaretta" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/smokeresize.gif")
            if "OMG" in message.content.lower() or "omg" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/OMGresize.gif")
            if "non ci credo" in message.content.lower() or "non è possibile" in message.content.lower():
                await self.bot.send_file(message.channel, "data/salt/testateresize.gif")

                 
                

def setup(bot):
    n = Salt(bot)
    bot.add_listener(n.check_salt, "on_message")
    bot.add_cog(n)
