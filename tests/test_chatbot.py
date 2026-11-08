# tests/test_chatbot.py

from chatbot import SupportChatbot
from echo_model import EchoModel
from order_tool import OrderLookup
from stock_tool import StockLookup


def test_chatbot_works_with_any_model_that_has_a_reply_method():
    order_tool = OrderLookup({"A100": "shipped"})
    stock_tool = StockLookup({"rain jacket": 12})
    bot = SupportChatbot("Sunny", "Be friendly.", order_tool, stock_tool, EchoModel())
    assert bot.respond("good morning") == "You said: good morning"
