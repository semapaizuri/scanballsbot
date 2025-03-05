import asyncio
import time

async def main():
    print("ya princhu")
    tasks = [sendMail(x) for x in range(5, 10, 2)]
    await asyncio.gather(*tasks)


async def sendMail(n):
    print(f"mail {n} sent")
    await asyncio.sleep(3)
    print(f"mail {n} delivered")

asyncio.run(main())