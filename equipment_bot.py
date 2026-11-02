# equipment_bot.py
# Author: Jackson Scott

HANDOFF_WORDS = ["reserve", "book", "rent", "pay"]


class EquipmentAssistant:
    """A mock rental assistant. Its replies are rules not AI"""

    def __init__(self, name, instructions, equipment_tool):
        """Set up the assistant with name, instructions, and the equipment_tool"""
        self.name = name
        self.instructions = instructions
        self.equipment_tool = equipment_tool
        self.history = []

    def respond(self, user_message):
        """Record user message, chooses reply, records it, and returns it"""
        reply = self.choose_reply(user_message)
        self.history.append({"role": "user", "content": user_message})
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a reply using rules"""
        text = user_message.lower()
        if self.needs_human(text):
            return "I cant process reservations here. I am passing you to a human responder"
        if "price" in text or "cost" in text or "available" in text:
            return self.item_reply(user_message)
        if "hello" in text:
            return f"Hello! I'm {self.name}. Ask me about our rental car availability"
        return "I'm not sure how to help with that. I can check rental details"

    def needs_human(self, text):
        """Return True if the message requires staff action."""
        return any(word in text for word in HANDOFF_WORDS)

    def item_reply(self, user_message):
        """Use the equipment tool to answer questions"""
        item = self.equipment_tool.find_item(user_message)
        if item is None:
            return "Which item? I can check our kayaks, tents, or paddleboards"
        details = self.equipment_tool.get_details(item)
        return f"The {item} is available at {details}"
