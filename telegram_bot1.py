from TelegramBotAPI.types import sendMessage
from TelegramBot.plugin import BotPlugin
import asyncio
class Ping(BotPlugin):

    @asyncio.coroutine
    def startPlugin(self):
        pass

    @asyncio.coroutine
    def stopPlugin(self):
        pass

    @asyncio.coroutine
    def on_message(self, msg):

        if hasattr(msg, 'text'):
            m = sendMessage()
            m.chat_id = msg.chat.id
            if msg.text == 'Hello':
                m.text = 'Hello my name is %s' % os.environ['BOT_NAME']
            else:
                m.text = 'You said: "%s"' % msg.text

        rsp = yield from self.send_method(m)
        return True