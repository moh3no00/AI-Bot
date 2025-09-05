class RiskManager:
    """مدیریت ریسک ساده با حد ضرر و حد سود"""

    def __init__(self, stop_loss: float, take_profit: float):
        self.stop_loss = stop_loss
        self.take_profit = take_profit

    def check(self, entry_price: float, current_price: float) -> str:
        """بررسی وضعیت معامله نسبت به قیمت فعلی"""
        if self.stop_loss is not None and current_price <= self.stop_loss:
            return "stop_loss"
        if self.take_profit is not None and current_price >= self.take_profit:
            return "take_profit"
        return "hold"
