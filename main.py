from bot import init_db
from asyncio import run


async def main():
    await init_db()


if __name__ == "__main__":
    run(main())
