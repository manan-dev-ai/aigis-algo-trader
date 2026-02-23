import asyncio
import os
import structlog
from dotenv import load_dotenv

# Import your custom modules
from utils.logger import setup_logger
from core.risk_manager import RiskManager
from strategies.sniper import SniperBot

# 1. Initialize System Components
load_dotenv()  # Load API keys from .env
logger = setup_logger()

async def main():
    print("""
    =========================================
       A.I.G.I.S. SYSTEM ONLINE 🛡️
       Mode: PAPER TRADING (TRIAL)
       Architecture: High-Speed Async
    =========================================
    """)
    
    try:
        # 2. Setup the Brain & Strategy
        risk_guard = RiskManager()
        sniper = SniperBot(risk_guard)
        
        # 3. Start the Engines
        # We use gather to run multiple tasks at once in the future
        logger.info("🚀 Starting A.I.G.I.S. Core Services...")
        
        await asyncio.gather(
            sniper.start_hunting(),
            # In the future, you will add the Guardian News bot here
        )

    except Exception as e:
        logger.error("❌ SYSTEM CRASHED", error=str(e))

if __name__ == "__main__":
    try:
        # Launch the async loop
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n🛑 SYSTEM SHUTDOWN BY USER. Closing all connections...")