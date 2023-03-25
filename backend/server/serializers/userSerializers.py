def userEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],
        "photo": user["photo"],
        "usn": user["usn"],
        "sem": user["sem"],
        "branch": user["branch"],
        "section": user["section"],
        "verified": user["verified"],
        "password": user["password"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }


def userResponseEntity(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "role": user["role"],
        "usn": user["usn"],
        "sem": user["sem"],
        "branch": user["branch"],
        "section": user["section"],
        "photo": user["photo"],
        "created_at": user["created_at"],
        "updated_at": user["updated_at"]
    }


def embeddedUserResponse(user) -> dict:
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "photo": user["photo"],
        "usn": user["usn"],
        "sem": user["sem"],
        "branch": user["branch"],
        "section": user["section"],
    }


def userListEntity(users) -> list:
    return [userEntity(user) for user in users]

