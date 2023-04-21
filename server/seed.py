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

        print("Populating users")
        gail = User(username = "gail", _password_hash = "1234")
        henry = User(username = "henry", _password_hash = "password")

        users = [gail, henry]

        print("Populating module_contents")
        module_content1 = ModuleContent(video_url = "https://www.youtube.com/embed/bBPFUWQfjLM", content = "Hello! Welcome to the first module in your journey to learning Croatian. In this module we will be going over some basic greetings and phrases. As you go through these modules, please first watch the video before moving onto to the vocabulary words. This will help prepare you to have the correct pronounciation of each word. Refer back to the video anytime when so that you can practice pronounciation as there are words with special accent marks that are not present in English. Remember you can save any vocab word from any module so that you can refer to them later! Happy learning and Sretno Ti!", lesson_level = 1)
        module_content2 = ModuleContent(video_url = "https://www.youtube.com/embed/pF58Ngo-_5Y", content = "Dobra dan! Welcome to the second module in your journey to learning Croatian. In this module, we will adding some complexity by showing you some phrases so that you can start stitching words together. To emphasis again, pronounciation of words is as important as learning the mearning of each word. So please refer to the video first before moving onto the vocabulary portion of the module. You're doing great and I'm excited to hear about your progress in the next module! Super ti ide!", lesson_level = 2)
        module_content3 = ModuleContent(video_url = "https://www.youtube.com/embed/zOShUAfhHIA", content = "Dobrodošli u posljednji modul! Welcome to the last module! In this final module, we will be going over more phrases - specifically greetings so that you can get around when visiting the dream destinationi Rovinj. Please again refer to the video before continuing onto the vocabulary words! Uči i uči dobro!", lesson_level = 3)

        modules = [module_content1, module_content2, module_content3]

        print("Populating vocab_words")
        word1 = Vocab(english_word = "Thank you", croatian_word = "Hvala", module_content_id=1)
        word2 = Vocab(english_word = "Good day", croatian_word = "Dobar dan", module_content_id=1)
        word3 = Vocab(english_word = "Beautiful", croatian_word = "Lijepo", module_content_id=1)
        word4 = Vocab(english_word = "Hello", croatian_word = "Zdravo",  module_content_id=1)
        word5 = Vocab(english_word = "Food", croatian_word = "Hrana", module_content_id=1)
        word6 = Vocab(english_word = "Sea", croatian_word = "More",  module_content_id=1)
        word7 = Vocab(english_word = "City", croatian_word = "Grad",  module_content_id=1)
        word8 = Vocab(english_word = "Mountain", croatian_word = "Planina",  module_content_id=1)
        word9 = Vocab(english_word = "Bird", croatian_word = "Ptica",  module_content_id=1)
        word10 = Vocab(english_word = "House", croatian_word = "Kuća",  module_content_id=1)
        word11 = Vocab(english_word = "Car", croatian_word = "Auto",  module_content_id=1)
        word12 = Vocab(english_word = "Coffee", croatian_word = "Kava",  module_content_id=1)
        word13 = Vocab(english_word = "Beer", croatian_word = "Pivo",  module_content_id=1)
        word14 = Vocab(english_word = "Water", croatian_word = "Voda",  module_content_id=1)
        word15 = Vocab(english_word = "Church", croatian_word = "Crkva",  module_content_id=1)
        word16 = Vocab(english_word = "Sun", croatian_word = "Sunce",  module_content_id=1)
        word17 = Vocab(english_word = "Night", croatian_word = "Noć",  module_content_id=1)
        word18 = Vocab(english_word = "Day", croatian_word = "Dan",  module_content_id=1)
        word19 = Vocab(english_word = "Cloud", croatian_word = "Oblak", module_content_id=1)
        word20 = Vocab(english_word = "Flower", croatian_word = "Cvijet",  module_content_id=1)
        word21 = Vocab(english_word = "Tree", croatian_word = "Drvo", module_content_id=1)
        word22 = Vocab(english_word = "River", croatian_word = "Rijeka", module_content_id=1)
        word23 = Vocab(english_word = "Island", croatian_word = "Otok", module_content_id=1)
        word24 = Vocab(english_word = "Wind", croatian_word = "Vjetar", module_content_id=1)
        word25 = Vocab(english_word = "Stone", croatian_word = "Kamen", module_content_id=1)
        word26 = Vocab(english_word = "Forest", croatian_word = "Šuma", module_content_id=1)
        word27 = Vocab(english_word = "Square", croatian_word = "Trg", module_content_id=1)
        word28 = Vocab(english_word = "Sandy Beach", croatian_word = "Pješčana plaža", module_content_id=1)
        word29 = Vocab(english_word = "Blue Color", croatian_word = "Plava Boja", module_content_id=1)
        word30 = Vocab(english_word = "Red Color", croatian_word = "Crvena Boja", module_content_id=1)
        word31 = Vocab(english_word = "Green Color", croatian_word = "Zelena Boja", module_content_id=1)
        word32 = Vocab(english_word = "Yellow Color", croatian_word = "Žuta Boja", module_content_id=1)
        word33 = Vocab(english_word = "Kitchen", croatian_word = "Kuhinja", module_content_id=1)
        word34 = Vocab(english_word = "Bathroom", croatian_word = "Kupaonica", module_content_id=1)
        word35 = Vocab(english_word = "Breakfast", croatian_word = "Zajutrak", module_content_id=1)
        word36 = Vocab(english_word = "Lunch", croatian_word = "Ručak", module_content_id=1)
        word37 = Vocab(english_word = "Dinner", croatian_word = "Večera", module_content_id=1)
        word38 = Vocab(english_word = "Milk", croatian_word = "Mlijeko", module_content_id=1)
        word39 = Vocab(english_word = "Cheese", croatian_word = "Sir", module_content_id=1)
        word40 = Vocab(english_word = "Butter", croatian_word = "Maslac", module_content_id=1)
        word41 = Vocab(english_word = "Eggs", croatian_word = "Jaja", module_content_id=1)
        word42 = Vocab(english_word = "Meat", croatian_word = "Meso", module_content_id=1)
        word43 = Vocab(english_word = "Fish", croatian_word = "Riba", module_content_id=1)
        word44 = Vocab(english_word = "Chicken", croatian_word = "Piletina", module_content_id=1)
        word45 = Vocab(english_word = "Beef", croatian_word = "Govedina", module_content_id=1)
        word46 = Vocab(english_word = "Pork", croatian_word = "Svinjetina", module_content_id=1)
        word47 = Vocab(english_word = "Vegetables", croatian_word = "Povrće", module_content_id=1)
        word48 = Vocab(english_word = "Fruit", croatian_word = "Voće", module_content_id=1)
        word49 = Vocab(english_word = "Bread", croatian_word = "Kruh", module_content_id=1)
        word50 = Vocab(english_word = "Soup", croatian_word = "Juha", module_content_id=1)
        word51 = Vocab(english_word = "Salad", croatian_word = "Salata", module_content_id=1)
        word52 = Vocab(english_word = "Dessert", croatian_word = "Desert", module_content_id=1)
        word53 = Vocab(english_word = "Ice Cream", croatian_word = "Sladoled", module_content_id=1)
        word54 = Vocab(english_word = "Cake", croatian_word = "Kolač", module_content_id=1)
        word55 = Vocab(english_word = "Coffee with Milk", croatian_word = "Kava s mlijekom", module_content_id=1)
        word56 = Vocab(english_word = "Tea", croatian_word = "Čaj", module_content_id=1)
        word57 = Vocab(english_word = "Juice", croatian_word = "Sok", module_content_id=1)
        word58 = Vocab(english_word = "Wine", croatian_word = "Vino", module_content_id=1)
        word59 = Vocab(english_word = "School", croatian_word = "Škola", module_content_id=1)
        word60 = Vocab(english_word = "Sailor", croatian_word = "Moreplovac", module_content_id=1)

        vocabs1 = [word1, word2, word3, word4, word5, word6, word7, word8, word9, word10, word11, word12, word13, word14, word15, word16, word17, word18, word19, word20, word21, word22, word23, word24, word25, word26, word27, word28, word29, word30, word31, word32, word33, word34, word35, word36, word37, word38, word39, word40, word41, word42, word43, word44, word45, word46, word47, word48, word49, word50, word51, word52, word53, word54, word55, word56, word57, word58, word59, word60]

        word61 = Vocab(english_word="What's your favorite food?", croatian_word="Koja ti je najdraža hrana?", module_content_id=3)
        word62 = Vocab(english_word="Where do you live?", croatian_word="Gdje živiš?", module_content_id=3)
        word63 = Vocab(english_word="When is your birthday?", croatian_word="Kada ti je rođendan?", module_content_id=3)
        word64 = Vocab(english_word="Why did you choose that?", croatian_word="Zašto si to odabrao?", module_content_id=3)
        word65 = Vocab(english_word="Who is your best friend?", croatian_word="Tko ti je najbolji prijatelj?", module_content_id=3)
        word66 = Vocab(english_word="Do you like to read?", croatian_word="Volite li čitati?", module_content_id=3)
        word67 = Vocab(english_word="Have you traveled abroad?", croatian_word="Jeste li putovali u inozemstvo?", module_content_id=3)
        word68 = Vocab(english_word="How do you relax?", croatian_word="Kako se opuštate?", module_content_id=3)
        word69 = Vocab(english_word="What's your favorite hobby?", croatian_word="Koji ti je najdraži hobi?", module_content_id=3)
        word70 = Vocab(english_word="What do you do for a living?", croatian_word="Čime se bavite?", module_content_id=3)
        word71 = Vocab(english_word="Did you watch the game last night?", croatian_word="Jeste li gledali utakmicu sinoć?", module_content_id=3)
        word72 = Vocab(english_word="How do you stay fit?", croatian_word="Kako ostajete u formi?", module_content_id=3)
        word73 = Vocab(english_word="What's your favorite movie?", croatian_word="Koji ti je najdraži film?", module_content_id=3)
        word74 = Vocab(english_word="Do you like to cook?", croatian_word="Volite li kuhati?", module_content_id=3)
        word75 = Vocab(english_word="Have you ever been scuba diving?", croatian_word="Jeste li ikad ronili?", module_content_id=3)
        word76 = Vocab(english_word="What's your dream vacation destination?", croatian_word="Koja ti je omiljena destinacija za odmor?", module_content_id=3)
        word77 = Vocab(english_word="Did you enjoy the concert?", croatian_word="Jeste li uživali na koncertu?", module_content_id=3)
        word78 = Vocab(english_word="How do you learn new things?", croatian_word="Kako učite nove stvari?", module_content_id=3)
        word79 = Vocab(english_word="Do you prefer cats or dogs?", croatian_word="Više volite mačke ili pse?", module_content_id=3)
        word80 = Vocab(english_word="What's your favorite book?", croatian_word="Koja ti je omiljena knjiga?", module_content_id=3)
        word81 = Vocab(english_word="Have you ever gone skydiving?", croatian_word="Jeste li ikad", module_content_id=3)


        vocabs3 = [word61, word62, word63, word64, word65, word66, word67, word68, word69, word70, word71, word72, word73, word74, word75, word76, word77, word78, word79, word80, word81]

        word82 = Vocab(english_word="At the train station", croatian_word="Na željezničkoj stanici", module_content_id=2)
        word83 = Vocab(english_word="In the airport", croatian_word="U zračnoj luci", module_content_id=2)
        word84 = Vocab(english_word="At the hotel", croatian_word="U hotelu", module_content_id=2)
        word85 = Vocab(english_word="In the city center", croatian_word="U centru grada", module_content_id=2)
        word86 = Vocab(english_word="At the post office", croatian_word="Na pošti", module_content_id=2)
        word87 = Vocab(english_word="At the bank", croatian_word="U banci", module_content_id=2)
        word88 = Vocab(english_word="At the hospital", croatian_word="U bolnici", module_content_id=2)
        word89 = Vocab(english_word="At the pharmacy", croatian_word="U ljekarni", module_content_id=2)
        word90 = Vocab(english_word="At the police station", croatian_word="Na policijskoj postaji", module_content_id=2)
        word91 = Vocab(english_word="At the library", croatian_word="U knjižnici", module_content_id=2)
        word92 = Vocab(english_word="At the university", croatian_word="Na sveučilištu", module_content_id=2)
        word93 = Vocab(english_word="At the museum", croatian_word="U muzeju", module_content_id=2)
        word94 = Vocab(english_word="At the theater", croatian_word="U kazalištu", module_content_id=2)
        word95 = Vocab(english_word="At the cinema", croatian_word="U kinu", module_content_id=2)
        word96 = Vocab(english_word="At the restaurant", croatian_word="U restoranu", module_content_id=2)
        word97 = Vocab(english_word="At the bar", croatian_word="U baru", module_content_id=2)
        word98 = Vocab(english_word="At the club", croatian_word="U klubu", module_content_id=2)
        word99 = Vocab(english_word="At the gym", croatian_word="U teretani", module_content_id=2)
        word100 = Vocab(english_word="At the park", croatian_word="U parku", module_content_id=2)
        word101 = Vocab(english_word="At the beach", croatian_word="Na plaži", module_content_id=2)
        word102 = Vocab(english_word="At the office", croatian_word="Na poslu", module_content_id=2)
        word103 = Vocab(english_word="At home", croatian_word="Doma", module_content_id=2)
        word104 = Vocab(english_word="At the market", croatian_word="Na tržnici", module_content_id=2)
        word105 = Vocab(english_word="At the church", croatian_word="U crkvi", module_content_id=2)
        word106 = Vocab(english_word="At the mosque", croatian_word="U džamiji", module_content_id=2)

        vocabs2 = [word82, word83, word84, word85, word86, word87, word88, word89, word90,    word91, word92, word93, word94, word95, word96, word97, word98, word99,    word100, word101, word102, word103, word104, word105, word106]

        db.session.add_all(users)
        db.session.add_all(vocabs1)
        db.session.add_all(vocabs2)
        db.session.add_all(vocabs3)
        db.session.add_all(modules)
        db.session.commit()

        print("Seeding done!")
