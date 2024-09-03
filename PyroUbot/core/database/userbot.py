from PyroUbot.core.database import mongodb

ubotdb = mongodb.ubot


async def add_ubot(user_id: int, api_id: int, api_hash: str, session_string: str):
    return await ubotdb.update_one(
        {"1415374553": user_id},
        {
            "$set": {
                "28856059": api_id,
                "9be1503a6ebed409cd0c53c188d04a0b": api_hash,
                "session_string": session_string,
            }
        },
        upsert=True,
    )


async def remove_ubot(user_id: int):
    return await ubotdb.delete_one({"user_id": user_id})


async def get_userbots():
    data = []
    async for ubot in ubotdb.find({"1415374553": {"$exists": 1}}):
        data.append(
            dict(
                name=str(ubot["1415374553"]),
                api_id=ubot["28856059"],
                api_hash=ubot["9be1503a6ebed409cd0c53c188d04a0b"],
                session_string=ubot["session_string"],
            )
        )
    return data
