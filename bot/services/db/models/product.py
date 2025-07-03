from decimal import Decimal
from typing import Optional
from sqlalchemy import ForeignKey, Integer, String, Float, Numeric
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    products: Mapped[list["Product"]] = relationship("Product", back_populates="group")


class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    group_id: Mapped[int] = mapped_column(
        ForeignKey("groups.id", ondelete="CASCADE"), nullable=False
    )
    type: Mapped[str] = mapped_column(String, nullable=False)

    group: Mapped["Group"] = relationship("Group", back_populates="products")

    __mapper_args__ = {
        "polymorphic_on": type,
        "polymorphic_identity": "product",
        "with_polymorphic": "*",
    }


class Snus(Product):
    __tablename__ = "snus"

    id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    taste: Mapped[str] = mapped_column(String, nullable=False)
    strength: Mapped[int] = mapped_column(Integer, default=0, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "snus"}


class Liquid(Product):
    __tablename__ = "liquids"

    id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    taste: Mapped[str] = mapped_column(String, nullable=False)
    strength: Mapped[int] = mapped_column(Integer, default=50, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "liquid"}


class Consumable(Product):
    __tablename__ = "consumables"

    id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    resistance: Mapped[float] = mapped_column(Float, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "consumable"}


class PodSystem(Product):
    __tablename__ = "podsystems"

    id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)

    __mapper_args__ = {"polymorphic_identity": "podsystem"}


class Disposable(Product):
    __tablename__ = "disposables"

    id: Mapped[int] = mapped_column(ForeignKey("products.id"), primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    puffs: Mapped[int] = mapped_column(Integer, nullable=False)
    taste: Mapped[str] = mapped_column(String, nullable=False)
    strength: Mapped[int] = mapped_column(Integer, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "disposable"}
