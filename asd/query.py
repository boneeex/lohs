from database import Base, async_engine

async def create_tables():
    async with async_engine.begin() as conn:
        print("Attempting to create tables...")
        await conn.run_sync(Base.metadata.create_all)