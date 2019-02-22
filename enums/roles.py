from enum import Enum
class RoleEnum(Enum):
    ADMIN = 1
    HR = 2

    @classmethod
    def get_by_id(cls,id):
        if(id==1):
            return RoleEnum.ADMIN
        elif(id == 2):
            return RoleEnum.HR
