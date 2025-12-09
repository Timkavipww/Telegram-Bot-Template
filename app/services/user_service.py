from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    async def get_users(self):
        return await self.repo.get_all()
    
    async def get_user(self, telegram_id: int):
        return await self.repo.get_by_id(telegram_id)

    async def create_user(self, id: int, username: str = None):
        return await self.repo.create(id, username)

    async def update_user(self, telegram_id: int, **kwargs):
        return await self.repo.update(telegram_id, **kwargs)
