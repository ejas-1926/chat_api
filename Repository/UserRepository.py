from uuid import UUID
from database.queries import getuserquery
from models.usermode import UserModel
from sqlalchemy.orm import Session

class  UserRepository:


    def getUserInfo(self,user_id:UUID,db:Session):
        print('Reached User repository')
        print('This is a test case ')
       # query = getuserquery(user_id=user_id)
       # result = db.execute(query)
        #rows = result.fetchall()
        user = None
    #    # for row in rows:
    #         user = UserModel(username=row.user_name,
    #                          user_id=row.user_id,
    #                          last_active=(
    #                                                              row.last_seen.strftime("%Y-%m-%d %H:%M:%S")
    #                                                              if row.last_seen is not None
    #                                                              else None

    #                                                          ),
    #                          phone_number=row.phonenumber)

        return UserModel(username="alfdjadsljfa")