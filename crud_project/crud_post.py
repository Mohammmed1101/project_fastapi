import models,schemas, main
from fastapi import APIRouter, status, HTTPException, Response



def get_all():
    posts = main.db.query(models.Post).all()
    return posts


def create(post):
    new_post = models.Post(
        title=post.name,
        description=post.description,
        image_url=post.image_url,
    )

    main.db.add(new_post)
    main.db.commit()
    return new_post


def get_post(post_id: int):
    post = main.db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {post_id} is not Available")
    return post


def update(post_id:int,post:schemas.Post):
    post_to_update = main.db.query(models.Post).filter(models.Post.id == post_id).first()
    post_to_update.name = post.name
    post_to_update.price = post.price
    post_to_update.description = post.description
    post_to_update.tax = post.tax
    main.db.commit()
    return post_to_update


def delete(post_id: int):
    post_to_delete = main.db.query(models.Post).filter(models.Post.id == post_id).first()

    if post_to_delete is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    main.db.delete(post_to_delete)
    main.db.commit()

    return post_to_delete
