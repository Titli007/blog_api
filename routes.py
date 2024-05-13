from fastapi import APIRouter, HTTPException
from typing import List
from fastapi.encoders import jsonable_encoder
from models import BlogPost, Comment, Like, Dislike
from databases import (
    blog_post_collection,
    comments_collection,
    likes_collection,
    dislikes_collection,
)
from bson import ObjectId

router = APIRouter()

# Blog Post routes
@router.get("/posts", response_model=List[BlogPost])
async def get_posts():
    posts = await blog_post_collection.find().to_list(1000)
    return posts

@router.post("/posts", response_model=BlogPost)
async def create_post(post: BlogPost):
    post_dict = post.dict(by_alias=True)  # Ensure conversion from Pydantic model to dict
    new_post = await blog_post_collection.insert_one(post_dict)
    created_post = await blog_post_collection.find_one({"_id": new_post.inserted_id})
    return jsonable_encoder(created_post)  # Convert MongoDB BSON to JSON

@router.put("/posts/{post_id}", response_model=BlogPost)
async def update_post(post_id: str, post: BlogPost):
    await blog_post_collection.update_one({"_id": ObjectId(post_id)}, {"$set": post.__dict__})
    updated_post = await blog_post_collection.find_one({"_id": ObjectId(post_id)})
    return updated_post

@router.delete("/posts/{post_id}")
async def delete_post(post_id: str):
    await blog_post_collection.delete_one({"_id": ObjectId(post_id)})
    return {"message": "Post deleted successfully"}

# Comment routes
@router.post("/posts/{post_id}/comments", response_model=Comment)
async def create_comment(post_id: str, comment: Comment):
    comment_dict = comment.__dict__
    comment_dict["post_id"] = post_id
    new_comment = await comments_collection.insert_one(comment_dict)
    created_comment = await comments_collection.find_one({"_id": new_comment.inserted_id})
    return created_comment

# Like routes
@router.post("/posts/{post_id}/likes", response_model=Like)
async def like_post(post_id: str, like: Like):
    like_dict = like.__dict__
    like_dict["post_id"] = post_id
    new_like = await likes_collection.insert_one(like_dict)
    created_like = await likes_collection.find_one({"_id": new_like.inserted_id})
    return created_like

# Dislike routes
@router.post("/posts/{post_id}/dislikes", response_model=Dislike)
async def dislike_post(post_id: str, dislike: Dislike):
    dislike_dict = dislike.__dict__
    dislike_dict["post_id"] = post_id
    new_dislike = await dislikes_collection.insert_one(dislike_dict)
    created_dislike = await dislikes_collection.find_one({"_id": new_dislike.inserted_id})
    return created_dislike