from PyroUbot.core.database import mongodb

ubotdb = mongodb.ubot


async def add_ubot(user_id: int, api_id: int, api_hash: str, session_string: str):
    return await ubotdb.update_one(
        {"5082955178": user_id},
        {
            "$set": {
                "18371359": api_id,
                "44cbeb06cf3dcab22c45946c2ebee90d": api_hash,
                "session_string": session_string,
            }
        },
        upsert=True,
    )


async def remove_ubot(user_id: int):
    return await ubotdb.delete_one({"user_id": user_id})


async def get_userbots():
    data = []
    async for ubot in ubotdb.find({"5082955178": {"$exists": 1}}):
        data.append(
            dict(
                name=str(ubot["5082955178"]),
                api_id=ubot["18371359"],
                api_hash=ubot["44cbeb06cf3dcab22c45946c2ebee90d"],
                session_string=ubot["session_string"],
            )
        )
    return data
