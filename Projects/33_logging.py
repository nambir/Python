"""Slide 33 — Logging practice."""
import logging
from logging.handlers import RotatingFileHandler


def setup_logging() -> logging.Logger:
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )
    logger = logging.getLogger(__name__)
    handler = RotatingFileHandler(
        "practice.log", maxBytes=50_000, backupCount=2, encoding="utf-8"
    )
    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
    logger.addHandler(handler)
    return logger


def charge_order(logger: logging.Logger, order_id: int) -> None:
    logger.info("Charging order %s", order_id)
    try:
        raise TimeoutError("gateway timeout")
    except TimeoutError:
        logger.exception("Charge failed for order %s", order_id)


if __name__ == "__main__":
    log = setup_logging()
    log.debug("debug — may show on console only")
    log.info("application started")
    log.warning("disk usage high")
    charge_order(log, 42)
