from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_all(self):
        query = select(User)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, id: int, username: str):
        user = User(id=id, username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    async def get_by_id(self, telegram_id: int):
        result = await self.session.execute(
            select(User).where(User.id == telegram_id)
        )
        return result.scalars().first()
    
    
    async def update(self, telegram_id: int, **kwargs):
        await self.session.execute(
            update(User)
            .where(User.id == telegram_id)
            .values(**kwargs)
        )