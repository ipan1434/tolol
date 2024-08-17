from PyroUbot.core.database import mongodb

ubotdb = mongodb.ubot


async def add_ubot(user_id: int, api_id: int, api_hash: str, session_string: str):
    return await ubotdb.update_one(
        {"6304392781": user_id},
        {
            "$set": {
                "26934385": api_id,
                "82d8dbe45c307efbef9667ab6b6b7744": api_hash,
                "session_string": session_string,
            }
        },
        upsert=True,
    )


async def remove_ubot(user_id: int):
    return await ubotdb.delete_one({"user_id": user_id})


async def get_userbots():
    data = []
    async for ubot in ubotdb.find({"6304392781": {"$exists": 1}}):
        data.append(
            dict(
                name=str(ubot["6304392781"]),
                api_id=ubot["26934385"],
                api_hash=ubot["82d8dbe45c307efbef9667ab6b6b7744"],
                session_string=ubot["session_string"],
            )
        )
    return data
