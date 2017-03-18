#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/t1", max_overflow=5)

Base = declarative_base()

# 操作表


# 创建单表


class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    extra = Column(String(16))

    __table_args__ = (UniqueConstraint('id', 'name', name='uix_id_name'), Index('ix_id_name', 'name', 'extra'),)

    def __repr__(self):
        return "%s-%s" % (self.id, self.name)


# 一对多


class Favor(Base):
    __tablename__ = 'favor'
    nid = Column(Integer, primary_key=True)
    caption = Column(String(50), default='red', unique=True)

    def __repr__(self):
        return "%s-%s" % (self.nid, self.caption)


class Person(Base):
    __tablename__ = 'person'
    nid = Column(Integer, primary_key=True)