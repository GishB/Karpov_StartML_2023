from database import Base, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean, func, ForeignKey, TIMESTAMP


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    text = Column(String)
    topic = Column(String)


# if __name__ == "__main__":
# session = SessionLocal()
# test_list = []
# for data in (session.query(Post)\
#         .filter(Post.topic == "business")
#         .order_by(Post.id.desc()).limit(10).all()):
#     test_list.append(data.id)
# print(test_list)

# if __name__ == "__main__":
#     session = SessionLocal()
#     test_list = []
#     for data in (session.query(User.country, User.os, func.count(User.id))\
#             .filter(User.exp_group == 3)\
#             .group_by(User.country, User.os)\
#             .having(func.count(User.id) > 100)\
#             .order_by(func.count(User.id).desc()).all()):
#         test_list.append((data))
#     print(test_list)

if __name__ == "__main__":
    session = SessionLocal()
