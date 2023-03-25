def missing_helpers(person) -> dict:
    return {
        "name": person["name"],
        "contact": person['contact_number'],
        "fir": person["fir"],
        "last_seen": person["last_seen"],
        "url": person["image_url"],
        "secure": person["secure_url"],
    }

def users_serializer(users) -> list:
    return [missing_helpers(user) for user in users]

def found_helpers(person) -> dict:
    return {
        "name": person["name"],
        "contact": person['contact_number'],
        "fir": person["fir"],
        "last_seen": person["last_seen"],
        "url": person["image_url"],
        "found": [{"score" : item['score'], "url": item['real_time_location']} for item in person["found"] ],
    }

def found_serializer(users) -> list:
    return [found_helpers(user) for user in users]