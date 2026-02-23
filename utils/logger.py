import structlog
import logging
import sys

def setup_logger():
    """
    Configures a high-speed, structured logger.
    """
    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.processors.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.dev.ConsoleRenderer()  # Makes logs colorful and readable
        ],
        logger_factory=structlog.PrintLoggerFactory(),
        cache_logger_on_first_use=True,
    )
    
    return structlog.get_logger()

# Create a singleton instance to import elsewhere
logger = setup_logger()