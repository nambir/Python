"""Slide 20 — Async / Await practice."""
import asyncio
import time


async def fetch_data(n: int) -> str:
    await asyncio.sleep(0.3)
    return f"result-{n}"


async def main() -> None:
    start = time.time()
    results = await asyncio.gather(fetch_data(1), fetch_data(2), fetch_data(3))
    print("results:", results)
    print(f"elapsed: {time.time() - start:.2f}s (concurrent, not 0.9s)")


if __name__ == "__main__":
    asyncio.run(main())
