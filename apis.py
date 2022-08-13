from autobahn.wamp import ApplicationError
from autobahn import wamp

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select

from model import Account, Base
from serializers import AccountSchema
from helpers import validate_call_params


class AccountManager:
    def __int__(self):
        self.engine = engine = create_async_engine(
            'sqlite+aiosqlite://user.db', echo=False)
        self.async_session = sessionmaker(
            engine, expire_on_commit=False, class_=AsyncSession, autoflush=False
        )

    async def sync_database(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @wamp.register('pk.codebase.create.account', check_types=True)
    @validate_call_params(AccountSchema, lambda session: session.async_session)
    async def create(self, fullname: str, age: int, email: str):
        account_schema = AccountSchema()
        account = Account(full_name=fullname, age=age, email=email)

        async with self.async_session() as session:
            async with session.begin():
                session.add(account)

            return account_schema.dump(account)
