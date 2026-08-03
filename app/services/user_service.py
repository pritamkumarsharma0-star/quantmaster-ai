from sqlalchemy.orm import Session

from app.models.user import User


def get_user(db: Session, telegram_id: str):
    return db.query(User).filter(
        User.telegram_id == telegram_id
    ).first()


def create_user(db: Session, telegram_id: str, name: str):
    user = User(
        telegram_id=telegram_id,
        name=name,
        score=0,
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_score(db: Session, telegram_id: str, points: int):
    user = get_user(db, telegram_id)

    if user:
        user.score += points
        db.commit()
        db.refresh(user)

    return user