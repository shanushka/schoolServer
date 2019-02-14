def validRoleObject(RoleObject):
    if ("type" in RoleObject and RoleObject["type"] == "admin" or RoleObject["type"] == "hr"):
        return True

    return False


def validUserObject(UserObject):
    if (
            "name" in UserObject and "password" in UserObject and "email" in UserObject and "contact_number" in UserObject and "role_id" in UserObject):
        return True
    return False


def validStudentObject(StudentObject):
    if (
            "name" in StudentObject and "roll_number" in StudentObject and "father_name" in StudentObject and "mother_name" in StudentObject and "contact_number" in StudentObject and "class_id" in StudentObject):
        return True
    return False


def validClassObject(ClassObject):
    if (
            "grade" in ClassObject and "section" in ClassObject):
        return True
    return False


invalidObjectMessage = {
    "error": "Need a valid data"
}
