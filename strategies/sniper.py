import asyncio
import random
import yaml
from utils.logger import logger
from core.risk_manager import RiskManager

class SniperBot:
    def __init__(self, risk_manager: RiskManager):
        self.risk_manager = risk_manager
        self.load_config()
        self.is_active = False

    def load_config(self):
        with open("config.yaml", "r") as f:
            config = yaml.safe_load(f)
            self.watchlist = config['strategy']['sniper']['watchlist']
            self.buy_threshold = config['strategy']['sniper']['buy_rsi_threshold']

    async def start_hunting(self):
        """The main loop that watches the market"""
        self.is_active = True
        logger.info("🔭 Sniper Bot: Online and Scanning...", watchlist=self.watchlist)

        while self.is_active:
            for symbol in self.watchlist:
                await self.analyze_symbol(symbol)
            
            # Scan every 5 seconds
            await asyncio.sleep(5)

    async def analyze_symbol(self, symbol):
        """
        1. Gets Data
        2. Checks Strategy
        3. Asks Risk Manager
        4. Executes
        """
        # --- SIMULATION BLOCK (Replace with API call later) ---
        current_price = random.uniform(100, 3000)
        rsi_value = random.randint(20, 80) # Random RSI for testing
        # ----------------------------------------------------

        logger.debug(f"Scanning {symbol}", rsi=rsi_value, price=round(current_price, 2))

        # THE STRATEGY: Buy if RSI is low (Oversold)
        if rsi_value < self.buy_threshold:
            logger.info("🎯 Signal Detected", symbol=symbol, rsi=rsi_value)
            
            # Ask Permission
            if self.risk_manager.check_trade_permission(symbol, current_price):
                self.execute_paper_trade(symbol, current_price)

    def execute_paper_trade(self, symbol, price):
        """Simulates sending an order to the broker"""
        logger.info("🔥 EXECUTING BUY ORDER", symbol=symbol, price=round(price, 2))
        
        # Tell Risk Manager we took a trade
        # Simulating a random result (Profit or Loss)
        simulated_pnl = random.choice([-50, 100, 200, -20]) 
        self.risk_manager.record_trade(pnl=simulated_pnl)