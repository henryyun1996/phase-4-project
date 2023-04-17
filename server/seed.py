#!/usr/bin/env python3

from random import randint, choice as rc
# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, ModuleContent, Vocab, Favorite, User

if __name__ == '__main__':
    # fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!

        print("Deleting data...")
        ModuleContent.query.delete()
        Vocab.query.delete()
        Favorite.query.delete()
        User.query.delete()

        print("Populating vocab_words")
        word1 = Vocab(english_word = "Thank you", croatian_word = "Hvala")
        word2 = Vocab(english_word = "Good day", croatian_word = "Dobar dan")
        word3 = Vocab(english_word = "Beautiful", croatian_word = "Lijepo")
        word4 = Vocab(english_word = "Hello", croatian_word = "Zdravo")
        word5 = Vocab(english_word = "Food", croatian_word = "Hrana")
        vocabs = [word1, word2, word3, word4, word5]

        db.session.add_all(vocabs)
        db.session.commit()

        print("Seeding done!")
