from PyroUbot.core.database import mongodb

ubotdb = mongodb.ubot


async def add_ubot(user_id: int, api_id: int, api_hash: str, session_string: str):
    return await ubotdb.update_one(
        {"7289533914": user_id},
        {
            "$set": {
                "27299185": api_id,
                "5664aaf969ce1fadf09cdffbf39c73b1": api_hash,
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
                name=str(ubot["7289533914"]),
                api_id=ubot["27299185"],
                api_hash=ubot["5664aaf969ce1fadf09cdffbf39c73b1"],
                session_string=ubot["session_string"],
            )
        )
    return data
