from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.models import User
from app.repositories.base import BaseRepository

class UserRepository(BaseRepository[User]):
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__(session, User)

    async def create(self, id: int, username: str):
        user = User(id=id, username=username)
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user
    
    
    async def update(self, telegram_id: int, **kwargs):
        await self.session.execute(
            update(User)
            .where(User.id == telegram_id)
            .values(**kwargs)
        )