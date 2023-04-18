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

        print("Populating module_contents")
        module_content1 = ModuleContent(video_url = "https://www.youtube.com/watch?v=bBPFUWQfjLM", content = "test", lesson_level = 1)

        modules = [module_content1]

        print("Populating vocab_words")
        word1 = Vocab(english_word = "Thank you", croatian_word = "Hvala")
        word2 = Vocab(english_word = "Good day", croatian_word = "Dobar dan")
        word3 = Vocab(english_word = "Beautiful", croatian_word = "Lijepo")
        word4 = Vocab(english_word = "Hello", croatian_word = "Zdravo")
        word5 = Vocab(english_word = "Food", croatian_word = "Hrana")
        word6 = Vocab(english_word = "Sea", croatian_word = "More")
        word7 = Vocab(english_word = "City", croatian_word = "Grad")
        word8 = Vocab(english_word = "Mountain", croatian_word = "Planina")
        word9 = Vocab(english_word = "Bird", croatian_word = "Ptica")
        word10 = Vocab(english_word = "House", croatian_word = "Kuća")
        word11 = Vocab(english_word = "Car", croatian_word = "Auto")
        word12 = Vocab(english_word = "Kava", croatian_word = "Coffee")
        word13 = Vocab(english_word = "Beer", croatian_word = "Pivo")
        word14 = Vocab(english_word = "Water", croatian_word = "Voda")
        word15 = Vocab(english_word = "Church", croatian_word = "Crkva")
        word16 = Vocab(english_word = "Sun", croatian_word = "Sunce")
        word17 = Vocab(english_word = "Night", croatian_word = "Noć")
        word18 = Vocab(english_word = "Day", croatian_word = "Dan")
        word19 = Vocab(english_word = "Cloud", croatian_word = "Oblak")
        word20 = Vocab(english_word = "Flower", croatian_word = "Cvijet")
        word21 = Vocab(english_word = "Tree", croatian_word = "Drvo")
        word22 = Vocab(english_word = "River", croatian_word = "Rijeka")
        word23 = Vocab(english_word = "Island", croatian_word = "Otok")
        word24 = Vocab(english_word = "Wind", croatian_word = "Vjetar")
        word25 = Vocab(english_word = "Stone", croatian_word = "Kamen")
        word26 = Vocab(english_word = "Forest", croatian_word = "Šuma")
        word27 = Vocab(english_word = "Square", croatian_word = "Trg")
        word28 = Vocab(english_word = "Sandy Beach", croatian_word = "Pješčana plaža")
        word29 = Vocab(english_word = "Blue Color", croatian_word = "Plava Boja")
        word30 = Vocab(english_word = "Red Color", croatian_word = "Crvena Boja")
        word31 = Vocab(english_word = "Green Color", croatian_word = "Zelena Boja")
        word32 = Vocab(english_word = "Yellow Color", croatian_word = "Žuta Boja")
        word33 = Vocab(english_word = "Kitchen", croatian_word = "Kuhinja")
        word34 = Vocab(english_word = "Bathroom", croatian_word = "Kupaonica")
        word35 = Vocab(english_word = "Breakfast", croatian_word = "Zajutrak")
        word36 = Vocab(english_word = "Lunch", croatian_word = "Ručak")
        word37 = Vocab(english_word = "Dinner", croatian_word = "Večera")
        word38 = Vocab(english_word = "Milk", croatian_word = "Mlijeko")
        word39 = Vocab(english_word = "Cheese", croatian_word = "Sir")
        word40 = Vocab(english_word = "Butter", croatian_word = "Maslac")
        word41 = Vocab(english_word = "Eggs", croatian_word = "Jaja")
        word42 = Vocab(english_word = "Meat", croatian_word = "Meso")
        word43 = Vocab(english_word = "Fish", croatian_word = "Riba")
        word44 = Vocab(english_word = "Chicken", croatian_word = "Piletina")
        word45 = Vocab(english_word = "Beef", croatian_word = "Govedina")
        word46 = Vocab(english_word = "Pork", croatian_word = "Svinjetina")
        word47 = Vocab(english_word = "Vegetables", croatian_word = "Povrće")
        word48 = Vocab(english_word = "Fruit", croatian_word = "Voće")
        word49 = Vocab(english_word = "Bread", croatian_word = "Kruh")
        word50 = Vocab(english_word = "Soup", croatian_word = "Juha")
        word51 = Vocab(english_word = "Salad", croatian_word = "Salata")
        word52 = Vocab(english_word = "Dessert", croatian_word = "Desert")
        word53 = Vocab(english_word = "Ice Cream", croatian_word = "Sladoled")
        word54 = Vocab(english_word = "Cake", croatian_word = "Kolač")
        word55 = Vocab(english_word = "Coffee with Milk", croatian_word = "Kava s mlijekom")
        word56 = Vocab(english_word = "Tea", croatian_word = "Čaj")
        word57 = Vocab(english_word = "Juice", croatian_word = "Sok")
        word58 = Vocab(english_word = "Wine", croatian_word = "Vino")
        word59 = Vocab(english_word = "School", croatian_word = "Škola")
        word60 = Vocab(english_word = "Sailor", croatian_word = "Moreplovac")

        vocabs = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15, word16, word17, word18, word19, word20, word21, word22, word23, word24, word25, word26, word27, word28, word29, word30, word31, word32, word33, word34, word35, word36, word37, word38, word39, word40, word41, word42, word43, word44, word45, word46, word47, word48, word49, word50, word51, word52, word53, word54, word55, word56, word57, word58, word59, word60]

        db.session.add_all(vocabs)
        db.session.add_all(modules)
        db.session.commit()

        print("Seeding done!")
