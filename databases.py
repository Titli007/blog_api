import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017/blog_api")
database = client.blog_db

blog_post_collection = database.get_collection("blog_posts")
comments_collection = database.get_collection("comments")
likes_collection = database.get_collection("likes")
dislikes_collection = database.get_collection("dislikes")