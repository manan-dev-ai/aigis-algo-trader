import yaml
from datetime import datetime
from utils.logger import logger

class RiskManager:
    def __init__(self):
        self.load_config()
        self.current_daily_loss = 0.0
        self.trades_taken_today = 0
        self.kill_switch_active = False
        logger.info("🛡️ Risk Manager Initialized", daily_limit=self.max_daily_loss)

    def load_config(self):
        """Reads rules from config.yaml"""
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
            self.max_daily_loss = config['risk_management']['max_daily_loss']
            self.max_trades = config['risk_management']['max_trades_per_day']
            self.capital = config['risk_management']['capital']

    def check_trade_permission(self, symbol, projected_cost):
        """
        The Master Approval Function.
        Returns: (True/False, "Reason")
        """
        # 1. Check Global Kill Switch (Triggered by News Bot)
        if self.kill_switch_active:
            logger.warning("⛔ Trade Rejected", symbol=symbol, reason="Kill Switch Active")
            return False

        # 2. Check Daily Loss Limit
        if self.current_daily_loss >= self.max_daily_loss:
            logger.error("🛑 Trading Halted", symbol=symbol, reason="Daily Loss Limit Hit")
            return False

        # 3. Check Over-trading
        if self.trades_taken_today >= self.max_trades:
            logger.warning("💤 Trade Rejected", symbol=symbol, reason="Max Daily Trades Reached")
            return False

        # 4. Check Capital
        if projected_cost > (self.capital * 0.5): # Never use >50% on one trade
            logger.warning("⚠️ Trade Rejected", symbol=symbol, reason="Position Size Too Big")
            return False

        return True

    def record_trade(self, pnl):
        """Call this after a trade is closed to update risk stats"""
        self.trades_taken_today += 1
        if pnl < 0:
            self.current_daily_loss += abs(pnl)
            logger.info("📉 Loss Recorded", amount=pnl, total_loss=self.current_daily_loss)
        else:
            logger.info("💰 Profit Recorded", amount=pnl)

    def trigger_kill_switch(self):
        """Called by the News Bot when 'Market Crash' is detected"""
        self.kill_switch_active = True
        logger.critical("🚨 KILL SWITCH ACTIVATED. TRADING STOPPED.")