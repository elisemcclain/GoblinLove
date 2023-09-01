#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from models import db, User, Trait, TraitAssociation, Goblin, Date, Dialogue, Response, Outcome
from app import app

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        User.query.delete()
        Trait.query.delete()
        TraitAssociation.query.delete()
        Goblin.query.delete()
        Date.query.delete()
        Dialogue.query.delete()
        Response.query.delete()
        Outcome.query.delete()
        db.session.commit()
        print("deleted all data")

        print("Creating users...")
        user1 = User(username="user1", password="Password#1", email="grantbruemmer@gmail.com")
        user2 = User(username="user2", password="Password#2", email="fakeuser@gmail.com")
        user3 = User(username="user3", password="Password#3", email="fakeuser2@gmail.com")
        users = [user1, user2, user3]
        db.session.add_all(users)
        db.session.commit()

        print("Creating traits...")
        trait1 = Trait(name="Mischievious")
        trait2 = Trait(name="Greedy")
        trait3 = Trait(name="Crafty")
        trait4 = Trait(name="Cautious")
        trait5 = Trait(name="Optimistic")
        trait6 = Trait(name="Playful")
        trait7 = Trait(name="Stubborn")
        trait8 = Trait(name="Superstitious")
        trait9 = Trait(name="Curious")
        trait10 = Trait(name="Impulsive")


        traits = [trait1, trait2, trait3, trait4, trait5, trait6, trait7, trait8, trait9, trait10]
        db.session.add_all(traits)
        db.session.commit()


        print("Creating trait associations...")
        trait_association1 = TraitAssociation(trait_id=trait1.id, user_id=user1.id)
        trait_association2 = TraitAssociation(trait_id=trait2.id, user_id=user2.id)
        trait_association3 = TraitAssociation(trait_id=trait3.id, user_id=user3.id)
        trait_association4 = TraitAssociation(trait_id=trait4.id, user_id=user1.id)
        trait_association5 = TraitAssociation(trait_id=trait5.id, user_id=user2.id)
        trait_association6 = TraitAssociation(trait_id=trait6.id, user_id=user3.id)
        trait_association7 = TraitAssociation(trait_id=trait7.id, user_id=user1.id)
        trait_association8 = TraitAssociation(trait_id=trait8.id, user_id=user2.id)
        trait_association9 = TraitAssociation(trait_id=trait9.id, user_id=user3.id)
        trait_association10 = TraitAssociation(trait_id=trait10.id, user_id=user1.id)
        trait_associations = [trait_association1, trait_association2, trait_association3, trait_association4, trait_association5, trait_association6, trait_association7, trait_association8, trait_association9, trait_association10]
        db.session.add_all(trait_associations)
        db.session.commit()

        print("Creating goblins...")

        grubnub = Goblin(
            name="Grubnub",
            artist = "Dave Rapoza",
            img_url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/88e39bc8-2533-40fc-bccd-5fe75d3e2b24/d26gekj-ecb40047-7e16-47cd-8ac5-ed192bebff1e.jpg/v1/fit/w_670,h_900,q_70,strp/goblin_by_daverapoza_d26gekj-375w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9OTAwIiwicGF0aCI6IlwvZlwvODhlMzliYzgtMjUzMy00MGZjLWJjY2QtNWZlNzVkM2UyYjI0XC9kMjZnZWtqLWVjYjQwMDQ3LTdlMTYtNDdjZC04YWM1LWVkMTkyYmViZmYxZS5qcGciLCJ3aWR0aCI6Ijw9NjcwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.ksbPGS_Z81SL00G1H5Mizs_2qjYDihzhGLS3P8aIkK4",
            description="Grubnub may be a bit slow-witted, but he's got a heart of gold. He enjoys helping his peers and the simpler things in life. He often misinterprets social cues, which can lead to awkwardness."
            )
        sneezle = Goblin(
            name="Sneezle",
            artist = "Jonas Jensen Art", 
            img_url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/39e41513-3c17-4015-b185-238348b495e2/d5eg2x1-2222b77a-f2a0-4f93-826e-9d1a62876ace.jpg/v1/fit/w_812,h_728,q_70,strp/goblin_by_jonasjensenart_d5eg2x1-414w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NzI4IiwicGF0aCI6IlwvZlwvMzllNDE1MTMtM2MxNy00MDE1LWIxODUtMjM4MzQ4YjQ5NWUyXC9kNWVnMngxLTIyMjJiNzdhLWYyYTAtNGY5My04MjZlLTlkMWE2Mjg3NmFjZS5qcGciLCJ3aWR0aCI6Ijw9ODEyIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.GOpf5bDf2UclvChWXpvmM2PrwQWfeb6LnF1_Cp_IkhU", 
            description="Sneezle is a bit of a prankster. He loves sarcasm and practical jokes. He doesn't take life seriously and prefers to live in the moment. He isn't afraid to call out things he thinks are wrong, and can be quick to judge."
            )
        blort = Goblin(
            name="Blort", 
            artist = "SirenD", 
            img_url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/350ef5de-d6a6-499c-8968-e3f548f626bd/d3bgk4j-0983a636-2dec-4afb-ab1a-d0d402e2352c.jpg/v1/fill/w_900,h_637,q_75,strp/goblin_s_best_friend_by_sirend_d3bgk4j-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NjM3IiwicGF0aCI6IlwvZlwvMzUwZWY1ZGUtZDZhNi00OTljLTg5NjgtZTNmNTQ4ZjYyNmJkXC9kM2JnazRqLTA5ODNhNjM2LTJkZWMtNGFmYi1hYjFhLWQwZDQwMmUyMzUyYy5qcGciLCJ3aWR0aCI6Ijw9OTAwIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.zSoAp6hxUKLzs1NaijaIA-x_XRZn1InXxscZMmHp6uk", 
            description="Blort is a lover, not a fighter. He has always had a soft spot for animals, and enjoys their company more than the people. He lives simply and loves deeply. He can come across as shy, but when he opens up you can see just how good of a person he truly is."
            )
        grimble = Goblin(
            name="Grimble", 
            artist = "Jonas Jensen Art", 
            img_url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/39e41513-3c17-4015-b185-238348b495e2/d64k3v1-a8e8931c-ccaf-49af-890b-a38b0fd74728.jpg/v1/fit/w_828,h_1154,q_70,strp/goblin_shaman_by_jonasjensenart_d64k3v1-414w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTIxMyIsInBhdGgiOiJcL2ZcLzM5ZTQxNTEzLTNjMTctNDAxNS1iMTg1LTIzODM0OGI0OTVlMlwvZDY0azN2MS1hOGU4OTMxYy1jY2FmLTQ5YWYtODkwYi1hMzhiMGZkNzQ3MjguanBnIiwid2lkdGgiOiI8PTg3MCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.BmjtCMNFmY3jXEsZ4GkFxpVFBsUkWPSOqiCoVWBO8nM", 
            description="Grimble considers himself a dashing adventurer. He may come across as a bit of a blowhard, but in reality he is deeply insecure. His craving for attention often gets him in trouble, but those he loves will never have a more loyal companion than Grimble."
            )
        zongo = Goblin(
            name="Zongo", 
            artist = "Thomas Wievegg", 
            img_url = "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4cb531bc-c606-411b-8e3f-8f95895d1829/d6pz3h3-45094d2d-136b-4e49-a359-a37a4bd18d95.jpg/v1/fit/w_800,h_1038,q_70,strp/goblin_by_thomaswievegg_d6pz3h3-414w-2x.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTAzOCIsInBhdGgiOiJcL2ZcLzRjYjUzMWJjLWM2MDYtNDExYi04ZTNmLThmOTU4OTVkMTgyOVwvZDZwejNoMy00NTA5NGQyZC0xMzZiLTRlNDktYTM1OS1hMzdhNGJkMThkOTUuanBnIiwid2lkdGgiOiI8PTgwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.DhVqrDdIz4KSYckucxuM9fZMiQ0nGx2ztIf7THbvEh8", 
            description="Zongo thinks he is the smartest goblin booyahg to ever live. He finds comfort in knowing he is unmatched in magical prowess here in the village. His personality can be a bit grating at first, but he is a passionate man. He's also very handsome."
            )

        goblins = [grubnub, sneezle, blort, grimble, zongo]
        db.session.add_all(goblins)
        db.session.commit()

        print("Creating dates...")

        date1 = Date(
            name="Baseball",
            description="Nothing says freedom like a good game of baseball. Goblins love playing baseball! as a matter of fact, this is their favorite pastime. Using the bones of their enemies, Goblins bash one another in the 'base' until one of them gives up!",
            part_1 = "You've invited your date to play baseball with you. How would you like to approach playing with them?",
            part_2 = "Shortly after the two of you begin the game together, you are interrupted by the sounds of a child screaming for their parent. How do you respond?",
            part_3 = "After playing for what seems like hours, the game finally ends. Your date stands expectantly--you realize they are waiting for you to do something. What do you do?",
            )


        date2 = Date(
            name="Grab a Drink",
            description="When you've had a long day of raiding, the best thing you can do is sit down at the rotten elder tree saloon and grab a lukewarm glass of Muk. Muk is made from local forest fungi and potatoes. With plenty of farmhouse funk, this wild fermented Muk will leave a vibrant zestiness on your tongue!",
            part_1 = "After fetching a table, the server brings over two room temperature pints of Muk. The aromatics fill you and your date's nostrils. They look at you expectantly--it seems that they would like you to start the conversation. What do you open with?",
            part_2 = "The server comes back with a fresh round and a complementary plate of peanuts. You do notice that your date has been slipped a note by the server... what do you say?",
            part_3 = "The night is just about wrapped up. The server comes back around and drops off the check. Who's paying?"
            )


        date3 = Date(
            name="Home Cooked Meal",
            description="What could be more romantic than a home cooked meal? You can really express yourself with cooking, and your partner will learn just who you are by the time its done. With top shelf ingredients, such as zucchini (stolen), rice (stolen), tomatoes (stolen), salt (stolen), and fresh dwarf ribs (stolen?) you have plenty of options!",
            part_1 = "You've got a great set of ingredients and your date sits watching as you hoist them out of larder. What are you going to make?",
            part_2 = "Oh no! It seems you completely forgot to season your dish! You already finished plating and everything... What are you going to do!?!",
            part_3 = "After the meal wraps up, there is an awkward silence from your date. Are they expecting you to ask them to stay over? What do you say?"
            )



        dates = [date1, date2, date3]
        db.session.add_all(dates)
        db.session.commit()



        print("Creating dialogues...")
        dialogues_1 = {
            'dialogue1': Dialogue(date_part=1, date_id=date1.id, trait_id=trait1.id, description="You decide it could be pretty funny to sabotage their game by giving them a bone with a giant crack down its center."),
            'dialogue2': Dialogue(date_part=1, date_id=date1.id, trait_id=trait2.id, description="You find the best bone in the pile and take it for yourself. No way they are beating you. Matter of fact, you think you'll take this bone home later. No one else should even have access to it."),
            'dialogue3': Dialogue(date_part=1, date_id=date1.id, trait_id=trait3.id, description="You find a few decent bones and wrap a band of leather around each. This will surely help with grip stability, and hopefully your date with appreciate it."),
            'dialogue4': Dialogue(date_part=1, date_id=date1.id, trait_id=trait4.id, description="You try to pick out the most normal, non-threatening bones from the pile for both you and your partner. Better safe than sorry."),
            'dialogue5': Dialogue(date_part=1, date_id=date1.id, trait_id=trait5.id, description="You figure that the best way to play is to be honest. This will be fun either way, and you let your partner pick out their own bone while you just grab whatever's nearby."),
            'dialogue6': Dialogue(date_part=1, date_id=date1.id, trait_id=trait6.id, description="You think that it could be good fun to mix up the game a bit. You decide you should both wear blindfolds!"),
            'dialogue7': Dialogue(date_part=1, date_id=date1.id, trait_id=trait7.id, description="You let your partner know that they aren't going to play by the rules. They're going to play by yours. This isn't going their way."),
            'dialogue8': Dialogue(date_part=1, date_id=date1.id, trait_id=trait8.id, description="You are shocked that you almost forgot to do your pregame ritual! There is only one true way to be safe, and it involves candles, incense, and interpretation of the clouds."),
            'dialogue9': Dialogue(date_part=1, date_id=date1.id, trait_id=trait9.id, description="You can't help but wonder what your partner is going to do. You decide to let them take the lead on how the game should be played."),
            'dialogue10': Dialogue(date_part=1, date_id=date1.id, trait_id=trait10.id, description="You decide it's a horrible idea to play here. It should be over by the riverbank. The lighting is better, and it could be more exciting."),
            'dialogue11': Dialogue(date_part=2, date_id=date1.id, trait_id=trait1.id, description="You decide to run up and pretend to be their parent. Hopefully the child plays along--it could be funny to see how your date responds!"),
            'dialogue12': Dialogue(date_part=2, date_id=date1.id, trait_id=trait2.id, description="You figure the kid could have some food or money on him, so you decide to rob him."),
            'dialogue13': Dialogue(date_part=2, date_id=date1.id, trait_id=trait3.id, description="You quickly grab a thin strip of bark and coil it into a cone to call for their parents."),
            'dialogue14': Dialogue(date_part=2, date_id=date1.id, trait_id=trait4.id, description="You are nervous. This child could easily be a trap set to rob you. You decide to sneak away and ignore the child until he leaves."),
            'dialogue15': Dialogue(date_part=2, date_id=date1.id, trait_id=trait5.id, description="You are confident that the child will find their parents, and assure the child as much. You, the child and your date look for their parents together."),
            'dialogue16': Dialogue(date_part=2, date_id=date1.id, trait_id=trait6.id, description="You think that the child could use some cheering up. You hand them a bone and ask if they want to play while they wait for their parents."),
            'dialogue17': Dialogue(date_part=2, date_id=date1.id, trait_id=trait7.id, description="You completely ignore the child, pretending they do not exist. This nuisance will not ruin your game."),
            'dialogue18': Dialogue(date_part=2, date_id=date1.id, trait_id=trait8.id, description="You realize this child is a terrible omen. The child must find their parents--and soon. If they are not found, the whole date will be cursed."),
            'dialogue19': Dialogue(date_part=2, date_id=date1.id, trait_id=trait9.id, description="You can't help but wonder what lead to the child being separated from their parents to begin with. You decide to ask the child some questions."),
            'dialogue20': Dialogue(date_part=2, date_id=date1.id, trait_id=trait10.id, description="You go and grab the child under your arm and begin running and shouting for their parents in a full sprint."),
            'dialogue21': Dialogue(date_part=3, date_id=date1.id, trait_id=trait1.id, description="You move in like you are going for a kiss, but pants them at the last second."),
            'dialogue22': Dialogue(date_part=3, date_id=date1.id, trait_id=trait2.id, description="You pronounce that you are the victor, and that your date should pay you for entertaining them."),
            'dialogue23': Dialogue(date_part=3, date_id=date1.id, trait_id=trait3.id, description="You grab your date by the hip and dip them low. Comfort them in your arms and pretend go in for a kiss, only to pull off a piece of grass stuck to their cheek and wink at them."),
            'dialogue24': Dialogue(date_part=3, date_id=date1.id, trait_id=trait4.id, description="You approach your date and congratulate them on the game. It was a fun time, but you are too nervous to push your luck."),
            'dialogue25': Dialogue(date_part=3, date_id=date1.id, trait_id=trait5.id, description="You think the two of you had a grand time together! You take the lead and move in directly for a kiss, knowing they will accept your advances."),
            'dialogue26': Dialogue(date_part=3, date_id=date1.id, trait_id=trait6.id, description="You wink playfully and giggle as you start running from your date. You expect them to chase after you."),
            'dialogue27': Dialogue(date_part=3, date_id=date1.id, trait_id=trait7.id, description="You won't be making the move. That's their job. You invited them here, let them prove they want to be here."),
            'dialogue28': Dialogue(date_part=3, date_id=date1.id, trait_id=trait8.id, description="You know its bad luck to kiss on the first date, and choose to instead leave it at a friendly hug."),
            'dialogue29': Dialogue(date_part=3, date_id=date1.id, trait_id=trait9.id, description="You wonder what they will do if you run up and grab them by the hand, so you do just that."),
            'dialogue30': Dialogue(date_part=3, date_id=date1.id, trait_id=trait10.id, description="You move without hesitation and hold them close, giving them the charge to finish what you started."),
        }


        dialogues_2 = {
            'dialogue31': Dialogue(date_part=1, date_id=date2.id, trait_id=trait1.id, description="You realize that after a couple mugs of Muk, you might convince them to join your plan to overthrow the goblin government. You open with a question on their politics."),
            'dialogue32': Dialogue(date_part=1, date_id=date2.id, trait_id=trait2.id, description="You ask if they would purchase you a goblin made tiara because you deserve it, but mostly to show everyone at the Rotten Elder Tree Saloon that you're better than them."),
            'dialogue33': Dialogue(date_part=1, date_id=date2.id, trait_id=trait3.id, description="You debate if it's worth it, but decide to open with how much you like them, you might spark jealousy amongst the other goblin boys if they get wind of this!"),
            'dialogue34': Dialogue(date_part=1, date_id=date2.id, trait_id=trait4.id, description="You waffle back and forth for 7 hours before sitting to join your date, but you refuse to drink the provided Muk in case it has been poisoned. Instead, you bring your own Muk from home and ask if they want some."),
            'dialogue35': Dialogue(date_part=1, date_id=date2.id, trait_id=trait5.id, description="You just know in your goblin heart that this goblin is the one. The Muk is just lubricant for your heart. You flat out tell them you love them!"),
            'dialogue36': Dialogue(date_part=1, date_id=date2.id, trait_id=trait6.id, description="You let him wait awkwardly so he can squirm a bit, but you're already planning out what great jokes once he breaks the silence."),
            'dialogue37': Dialogue(date_part=1, date_id=date2.id, trait_id=trait7.id, description="You love Muk, but you DON'T like being forced to do something. You begrudingly begin talking about the weather, but it'll be the last time that happens."),
            'dialogue38': Dialogue(date_part=1, date_id=date2.id, trait_id=trait8.id, description="You are stoked for this date, you ONLY wear the color orange, no matching socks, and ask your date if they brought a worm to sacrifice to the Muk Lord."),
            'dialogue39': Dialogue(date_part=1, date_id=date2.id, trait_id=trait9.id, description="You haven't been to this local saloon yet, so you're intrigued. It'll be your first time trying Muk! You ask if they are a regular here."),
            'dialogue40': Dialogue(date_part=1, date_id=date2.id, trait_id=trait10.id, description="You said yes before you checked your calendar. Shoot, you were supposesd to go on a date with Poorg. Oh well! You ask them if they are friends with Poorg. (Poor Poorg)"),
            'dialogue41': Dialogue(date_part=2, date_id=date2.id, trait_id=trait1.id, description="You are positively sure they're on to your scheme to slip out without paying for the Muk. Crikey!"),
            'dialogue42': Dialogue(date_part=2, date_id=date2.id, trait_id=trait2.id, description="You stop the server before they can leave and request an extra complimentary to-go bag of peanuts. You get midnight munchies bad!"),
            'dialogue43': Dialogue(date_part=2, date_id=date2.id, trait_id=trait3.id, description="You scan your date's face as they read the note to see if the note is bad or not. Whatever it is, you know you can talk your way out of it with your appalling charisma. "),
            'dialogue44': Dialogue(date_part=2, date_id=date2.id, trait_id=trait4.id, description="You scoot your chair back from the table, ready to bolt if it seems like there is any danger. You are not afraid to leave your date behind to save yourself."),
            'dialogue45': Dialogue(date_part=2, date_id=date2.id, trait_id=trait5.id, description="You dismiss the weirdnesss of the note. You're pretty confident the server is passing along their number to you because they're too shy to give it directly. They've been making oogly eyes at you all night."),
            'dialogue46': Dialogue(date_part=2, date_id=date2.id, trait_id=trait6.id, description="You match their energy and pull out your own pen and paper from your rucksack. The battle of passing secrets has begun!"),
            'dialogue47': Dialogue(date_part=2, date_id=date2.id, trait_id=trait7.id, description="You refuse the free peanuts and you dip the note in your mug of Muk before your date can read it. No one can out do you tonight!"),
            'dialogue48': Dialogue(date_part=2, date_id=date2.id, trait_id=trait8.id, description="You panic. Oh no. This is absolutely a bad omen and you must immediately begin reciting the Star Spangled Banner repeatedly until you feel warm and fuzzy inside again."),
            'dialogue49': Dialogue(date_part=2, date_id=date2.id, trait_id=trait9.id, description="You get tinglies in your brain. You must know the note's contents! You hold your breath until they agree to share (they don't agree and you pass out into the bowl of peanuts on the table)."),
            'dialogue50': Dialogue(date_part=2, date_id=date2.id, trait_id=trait10.id, description="You launch yourself across the table for the note before a second has passed. Peanuts and Muk go everywhere, covering you and your date."),
            'dialogue51': Dialogue(date_part=3, date_id=date2.id, trait_id=trait1.id, description="You suggest a harmless dine and dash trick You have to make sure you're not with a lame-o who doesn't like to have fun!"),
            'dialogue52': Dialogue(date_part=3, date_id=date2.id, trait_id=trait2.id, description="You grab the check immediately and slide it to your date across the table. You are a pampered princess and shouldn't have to worry about paying."),
            'dialogue53': Dialogue(date_part=3, date_id=date2.id, trait_id=trait3.id, description="You pretend to forget your wallet (even though you didn't) and ask them to cover you. You haven't had to pick up a check in years with this trick."),
            'dialogue54': Dialogue(date_part=3, date_id=date2.id, trait_id=trait4.id, description="You lunge for the check. You don't want to look cheap in front of your date! Even though you are cheap."),
            'dialogue55': Dialogue(date_part=3, date_id=date2.id, trait_id=trait5.id, description="You barely notice the check wass dropped off. You are too lost in the beautiful, sparkling, swamp-green eyes of your date, drifting into pure honeymoon phase bliss."),
            'dialogue56': Dialogue(date_part=3, date_id=date2.id, trait_id=trait6.id, description="You grab the check and play keep away for a bit. You know it's always a hit with dates."),
            'dialogue57': Dialogue(date_part=3, date_id=date2.id, trait_id=trait7.id, description="You begin a tense standoff of who will give in first and grab the check. You refuse to be the first to cave."),
            'dialogue58': Dialogue(date_part=3, date_id=date2.id, trait_id=trait8.id, description="You don't know much, but it can't be a good omen to have to pay on your first date. You push the check across the table."),
            'dialogue59': Dialogue(date_part=3, date_id=date2.id, trait_id=trait9.id, description="You don't know what to do. Will they be offended if I don't reach for the check? Will they be offended if you don't? Your body explodes with the pressure of indecision and panic."),
            'dialogue60': Dialogue(date_part=3, date_id=date2.id, trait_id=trait10.id, description="You grab the check before it hits the table and throw your card down. You then stand up, climb on top of the table, and shout out that you are picking up the tab for the entire bar."),
        }
        

        dialogues_3 = {
            'dialogue61': Dialogue(date_part=1, date_id=date3.id, trait_id=trait1.id, description="You love the idea of going to their grotto for a home cooked meal. You can raid their bedroom for secrets and red flags while they aren't looking."),
            'dialogue62': Dialogue(date_part=1, date_id=date3.id, trait_id=trait2.id, description="You would of course expect nothing less than a gourmet home cooked meal. They can cook absolutely everything, and you can enjoy being served delicious hors d'oeuvres. You won't even lift a hairy finger"),
            'dialogue63': Dialogue(date_part=1, date_id=date3.id, trait_id=trait3.id, description="You realize this would be the perfect time to try out the smoked Org Liver Stew recipe you've had your eye on. The recipe was passed down from your great grandgoblinma BawkBawk"),
            'dialogue64': Dialogue(date_part=1, date_id=date3.id, trait_id=trait4.id, description="You try to sway them to get takeout noodles from Olive Gooben, put they insist on cooking. You agree, but bring a snack just in case it's horrendous tasting."),
            'dialogue65': Dialogue(date_part=1, date_id=date3.id, trait_id=trait5.id, description="You are about to loose your marbles you're so fired up with excitement. You just KNOW that a home cooked bowl of warm Beetle Beans is the way to your hungry heart."),
            'dialogue66': Dialogue(date_part=1, date_id=date3.id, trait_id=trait6.id, description="You hope gravy is on the menu because you can't wait to start a grueling food fight in the kitchen. The messier, the better!"),
            'dialogue67': Dialogue(date_part=1, date_id=date3.id, trait_id=trait7.id, description="You are happy to share a home cooked meal, but if it's not half as good as your own Slop Glop Sammy recipe, it's a NO from you, dawg."),
            'dialogue68': Dialogue(date_part=1, date_id=date3.id, trait_id=trait8.id, description="You wager that a home cooked meal is acceptable, but only if it's muggy and the maggots living in your back swamp have no shadow."),
            'dialogue69': Dialogue(date_part=1, date_id=date3.id, trait_id=trait9.id, description="You are anxious to try something new! You are growing so bored of drinking Muk every date. You don't know how much more Muk you can take."),
            'dialogue70': Dialogue(date_part=1, date_id=date3.id, trait_id=trait10.id, description="You say yes before you even realize you're allergic to Nutmeg Borgle Brine Soup they're making."),
            'dialogue71': Dialogue(date_part=2, date_id=date3.id, trait_id=trait1.id, description="You lose your marbles for a very dark moment. You decide the best plan of action will to break out a big bottle of Muk and hope they don't notice."),
            'dialogue72': Dialogue(date_part=2, date_id=date3.id, trait_id=trait2.id, description="You don't really sweat it because the less they eat, the more you get to eat later. And you already had to slave over this microwaved ramen so they should be gratfeul"),
            'dialogue73': Dialogue(date_part=2, date_id=date3.id, trait_id=trait3.id, description="You turn to bring the dishes over to the table to eat, but somehow drop everything on the floor, ruining all the food. Oops! Guess we'll have to get Olive Gooblin for dinner. :)"),
            'dialogue74': Dialogue(date_part=2, date_id=date3.id, trait_id=trait4.id, description="You begin sweating profusely. What if they hate it and then tell me they hate me and never want to see me again? You then begin seasoning your dish with your tears."),
            'dialogue75': Dialogue(date_part=2, date_id=date3.id, trait_id=trait5.id, description="You brush it off because our true love's passion will be the seasoning!"),
            'dialogue76': Dialogue(date_part=2, date_id=date3.id, trait_id=trait6.id, description="You are not miffed because you planned a food fight anyways. This meal ss not for eating, it's for throwing forcibly at your date's face."),
            'dialogue77': Dialogue(date_part=2, date_id=date3.id, trait_id=trait7.id, description="You throw all the food in the trash and start completely over. They will eat nothing less than the best Kump Rump Lumps in the village!"),
            'dialogue78': Dialogue(date_part=2, date_id=date3.id, trait_id=trait8.id, description="You were afraid of this. Even though you performed your routine ritual of a worm dance for a good omen, the dance was sloppy and rushed. This is your punishment."),
            'dialogue79': Dialogue(date_part=2, date_id=date3.id, trait_id=trait9.id, description="You fret for 3 minutes but then decide to accept your fate. Maybe you can add Sriracha sauce and they won't notice? Sriracha fixes everything"),
            'dialogue80': Dialogue(date_part=2, date_id=date3.id, trait_id=trait10.id, description="You swipe the dish out from your date's hands before they can take a bite of your garbage food. Before they can even scowl, you have DoorDashed McGoblin's to your front door."),
            'dialogue81': Dialogue(date_part=3, date_id=date3.id, trait_id=trait1.id, description="You feel a grin spread across your googly goblin face. You knew a warm bowl of Bungle Stew would get them wanting more (love & cuddless)."),
            'dialogue82': Dialogue(date_part=3, date_id=date3.id, trait_id=trait2.id, description="You love the idea of them staying over, but wonder if there's a better goblin for you still out there. Let's be real, you're a catch."),
            'dialogue83': Dialogue(date_part=3, date_id=date3.id, trait_id=trait3.id, description="You pretend to act suave like you don't care, but secretly, you'll die if they don't stay over."),
            'dialogue84': Dialogue(date_part=3, date_id=date3.id, trait_id=trait4.id, description="You still can't tell if they find you repulsing or not. You decid the awkwardness is unpleasant and leave your own home so they won't be bothered by your presence."),
            'dialogue85': Dialogue(date_part=3, date_id=date3.id, trait_id=trait5.id, description="You are positive they are the love of your life. You lock all the doors so they can't leave you. This is the first night of forever."),
            'dialogue86': Dialogue(date_part=3, date_id=date3.id, trait_id=trait6.id, description="You love the awkwardness. You ask if they wanna play rock paper scissors to decide."),
            'dialogue87': Dialogue(date_part=3, date_id=date3.id, trait_id=trait7.id, description="You want them to stay, but you refuse to be the one to ask. This is a power battle and you will not lose."),
            'dialogue88': Dialogue(date_part=3, date_id=date3.id, trait_id=trait8.id, description="You desperately want them to stay but it is terribly bad juju to let a date stay over without the written blessing of the queen goblin mother, Horga."),
            'dialogue89': Dialogue(date_part=3, date_id=date3.id, trait_id=trait9.id, description="You are intrigued, but you don't know why they would want to stay. What would you even do? You don't have any fun puzzles or trivia to whip out for entertainment."),
            'dialogue90': Dialogue(date_part=3, date_id=date3.id, trait_id=trait10.id, description="You say yes! Then you remember you forgot to clean your bathroom. There are socks EVERYWHERE."),
        }




        all_dialogues = list(dialogues_1.values()) + list(dialogues_2.values()) + list(dialogues_3.values())
        db.session.add_all(all_dialogues)
        db.session.commit()
        dialogues_list = Dialogue.query.all()
        print("Creating traits...")
        print("Creating responses...")
        responses_1 = {
            'response1': Response(
                dialogue_id=dialogues_list[0].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub stared at the bone with the giant crack down its center that you had handed him. "
                "His brow furrowed as he examined it, trying to make sense of the situation. Why would you give him a broken bone? "
                "Did you think it was some kind of joke? Grubnub scratched his head, his confusion evident on his face.\n\n"
                "'Uh... you give Grubnub broken bone?' he asked, his voice a mixture of curiosity and uncertainty. "
                "'What Grubnub do with this? It not good for bashing, right?'\n\n"
                "He held the cracked bone up to show you, hoping for an explanation. "
                "His heart of gold wanted to believe that there must be a reason behind this, even though his understanding of the situation was a bit muddled. "
                "He wasn't quite sure how to react to this unexpected twist in the game, but he was willing to go along with it as long as it didn't involve hurting anyone.\n\n"
                "'Maybe Grubnub use this as... um, talking stick? Like, whoever holds broken bone gets to say something?' he suggested with a hopeful smile, "
                "trying to find a positive angle to the situation."
                "He ends up singing into the bone for a while and seems to be enjoying himself.", 
                outcome=False
            ),
            'response2': Response(
                dialogue_id=dialogues_list[1].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub observed as his date confidently strode over to the pile of bones and selected what they deemed the best bone. A sense of puzzlement crossed his features as he watched their actions unfold. The idea of taking the best bone for oneself, with the intention of not sharing it with anyone else, didn't quite match up with Grubnub's understanding of fun and togetherness.\n\n"
                "'Uh, you take best bone,' Grubnub remarked, tilting his head slightly as he tried to make sense of the situation. 'Grubnub thought we play together, be on same team.'\n\n"
                "He fidgeted with the bone he held, a bit unsure of how to respond to his date's competitive approach. While his heart of gold prompted him to want to help others enjoy the game, he also understood that everyone had their own way of approaching things.\n\n"
                "'But, uh, maybe we all have fun anyway,' Grubnub suggested with an awkward smile, attempting to find a common ground between his date's strategy and his own values.",
                outcome = False
            ),
            'response3': Response(
                dialogue_id=dialogues_list[2].id, 
                goblin_id=grubnub.id, 
                response="Grubnub watched with his slightly awkward charm as you gathered a few decent bones and skillfully wrapped bands of leather around each. He scratched his head in curiosity, intrigued by your resourcefulness and thoughtfulness.\n\n"
                "'Oh, that's smart!' he exclaimed, a genuine smile brightening his face. 'Leather grip make bones better, huh? Grubnub didn't think of that.'\n\n"
                "Grubnub's admiration for your approach was evident, even if he didn't quite grasp all the details. The idea of enhancing the bones for better grip stability seemed like a brilliant solution to him.\n\n"
                "As you continued to prepare the bones, he couldn't help but ask, 'You think this make game even more fun? Maybe everyone use leather grip?'\n\n"
                "His excitement to learn from your ingenuity and make the game more enjoyable for everyone reflected his heart of gold, always seeking to contribute positively to the moment.", 
                outcome=True),
            'response4': Response(
                dialogue_id=dialogues_list[3].id, 
                goblin_id=grubnub.id, 
                response="Grubnub observed your careful selection of the most normal and non-threatening bones from the pile. He tilted his head to the side, his brow furrowing in contemplation as he processed your approach.\n\n"
                "'Oh, you choose non-scary bones,' he noted, a bit of surprise in his voice. 'That good thinking. Grubnub not want to get bashed too hard.'\n\n"
                "Your consideration for both yourself and your partner resonated with Grubnub's desire for safety and camaraderie. It was clear that he appreciated your thoughtful gesture.\n\n"
                "With a nod, he added, 'Maybe we have more fun this way, not too ouchy. You always think about everyone.'", 
                outcome=True),
            'response5': Response(
                dialogue_id=dialogues_list[4].id, 
                goblin_id=grubnub.id, 
                response="Grubnub watched as you chose to approach the game with honesty and simplicity. A warm smile spread across his face, recognizing your genuine attitude and willingness to enjoy the experience without overthinking.\n\n"
                "'Just going with what's nearby?' he remarked, a mix of curiosity and admiration in his voice. 'That's the Goblin way. I like it.'\n\n"
                "Your carefree approach resonated with Grubnub's preference for straightforwardness and the joy of the moment. He could relate to your outlook.\n\n"
                "With a nod, he added, 'Yeah, it's all about fun. We play together, we all have fun. You really understand that.'", 
                outcome=True),
            'response6': Response(
                dialogue_id=dialogues_list[5].id, 
                goblin_id=grubnub.id, 
                response="Grubnub's eyes widened as you suggested spicing up the game by introducing blindfolds. He seemed both intrigued and uncertain, trying to process the idea.\n\n"
                "'Blindfolds?' he repeated, his voice a mix of curiosity and caution. 'That make it... interesting, right?'\n\n"
                "Your creative suggestion caught Grubnub's attention, pushing the boundaries of his understanding of the game. The notion of blindfolds seemed to pique his curiosity.\n\n"
                "He scratched his head and then grinned. 'Maybe we try it! Grubnub not see how it go, but that Goblin-y for sure!'", 
                outcome=False),
            'response7': Response(
                dialogue_id=dialogues_list[6].id, 
                goblin_id=grubnub.id, 
                response="Grubnub's expression shifted as he listened to your declaration. Confusion furrowed his brow, "
                "and his heart of gold struggled to understand the change in tone.\n\n"
                "'Wait, not their rules? Grubnub not understand,' he mumbled, his voice tinged with a hint of unease. "
                "'Why not play together? Everyone have fun.'\n\n"
                "The concept of asserting his own rules over someone else's seemed foreign to him. "
                "Grubnub's nature was rooted in inclusivity and simplicity, aiming to create joy and camaraderie rather than discord. "
                "The idea of imposing his will in a way that could potentially upset his partner wasn't something that resonated well with him.\n\n"
                "He scratched his head, his awkwardness evident as he tried to navigate this new territory. "
                "'Maybe... maybe we talk about it? Find way to make fun for both?' he suggested, his voice carrying a mix of hope and uncertainty.\n\n"
                "When you deny his request, Grubnub seems to be unable to hide his emotions as a tear wells in his eye.", 
                outcome=False),
            'response8': Response(
                dialogue_id=dialogues_list[7].id, 
                goblin_id=grubnub.id, 
                response="Grubnub's eyes widened in surprise as you began to set up an elaborate pregame ritual involving candles, incense, and cloud interpretation. "
                "He watched in a mix of curiosity and bewilderment, his brow furrowing as he tried to process what he was witnessing.\n\n"
                "'Wait, candles and clouds? Grubnub not understand,' he mumbled, scratching his head in confusion. "
                "His heart of gold prompted him to be open-minded, but the intricacies of this ritual were beyond his grasp.\n\n"
                "With a hesitant smile, he tilted his head and asked, 'This Goblin-y way to be safe?' But... game already fun, right?'\n\n"
                "He might not fully comprehend the purpose of the ritual, but he is willing to be a good sport.", 
                outcome=False),
            'response9': Response(
                dialogue_id=dialogues_list[8].id, 
                goblin_id=grubnub.id, 
                response="Grubnub's eyes brightened with a mix of surprise and excitement at the prospect of taking the lead in the game. He smiled like you've never seen.\n\n"
                "'Grubnub in charge? Okay!' he exclaimed, a hint of enthusiasm in his voice. 'We play Goblin baseball, make it fun!'\n\n"
                "Your decision to let Grubnub take charge resonated with his nature, which thrived on camaraderie and simple enjoyment.\n\n"
                "With a determined nod, he added, 'We use bones, have fun, and bash the 'base' good! Grubnub lead, everyone have a great time!'\n\n", 
                outcome=True),
            'response10': Response(
                dialogue_id=dialogues_list[9].id, 
                goblin_id=grubnub.id, 
                response="Grubnub tilted his head in consideration as you expressed your desire to relocate the game to the riverbank.\n\n"
                "'Move game to riverbank? Better lighting, more exciting?' he repeated, a mix of curiosity and uncertainty in his voice. 'Hmm, maybe that Goblin-y way to play.'\n\n"
                "Your suggestion to move the game to a different location seemed to intrigue Grubnub, even if he couldn't fully grasp all the reasons behind it.\n\n"
                "He scratched his head and then smiled. 'Okay, we try it! Grubnub curious. Maybe riverbank make game even more fun!'\n\n", 
                outcome=True),
            'response11': Response(
                dialogue_id=dialogues_list[0].id, 
                goblin_id=sneezle.id, 
                response="Sneezle rolled his eyes dramatically as you hand him the cracked bone. 'Oh, great, We're off to a fantastic start,' he muttered, his amusement more sarcastic than genuine.\n\n"
                    "'Cracked bone, huh? Original,' Sneezle added with an exaggerated yawn. He didn't seem too thrilled with the idea but resigned to the absurdity of it all.\n\n"
                    "He clearly didn't enjoy being toyed with like that. 'Yeah, well, I'll end up winning anyways.'", 
                outcome=False),
            'response12': Response(
                dialogue_id=dialogues_list[1].id, 
                goblin_id=sneezle.id, 
                response="Sneezle raised an eyebrow at your confident bone selection. 'Ah, claiming the throne, are we?' he quipped, his tone tinged with sarcasm.\n\n"
                    "'Best bone, best player, what's next? A crown?' Sneezle's mockery was evident, his playful spirit channeling his disbelief.\n\n"
                    "He sighed playfully and gave a thumbs-up. 'Hey maybe we should make your crown out of bones too! Get it? Bone-head!'", 
                outcome=False),
            'response13': Response(
                dialogue_id=dialogues_list[2].id, 
                goblin_id=sneezle.id, 
                response="Sneezle's eyes widened in mock astonishment at your attempt to improve bone grip. 'Leather grips, the pinnacle of Goblin innovation,' he deadpanned.\n\n"
                    "'Stability, right. Because bones can get quite wobbly,' Sneezle's sarcasm was on full display as he teased.\n\n"
                    "He chuckled dryly and gave a thumbs-up. 'Who knew Goblin baseball needed such sophisticated solutions?'", 
                outcome=False),
            'response14': Response(
                dialogue_id=dialogues_list[3].id, 
                goblin_id=sneezle.id, 
                response="Sneezle raised an eyebrow at your cautious approach to bone selection. 'Oh, going for the less scary bones, I see,' he remarked with a smirk.\n\n"
                    "'Good thing we're not going off to a real fight or we'd take all the glory!' Sneezle winked playfully, his sarcasm seemed flirtatious.\n\n"
                    "He chuckled and gave a thumbs-up. 'Let's hope these 'non-threatening' bones are up for some exciting base-bashing!'", 
                outcome=True),
            'response15': Response(
                dialogue_id=dialogues_list[4].id, 
                goblin_id=sneezle.id, 
                response="Sneezle let out an exaggerated laugh at your spontaneous approach. 'Just grab whatever, why not?' he said through stifled chuckles.\n\n"
                    "'No need for a plan when chaos can reign,' Sneezle walked up and grabbed the smallest bone in the pile. \n\n"
                    "He smiled and gave a wink. 'Let's see how your 'strategy' plays out in this bone-bashing masterpiece!'", 
                outcome=True),
            'response16': Response(
                dialogue_id=dialogues_list[5].id, 
                goblin_id=sneezle.id, 
                response="Sneezle's expression turned quizzical as you suggested blindfolds. 'Oh, going for the ultimate challenge, I see,' he remarked, a hint of amusement in his voice.\n\n"
                    "'Who needs to see when you can just feel your way to victory?' Sneezle's playful sarcasm was evident in his response. You think he loves this.\n\n"
                    "'Let's see if this adds a whole new level of excitement to our bone-bashing antics!'", 
                outcome=True),
            'response17': Response(
                dialogue_id=dialogues_list[6].id, 
                goblin_id=sneezle.id, 
                response="Sneezle's eyebrow arched at your declaration to play by your rules. 'Oh, so you get to decide everything, huh?' he retorted with a smirk.\n\n"
                    "'Rules are so yesterday, aren't they?' Sneezle's playful tone was mixed with a hint of annoyance.\n\n"
                    "He chuckled but rolled his eyes. 'Let's see how your revolutionary rules impact this bone-bashing saga.'", 
                outcome=True),
            'response18': Response(
                dialogue_id=dialogues_list[7].id, 
                goblin_id=sneezle.id, 
                response="Sneezle's expression turned puzzled as you mentioned the pregame ritual. 'Candles, incense, and clouds, huh?' he repeated with a raised eyebrow. 'Right, because bones totally care about clouds.'\n\n"
                    "'Let's add a touch of mystic ambiance to our bone-bashing extravaganza, because that's what we're missing,' Sneezle's sarcasm dripped like honey.\n\n"
                    "He let out an exaggerated sigh. 'Sure, let's see if those clouds will tell us how to win the bone-bashing championship,' He plopped down on the ground next to you and started picking at his feet.", 
                outcome=False),
            'response19': Response(
                dialogue_id=dialogues_list[8].id, 
                goblin_id=sneezle.id, 
                response="Sneezle couldn't help but smile with excitement as you decided to let him take the lead. 'Oh, giving me the throne, are you?' he teased with a grin.\n\n"
                    "'As you say, your Bone-Bashing Highness,' Sneezle added with exaggerated grandeur and proper flourish.\n\n"
                    "He chuckled and gave a playful salute. 'Let's start by ditching the bones!'", 
                outcome=True),
            'response20': Response(
                dialogue_id=dialogues_list[9].id, 
                goblin_id=sneezle.id, 
                response="Sneezle's expression turned intrigued as you mentioned moving the game. 'Riverbank, huh? Sounds like an upgrade!' he remarked with a grin.\n\n"
                    "'A change of scenery eh? Hope you dont mind getting wet!' Sneezle's playful tone was evident as he responded.\n\n"
                    "He chuckled and gave a thumbs-up. 'Let's see if this riverbank takes to our game. If not, there's always swimming!'", 
                outcome=True),
            'response21': Response(
                dialogue_id=dialogues_list[0].id, 
                goblin_id=blort.id, 
                response="Blort's eyes shifted to the bone in your hands, and he couldn't help but look a bit concerned.\n\n"
                "'Oh, well, that's a twist,' he mumbled, his voice tinged with uncertainty. You could sense his hesitation as he tried to process the notion of using a cracked bone.\n\n"
                "His brows furrowed in thought, and he shifted nervously on his feet, his fingers fidgeting with the hem of his clothing. "
                "'Um, cracking bones for a good laugh, huh? That's quite the icebreaker,' Blort added, his tone a mixture of curiosity and apprehension.\n\n"
                "He paused, his gaze flickering between you and the bone. 'I guess... if you think it'll be fun, then maybe we can give it a try?' he finally said, "
                "his voice softening with a touch of optimism. It was clear that he was willing to go along with the idea, even if he wasn't entirely convinced.", 
                outcome=False),
            'response22': Response(
                dialogue_id=dialogues_list[1].id, 
                goblin_id=blort.id, 
                response="Blort's expression turned slightly puzzled as you confidently claimed the best bone for yourself. His brows furrowed, and he seemed a bit unsure how to respond to your assertiveness.\n\n"
                "'Oh, well, that's big,' he remarked with a hint of shyness in his voice. His gaze shifted to the bone you were holding, and he gave it a nervous look.\n\n"
                "'Best bone, huh? I guess it's good to have a favorite,' Blort added, his tone tinged with a mix of curiosity and fear.\n\n"
                "He smiled shyly, his eyes unable to meet yours. 'I'll just pick out one that feels right, I suppose. Can't really compete with the best, after all.'", 
                outcome=False),
            'response23': Response(
                dialogue_id=dialogues_list[2].id, 
                goblin_id=blort.id, 
                response="Blort's face lit up with appreciation as you wrapped leather bands around the bones. His eyes sparkled with clear delight, and he couldn't hide his admiration for your thoughtful gesture.\n\n"
                "'Oh, that's so nice of you,' he said, his voice warm with gratitude. He gently reached out to touch one of the wrapped bones, his fingers tracing over the leather.\n\n"
                "'Leather bands for grip stability, huh? That's... quite clever,' Blort added, genuinely impressed by the practicality of your idea. He looked up at you with a warm smile.\n\n"
                "He smiled and gave you happy nod. 'I'm sure these grips will come in handy. Thanks for thinking of me!'", 
                outcome=True),
            'response24': Response(
                dialogue_id=dialogues_list[3].id, 
                goblin_id=blort.id, 
                response="Blort's gaze softened as you carefully selected bones from the pile that seemed less intimidating. A warm smile graced his lips, and he nodded in approval.\n\n"
                "'Considerate choice,' he commented, his voice carrying a sense of appreciation. He examined the bones you had picked out and gave a gentle nod.\n\n"
                "'I was nervous until now. This makes me far more comfortable!' Blort added with a twinkle in his eye.\n\n"
                "He chuckled softly and nodded again. 'Let's keep it lighthearted and enjoyable!'", 
                outcome=True),
            'response25': Response(
                dialogue_id=dialogues_list[4].id, 
                goblin_id=blort.id, 
                response="Blort's eyes brightened with a warm smile as you suggested an open and honest approach to the game. He nodded in agreement, clearly liking the idea.\n\n"
                "'I prefer an honest and open partner, it makes me happy that you feel the same' he said, his voice genuine and appreciative.\n\n"
                "Blort looked at the bones and then at you, his expression warm. 'I'll just grab whatever's nearby, too. Let's keep it spontaneously fair!'", 
                outcome=True),
            'response26': Response(
                dialogue_id=dialogues_list[5].id, 
                goblin_id=blort.id, 
                response="Blort's eyes widened with fear as you suggested wearing blindfolds. He blinked a few times, clearly surprised by the idea.\n\n"
                "'Blindfolds?' he repeated, his voice tinged with dread. 'That could be... interesting, I suppose.'\n\n"
                "His fingers played with the edge of his clothing as he thought about the proposal. 'I mean, it's certainly new to me'\n\n"
                "Blort's shy smile oozed regret. 'Alright, let's get on with it. Blindfolded bone-bashing, here we come...'", 
                outcome=False),
            'response27': Response(
                dialogue_id=dialogues_list[6].id, 
                goblin_id=blort.id, 
                response="Blort's expression shifted, his brows furrowing slightly as you declared your intention to play by your own rules.\n\n"
                "'Wait, not the usual rules? I'm not sure I understand,' he mumbled, his voice carrying the air of confusion. 'Why not just play together and have fun?'\n\n"
                "The concept of asserting different rules seemed to puzzle him.\n\n"
                "He scratched his head, his shyness evident. 'Maybe... we can just see how it goes and change it later?' he suggested hesitantly.\n\n"
                "After you remained firm, Blort gave in rather than risk further conflict.",
                outcome=False),
            'response28': Response(
                dialogue_id=dialogues_list[7].id, 
                goblin_id=blort.id, 
                response="Blort's eyes widened as you mentioned your pregame ritual, There seemed to be a glint in his eye.\n\n"
                "'Oh, a pregame ritual? That sounds wonderful!' he sat and watched you prepare your items and begin.\n\n"
                "His fingers fidgeted with the hem of his clothing as he listened. 'Candles, incense, and interpretation of clouds, you say?'\n\n"
                "Blort's smile radiated brightly. 'Well, that's certainly a unique way to prepare. I can't wait to see how it's done!'", 
                outcome=True),
            'response29': Response(
                dialogue_id=dialogues_list[8].id, 
                goblin_id=blort.id, 
                response="Blort's gentle smile brightened as you suggested letting him take the lead. He shook his head in disagreement, his eyes reflecting his easygoing nature.\n\n"
                "'That's a very, very kind thought, but I would like you to lead me. I fear I'd make a fool of myself. But, thank you, truly, for suggesting it,' he said, his voice filled with warmth.\n\n"
                "Blort's fingers played with the edge of his clothing as he waited, 'Just show me the way, and I'll follow along. Let's make this game a memorable one!'", 
                outcome=True),
            'response30': Response(
                dialogue_id=dialogues_list[9].id, 
                goblin_id=blort.id, 
                response="Blort's eyes lit up with a spark of interest as you proposed the idea of moving the game to the riverbank. A mischievous grin tugged at his lips.\n\n"
                "'Riverbank, eh? Now that's an intriguing twist,' he remarked, his voice carrying a playful tone. He gazed at the nearby river, lost in thought.\n\n"
                "A soft chuckle escaped his lips. 'A touch of adventure and who knows what other surprises await us by the water's edge. I'm in!'", 
                outcome=True),
            'response31': Response(
                dialogue_id=dialogues_list[0].id, 
                goblin_id=grimble.id, 
                response="Grimble's expression shifted from his usual bravado to one of subtle irritation as you handed him the cracked bone. His brows furrowed slightly.\n\n"
                "'Oh, how charming,' he muttered, his voice laced with sarcasm. He examined the bone with a critical eye, his annoyance evident.\n\n"
                "His lips curved into a tight smile that didn't quite reach his eyes. 'A cracked bone? How wonderfully considerate of you,' he said, his tone dripping with spite.\n\n"
                "With a dismissive wave, Grimble tossed the cracked bone aside and folded his arms. 'Well, aren't we the pinnacle of generosity today?'\n\n"
                "Something about his response hinted at a deeper sadness. This insult truly hurt him.", 
                outcome=False),
            'response32': Response(
                dialogue_id=dialogues_list[1].id, 
                goblin_id=grimble.id, 
                response="Grimble's eyebrows shot up in surprise as you confidently claimed the best bone for yourself. His expression shifted from surprise to mild annoyance.\n\n"
                "'Ah, the grand prize goes to you,' he remarked with a touch of sarcasm, his voice tinged with a hint of irritation. He looked at the remaining bones, unimpressed.\n\n"
                "His lips curled into a half-smile, half-smirk. 'By all means, take the crown jewel. I'll just make do with whatever you deem unworthy of your greatness.'\n\n"
                "Grimble's eyes rolled as he picked up a bone. 'Who knew bone selection could be such a riveting competition?'", 
                outcome=False),
            'response33': Response(
                dialogue_id=dialogues_list[2].id, 
                goblin_id=grimble.id, 
                response="Grimble's eyes lit up with surprise and a touch of genuine appreciation as you wrapped bands of leather around the bones. His demeanor softened.\n\n"
                "'Leather bands, huh? That's a thoughtful touch,' he commented, his voice warm. He examined the wrapped bones with a pleased expression.\n\n"
                "A genuine smile graced his lips. 'Well, well, someone's looking out for our comfort. Can't say I mind the extra effort for a better grip.'\n\n"
                "As he picked up a bone with a leather band, Grimble's smile lingered. 'Let's make sure these grips elevate our bone-bashing prowess, shall we?'", 
                outcome=True),
            'response34': Response(
                dialogue_id=dialogues_list[3].id, 
                goblin_id=grimble.id, 
                response="Grimble's eyebrows raised in mild surprise as you opted for the most normal bones. He tilted his head, considering your choice.\n\n"
                "'Playing it safe, are we?' he mused with a hint of amusement, his voice carrying a touch of curiosity. He examined the bones before him.\n\n"
                "A smirk tugged at his lips. 'Well, well, no need to raise any unnecessary alarms. Let's keep it civil, then.'\n\n"
                "As he picked up a bone, Grimble's eyes danced with a playful glint. 'Who says safe can't be fun.'", 
                outcome=True),
            'response35': Response(
                dialogue_id=dialogues_list[4].id, 
                goblin_id=grimble.id, 
                response="Grimble's lips curved into a knowing smile as you chose to be honest and let him select his own bone. He nodded appreciatively.\n\n"
                "'No tricks, no games, just straightforward. I like your style,' he remarked, his voice carrying a tone of approval. He examined the bones.\n\n"
                "His grin grew wider. 'Let's keep things fair and see how it plays out in our bone-bashing adventure.'\n\n"
                "Grimble flourished the closest bone and bowed deeply. 'May the most straightforward player win.'", 
                outcome=True),
            'response36': Response(
                dialogue_id=dialogues_list[5].id, 
                goblin_id=grimble.id, 
                response="Grimble's eyebrows shot up in surprise as you suggested both of you wearing blindfolds. He blinked a few times, processing the idea.\n\n"
                "'Blindfolds? Now that's a twist I didn't see coming,' he said with a chuckle, his voice tinged with a mix of intrigue and uncertainty. He contemplated the concept.\n\n"
                "A playful grin tugged at his lips. 'Well, well, this could either be an epic disaster or a legendary tale to tell. Count me in!'\n\n"
                "As he tied the blindfold around his eyes, Grimble's laughter echoed. 'Let's navigate this game with a whole new level of challenge!'", 
                outcome=True),
            'response37': Response(
                dialogue_id=dialogues_list[6].id, 
                goblin_id=grimble.id, 
                response="Grimble's expression shifted from his usual bravado to one of clear annoyance as you declared your intent to change the rules. His brows furrowed.\n\n"
                "'Oh, how marvelous. Changing the rules to your favor, very mature.' he muttered, his voice dripping with dissapointment.\n\n"
                "His lips curved into a tight, cynical smile. 'Congratulations, you've managed to put a damper on what was supposed to be a simple game.'\n\n"
                "He continued, 'Well, by all means, do enlighten me on your new set of rules. Let's see where this farcical journey leads.'", 
                outcome=False),
            'response38': Response(
                dialogue_id=dialogues_list[7].id, 
                goblin_id=grimble.id, 
                response="Grimble's eyebrows raised in mild surprise as you mentioned your pregame ritual. He watched with curiosity as you lit candles and incense.\n\n"
                "'A ritual, you say?' he mused, his voice piqued with curiousity. He observed as you interpreted the clouds.\n\n"
                "A faint smile tugged at his lips. 'Well, I can't say I've seen someone prepare for a game quite like this. Let's hope your ritual brings some luck!'\n\n"
                "As he picked up his bone, Grimble's gaze remained on the sky. 'May the winds of fate guide our bones to victory, or at least friendship,' his eyes switched to yours like a moth discovering flame.", 
                outcome=True),
            'response39': Response(
                dialogue_id=dialogues_list[8].id, 
                goblin_id=grimble.id, 
                response="Grimble's grin deepened as you entrusted him with the game's direction. He looked at you, his eyes holding a hint of warmth and appreciation.\n\n"
                "'Leaving it in my capable hands, huh?' he said with a charming chuckle, his voice carrying a playful yet affectionate tone. He pondered his choices.\n\n"
                "A tender smile played on his lips. 'Well, let's make this a night to remember. I'll craft an adventure that we'll both cherish, bone-bashing and all.'\n\n"
                "As he picked up a bone, Grimble's gaze lingered on you. 'Lets make some memories together'", 
                outcome=True),
            'response40': Response(
                dialogue_id=dialogues_list[9].id, 
                goblin_id=grimble.id, 
                response= "Grimble's eyes widened in surprise as you suggested moving the game to the riverbank. He blinked a few times, considering the idea.\n\n"
                "'Riverbank, huh? Well, well, aren't you the adventurous one?' he said with a grin, his voice carrying a mix of curiosity and excitement. He looked to the river.\n\n"
                "His grin grew wider. 'A change of scenery might just breathe new life into this bone-bashing bonanza. Let's make this game a riverbank legend!'\n\n"
                "As he started walking towards the river, Grimble's enthusiasm was contagious. 'Come on, let's make this game one for the ages by the water's edge!'", 
                outcome=True),
            'response41': Response(
                dialogue_id=dialogues_list[0].id, 
                goblin_id=zongo.id, 
                response="Zongo's eyes narrowed as he looked at the cracked bone in his hand, a mixture of suspicion and irritation evident on his face.\n\n"
                "'Oh, how utterly predictable,' he drawled, his voice dripping with condescension. He tapped the bone with his finger, his annoyance clear.\n\n"
                "With a dismissive wave of his hand, Zongo conjured a small illusion, making the bone you hold to appear even more cracked and shattered than his. 'Clearly, this bone was beneath you. Bravo for the theatrics.'\n\n"
                "He tossed the bone aside with a sigh. 'Let's not waste any more time on such petty tricks, shall we?'", 
                outcome=False),
            'response42': Response(
                dialogue_id=dialogues_list[1].id, 
                goblin_id=zongo.id, 
                response="Zongo's eyebrow arched in mild annoyance as you immediately claimed the best bone for yourself. He looked at the remaining bones with a hint of disdain.\n\n"
                "'Like a child running to steal the best piece of meat before dinner,' he commented with a sarcastic smirk. He examined the lesser bones.\n\n"
                "With a flourish of his hand, Zongo summoned a sparkling light around the bone he chose, making it radiate light. 'These bones shall suffice.'\n\n"
                "He brandished his bone in your direction. 'Let's see if you are worthy of such avarice.'", 
                outcome=False),
            'response43': Response(
                dialogue_id=dialogues_list[2].id, 
                goblin_id=zongo.id, 
                response="Zongo's lips curled into a smirk as he observed you wrapping leather bands around the bones. He raised an eyebrow, clearly unimpressed.\n\n"
                "'Leather bands? How quaint,' he remarked with a touch of mockery. He examined the adorned bones with a critical eye.\n\n"
                "He picked up a bone with a dismissive shrug. 'Let's see if these elaborate trinkets enhance your bone-bashing prowess, shall we?'\n\n"
                "A sly grin crossed his face as he conjured a shimmering adhesive on his fingertips. 'Though I must say, my magical grip enhancement might overshadow your practical approach.'", 
                outcome=True),
            'response44': Response(
                dialogue_id=dialogues_list[3].id, 
                goblin_id=zongo.id, 
                response="Zongo's eyes rolled with a mixture of annoyance and amusement as you chose to play it safe with the bone selection. He scoffed.\n\n"
                "'Opting for mediocrity, I see,' he quipped with a derisive smirk, his voice tinged with condescension. He examined the bones before him.\n\n"
                "With a flick of his finger, Zongo conjured a brief illusion, making the bones shimmer with an ethereal light. 'Let's hope your spineless choices don't lead to a spineless game.'\n\n"
                "He picked up a bone with an exaggerated sigh. 'Let's indulge your lack of audacity--for now.'", 
                outcome=False),
            'response45': Response(
                dialogue_id=dialogues_list[4].id, 
                goblin_id=zongo.id, 
                response="Zongo's lips curled into a smirk as you opted for honesty and randomness in selecting bones. He raised an eyebrow, clearly amused by your approach.\n\n"
                "'Ah, relinquishing control, how novel. I will not be doing the same' he commented with a touch of mockery. He examined the bones with mild interest.\n\n"
                "With a flourish of his hand, Zongo conjured a flicker of flames around his chosen bone, making it seem like a prized artifact. 'A fitting choice for an experiment in unpredictability.'\n\n"
                "He picked up the bone with a casual shrug. 'Let's pit your honestly against my ambition. I fear I will not be losing today.'", 
                outcome=False),
            'response46': Response(
                dialogue_id=dialogues_list[5].id, 
                goblin_id=zongo.id, 
                response="Zongo's lips curled into an amused smile as you proposed playing blindfolded. He chuckled softly.\n\n"
                "'Blindfolds? Well, I must admit, this is an unexpected twist,' he commented with his voice carrying a hint of excitement. He examined the blindfolds.\n\n"
                "With a flick of his finger, Zongo conjured an illusion of true darkness on his blindfold,'This shall be a bit of a sensory experiment. How intriguing.'\n\n"
                "He picked up a bone, his smirk evolving into a grin. 'Let's embrace this challenge and see who leads whom?'", 
                outcome=True),
            'response47': Response(
                dialogue_id=dialogues_list[6].id, 
                goblin_id=zongo.id, 
                response="Zongo's eyes flashed with irritation as you asserted your dominance over the game. He frowned, clearly displeased by your defiance.\n\n"
                "'Oh, how delightful,' he remarked with clear hostility. He glared at the bones before him.\n\n"
                "With a dismissive wave of his hand, Zongo lit the piles of bones ablaze. 'If you think yourself superior to me, you are assuredly mistaken.'\n\n"
                "Wath another flick of his wrist the flames dissipate before damaging the pile. 'Let's see how your pitiful attempt to belittle me pans out. We play your way, but I will win.'", 
                outcome=False),
            'response48': Response(
                dialogue_id=dialogues_list[7].id, 
                goblin_id=zongo.id, 
                response="Zongo's expression narrowed inquisitively as you revealed your pregame ritual.\n\n"
                "'A ritual for safety, how quaintly superstitious,' he commented not unkindly. He examined the candles and incense.\n\n"
                "With a wave of his hand, Zongo conjured a playful illusion of clouds forming intricate patterns. 'Ah, the interpretation of clouds. I used to spend hours lost in them.'\n\n"
                "After a long moment, he picked up a bone and smiled softly. 'Let's see if your shamanic incantations and cloud-based divinations will sway the cosmic forces in your favor.'",
                outcome=True),
            'response49': Response(
                dialogue_id=dialogues_list[8].id, 
                goblin_id=zongo.id, 
                response="Zongo's eyebrow arched with a mixture of surprise and smug satisfaction as you granted him the authority to lead the game. He smirked, clearly pleased.\n\n"
                "'Ah, finally recognizing my unparalleled genius,' he quipped. He looked at the bones with new confidence.\n\n"
                "With a flourish of his hand, Zongo conjured a layer of frost around the pile of bones, making them shine with crystaline brilliance. 'Behold, a game molded by my cold heart!'\n\n"
                "He picked up a bone with a triumphant smile. 'Let the masterpiece begin as I orchestrate our symphony. Mind the frostbite, darling.'", 
                outcome=True),
            'response50': Response(
                dialogue_id=dialogues_list[9].id, 
                goblin_id=zongo.id, 
                response="Zongo's expression shifted with a mix of annoyance and mild intrigue as you proposed relocating the game to the riverbank. He sighed, clearly unimpressed.\n\n"
                "'Riverbank? Really? How mundane,' he commented with a touch of disdain. He looked toward the river with a dismissive glance.\n\n"
                "With a wave of his hand, Zongo conjured a subtle illusion, casting a faint shimmer over the bones. 'Perhaps this scenery change will salvage the impending banality.'\n\n"
                "He picked up a bone with a hint of annoyance. 'Let's hope your uninspiring suggestion doesn't taint the grandeur of our bone-bashing spectacle.'", 
                outcome=False),
        }
        responses_2 = {
            'response51': Response(
                dialogue_id=dialogues_list[10].id, 
                goblin_id=grubnub.id, 
                response=
                "You decide to run up and pretend to be their parent, putting on an exaggerated, comical voice. 'Fear not, little one! It is I, your long-lost parent, here to rescue you from the clutches of the nefarious baseball game!' The child looks at you with a mix of confusion and amusement, clearly not buying your act. They giggle nonetheless."
                "\n\nGrubnub tilts his head and furrows his brow, trying to process the situation. He scratches his head and mumbles, 'Uh, are you really their parent? I don't remember you saying that you had kid before.'"
                "\n\nYou burst into laughter, realizing that Grubnub took your act seriously. You explain the situation, and Grubnub's face lights up with understanding. 'Ohhh, I get it now! You trying to be funny and make kid happy.' He chuckles."
                "\n\nThe child's actual parent arrives, slightly out of breath, and thanks you for trying to entertain their child. Grubnub enthusiastically chimes in, 'Yeah, we were just playin'!' The parent smiles, grateful for your playful interaction with their child. As the parent and child walk away, you and Grubnub share a hearty laugh.",
                outcome=True
            ),
            'response52': Response(
                dialogue_id=dialogues_list[11].id, 
                goblin_id=grubnub.id, 
                response=
                "With a troubling sense of greed, you make a decision that Grubnub would clearly find unsettling. You go ahead with your plan and begin pilfering throught the child's posessions."
                "\n\nGrubnub's eyes widen, and he stammers, 'Wait, what are ya...? Hey, that's not right! We ain't supposed to do that!'"
                "\n\nYou manage to take a few coins and a snack from the child's pockets. The child starts crying just as the parents finally spot the child."
                "\n\nGrubnub's disappointment is palpable as he crosses his arms and looks away from you. 'I thought we were having fun together. This ain't the kinda stuff I'm okay with.'"
                "\n\nThe child's parent approaches, clearly upset, and asks what's going on. Grubnub steps forward, explaining the situation and distancing himself from your actions."
                "\n\nAs you're forced to confront the consequences of your actions, Grubnub keeps his distance and looks disappointed in you. It seems your choice has put a damper on the otherwise pleasant date.",
                outcome=False
            ),
            'response53': Response(
                dialogue_id=dialogues_list[12].id, 
                goblin_id=grubnub.id, 
                response=
                "Seeing the distressed child, you spring into action. You quickly grab a thin strip of bark from the ground and deftly coil it into a makeshift cone. Holding it up to your mouth, you let out a high-pitched, goblin-style imitation of a bird call."
                "\n\nGrubnub watches with fascination as you emit a surprisingly accurate bird-like sound. 'Wow, you're pretty good at that!' he exclaims, a hint of admiration in his voice."
                "\n\nThe child, momentarily distracted by the unexpected noise, stops crying and starts to giggle at your antics. Soon enough, their parent arrives, thanking you for your creative solution."
                "\n\nGrubnub claps his hands in delight, a wide grin on his face. 'You sure know how to make things fun! That was a clever idea.'"
                "\n\nThe child's parent is grateful for your help, and you and Grubnub share a sense of accomplishment. The date continues on a positive note as you and Grubnub enjoy each other's company and the game of 'baseball'.",
                outcome=True
            ),
            'response54': Response(
                dialogue_id=dialogues_list[13].id, 
                goblin_id=grubnub.id, 
                response=
                "Feeling a sense of unease, you can't shake the thought that this situation might not be what it seems. You glance around nervously and lean in to whisper to Grubnub, 'Hey, I've got a bad feeling about this. I think we should sneak away and not get involved.'"
                "\n\nGrubnub raises an eyebrow and looks at you in surprise. 'Really? But, what if they need help? Maybe we should at least see what's goin' on.'"
                "\n\nDespite Grubnub's curiosity, you remain firm in your decision. You discreetly slip away from the scene, leaving the child and their situation behind."
                "\n\nAs you and Grubnub distance yourselves from the child's cries, you can't help but feel a pang of guilt. Grubnub's disappointment is evident as he sighs and mutters, 'I thought we were here to be kind and stuff.'"
                "\n\nThe two of you continue on, but there's a palpable sense of tension between you. The rest of the date feels a bit awkward as you both try to enjoy the baseball game while the memory of the abandoned child lingers in the air.",
                outcome=False
            ),
            'response55': Response(
                dialogue_id=dialogues_list[14].id, 
                goblin_id=grubnub.id, 
                response=
                "Confident in the child's ability to find their parents, you decide to take a proactive approach. You crouch down to the child's eye level and give them a reassuring smile. 'Don't worry, little one. We'll help you find your parents.'"
"\n\nGrubnub nods in agreement, his eyes filled with determination. 'Yeah, we're all gonna work together and make sure you're safe.'"
"\n\nThe child sniffs, wiping away tears, and takes your hand. Grubnub joins your side, and the three of you start scanning the area for the child's parents."
"\n\nGrubnub spots the parents a short distance away, looking frantic as they search for their missing child. With a wave and a cheerful shout, he points them in your direction."
"\n\nThe child's parents rush over with relieved expressions, thanking you and Grubnub profusely for your help. Grubnub grins proudly, clearly pleased to have played a part in reuniting the family."
"\n\nAs the child is happily embraced by their parents, Grubnub turns to you with a big smile. 'See? Teamwork always works! That was pretty awesome!'"
"\n\nYou share a triumphant grin with Grubnub, proud of how the situation turned out. The date continues on a high note.",
                outcome=True
            ),
            'response56': Response(
                dialogue_id=dialogues_list[15].id, 
                goblin_id=grubnub.id, 
                response=
                "Noticing the child's distress, you're determined to bring a smile to their face. You search your surroundings and spot a discarded bone. Picking it up, you offer it to the child with a warm smile."
"\n\n'Hey there, how about playing with us while we wait for your parents?' you suggest, your voice gentle and reassuring."
"\n\nGrubnub watches your actions with an approving nod, a soft smile tugging at his lips. 'Yeah, that's a real nice thing to do.'"
"\n\nThe child's eyes light up, and they eagerly accept the bone with a grateful smile. You demonstrate how to 'swing' the bone like a bat, and soon enough, you're engaged in a violent game of baseball with the child."
"\n\nGrubnub claps his hands in delight as he pretends to be the commentator, adding a playful twist to the game. The child's parents approach, relieved to find their child in high spirits."
"\n\nGrubnub waves them over, his face glowing with satisfaction. 'We've been havin' a blast here! Your kid's really good at this game!' Grubnub's forehead is bleeding from one of the child's more accurate bashings."
"\n\nThe child's parents chuckle and express their gratitude. As they take their child's hand, the child excitedly tells them about the fun game they played with you and Grubnub."
"\n\nGrubnub gives you an appreciative pat on the back. 'You sure know how to make a tough situation better.' The date continues on a positive note as you all enjoy the game and each other's company.",
                outcome=True
            ),
            'response57': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=grubnub.id, 
                response=
                "In a move that clearly surprises and disappoints Grubnub, you choose to completely ignore the distressed child. Focused solely on the baseball game, you pretend as if the child doesn't exist and continue playing."
"\n\nGrubnub looks at you with a mix of confusion and disapproval. 'Hey, that ain't right. We should help or at least see what's goin' on.'"
"\n\nDespite Grubnub's protest, you remain unwavering in your decision. You continue to play the game, making it evident that the child's cries are nothing more than an inconvenience to you."
"\n\nThe child's parents finally arrive, clearly upset and frustrated by your lack of response. Grubnub steps forward to explain the situation, distancing himself from your actions."
"\n\nThe child's parents express their gratitude to Grubnub for his concern and take their child's hand, giving you a disapproving look before leaving."
"\n\nGrubnub lets out a heavy sigh and looks at you with disappointment. 'I thought we were supposed to be kind to others. That wasn't very nice.' The rest of the date feels tense and awkward as Grubnub's disappointment lingers in the air.",
                outcome=False
            ),
            'response58': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=grubnub.id, 
                response=
                "A sense of superstition and urgency washes over you as you contemplate the situation. You turn to Grubnub with a serious expression and explain, 'Grubnub, we can't ignore this. It's like a bad omen. If we don't help this child find their parents soon, the whole date could be cursed.'"
"\n\nGrubnub blinks in surprise, his brow furrowing as he processes your words. 'A cursed date? I ain't never heard of somethin' like that before.'"
"\n\nYou nod emphatically, your conviction clear. 'It's serious, Grubnub. We need to make sure this child finds their parents as soon as possible.'"
"\n\nGrubnub's eyes widen, and he nods in agreement. 'Right, then. Let's do whatever we can to help.'"
"\n\nYou, Grubnub, and the child start searching the area together, your determination driving you forward. With joint efforts, you manage to locate the child's parents, who express their gratitude for your assistance."
"\n\nGrubnub beams with pride, his eyes shining as he turns to you. 'I'm glad we did the right thing. No curses on us!'"
"\n\nAs the child's parents thank both of you, the atmosphere is filled with relief and a sense of accomplishment. The rest of the date proceeds on a positive note, with you and Grubnub enjoying the baseball game and each other's company.",
                outcome=True
            ),
            'response59': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=grubnub.id, 
                response=
                "Intrigued by the circumstances, you decide to strike up a conversation with the child. Crouching down to their eye level, you ask gently, 'Hey there, little one. Do you remember where you last saw your parents? We want to make sure you find them.'"
"\n\nGrubnub watches with interest, nodding in approval. 'Yeah, it's good to get some info so we can help.'"
"\n\nThe child sniffs and wipes their tears, looking up at you with big eyes. 'I was watching the game with them, and then I wanted to go find some bugs to eat. When I came back, they weren't there.'"
"\n\nGrubnub frowns, clearly empathetic. 'Oh no, that's gotta be scary. But we're gonna make sure you're back with them real soon.'"
"\n\nWith the child's description in mind, you and Grubnub continue searching the area, keeping an eye out for the parents. Eventually, you spot them and reunite the family."
"\n\nGrubnub grins broadly, giving you a thumbs up. 'Nice job, partner! We did it!'"
"\n\nAs the child is embraced by their relieved parents, you share a satisfied smile with Grubnub. The date continues on a positive note as you all enjoy the baseball game and the heartwarming reunion.",
                outcome=True
            ),
            'response60': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=grubnub.id, 
                response=
                "With a burst of determination, you scoop up the child under your arm and break into a sprint, shouting at the top of your lungs for their parents."
"\n\nGrubnub's eyes widen in surprise as he watches you take charge. 'Hey, hold on there! You're really goin' for it!'"
"\n\nYour shout reverberates across the area, catching the attention of the child's parents who turn and rush towards you, their faces etched with concern."
"\n\nGrubnub quickly joins in the effort, his voice combining with yours in a chorus of urgency. 'Hey, over here! We got your kiddo!'"
"\n\nThe parents spot you and Grubnub, and their faces light up with relief. As they approach, you gently set the child down, allowing them to reunite with their family."
"\n\nGrubnub pats you on the back, an impressed grin on his face. 'You sure know how to make a scene! That was real quick thinkin'!'"
"\n\nWith the family's heartfelt thanks and smiles all around, the tension eases, and the date continues on a positive note as you and Grubnub enjoy the baseball game and each other's company.",
                outcome=True
            ),
            'response61': Response(
                dialogue_id=dialogues_list[10].id, 
                goblin_id=sneezle.id, 
                response=
                "With a mischievous glint in your eye, you seize the opportunity for a prank. You dash forward and grab the child's hand, dramatically declaring, 'Fear not, young one! It is I, your long-lost parent, here to whisk you away from the clutches of the mighty baseball game!'"
"\n\nSneezle watches your antics with an amused smirk, clearly entertained by your impulsive act. 'Oh, this is gonna be rich.'"
"\n\nThe child looks at you with a mix of surprise and amusement, playing along with your absurd roleplay. They giggle at your over-the-top performance."
"\n\nSneezle chuckles, his voice dripping with sarcasm. 'Oh, brilliant! A thespian in the making!'"
"\n\nJust as the child's parent arrives, trying to stifle their laughter, you drop the act and share a wink with them. 'Just a little theatrical moment,' you explain with a grin."
"\n\nSneezle chuckles again, clearly enjoying the show. 'Well, that was a performance for the ages, my friend.'"
"\n\nAs the parent and child walk away, sharing their own amused remarks, you and Sneezle share a hearty laugh over the ridiculousness of the situation.",  
                outcome=True
            ),
            'response62': Response(
                dialogue_id=dialogues_list[11].id, 
                goblin_id=sneezle.id, 
                response=
                "You surprise Sneezle with your unexpected and questionable decision. Ignoring his bewildered look, you make your way toward the child with intentions of robbing them."
"\n\nSneezle's eyes widen in disbelief, his sarcastic demeanor momentarily replaced by genuine astonishment. 'Oh, bold move there, partner.'"
"\n\nYou proceed with your plan, taking a few coins and a snack from the child's pockets. The child starts crying, and their parent is alerted to the commotion."
"\n\nSneezle crosses his arms and leans against a tree, his voice dripping with sarcasm. 'Ah, the classic act of generosity, I see.'"
"\n\nThe child's parent arrives, clearly upset, and asks what's happening. Sneezle steps forward, his tone biting, 'Seems like our friend here has some... unique methods of bonding with children.'"
"\n\nAs you're forced to face the consequences of your actions, Sneezle keeps his distance and offers a deadpan commentary on the situation. It's clear he's unimpressed with your choice."
"\n\nThe child's parent addresses the situation, and the tension in the air is palpable. Sneezle's blunt remarks serve as a reminder of the seriousness of your actions, making the rest of the date feel awkward and strained.",
                outcome=False
            ),
            'response63': Response(
                dialogue_id=dialogues_list[12].id, 
                goblin_id=sneezle.id, 
                response=
                "In a surprisingly earnest moment, you take swift action. Spotting a thin strip of bark on the ground, you deftly coil it into a makeshift cone. Holding it up to your mouth, you let out a high-pitched, goblin-style imitation of a bird call."
"\n\nSneezle watches with a mixture of amusement and approval, his typical sarcasm momentarily absent. 'Well, who knew you had the vocal chops?'"
"\n\nThe child's cries stop for a moment as they look around, puzzled by the unexpected sound. Sneezle adds to the effect by mimicking the call in a comical manner, causing the child to giggle."
"\n\nSneezle chuckles, a genuine smile on his face. 'Well, well, aren't you the avian maestro?'"
"\n\nThe child's parent arrives, following the sound of your calls, and they express their gratitude for your creative solution. Sneezle nods in approval, his appreciation evident."
"\n\nAs the parent and child walk away, sharing their own amused remarks, you and Sneezle exchange a nod of camaraderie. The date continues on a positive note as you both enjoy the baseball game and each other's company.",
                outcome=True
            ),
            'response64': Response(
                dialogue_id=dialogues_list[13].id, 
                goblin_id=sneezle.id, 
                response=
                "Your suspicion takes over, and you decide to take matters into your own hands. With a quick glance at Sneezle, you discreetly back away from the scene, ignoring the distressed child's cries."
"\n\nSneezle raises an eyebrow, his sarcasm evident in his tone. 'Ah, yes, because nothing says a great date like evading potential child conspirators.'"
"\n\nDespite Sneezle's commentary, you maintain your decision and distance yourself from the child. You and Sneezle continue the game as if nothing happened."
"\n\nSneezle lets out a dry chuckle, his voice unpleased. 'How rude of that child to be so loud, right?'"
"\n\nAs you both play on, the child's parent eventually arrives, looking for their child. Sneezle gestures to the approaching parent. 'Just in time to save us from the 'treacherous' toddler, it seems.'"
"\n\nThe date carries on, though there's an undercurrent of tension between you and Sneezle. His biting remarks serve as a constant reminder of your decision, and the atmosphere remains a bit strained.",
                outcome=False
            ),
            'response65': Response(
                dialogue_id=dialogues_list[14].id, 
                goblin_id=sneezle.id, 
                response=
                "Confidence fills you as you take charge of the situation. Kneeling down beside the child, you offer a reassuring smile and gently pat their shoulder. 'Don't worry, little one. We're here to help you find your parents. They're probably looking for you too.'"
"\n\nSneezle watches with a raised eyebrow, his tone sardonic yet strangely approving. 'Well, aren't you the ray of sunshine?'"
"\n\nWith a nod to Sneezle, you take the child's hand, and together, the three of you start scanning the surroundings. Sneezle joins in, his initial skepticism giving way to a genuine desire to assist."
"\n\nSneezle spots the child's parents first, pointing them out with an amused grin. 'Well, what do you know? Looks like your parents found their way back from the abyss.'"
"\n\nThe child's parents rush over with a mix of relief and gratitude. You exchange a knowing glance with Sneezle, appreciating his participation despite his sarcastic demeanor."
"\n\nSneezle's lips quirk into a half-smile, a rare moment of sincerity. 'I guess things can work out after all.'"
"\n\nAs the child is joyfully embraced by their parents, you share a nod of satisfaction with Sneezle. The date continues on a positive note, and you both enjoy the rest of the baseball game and each other's company.",
                outcome=True
            ),
            'response66': Response(
                dialogue_id=dialogues_list[15].id, 
                goblin_id=sneezle.id, 
                response=
                "Your empathetic side takes over, and you decide to bring a smile to the child's face. You spot a nearby bone from a past goblin baseball game and pick it up. With a playful grin, you offer it to the child and suggest, 'Hey, how about we have a pretend game of baseball while we wait for your parents?'"
"\n\nSneezle watches with an amused glint in his eye, 'Well I for one am always down to teach a child a bit of violence.'"
"\n\nThe child's eyes light up, and they accept the bone with a grateful smile. You show them how to 'swing' it like a bat, and soon enough, you're immersed in an imaginative game of baseball."
"\n\nSneezle chuckles softly, his voice surprisingly gentle. 'Well, ain't you the charitable soul?'"
"\n\nThe child's parents arrive, relieved to find their child enjoying themselves. Sneezle steps forward, flashing a cheeky grin. 'Fear not, good parents, for we have bestowed upon your child the gift of goblin-style entertainment.'"
"\n\nAs the parent and child share a laugh, you and Sneezle exchange a knowing look. The rest of the date proceeds on a positive note, with you all enjoying the baseball game and the cheerful atmosphere.",
                outcome=True
            ),
            'response67': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=sneezle.id, 
                response=
                "You decide to brush off the situation and focus solely on the game. Ignoring the child's cries, you immerse yourself in the baseball match as if the child doesn't exist."
"\n\nSneezle laughs to himself and says, 'Ah, yes, nothing like the sweet symphony of children's distress to enhance the game.'"
"\n\nAs the child's parent arrives and takes care of the situation, Sneezle leans against a tree and remarks, 'Well, your dedication to the match is truly admirable. The child might have missed their true calling as a goblin umpire.'"
"\n\nYou both share a chuckle, the humor in Sneezle's remark lightening the mood. Despite your choice, the date continues on a surprisingly positive note as you and Sneezle enjoy the baseball game and each other's company.",
                outcome=True
            ),
            'response68': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=sneezle.id, 
                response=
                "In a moment of playful melodrama, you decide to spin a tale of impending doom. You turn to Sneezle with a grave expression and declare, 'Sneezle, mark my words. This child is an omen of misfortune. If we don't help them find their parents and break the curse, this date will be doomed for eternity!'"
"\n\nSneezle's eyes widen in mock surprise, his tone dripping with sarcasm. 'Ah, yes, because we all know goblin dates are prime territory for ancient curses.'"
"\n\nYou play along with the dramatic narrative, nodding solemnly. 'It's true, Sneezle. We must be the heroes this child needs, or suffer the dire consequences.'"
"\n\nSneezle chuckles, a grin tugging at his lips. 'Well, who am I to argue with the great curse-breaker? Lead the way, oh wise one.'"
"\n\nWith a theatrical flourish, you and Sneezle assist the child in their search for their parents. As you reunite the family, Sneezle quips, 'Crisis averted, curse dispelled.'"
"\n\nThe date continues, but you get the sense that Sneezle didn't get that you were serious. Things take a slightly awkward turn as the game resumes.",
                outcome=False
            ),
            'response69': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=sneezle.id, 
                response=
                "Curiosity getting the better of you, you decide to engage the child in conversation. Kneeling down beside them, you ask with a gentle smile, 'Hey there, little one. Can you tell us how you got separated from your parents? We want to make sure you're back with them.'"
"\n\nSneezle watches your inquisitive approach with a raised eyebrow, his tone laced with sarcasm. 'Ah, yes, because clearly we're on the case of the century.'"
"\n\nThe child sniffs and wipes their tears, looking up at you with wide eyes. 'I was watching the game with them, and then I saw a shiny beetle and followed it. When I looked around, they were gone.'"
"\n\nSneezle lets out an amused snort, his voice tinged with mockery. 'Ah, the elusive beetle chase, of course.'"
"\n\nYou suppress a chuckle and nod, your understanding clear. With the child's description in mind, you and Sneezle continue searching for the parents, united in your quest."
"\n\nSneezle spots the parents first, his smirk growing. 'Looks like they've been found. Mystery solved.'"
"\n\nAs the family is happily reunited, you share a nod of satisfaction with Sneezle. The date proceeds on a positive note as you both enjoy the baseball game and each other's company.",
                outcome=True
            ),
            'response70': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=sneezle.id, 
                response=
                "In a bold move, you decide to take action immediately. Without hesitation, you scoop up the child under your arm and break into a full sprint, shouting at the top of your lungs for their parents."
"\n\nSneezle's eyes widen in surprise, his usual sarcasm momentarily replaced by genuine astonishment. 'Well, color me impressed. The hero we didn't know we needed.'"
"\n\nYour shout echoes through the area, and the child's startled cries soon turn into laughter as they enjoy the exhilarating ride. You sprint across the field, your determination driving you forward."
"\n\nSneezle's lips twitch into an amused smile, his voice laced with a hint of approval. 'Well, well, looks like someone's got a need for speed.'"
"\n\nThe child's parents spot you from a distance and rush over, their faces a mixture of concern and relief. You gently set the child down, allowing them to reunite with their family."
"\n\nSneezle claps you on the back, an impressed grin on his face. 'You certainly know how to make an entrance.'"
"\n\nAs the family shares their gratitude, you and Sneezle exchange a satisfied nod. The date continues on a high note as you both enjoy the baseball game and the memorable moment you created.",
                outcome=False
            ),
            'response71': Response(
                dialogue_id=dialogues_list[10].id, 
                goblin_id=blort.id, 
                response=
                "In a bold move, you decide to take action immediately. Without hesitation, you scoop up the child under your arm and break into a full sprint, shouting at the top of your lungs for their parents."
"\n\nSneezle's eyes widen in surprise, his usual sarcasm momentarily replaced by genuine astonishment. 'Well, color me impressed. The hero we didn't know we needed.'"
"\n\nYour shout echoes through the area, and the child's startled cries soon turn into laughter as they enjoy the exhilarating ride. You sprint across the field, your determination driving you forward."
"\n\nSneezle's lips twitch into an amused smile, shouting out to you as you run around, 'Well, well, looks like someone's got a need for speed.'"
"\n\nThe child's parents spot you from a distance and rush over, their faces a mixture of concern and relief. You gently set the child down, allowing them to reunite with their family."
"\n\nSneezle claps you on the back, an impressed grin on his face. 'You certainly know how to make an entrance.'"
"\n\nAs the family shares their gratitude, you and Sneezle exchange a satisfied nod. The date continues on a high note as you both enjoy the baseball game and the memorable moment you created.",
                outcome=True
            ),
            'response72': Response(
                dialogue_id=dialogues_list[11].id, 
                goblin_id=blort.id, 
                response=
                "With a mischievous glint in your eye, you decide to play a lighthearted prank on Blort. You run up to the child and pretend to be their parent, hamming it up for comedic effect."
"\n\nBlort blinks in surprise, his shy demeanor momentarily thrown off by the unexpected situation. 'Oh, um, I wasn't expecting that. You have a kid?'"
"\n\nYou put on an exaggerated show, complete with dramatic gestures and a funny voice. The child giggles at your antics, clearly enjoying the spectacle."
"\n\nBlort's lips twitch into an amused smile, his bashful demeanor giving way to amusement. 'Well, I certainly wasn't expecting this. At least your kid seems nice!'"
"\n\nAs the child's real parent arrives, you drop the act and share a wink with Blort, revealing your prank. He chuckles and shakes his head in good-natured amusement."
"\n\nBlort pats you on the shoulder, a nervouse grin on his face. 'You really fooled me, huh? I was uhh, sure surprised there for a second.' The rest of the date proceeds a little awkwardly as Blort seems nervouse as to what you'll do next.",
                outcome=False
            ),
            'response73': Response(
                dialogue_id=dialogues_list[12].id, 
                goblin_id=blort.id, 
                response=
                "Your decision takes a disturbing turn as you choose to rob the child, an action that goes against Blort's gentle nature. Ignoring Blort's shock, you approach the child with intentions of taking their belongings, casting a shadow over the date."
"\n\nBlort's eyes widen in disbelief and concern, his kind-hearted personality clearly rattled. 'Hey, wait, that's really not okay.'"
"\n\nYou proceed with your unsettling plan, attempting to take something from the child. The child cries out, and their parent is alerted to the situation."
"\n\nBlort's voice is firm, his concern evident. 'We can't do this, it's not right.'"
"\n\nThe child's parent arrives, their face a mix of anger and concern as they confront the situation. Blort steps forward, his tone serious, 'I'm sorry, this was just a misunderstanding.' You realize he is trying to cover for you."
"\n\nAs you're confronted by the child's parent, you come to realize the gravity of your actions. Blort's disapproval and disappointment serve as a reminder that your choices have consequences, casting a somber tone over the rest of the date.",
                outcome=False
            ),
            'response74': Response(
                dialogue_id=dialogues_list[13].id, 
                goblin_id=blort.id, 
                response=
                "With a compassionate and resourceful instinct, you decide to help the child by quickly grabbing a thin strip of bark and coiling it into a makeshift cone. Holding it up to your mouth, you let out a series of gentle calls to attract the attention of their parents."
"\n\nBlort watches your actions with a soft smile, his appreciation for your kind-hearted approach evident. 'That's really clever of you.'"
"\n\nThe child's cries pause as they listen to the unusual sound. They look at you with curiosity, and you continue your improvised bird-like calls, creating a comforting and familiar atmosphere."
"\n\nBlort chuckles softly, his voice warm. 'You've got quite the knack for creative solutions.'"
"\n\nJust as you're about to give it another try, the child's parent arrives, following the sound of your calls. They express their gratitude for your effort, and Blort nods in approval."
"\n\nBlort pats you on the back with a genuine smile. 'You really made a difference here.' The date continues on a positive note as you all enjoy the baseball game and the sense of unity you've fostered.",
                outcome=True
            ),
            'response75': Response(
                dialogue_id=dialogues_list[14].id, 
                goblin_id=blort.id, 
                response=
                "In a moment of unease, you decide to take cautious action. Ignoring the child's cries, you discreetly move away, wanting to avoid any potential danger or complications."
"\n\nBlort watches your retreating figure with a mix of surprise and concern, his caring nature evident in his response. 'Hey, are you okay?'"
"\n\nYou maintain your distance from the child, focusing solely on the baseball game as if the situation hadn't occurred."
"\n\nBlort's voice is gentle as he approaches you. 'I hope everything's alright. I'm going to go help the child find their parents. I'll be right back, okay?'"
"\n\nEventually the child's parent arrive and attend to the situation; Blort returns to your side, offering you a supportive smile."
"\n\nBlort's reassuring presence helps ease your nerves, but you can't help but feel that Blort pities you a bit.",
                outcome=False
            ),
            'response76': Response(
                dialogue_id=dialogues_list[15].id, 
                goblin_id=blort.id, 
                response=
                "With a calm and reassuring demeanor, you decide to take charge of the situation. Kneeling down beside the child, you offer a comforting smile and gently pat their shoulder. 'Don't worry, little one. We're here to help you find your parents. They're probably looking for you too.'"
"\n\nBlort watches your actions with a warm smile, his kind-hearted nature in sync with your reassuring approach. 'You're really good with kids. I'll keep that in mind.'"
"\n\nWith a nod to Blort, you take the child's hand, and together, the three of you begin searching for their parents. Blort joins in with a sense of determination, his caring presence a source of comfort."
"\n\nBlort spots the child's parents first and points them out with a pleased grin. 'Looks like we found them!'"
"\n\nThe child's parents rush over with a mix of relief and gratitude. You and Blort exchange a satisfied glance, proud of your combined efforts."
"\n\nBlort's voice is warm as he addresses the parents. 'Glad we could help reunite your family.' The date continues on a positive note as you all enjoy the baseball game. You can't help but notice Blort seems to be looking at you differently.",
                outcome=True
            ),
            'response77': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=blort.id, 
                response=
                "Your empathetic side takes over as you decide to bring a smile to the child's face. You spot a nearby bone from a past goblin baseball game and pick it up. With a kind smile, you offer it to the child and suggest, 'Hey there, little one. How about we have a pretend game of baseball while we wait for your parents?'"
"\n\nBlort watches your thoughtful gesture with an appreciative grin, his own compassionate nature resonating with your actions. 'That's really sweet of you.'"
"\n\nThe child's eyes light up as they accept the bone, and you show them how to 'swing' it like a bat. Soon, the three of you are engaged in an imaginative game of baseball, laughter filling the air."
"\n\nBlort chuckles softly, his voice warm. 'You've got a knack for bringing joy to others.'"
"\n\nThe child's parents arrive, a mix of relief and gratitude on their faces. Blort steps forward with a warm smile. 'We kept your child entertained while we waited.'"
"\n\nBlort's presence has truly made a difference, and you share a nod of camaraderie with him.",
                outcome=True
            ),
            'response78': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=blort.id, 
                response=
                "In a surprising turn, you decide to completely ignore the child and focus solely on the baseball game, determined not to let the situation disrupt your enjoyment."
"\n\nBlort's eyes widen in surprise, his compassionate nature clearly taken aback by your lack of action. 'Oh, um, do you not see the kid over there?'"
"\n\nYou remain engrossed in the game, seemingly unfazed by the child's cries as if they don't exist."
"\n\nBlort's voice is hesitant as he approaches you. 'I understand wanting to enjoy the game, but maybe we should still try to help the child?'"
"\n\nAs the child's parent arrives and attends to the situation, Blort maintains a respectful distance while offering a sympathetic smile."
"\n\nDespite your choice, Blort's gentle presence continues to shine through, and the two of you resume the baseball game, even if your approach has introduced an undercurrent of tension.",
                outcome=False
            ),
            'response79': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=blort.id, 
                response=
                "In a moment of genuine concern, you find yourself convinced of an unusual notion. Turning to Blort with a serious expression, you share your worries, 'Blort, I can't shake off this feeling. This child's presence feels like a bad omen. We need to help them find their parents soon, or I fear this date might be cursed.'"
"\n\nBlort's eyes widen in surprise, his gentle nature clearly taken aback by your sincerity. 'Oh, um, that's a bit... intense.'"
"\n\nYou share your conviction with Blort, expressing your concerns about the child's impact on the date's outcome."
"\n\nBlort's voice is soothing as he responds, 'I appreciate your concern, but let's not jump to conclusions just yet.'"
"\n\nAs you and Blort assist the child in their search for their parents, Blort's presence and reassurance help calm your unease. The child's parents are eventually found, and you share a nod of relief with Blort."
"\n\nBlort's smile is warm as he addresses you. 'It's good to care, but let's remember that we create our own destinies.' The date continues on a positive note as you all enjoy the baseball game and the sense of unity you've fostered.",
                outcome=True
            ),
            'response80': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=blort.id, 
                response=
                "Curiosity getting the better of you, you decide to engage the child in conversation. Kneeling down beside them, you ask with a gentle smile, 'Hey there, little one. Can you tell us how you got separated from your parents? We want to make sure you're back with them.'"
"\n\nBlort watches your approach with a soft smile, his kind-hearted nature in sync with your caring actions. 'That's thoughtful of you.'"
"\n\nThe child sniffs and wipes their tears, looking up at you with wide eyes. 'I was watching the game with them, and then I saw a shiny beetle and followed it. When I looked around, they were gone.'"
"\n\nBlort approaches the child and kneels gently, 'Well, that's quite the adventurous beetle chase.' He chuckles and ruffles the child's hair."
"\n\nYou nod in understanding and reassure the child that their parents are likely looking for them as well. Together with Blort, you continue to search for the parents, your combined efforts filling the air with a sense of unity."
"\n\nAs you reunite the family, Blort's smile is approving. 'Glad we could help bring this family back together.' The date continues on, and Blort seems to appreciate your kindness.",
                outcome=True
            ),
            'response81': Response(
                dialogue_id=dialogues_list[10].id, 
                goblin_id=grimble.id, 
                response=
                "With a mischievous glint in your eye, you decide to have a little fun with Grimble. You run up to the child and pretend to be their parent, putting on an exaggerated and humorous performance for comedic effect."
"\n\nGrimble raises an eyebrow in surprise, clearly caught off guard by your unexpected action. 'Well, I certainly didn't expect you to be a parent!'"
"\n\nYou play up the act, pretending to be an overly enthusiastic and slightly clueless parent. The child giggles at your antics, finding the situation amusing."
"\n\nGrimble chuckles softly, his tone tinged with amusement. 'I've got to hand it to you, I really believed you for a second.'"
"\n\nAs the child's real parent arrives, you drop the act and share a wink with Grimble. He bursts into laughter, shaking his head in amusement."
"\n\nGrimble gives you a playful nudge. 'You've got quite the sense of humor. I'm sure glad we could entertain the child for a spell.' The rest of the date proceeds with a lighthearted energy as you both enjoy the baseball game and the shared moment of amusement.",  
                outcome=True
            ),
            'response82': Response(
                dialogue_id=dialogues_list[11].id, 
                goblin_id=grimble.id, 
                response=
                "In a shocking and disturbing choice, you decide to take advantage of the situation. Ignoring Grimble's surprised expression, you approach the child and begin pilfering through their possessions."
"\n\nGrimble's eyes widen in disbelief and concern, his normally boisterous demeanor replaced with a serious and disapproving expression. 'Hey, wait, what exactly do you think you are doing?'"
"\n\nYou proceed with your unsettling plan, claiming money and treats from the child. They cry out in confusion and alarm."
"\n\nGrimble's voice is stern and authoritative as he intervenes. 'Stop right there! We're not doing this.'"
"\n\nThe child's parent arrives, their face a mix of anger and concern as they witness the situation. Grimble stands firm protective nature evident as he addresses the parent."
"\n\nAs you're confronted by the child's parent, you realize the gravity of your actions. Grimble's disappointment and disapproval serve as a reminder that your choices have consequences, casting a somber and tense atmosphere over the rest of the date.",
                outcome=False
            ),
            'response83': Response(
                dialogue_id=dialogues_list[12].id, 
                goblin_id=grimble.id, 
                response=
                "With a quick and clever instinct, you decide to help the child by grabbing a thin strip of bark and coiling it into an improvised cone. Holding it to your mouth, you emit a series of high-pitched calls, hoping to attract the attention of their parents."
"\n\nGrimble observes your actions with a nod of approval, recognizing your resourcefulness. 'Good thinking.'"
"\n\nThe child's cries momentarily subside as they listen to the unique sound. They cast a curious glance in your direction, clearly intrigued by your efforts."
"\n\nGrimble's tone is supportive. 'Let's hope this helps bring their parents back.'"
"\n\nJust as you're about to attempt another call, the child's parent arrives, drawn by the sound you've produced. They express their gratitude, and Grimble offers a nod of acknowledgment."
"\n\nYour efforts have proven successful, and you share a nod of camaraderie with Grimble. The date proceeds on a positive note as you both enjoy the baseball game and the sense of unity you've fostered.",
                outcome=True
            ),
            'response84': Response(
                dialogue_id=dialogues_list[13].id, 
                goblin_id=grimble.id, 
                response=
                "Feeling a sense of unease, you decide to take cautious action. Ignoring the child's cries, you quietly and discreetly move away, choosing to distance yourself from the situation."
"\n\nGrimble observes your retreat with a raised eyebrow, his curiosity piqued by your unexpected behavior. 'Everything alright?'"
"\n\nYou remain at a distance from the child, attempting to focus solely on the baseball game and act as though the situation didn't occur."
"\n\nGrimble's voice is gentle as he approaches you. 'If something's bothering you, you can always talk about it.'"
"\n\nAs the child's parent arrives and addresses the situation, Grimble stays by your side, offering a supportive presence."
"\n\nGrimble's companionship helps ease your nerves, and the two of you continue to enjoy the baseball game despite the distraction caused by the earlier events.",
                outcome=False
            ),
            'response85': Response(
                dialogue_id=dialogues_list[14].id, 
                goblin_id=grimble.id, 
                response=
                "With a reassuring and optimistic demeanor, you take charge of the situation. Kneeling down beside the child, you offer a comforting smile and gently assure them, 'Don't worry, little one. We're here to help you find your parents. They're probably looking for you too.'"
"\n\nGrimble watches your approach with a nod of approval, recognizing your caring and confident nature. 'That's the spirit.'"
"\n\nWith a nod to Grimble, you take the child's hand, and together, the three of you embark on a mission to search for their parents. Grimble joins in with a sense of purpose."
"\n\nGrimble spots the child's parents first and points them out with a pleased grin. 'Looks like we're making progress.'"
"\n\nThe child's parents rush over with relief and gratitude. You and Grimble exchange satisfied glances, proud of your teamwork and shared efforts."
"\n\nGrimble's tone is approving as he addresses the parents. 'We're glad we could help reunite your family.' The date continues with a positive energy as you all enjoy the baseball game and the sense of camaraderie you've established.",
                outcome=True
            ),
            'response86': Response(
                dialogue_id=dialogues_list[15].id, 
                goblin_id=grimble.id, 
                response=
                "Empathy guiding your actions, you decide to lift the child's spirits. Extending a kind smile, you offer them a bone you've found nearby and ask in a friendly tone, 'Hey there, how about a little game while we wait for your parents? We can pass the time together.'"
"\n\nGrimble's eyes shine with approval, his genuine kindness echoing your gesture. 'That's a lovely idea.'"
"\n\nThe child's tearful gaze shifts to the bone you've given them, curiosity mingling with gratitude. They nod shyly, intrigued by the prospect."
"\n\nGrimble's enthusiasm is infectious. 'Alright, let's make the best out of this wait! What sort of game would you like to play?'"
"\n\nWith the help of Grimble's creativity and your engaging presence, the three of you embark on a lighthearted adventure, turning a potentially distressing moment into a delightful memory."
"\n\nAs the child's parents arrive and the family is reunited, Grimble's smile reflects the contentment in his heart. 'See, we managed to make their waiting time enjoyable.' The date continues on an uplifting note, the baseball game enhanced by the camaraderie you've fostered.",
                outcome=True
            ),
            'response87': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=grimble.id, 
                response=
                "In an unexpected turn, you choose to ignore the child's distress and focus solely on the baseball game, determined not to let anything disrupt your enjoyment."
"\n\nGrimble raises an eyebrow in surprise, his concern evident as he speaks up. 'Hey, I get wanting to enjoy the game, but we can't just ignore a child in need.'"
"\n\nDespite your decision, Grimble's caring nature takes over. He approaches the child and gently addresses them, 'Hey, are you okay? Don't worry, we'll help you find your parents.'"
"\n\nYou continue to ignore the child, and by extension Grimble."
"\n\nGrimble's tone is gentle as he talks to the child. 'Let's look around together. We'll make sure you're back with your family.'"
"\n\nAs the child's parent arrives and addresses the situation, Grimble remains by their side, offering an uneasy glare."
"\n\nDespite your choice, Grimble's compassion shines through, and you share the experience of the baseball game, even if your approach has introduced a hint of tension.",
                outcome=False
            ),
            'response88': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=grimble.id, 
                response=
                "In a moment of seriousness, you find yourself unusually superstitious. Turning to Grimble with a grave expression, you share your concern, 'Grimble, call it a hunch, but I can't shake this feeling. Something about this child... it's like a dark cloud hanging over us. We should find their parents quickly, or who knows what might happen.'"
"\n\nGrimble's eyes widen in surprise, his typically carefree demeanor momentarily giving way to contemplation. 'Of course. We should help this child and put your mind at ease.'"
"\n\nYou continue to express your unease to Grimble, explaining your fears about the potential consequences."
"\n\nGrimble's response is measured. 'Let's not take any chances then.'"
"\n\nAs you and Grimble join forces to assist the child in their search for their parents, Grimble's presence serves as a steadying influence. Eventually, the child's parents are located, and you share a nod of reassurance with Grimble."
"\n\nGrimble's tone is thoughtful as he speaks. 'It's good to trust your instincts sometimes.' The date continues on a more cautious note as you both enjoy the baseball game and the unity you've established.",
                outcome=True
            ),
            'response89': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=grimble.id, 
                response=
                "Driven by curiosity, you decide to dive into conversation with the child. Gently crouching down beside them, you adopt a warm and compassionate tone, 'Hey there, little wanderer. What's the story behind this grand adventure? How did you end up separated from your folks?'"
"\n\nGrimble watches your approach with a grin of approval, his eyes reflecting an appreciative nod. 'I see where you're going with this.'"
"\n\nThe child sniffs, their teary eyes meeting yours. With a mixture of trust and hesitation, they begin to recount, 'We were all watching the thrilling game together. I got mesmerized by a dazzling dragonfly and couldn't resist chasing it. When I turned back, they were like... poof! Gone!'"
"\n\nGrimble's laughter dances in the air, his voice resonating with genuine amusement. 'A dragonfly, huh? Those tricky little daredevils.'"
"\n\nLeaning in, you listen closely to the child's tale, interjecting with understanding nods and soothing reassurances. Together with Grimble, you embark on a quest to reunite the child with their parents, your unity becoming a heartening beacon."
"\n\nAs the family is finally reunited, Grimble's eyes twinkle with joy. 'Look at that, our very own happy ending.' The date continues on an uplifting note as you all bask in the magic of the baseball game and the beautiful connection you've forged.",
                outcome=True
            ),
            'response90': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=grimble.id, 
                response=
                "With a burst of determination, you choose to take immediate action. Scooping up the child under your arm, you start sprinting across the area, your voice ringing out in urgent shouts as you call for their parents."
"\n\nGrimble's eyes widen in surprise and amusement, his initial shock quickly turning into a hearty chuckle. 'Well, I guess we're running now.'"
"\n\nThe child clings to you, a mixture of surprise and exhilaration in their eyes as the wind whizzes past. Their laughter mingles with your shouts, a chorus of voices echoing through the air."
"\n\nGrimble's laughter joins in the symphony, his voice infused with the thrill of the moment. 'You've turned this into quite the adventure!'"
"\n\nYour sprint comes to an end as the child's parents rush over with a mixture of relief and amusement on their faces. Grimble is there to welcome them with a grin, clearly enjoying the energetic scene."
"\n\nGrimble's voice is filled with mirth as he addresses the parents. 'I think we've managed to find you faster than we expected.' The date continues on a vibrant note as you all share a lively moment of unity and enjoyment.",
                outcome=True
            ),
            'response91': Response(
                dialogue_id=dialogues_list[10].id, 
                goblin_id=zongo.id, 
                response=
                "With a mischievous glint in your eye, you decide to pull a prank on Zongo. Striding up to the child, you slip into a role that is far from your usual self – that of their parent. You play your part with gusto, amplifying the theatrics while stealing a glance at Zongo, who watches with a mix of confusion and mild annoyance."
"\n\nZongo's brow furrows, his typically confident demeanor replaced by a hint of bafflement. 'What in the world are you up to?'"
"\n\nEmbracing the act, you emphasize your role with exaggerated gestures and a lively tone, intent on keeping Zongo guessing."
"\n\nZongo's voice carries a touch of exasperation. 'Alright, I'll bite. What's with this whole charade? You clearly are not their parent.'"
"\n\nAs the child's real parent arrives and you reveal the prank, Zongo lets out an exasperated sigh, his irritation thinly veiled."
"\n\nZongo's tone is unimpressed as he addresses you. 'You certainly have a knack for the unexpected, I'll give you that.' The date continues, though Zongo's mood might have been slightly dampened by the prank.",  
                outcome=False
            ),
            'response92': Response(
                dialogue_id=dialogues_list[11].id, 
                goblin_id=zongo.id, 
                response=
                "In a shockingly misguided choice, you entertain the idea of exploiting the child for personal gain. Pushing aside your usual persona, you approach the child with an unsettling intent, a decision that catches Zongo off guard."
"\n\nZongo's voice carries a mix of astonishment and disapproval. 'Whoa, hold on a second. What in the world are you even thinking?'"
"\n\nBefore you can fully act on your decision, a wave of realization washes over you, prompted by Zongo's appalled reaction. His disapproval weighs heavily on your conscience."
"\n\nZongo's tone is firm as he condemns your choice. 'This is not the kind of story we're going to be a part of.'"
"\n\nAs the child's real parent arrives, concern etched on their face, Zongo's gaze shifts between you and the unfolding situation. Relief washes over him as the family is reunited before the baseball game resumes."
"\n\nZongo's voice is laced with a mix of relief and malice. 'Let's stick to the game AND better choices, shall we?' The date continues with a renewed focus on the baseball game, the incident serving as a reminder of the importance of integrity.",
                outcome=False
            ),
            'response93': Response(
                dialogue_id=dialogues_list[12].id, 
                goblin_id=zongo.id, 
                response=
                "Thinking on your feet, you opt for a creative solution to aid the child. Swiftly grabbing a thin strip of bark, you expertly coil it into a cone shape. As you prepare to blow into it, Zongo steps in, his eyes gleaming with mischief. With a flick of his fingers, he weaves a touch of thaumaturgy magic into the bark, amplifying the sound into a resonating call for the child's parents."
"\n\nZongo's playful grin is paired with a subtle nod of approval. 'Now that's what I call thinking outside the box.'"
"\n\nThe child's eyes widen in wonder as the amplified sound captures their attention, instilling a sense of hope."
"\n\nZongo's voice carries a touch of satisfaction. 'Just a bit of magical enhancement to get our point across.'"
"\n\nAs the child's parents hurry over, their relief is mirrored by Zongo's appreciative nod towards you."
"\n\nZongo's tone is laced with camaraderie. 'Great job, partner. We made quite the team there.' The rest of the date continues with a sense of achievement, both of you enjoying the baseball game and the collaborative magic you've conjured.",
                outcome=True
            ),
            'response94': Response(
                dialogue_id=dialogues_list[13].id, 
                goblin_id=zongo.id, 
                response=
                "In a moment of trepidation, you find yourself succumbing to your nerves. Concerned that the child might be a potential trap, you opt for a discreet retreat, quietly fading into the background while ignoring the situation, hopeful that they'll eventually leave on their own."
"\n\nZongo's expression shifts as an idea forms in his mind. With a mischievous grin, he extends his hand toward you, casting an invisibility spell to shroud you from sight. Simultaneously, he weaves a touch of his thaumaturgy magic into the air, creating a resonating, booming voice that calls out for the child's parents."
"\n\nZongo's voice echoes heavy sarcasm and judgement. 'Well, if we're going for stealth, might as well go all out.'"
"\n\nThe child looks around, startled by the magical voice, while Zongo's suppressed chuckle is barely audible."
"\n\nZongo's voice carries a mix of mischief and amusement. 'I've always wanted to be a magical announcer.'"
"\n\nAs the child's parents rush over, finding their lost child, Zongo releases the invisibility spell with a flick of his fingers and flashes you a satisfied grin."
"\n\nZongo's tone is disapproving, 'Well, I see you have a knack for disappearing when things get tricky.' The date carries on, though an air of somberness has crept in, the baseball game becoming a backdrop to an encounter that has subtly shifted the dynamics between you and Zongo.",
                outcome=False
            ),
            'response95': Response(
                dialogue_id=dialogues_list[14].id, 
                goblin_id=zongo.id, 
                response=
                "Radiating unshakable confidence, you take charge of the situation. Flashing a self-assured grin, you crouch down beside the child and deliver your reassurance with a touch of flair, 'Fear not, youngster. With me around, finding your parents is as good as done. They must be frantically searching for the coolest kid in town.'"
"\n\nZongo watches your approach with a mixture of amusement and a raised eyebrow. 'Quite the confident speech there.'"
"\n\nThe child's eyes widen, a mixture of awe and hope in their gaze as they nod in agreement."
"\n\nZongo's voice is laden with wry amusement. 'Your confidence knows no bounds, huh?'"
"\n\nAs you, Zongo, and the child embark on your search, your collective determination pays off when the family is joyfully reunited."
"\n\nZongo's tone carries a hint of begrudging acknowledgment. 'Looks like your bold approach paid off.' The date continues with an air of victorious energy, the baseball game even more invigorating thanks to the confident camaraderie you've ignited.",
                outcome=True
            ),
            'response96': Response(
                dialogue_id=dialogues_list[15].id, 
                goblin_id=zongo.id, 
                response=
                "Recognizing the child's need for a lift, you swiftly take action. Digging into your bag, you retrieve a bone and offer it to the child with a warm smile. 'Hey there, sport. How about we have a little game to pass the time? And guess what? My partner here knows a thing or two about making things exciting.'"
"\n\nZongo's eyes gleam with approval, his focus shifting to you and your thoughtful approach. 'A thoughtful gesture indeed.'"
"\n\nThe child's eyes widen with curiosity as they eagerly accept the bone, intrigued by what's to come."
"Zongo's voice holds a touch of admiration, 'You know what? I've got something up my sleeve to make this even more unforgettable.' Zongo conjures a playful illusion, captivating the child's attention."
"\n\nZongo's tone carries a note of appreciation. 'You've got a knack for brightening their day.' The date continues with a spirited energy, the baseball game paired with the shared enjoyment you've kindled.",
                outcome=True
            ),
            'response97': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=zongo.id, 
                response=
                "Opting for an unorthodox approach, you purposely overlook the child, throwing yourself entirely into the baseball game. Your fixation on the match remains unbroken, and Zongo's eyes spark with mischief and determination."
"\n\nZongo's voice resonates with a playful challenge. 'Ah, the oblivious path, I see. Let's see how this unfolds.'"
"\n\nWhile your attention remains committed to the game, Zongo seizes the opportunity to wield his magical prowess. He conjures an enchanting illusion that captivates the child's interest and leads them closer to their waiting parents."
"\n\nZongo's tone carries a self-satisfied note. 'Magic, my friend, can be quite the guiding star.'"
"\n\nAs the child's parents locate them through Zongo's magical diversion, he receives their gratitude with a nod of acknowledgement."
"\n\nZongo's voice rings with indifference as he addresses you. 'Well, looks like you were too focused to notice, huh?' The date continues with an air of completion, Zongo's actions taking center stage in an experience that has subtly shifted the balance of attention.",
                outcome=False
            ),
            'response98': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=zongo.id, 
                response=
                "Amidst the unfolding events, an irrational fear takes hold of you. Convinced that the child's presence is an ill omen, you feel a growing urgency for their parents to be found, lest the date be cursed."
"\n\nZongo's reaction is one of clear disbelief. 'A cursed date? Seriously?'"
"\n\nAs your apprehension mounts, Zongo's voice carries an undertone of skepticism. 'You do realize this is just a child, right? I doubt they're a harbinger of doom.'"
"\n\nYour attempts to locate the child's parents intensify, your every action driven by the unfounded belief of impending misfortune."
"\n\nZongo's tone is marked by a mixture of amusement and frustration. 'I can't believe you're taking this so seriously.'"
"\n\nAs the child's parents are eventually found, Zongo exchanges a bemused glance with you, his reaction a testament to your baseless apprehension."
"\n\nZongo's voice carries a hint of incredulity. 'Well, I guess you got what you wanted—no curse in sight. I am glad we found their parents at least.' The date continues, though your unease leaves a lingering impact.",
                outcome=False
            ),
            'response99': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=zongo.id, 
                response=
                "Intrigued by the circumstances surrounding the child, you initiate a lively conversation. Your genuine curiosity leads you through a series of questions, enabling the child to share their story with you."
"\n\nZongo's occasional interjections add a layer of insight and humor to the unfolding narrative."
"\n\nAs the child's tale unravels, your empathetic engagement creates a connection between you. Moments later, the child's parents spot them, their reunion infused with gratitude."
"\n\nZongo's voice carries a note of acknowledgment. 'Nicely done. You brought them back together.' He conjures a detectives cap atop your head with a flick of his wrist and gives you a knowing smile as the game resumes.",
                outcome=True
            ),
            'response100': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=zongo.id, 
                response=
                "Without hesitation, you scoop up the child under your arm and break into a sprint, your voice echoing as you call out for their parents."
"\n\nZongo's eyes widen in disbelief. 'Are you actually...?'"
"\n\nAs you dash across the field, Zongo, seemingly amused by your boldness, casts a swift spell that enhances your speed, making you nearly blur as you race towards the child's parents."
"\n\nZongo's voice carries a touch of amusement. 'Mind the roots and rocks!'"
"\n\nThe child's parents spot you and their child, relief flooding their faces as they rush forward to reunite with their little one."
"\n\nZongo's tone reflects his amusement. 'Looks like your dramatic rescue worked out in the end.' You can't help but notice Zongo laughing to himself from time to time as he reflects on your absurd action.",
                outcome=True
            ),
        }
        responses_3 = {
            'response101': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=grubnub.id, 
                response=
                "The game's end marks a pause in the day's activities, and your date stands before you with anticipation in their eyes. Stepping closer, your intentions remain ambiguous. Yet, your actions deviate unexpectedly as you feign a kiss, only to swiftly lower their trousers in a prank."
"\n\nGrubnub's initial surprise shifts rapidly into confusion, his cheeks tinged with both embarrassment and uncertainty. He takes a cautious step back, his brow furrowing as he tries to decipher the nature of your prank."
"\n\nA heavy silence hangs between you, and you can see the hurt and sadness in Grubnub's eyes, his heart clearly wounded by the unexpected betrayal. His voice trembles slightly as he addresses you."
"\n\n'Was... was that really necessary?' he asks, his tone a mixture of hurt and disappointment. The atmosphere remains charged with a profound sense of awkwardness and regret, the prank leaving behind a palpable sense of hurt between you.",
                outcome=False
            ),
            'response102': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=grubnub.id, 
                response=
                "Your proclamation reverberates with an unsettling undertone, casting a shadow as you assert your victorious position and demand that your date pay for the amusement you've provided."
"\n\nGrubnub's expression undergoes a swift transformation, surprise giving way to discomfort as he takes a hesitant step back. His voice carries a note of unease. 'Oh, I didn't realize this was a competition.'"
"\n\nThe atmosphere turns strained, your words leaving a trail of tension in their wake. Despite the unease, you continue to press, your insistence bordering on aggression."
"\n\n'Come on, now,' you push further, a hint of coercion in your tone as you assert your dominance. 'You owe me for making this date interesting.'"
"\n\nGrubnub's discomfort deepens, and he hesitates before reluctantly complying. The air remains heavy with the uncomfortable exchange, your victory now marred by the discord that hangs in the space between you.",
                outcome=False
            ),
            'response103': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=grubnub.id, 
                response=
                "A mischievous twinkle lights up your eyes as you draw them close, your hand confidently resting on their hip as they sway low. Laughter bubbles from their lips, their warmth seeping into your embrace as you pull them snugly against you."
"\n\nAs you lean in, the air electrifies with anticipation, your lips poised as if to taste the sweetness of a kiss. But, in a playful twist, you divert your course, plucking a delicate piece of grass from their cheek and grinning as you hold it up, winking suggestively."
"\n\nGrubnub's reaction is a delightful mix of surprise and amusement. His laughter dances through the air, the sound like a sweet melody that harmonizes with the setting sun. He clears his throat playfully, voice laced with flirtatiousness. 'Well, I'll be a pigs uncle! I thought you kiss me!'"
"\n\nIn that shared moment, a potent blend of attraction and connection hangs in the air, an unspoken acknowledgment of the chemistry that's been building between you. Your actions and his response intertwine like the first notes of a secret love song, promising more to come.",
            outcome=True
            ),
            
            'response104': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=grubnub.id, 
                response=
                "With a wide, earnest grin on your face, you make your way toward your date, Grubnub. His eyes light up with a mix of surprise and happiness as you approach, clearly pleased by your presence."
        "\n\n'Hey there,' you say with a warm chuckle, 'That was quite the game, huh? Good job out there!' Your tone is genuine, and you make sure to emphasize the fun you had."
        "\n\nGrubnub's response is a genuine mixture of delight and modesty. 'Oh, uh, thanks! I, um, tried my best.' He scratches his head and looks a bit bashful."
        "\n\nThe two of you stand there for a moment, exchanging smiles and sharing a lighthearted atmosphere. It's a simple yet genuine interaction.",
                outcome=True
            ),
            'response105': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=grubnub.id, 
                response=
                "A surge of excitement pulses through your veins as you take a bold step forward, closing the distance between you and Grubnub. Your heart races as you gaze into his eyes, feeling the warmth of his presence enveloping you both."
"\n\nWith a gentle yet confident smile, you tilt your head slightly, wordlessly conveying your intentions. As you move in, his lips part in a soft gasp of surprise, but the spark of anticipation in his eyes is undeniable."
"\n\nTime seems to slow as your lips meet, the world around you fading into insignificance. The kiss is tender and full of promise, a sweet connection that ignites a fire of emotions deep within both of you."
"\n\nAs you pull away, the air is charged with an electric energy, and Grubnub's dazed yet dreamy expression mirrors your own. A soft, contented smile graces his lips, a silent affirmation of the meaningful connection you've shared.",
                outcome=True
            ),
            'response106': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=grubnub.id, 
                response=
                "With a mischievous glint in your eye, you playfully wink at Grubnub, letting out a light giggle that dances in the air. Without further ado, you start running away from him, the thrill of the chase making your heart race."
"\n\nAs you glance back, you expect to see him right behind you, caught up in the playful game. However, to your surprise, he blinks in confusion and seems momentarily unsure of what's happening. There's a brief pause, and then realization slowly dawns on him."
"\n\nA faint blush tinges his cheeks as he starts to grin, and his feet fumble into action as he clumsily begins to chase after you. His laughter joins yours, a chorus of joy as you both playfully dart around, caught in a lighthearted dance."
"\n\nThe moment is filled with shared laughter and genuine connection, a memory that will surely bring smiles to your faces for days to come.",
                outcome=True
            ),
            'response107': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=grubnub.id, 
                response=
                "A sense of confidence washes over you as you stand your ground, convinced that the initiative should come from your date. You've invited them here, after all, and you're eager to see if they're equally interested in taking things to the next level."
"\n\nYour demeanor is calm and composed as you wait, watching their every move with an air of expectation. Grubnub, however, seems momentarily uncertain, his gaze flickering between you and the surroundings. There's a brief pause before a small smile tugs at his lips."
"\n\nAs he steps closer, his expression shifts from uncertainty to determination, his heart shining through his eyes. With a soft yet sincere grin, he closes the gap between you, his hand reaching out to gently cup your cheek. It turns out he has some confidence in him after all."
"\n\nIn that moment, time seems to slow as his lips meet yours, a gentle yet meaningful kiss that sends shivers down your spine. The quiet intimacy of the gesture speaks volumes, a silent declaration of his feelings."
"\n\nAs the kiss ends, a warmth settles in the air, and you find yourselves sharing a tender moment that speaks of the connection you've forged. It's a memory that you'll carry with you, a testament to the beauty of allowing things to unfold naturally.",
                outcome=True
            ),
            'response108': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=grubnub.id, 
                response=
                "With a gentle smile, you decide to heed the age-old superstition and opt for a friendly hug instead of a kiss. After all, you don't want to tempt fate, and you want to ensure that your connection remains positive and free from any potential bad luck."
"\n\nAs you open your arms, Grubnub's gaze meets yours, and he returns your smile with a genuine one of his own. He steps forward, his arms encircling you in a warm embrace that feels surprisingly comforting and natural."
"\n\nThe hug lingers for a moment, a shared moment of closeness that speaks volumes without the need for words. It's a gesture of friendship and connection, a testament to the meaningful time you've spent together."
"\n\nAs you pull away, his gaze remains warm, and you both share a final smile before parting ways. While the romantic tension may not have escalated, the memory of your date's kindness and the friendly hug will remain a cherished part of your journey.",
                outcome=True
            ),
            'response109': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=grubnub.id, 
                response=
                "Curiosity piqued, you decide to test the waters and see how Grubnub reacts if you make a bold move. Without hesitation, you move closer to him and reach out, your fingers wrapping around his hand in a gentle yet confident grip."
"\n\nHis eyes widen in surprise as your touch registers, and for a moment, you sense a fleeting hint of uncertainty in his gaze. However, that uncertainty quickly gives way to a warm and genuine smile that lights up his features."
"\n\nSeemingly unfazed by the unexpected gesture, Grubnub's fingers instinctively intertwine with yours, his touch surprisingly gentle and reassuring. The connection feels natural and comfortable, an unspoken understanding passing between you."
"\n\nAs you stand hand in hand, a sense of camaraderie and connection envelops you both, creating a moment of quiet intimacy amidst the bustling surroundings. It's a simple yet meaningful gesture that speaks volumes about the potential for something more.",
                outcome=True
            ),
            'response110': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=grubnub.id, 
                response=
                "Driven by a surge of confidence and desire, you act on your instincts without hesitation. Closing the distance between you and Grubnub, you wrap your arms around him in a tight yet gentle embrace, drawing him close to you."
"\n\nHis initial surprise is quickly replaced by a mixture of anticipation and understanding, his body responding to your unspoken invitation. There's a subtle shift in his demeanor as he holds you in return, a silent acknowledgment of the shared connection."
"\n\nGrubnub takes the initiative and leans in, his lips meeting yours in a gentle yet meaningful kiss. The touch is soft and tender, a silent declaration of his affection."
"\n\nAs the kiss deepens, you feel a surge of warmth and connection, the intensity of the moment encapsulating the emotions swirling between you. In the midst of the shared intimacy, he pulls back slightly, his lips brushing against your ear as he whispers something that, despite its simplicity, carries a potent charm."
"\n\n'You... make my heart go all goblin-y,' he murmurs, his words accompanied by a playful nibble on your earlobe. His confession is accompanied by a nervous yet genuine chuckle, a testament to his endearing nature."
"\n\nThe memory of that whispered sentiment lingers in the air, adding a touch of whimsy to the romantic atmosphere. It's a moment that encapsulates the unique connection you share, reminding you of the beauty in embracing the authentic and heartfelt.",
                outcome=True
            ),
            'response111': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=sneezle.id, 
                response=
                "Embracing your mischievous side, you move in closer to Sneezle as if you're about to initiate a kiss. His eyes widen slightly, his surprise evident as he anticipates the romantic gesture."
"\n\nHowever, just as the tension mounts and the moment seems ripe for a kiss, you execute a swift and unexpected maneuver. Instead of kissing him, you playfully tug at his waistband, causing his pants to sag for a split second before they snap back into place."
"\n\nSneezle's reaction is a mix of amusement and disbelief, his laughter bubbling up as he grins at you. 'Oh, you sly trickster!' he exclaims, his tone a blend of mock indignation and genuine enjoyment."
"\n\nThe playful banter between you and Sneezle fills the air with a lighthearted energy, a reminder of the unique dynamic you share. It's a moment that showcases your ability to keep each other on your toes, sparking a connection that thrives on shared laughter and camaraderie.",  
                outcome=True
            ),
            'response112': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=sneezle.id, 
                response=
                "With a cold, calculated demeanor, you assert yourself as the victor and demand payment from your date for the entertainment you've provided. Your words carry a sense of entitlement and self-assuredness that leaves a chilling impact on the atmosphere."
"\n\nSneezle's initial reaction is a mixture of surprise and disbelief, his features contorting into a mixture of confusion and unease. 'Wait, are you serious? You're actually... expecting me to pay?'"
"\n\nAs your words sink in, the playful banter that once defined your interaction is replaced by a palpable tension. Sneezle's expression hardens, his sarcastic smile fading as his eyes narrow with a touch of indignation."
"\n\n'Look, I thought we were just having a good time here,' he retorts, his voice tinged with a combination of irritation and disappointment. Without waiting for a response, he turns on his heels and storms off, leaving behind a sense of unease and regret."
"\n\nAs you watch Sneezle's departing figure, you're struck by the realization that you have probably ruined your relationship with Sneezle.",
                outcome=True
            ),
            'response113': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=sneezle.id, 
                response=
                "A mischievous glint in your eye, you sweep Sneezle off his feet, your hand confidently finding his hip as you lower him in a dramatic dip. His surprised laughter fills the air, blending seamlessly with the playful atmosphere that surrounds you both."
"\n\nAs you hold Sneezle in the dramatic pose, you can't help but notice a small piece of grass stuck to his cheek. With a playful grin, you move in as if for a kiss, your lips mere inches from his."
"\n\nThe tension between you and Sneezle escalates, the anticipation tangible as you close the distance between your lips. But just as he leans in, you pluck the stray piece of grass from his cheek with a swift and deliberate motion."
"\n\nSneezle's laughter fills the air, a mixture of amusement and surprise, his eyes crinkling with genuine joy. 'Oh, you smooth operator, you!' he exclaims, his tone a delightful blend of mock awe and heartfelt appreciation."
"\n\nThe shared moment is one of playful intimacy, a testament to the connection you share. As Sneezle rises back to his feet, the lingering energy of the dip and the near-kiss hangs between you, a reminder of the shared laughter and flirtatious tension that will define this date.",
                outcome=True
            ),
            'response114': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=sneezle.id, 
                response=
                "With a friendly smile, you approach Sneezle and offer your congratulations on the game. You express how much fun you had, genuinely enjoying the time spent together. However, you admit that you're feeling a bit nervous and unsure about what comes next."
"\n\nSneezle's response is a playful twinkle in his eyes, his tone light and teasing. 'Oh, don't tell me you're getting cold feet now? After all that grand adventure on the field?'"
"\n\nHis good-natured ribbing is evident, and he chuckles softly as he continues. 'Don't worry. No pressure here. We're just a couple of goblins having a good time, right? If you're not feeling bold, that's perfectly fine.'"
"\n\nHis words carry a sense of camaraderie, an assurance that there's no need to rush into anything. As you share a laugh with Sneezle, you're reminded of the easygoing nature of your connection, a reminder that the journey is just as enjoyable as the destination.",
                outcome=True
            ),
            'response115': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=sneezle.id, 
                response=
                "Filled with a sense of excitement and connection, you're certain that you and Sneezle have had a wonderful time together. The playful banter and shared moments have built a strong foundation of camaraderie and attraction."
"\n\nBuoyed by this confidence, you take the lead, closing the distance between you and Sneezle. With a gentle yet assured gesture, you cup his cheek, your thumb brushing against his skin as you tilt his face toward yours. There's a spark in his eyes, an anticipation that mirrors your own."
"\n\nWithout hesitation, you lean in, your lips meeting his in a tender yet passionate kiss. The world seems to fade away as the two of you share this intimate moment, a culmination of the chemistry that has been building between you."
"\n\nSneezle responds to your advances with eagerness, his lips moving in sync with yours as he pulls you closer. It's a kiss filled with warmth, desire, and the unspoken promise of what the future might hold."
"\n\nAs the kiss deepens and then slowly breaks, a smile tugs at the corners of Sneezle's lips. 'Now that's what I call a grand finale,' he murmurs, his voice a soft mixture of satisfaction and playfulness."
"\n\nThe lingering energy of the kiss and the connection you share fills the air, creating a moment that will remain etched in your memory as a testament to the magic of unexpected connections.",
                outcome=True
            ),
            'response116': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=sneezle.id, 
                response=
                "A mischievous twinkle lights up your eyes as you wink playfully at Sneezle. With a light giggle escaping your lips, you take off in a burst of energy, your feet carrying you away from him. The wind rushes past you, and you can't help but glance back, expecting to see Sneezle giving chase."
"\n\nYour expectations are met as you catch sight of him, his laughter ringing through the air as he playfully follows after you. With each step, the sounds of your laughter and the patter of his footsteps create a symphony of shared joy."
"\n\nThe thrill of the chase adds a layer of excitement to the moment, the two of you engaged in a lighthearted game that symbolizes the carefree spirit of your connection. Sneezle's playfulness matches your own, his laughter infectious as he runs after you."
"\n\nEventually, you slow down, allowing him to catch up, both of you breathing slightly faster from the exertion. Sneezle grins, his eyes sparkling with mirth. 'If I keep hanging out with you I'm gonna have to start doing cardio again,' he teases."
"\n\nThe playful energy lingers between you, a reminder that friendship can be just as fulfilling as romance. As you share a grin with Sneezle, you're grateful for the moments of joy and connection that have woven themselves into your time together.",
                outcome=True
            ),
            'response117': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=sneezle.id, 
                response=
                "The air is charged with anticipation as you and Sneezle share a moment of lingering silence. The energy between you is palpable, a mix of curiosity and attraction that hangs in the air."
"\n\nYou catch a mischievous glint in Sneezle's eye, and his lips curve into a playful smile. His gaze remains locked with yours, a silent challenge that speaks volumes."
"\n\nAs the seconds tick by, Sneezle's confidence grows more apparent. With a slow, deliberate motion, he leans in closer, his hand reaching out to gently brush against yours. The touch is electric, sending a thrill down your spine."
"\n\nIn that moment, the world around you seems to fade away, leaving only the two of you in a bubble of anticipation. Sneezle's lips are inches away, and you can feel his breath on your skin."
"\n\nAnd then, finally, he closes the remaining distance, his lips meeting yours in a soft, lingering kiss. It's a gesture that speaks volumes, conveying the unspoken feelings that have been building between you."
"\n\nAs the kiss ends, Sneezle pulls back slightly, his eyes locked with yours. There's a playful spark in his gaze, a silent acknowledgment of the moment you've shared. And in that instant, you know that this is just the beginning of something that holds endless possibilities.",
                outcome=True
            ),
            'response118': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=sneezle.id, 
                response=
                "With a friendly smile, you open your arms, signaling your intention for a warm embrace. Sneezle's usual playful demeanor softens as he steps forward, accepting the invitation. His arms wrap around you, and you feel a sense of kinship."
"\n\nThe hug lingers for a moment, a reminder of the enjoyable time you've spent together during your date. As you pull away, Sneezle's gaze meets yours, a faint smile still playing on his lips. 'I had a great time today,' he says, his voice carrying a note of sincerity."
"\n\nDespite the absence of a kiss, the evening has been filled with shared laughter and moments that have brought you closer. As you continue to talk and enjoy each other's company, you realize that without the romantic gesture, the connection between you and Sneezle may be moving towards friendship.",
                outcome=False
            ),
            'response119': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=sneezle.id, 
                response=
                "A mischievous thought crosses your mind as you decide to take the initiative. With a playful grin, you break into a sudden sprint and reach out to grab Sneezle's hand. His surprise is evident as his fingers intertwine with yours, and you feel a rush of excitement as you lead him in a spontaneous dance of laughter and movement."
"\n\nThe two of you spin around, your steps matching the rhythm of your shared laughter. Sneezle's eyes sparkle with amusement, and his carefree spirit seems to mirror your own. As the dance comes to an end, you release his hand, both of you slightly breathless from the unexpected burst of energy."
"\n\nSneezle lets out a chuckle, shaking his head in amusement. 'Phew! As if I hadn't been tired enough from the game' he exclaims, his tone filled with light-heartedness. 'Next time we'll have to go dancing!'"
"\n\nAs you catch your breath, you meet Sneezle's gaze and share a moment of shared joy. The impromptu dance has added a playful and memorable touch to your date, a reminder of the unexpected twists and turns that life can bring when you're in good company.",
                outcome=True
            ),
            'response120': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=sneezle.id, 
                response=
                "In a bold and confident move, you close the distance between you and Sneezle, your arms wrapping around his waist as you pull him close. His surprise is fleeting, replaced by a sense of warmth and connection as your bodies press together. The atmosphere is charged with anticipation, the air thick with unspoken desire."
"\n\nSneezle's gaze meets yours, his eyes reflecting a mixture of surprise and longing. There's a raw vulnerability in this moment, as if you've both let down your guard and allowed yourselves to be truly seen by one another."
"\n\nYou hold each other close, the space between you narrowing until there's nothing but the shared warmth of your bodies. The world around you seems to fade away, leaving only the intoxicating intimacy of this moment. The unspoken question lingers in the air, a question that requires no words."
"\n\nAs the tension builds, Sneezle's fingers find their way to the back of your neck, his touch gentle yet possessive. In that instant, you can feel his hesitation and desire battling within him. With a soft exhale, he closes the remaining distance, his lips meeting yours in a kiss that carries all the intensity of the moment."
"\n\nTime seems to stand still as your lips move together, each touch igniting a spark that grows into a flame. The world fades away, leaving only the two of you, lost in the sweet intensity of the kiss.",
                outcome=True
            ),
            'response121': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=blort.id, 
                response=
                "With a mischievous glint in your eye, you lean in towards Blort, your lips inches away from his. The anticipation hangs in the air for a moment, and just as he starts to close his eyes, you shift your focus to his waistband. In one swift motion, you tug down on his pants, revealing his undergarments."
"\n\nBlort's eyes widen in surprise, his cheeks flushing with embarrassment as he stumbles back in shock. His hands move instinctively to his pants, hurriedly pulling them back up to cover himself. He looks at you with a mix of confusion and mild annoyance, his shyness momentarily overshadowed by the unexpected turn of events."
"\n\n'Oh my!' Blort stammers, his voice a mixture of surprise and mild indignation. 'I... I would prefer you not tease me so!' He shifts uncomfortably on his feet, his cheeks still tinged with pink."
"\n\nThe atmosphere between you takes on a slightly awkward tone, the playful prank having caught Blort off guard. As you both recover from the unexpected twist, you can't help but notice the obvious humiliation on his face.",
                outcome=False
            ),
            'response122': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=blort.id, 
                response=
                "A smug grin spreads across your face as you declare yourself the winner of your little game, your tone carrying a hint of superiority. 'Well, well, it seems I've managed to entertain you quite thoroughly,' you announce, raising an eyebrow for emphasis. 'As the victor, it's only fair that you compensate me for the delightful time I've provided.'"
"\n\nBlort's expression shifts from surprise to a mixture of confusion and disappointment. His eyes widen slightly, his soft features contorting into a pained expression. 'Oh, I... I wasn't aware there was a competition,' he mumbles, his voice tinged with a touch of sadness."
"\n\nYou can see the discomfort in Blort's demeanor, his shoulders slumping slightly as if deflated. He glances down at his feet, his shyness magnified by your demanding request. 'I suppose I must pay you,' he stammers softly. You notice his eyes begin to swell, threatening tears."
"\n\nThe atmosphere takes a somber turn, the playful mood having dissipated. Blort's reaction serves as a reminder that your actions can hurt others, and you find yourself regretting your avarice.",
                outcome=False
            ),
            'response123': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=blort.id, 
                response=
                "With a determined smile, you reach out and gently take Blort by the hip, guiding him into a dip. He blinks in surprise, clearly not expecting this playful gesture. Your arms wrap around his form, holding him close as you lean in as if going for a kiss."
"\n\nBut as you lean closer, your focus shifts to a small piece of grass stuck to his cheek. You pluck it off gently, a soft chuckle escaping you. You wink at him, your eyes meeting briefly in an awkward exchange."
"\n\nBlort's reaction is a mix of confusion and mild embarrassment. He shifts on his feet, his cheeks tinted with a light blush. 'Oh, uh, thank you,' he stammers, clearly unsure of the situation. 'I didn't realize... I mean, there was something on my face?'"
"\n\nThe moment is marked by an endearing awkwardness, the unexpected closeness leaving both of you momentarily unsure. As the tension eases, you share a nervous laugh.",
                outcome=False,
            ),
            'response124': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=blort.id, 
                response=
                "You step closer to Blort, offering a warm smile as you congratulate him on the game. His face lights up, clearly pleased by your kind words. 'Oh, thanks!' he responds, his voice carrying a mix of surprise and gratitude. 'I'm glad you had fun.'"
"\n\nHis genuine smile and appreciative demeanor create a friendly atmosphere between you. Blort seems genuinely happy with your company, and the casual conversation allows for a sense of ease to settle in."
"\n\nThis may not have been the most romantic of endings, but at least you will leave knowing you have a friend.",
                outcome=True
            ),
            'response125': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=blort.id, 
                response=
                "Feeling a sense of connection and the excitement of the moment, you decide to take the lead. Closing the gap between you and Blort, you lean in with confidence, aiming for a kiss. His wide eyes and stunned expression catch you off guard, and you can practically see the gears turning in his head."
"\n\nHowever, your advance seems to be a bit too bold for Blort, who takes a step back, clearly flustered. 'Uh, wait! I, uh...' he stammers, his cheeks flushing with embarrassment. 'I wasn't expecting...'"
"\n\nIt's clear that Blort's shy nature and unexpected reaction have created an awkward moment between you. While you were confident in your move, his response suggests that he might need more time to process the situation.",
                outcome=False
            ),
            'response126': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=blort.id, 
                response=
                "With a wink and a mischievous giggle, you decide to kick things up a notch. Playfully, you start running away from Blort, fully expecting him to chase after you. Your heart races as you hear his footsteps behind you, and the thrill of the chase adds a sense of excitement to the moment."
"\n\nHowever, as you glance back, you notice that Blort is still standing in place, a puzzled expression on his face. He seems to be taking the situation quite literally, his confusion evident in his furrowed brow. 'Wait, are we playing tag now?' he calls out, his tone a mix of uncertainty and amusement."
"\n\nIt appears that Blort has interpreted your playful gesture in an unexpectedly literal way. His response wasn't quite what you anticipated, so you decide to end the farse and reconvene with him."
"\n\n'Sorry I didn't play tag with you, I'm just a bit tired now,' Blort gives you a sorroy expression, and the two of you end your date awkwardly.",
                outcome=False
            ),
            'response127': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=blort.id, 
                response=
                "You decide to take a step back and let Blort make the next move. After all, you invited him here, so it's only fair to give him the opportunity to show his interest. You wait expectantly, hoping that he'll take the initiative and make a move."
"\n\nBlort's response is a mix of surprise and slight unease. He shifts his weight from one foot to the other, his gaze momentarily downcast. 'Oh, um, I guess that's it huh?' he stammers, his shy nature coming through. 'I hope you had fun!'"
"\n\nIt's clear that Blort is a bit caught off guard by your lack of action. Perhaps he didn't consider the dynamics of the situation in the same way you did.",
                outcome=False
            ),
            'response128': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=blort.id, 
                response=
                "As the date comes to an end, you find yourself hesitating. You remember the superstition that says it's bad luck to kiss on the first date, and you decide to err on the side of caution. With a friendly smile, you opt for a warm hug instead, hoping to convey your appreciation and enjoyment of the day."
"\n\nBlort's eyes light up with a mixture of understanding and relief. He reciprocates the hug with a genuine, albeit slightly bashful, smile. 'I'm glad you invited me today,' he says softly. 'Hugging is so nice. I hug my pets all the time!'"
"\n\nIt's clear that Blort values the connection you've established and appreciated the hug. The moment might not have been charged with raw intimacy, but the bond between you continues to grow.",
                outcome=True
            ),
            'response129': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=blort.id, 
                response=
                "Curiosity gets the best of you as you contemplate a spontaneous action. Without overthinking it, you make your move. Swiftly, you close the distance between you and gently take Blort's hand in yours. To your pleasant surprise, he doesn't resist or react awkwardly. Instead, he meets your gaze with a soft smile, his fingers intertwining with yours."
"\n\nAs you walk back together, fingers still intertwined, the atmosphere becomes charged with an understated intimacy. The silence between you is comfortable, punctuated by shared glances and the occasional chuckle."
"\n\nBlort's presence feels warm and reassuring, a reminder of the genuine connection you've established throughout the day. It's a simple gesture, but in its simplicity, it speaks volumes about the potential for something more.",
                outcome=True
            ),
            'response130': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=blort.id, 
                response=
                "A surge of boldness propels you forward as you bridge the gap between you and Blort, closing the distance in a swift movement. Your arms wrap around him, drawing him close. In the space of a heartbeat, his surprised expression gives way to a mixture of uncertainty and intrigue."
"\n\nThe shared moment hangs suspended in time, a charged atmosphere enveloping both of you. You can feel the rapid beating of Blort's heart against your chest, a testament to the emotions running beneath the surface. A shiver of anticipation courses through you."
"\n\nBlort's response is initially hesitant, a brief pause that lingers between you. But then, as if finding his resolve, he responds to the unspoken invitation. His lips meet yours, the kiss a gentle exploration of unfamiliar territory. It's an echo of his nature--simple, genuine, and filled with a quiet affection.",
                outcome=True
            ),
            'response131': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=grimble.id, 
                response=
                "Your mischievous impulse takes hold as you draw near to Grimble, your actions seemingly leading to a passionate moment. But just as the tension reaches its peak, you pull back abruptly and drop his trowsers, leaving him bewildered and taken aback."
"\n\nGrimble's reaction is swift and cutting. His eyes narrow in a mixture of irritation and confusion, his brows furrowing deeply. 'If this is your attempt at being funny, my friend, you have failed in that,' he remarks with a bitter edge to his voice. The disappointment is clear in his gaze, his insecurities momentarily exposed."
"\n\nThe atmosphere shifts, a palpable tension settling between you. It's a reminder that not all actions hold the same weight, and some can cut deeper than others. Your attempt at humor has left a mark that lingers, a reminder of the boundaries you've crossed.",  
                outcome=False
            ),
            'response132': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=grimble.id, 
                response=
                "Your proclamation rings through the air, its tone laced with a sense of superiority as you declare yourself the winner of the day's interactions, demanding a payment for the 'entertainment' you've provided."
"\n\nGrimble's reaction is a mixture of incredulity and annoyance. His eyes widen in surprise, and a disbelieving chuckle escapes him. 'You've got quite the imagination, don't you?' he retorts, his voice dripping with sarcasm. 'I didn't realize I was at a show. I'll not be paying you for this mummer's farce!'"
"\n\nThe awkwardness of the moment hangs heavily, the tension between you palpable. Your attempt to assert dominance has fallen flat, leaving a hostile feeling to the date's end.",
                outcome=False
            ),
            'response133': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=grimble.id, 
                response=
                "With a mischievous glint in your eye, you sweep Grimble off his feet, your hand confidently finding his hip as you lower him in a gentle dip. A surprised yelp escapes him, quickly followed by a nervous chuckle, his cheeks flushing slightly."
"\n\nAs the two of you share a playful moment, your eyes lock, and the atmosphere shifts. His lips part, as if in invitation, but you surprise him by reaching up and plucking a piece of grass from his cheek."
"\n\nGrimble's eyes widen in surprise, but before he can react, you wink at him, and the tension breaks. A soft laugh escapes him, and his initial embarrassment transforms into genuine amusement. 'Well played,' he remarks, a grin tugging at the corners of his lips."
"\n\nHis response is swift and unexpected, as he leans in to capture your lips with his own, the kiss deep and passionate. In that moment, the playful antics fade into the background, and the connection between you intensifies.",
                outcome=True
            ),
            'response134': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=grimble.id, 
                response=
                "With a friendly smile, you walk up to Grimble and pat him on the shoulder. 'Hey, that was a lot of fun,' you say. 'Thanks for the game.'"
"\n\nGrimble's grin widens, his chest puffing out with pride. 'Glad you enjoyed it!' he replies. 'I'm always up for a good match.'"
"\n\nAs you exchange a few more words, you can sense Grimble's genuine enthusiasm and his sincere pleasure in having shared this activity with you. His eyes gleam with a mix of satisfaction and relief, as if your positive feedback truly matters to him."
"\n\n'It was a great way to spend time together,' Grimble adds, his voice warm and appreciative. 'You know, I was worried you might not enjoy it as much as I do, but I'm glad we could have some fun.'"
"\n\nThe casual conversation eases any lingering tension from the game, and you find yourself genuinely enjoying Grimble's company. It's clear that even though you didn't win his heart, the time spent with Grimble was a victory in itself.",
                outcome=True
            ),
            'response135': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=grimble.id, 
                response=
                "As the game comes to an end, you're filled with a sense of contentment. The shared laughter, the friendly competition—it's been a wonderful time spent together. And as you catch Grimble's eye, you sense that he might be feeling the same way."
"\n\nWithout hesitation, you take a step closer to him. The atmosphere around you seems to shift, the air charged with a quiet intensity. Your gaze lingers on Grimble's lips, and your heart races in anticipation."
"\n\nClosing the distance between you, you press your lips against his in a soft, sweet kiss. It's a moment of connection, and the promise of more to come."
"\n\nGrimble responds to your advance with a mixture of surprise and pleasure. His arms wrap gently around you, pulling you closer as he returns the kiss with equal tenderness. In that moment, the world around you fades, leaving only the two of you and the warmth of your emotions."
"\n\nWhen you finally pull away, there's a soft, genuine smile on Grimble's face. 'I... I didn't see that coming,' he admits, his voice slightly breathless. 'But I'm glad you took the lead.'"
"\n\nYou meet his gaze, your heart skipping a beat at the vulnerability you see in his eyes. It's a fleeting yet powerful connection—one that signifies the beginning of something more.",
                outcome=True
            ),
            'response136': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=grimble.id, 
                response=
                "With a playful wink and a mischievous giggle, you turn on your heels and start running away from Grimble. Your heart races with a mix of excitement and anticipation, wondering how he'll respond to your playful challenge."
"\n\nYou hear the sound of footsteps behind you, growing closer with each passing moment. Grimble's laughter fills the air, his warm presence adding to the thrill of the chase. You steal a glance over your shoulder, catching his determined expression as he gains on you."
"\n\nAs you slow down, pretending to tire, Grimble catches up to you and wraps his arms around your waist, bringing you to a gentle stop. Both of you are breathless, your laughter merging with the rustling leaves and the beating of your hearts."
"\n\nIn that intimate moment, Grimble's eyes meet yours, his playfulness giving way to a deeper, more tender emotion. Without a word, he leans in, his lips meeting yours in a sweet and passionate kiss."
"\n\nTime seems to stand still as your lips move together, the world around you fading away. It's a kiss that's both familiar and new, filled with the promise of the connection you've built and the future that awaits."
"\n\nWhen you finally pull away, there's a gentle smile on Grimble's face. 'You're a handful, you know that?' he says, his tone affectionate. 'But I wouldn't have it any other way.'"
"\n\nAs you catch your breath, you find comfort in the warmth of Grimble's embrace and the shared laughter that echoes between you. It's a moment of genuine connection, one that solidifies the bond you've formed.",
                outcome=True
            ),
            'response137': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=grimble.id, 
                response=
                "Grimble's eyes meet yours, his expression a mix of amusement and something deeper, more intense. His playful smile lingers as he takes a step closer, his confidence evident in his stance."
"\n\n'You know what?' he says, his voice lower than before. 'I think it's about time someone took the initiative.'"
"\n\nBefore you can react, Grimble's arms wrap around your waist, pulling you close to him. Your breath catches as his lips meet yours in a passionate kiss, sending a rush of heat through your veins."
"\n\nIn that electrifying moment, time seems to slow down. The world around you fades away, leaving only the two of you in your own private universe. His lips are warm and insistent against yours, and you can feel the depth of his emotions in every touch."
"\n\nThe kiss deepens, becoming a passionate exchange that ignites a fire within you. Your heart races, and you find yourself responding to his every move, your bodies pressed together as if drawn by an irresistible force."
"\n\nWhen you finally break the kiss, both of you are breathless, your eyes locked in a lingering gaze. Grimble's playful facade has given way to something raw and genuine, his vulnerability visible in his eyes."
"\n\n'I've wanted to do that since the moment I saw you,' he admits, his voice husky. 'I may be a bit of a show-off, but this? This is real.'"
"\n\nAs you stand there, the weight of his words hangs in the air, the connection between you stronger than ever before. It's a moment that transcends the game you've been playing, and in its place, something meaningful and profound has taken root.",
                outcome=True
            ),
            'response138': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=grimble.id, 
                response=
                "With a gentle smile, you step closer to Grimble, your heart racing slightly as you wrap your arms around him in a warm and sincere embrace. His hesitation is only momentary before he responds, his arms encircling you in return."
"\n\nThe world around you seems to fade as you feel the comforting weight of Grimble's embrace, the warmth of his body pressed against yours. It's a simple gesture, but it speaks volumes, conveying a sense of closeness that words often struggle to capture."
"\n\nAfter a brief moment that feels both fleeting and timeless, you pull back slightly, meeting Grimble's gaze. His eyes hold a mixture of understanding and mild disappointment, a vulnerability that he allows you to see. Yet, his smile remains, a testament to his resilience."
"\n\n'Guess I'll have to steal a kiss from you next time,' he says softly, a playful glint in his eyes that contrasts with the unspoken emotions beneath. 'But hey, a hug's not a bad way to end the date, right?'"
"\n\nYou chuckle softly, appreciating Grimble's lightheartedness and his ability to find joy in the moment. There's a sense of connection that lingers in the air, a shared understanding that goes beyond words."
"As you part ways, you carry with you the memory of this simple yet profound moment, a testament to the depth of your connection with Grimble.",
                outcome=True
            ),
            'response139': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=grimble.id, 
                response=
                "As the thought takes root in your mind, a mischievous smile tugs at your lips. Without overthinking it, you close the distance between you and Grimble, your hand reaching out to grab his in a playful gesture."
"\n\nTo your delight, Grimble responds with unexpected enthusiasm. Instead of a simple handhold, he takes a step closer and smoothly twirls you around, his touch guiding you effortlessly. Laughter bubbles up between you, a joyful sound that reflects the carefree spirit of the moment."
"\n\nThe twirl comes to a graceful stop, leaving you facing Grimble once again. His eyes meet yours, and in that fleeting instant, the world seems to fall away, leaving only the two of you."
"\n\nWithout any further hesitation, Grimble's lips meet yours in a deep and intimate kiss. The world around you fades into the background as the sensation of his touch envelops you, igniting a warmth that spreads through your veins."
"\n\nTime seems to stand still as you share this stolen moment, a passionate connection that defies the limits of the day. When you finally pull away, a hushed silence lingers between you, filled with unspoken words and the promise of more to come."
"\n\nGrimble's eyes hold a mixture of emotions—desire, vulnerability, and a touch of surprise. A soft smile plays on his lips, and he brushes a strand of hair from your face."
"\n\n'Well, I wasn't expecting that,' he says, his voice a gentle murmur. 'But I guess some surprises are better than others.'"
"\n\nYou both share a moment of shared laughter, the tension of the moment broken by the easy camaraderie you've developed over the course of the date."
"\n\nAs you part ways, the memory of the twirl and the kiss lingers in your mind.",
                outcome=True
            ),
            'response140': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=grimble.id, 
                response=
                "The charged moment hangs in the air; without a hint of hesitation, you draw Grimble closer to you, his body pressed against yours in a sensual embrace."
"\n\nThe intensity of the connection between you is palpable, an electric current that sends shivers down your spine. Grimble responds in kind, his arms wrapping around you with a firm yet tender grip."
"\n\nThe anticipation builds as your lips draw closer, a magnetic pull that neither of you can resist. And then, finally, your mouths meet in a passionate, hungry kiss that ignites a fire within you."
"\n\nTime seems to blur as you lose yourself in the sensation of his lips against yours, the taste and feel of him driving you to the brink. Every touch, every press of his body against yours, fuels the growing heat between you."
"\n\nGrimble's fingers trace a path along your spine, sending shivers coursing through your body. The kiss deepens, becoming a shared exploration of each other's desires and vulnerabilities."
"\n\nWhen you eventually pull away, a low, almost guttural sound of satisfaction escapes Grimble's lips. His eyes meet yours, a mixture of passion and tenderness in his gaze."
"\n\n'You certainly know how to make a statement,' he murmurs, his voice husky with emotion. 'And I have to admit, I'm not complaining.'"
"\n\nA sense of contentment settles over you both, the intensity of the moment giving way to a quiet intimacy that speaks volumes."
"\n\nAs you part ways, the memory of the passionate kiss lingers on your lips, a promise of the connection and chemistry that define your time with Grimble.",
                outcome=False
            ),
            'response141': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=zongo.id, 
                response=
                "With a mischievous glint in your eye, you move in as if to go for a kiss, but at the last moment, you divert your aim and instead give Zongo's pants a swift tug downward."
"\n\nZongo's expression shifts from anticipation to confusion in an instant. His brow furrows as immediately pulls his breeches back in place, surprise quickly giving way to a flash of fury."
"\n\n'What is the meaning of this?' Zongo demands, his voice carrying a touch of irritation. In the blink of an eye, he raises a hand and mutters an incantation under his breath."
"\n\nTo your astonishment, you suddenly feel the sensation of wind on your legs, and then you look down to realize that your own pants have mysteriously vanished. You're left standing there in your underwear, feeling a mix of shock and embarrassment."
"\n\nZongo's lips curl into a self-satisfied smirk as he surveys his handiwork. 'Seems like a fair exchange, wouldn't you agree?' he remarks, his tone dripping with smug satisfaction."
"\n\nYou can't help but laugh, despite the embarrassment. Zongo may be infuriating, but you have to give him credit for his swift and creative retaliation."
"\n\n'Alright, Zongo, you win this round,' you concede, shaking your head with a grin. 'But mark my words, the battle is far from over.'"
"\n\nZongo's irritation seemingly forgotten and traded for confidence as he crosses his arms and leans against a nearby tree. 'I'll be waiting,' he says, a hint of challenge in his eyes. 'Just remember, I always win in the end.'",  
                outcome=False
            ),
            'response142': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=zongo.id, 
                response=
                "With an air of triumph, you announce that you are undoubtedly the victor of the game and that your date owes you for the enjoyable entertainment you've provided."
"\n\nZongo's eyebrows shoot up in surprise, his gaze narrowing at you. He doesn't seem pleased by your proclamation, and his response is swift."
"\n\nRaising a hand, Zongo mutters an incantation under his breath, and suddenly, a shower of glittering gold coins materializes in the air above you. They rain down in a cascading shimmer, surrounding you in a mesmerizing spectacle."
"\n\n'Payment made,' Zongo states with a smug grin, watching as the coins fall around you. 'But let's not forget that I refrained from using my magic in our contest. Had I played to win, I would have.'"
"\n\nYou find yourself insulted by his response, unable to suppress your anger. 'You can certainly try, Zongo,' you pronounce."
"\n\n'I do not try, I simple do,' Zongo replies, his confidence unwavering. 'Now, I shall take my leave and flee your avaracious stupidity.'"
"\n\nAs you both part ways, you feel you've made more of a rival of Zongo than a romantic parter.",
                outcome=False
            ),
            'response143': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=zongo.id, 
                response=
                "With a mischievous glint in your eye, you sweep your date into a gentle dip, cradling them in your arms with unexpected tenderness. As you lean in as if to share a kiss, your lips remain tantalizingly distant, and you pluck at something on their cheek."
"\n\nTo your surprise the piece of grass stuck there was nothing more than an illusion he had conjured. A knowing wink slides into his eye."
"\n\n'Ah, the allure of magic and mystery,' he remarks, his voice rich with satisfaction. 'Isn't it fascinating how reality be so easily warped by our perceptions?'"
"\n\nYou smile shyly in agreement, appreciating Zongo's playful approach to the situation. 'At least this fake reality got me a little closer to you,' you reply, your gaze lingering on his lips."
"\n\n'Indeed, I pride myself on it,' Zongo says, his smug grin undeniably charming. 'However, I would like to show you something else.' He leans in and kisses you deeply. His lips seem to be electrified as they press against yours."
"\n\nAs a shiver runs down your spine, you give yourself to the moment and are transported to the stars. Among the constellations nothing seems to exist but your shared intimacy. As he pulls away, you are washed back to reality."
"\n\n'That, my dear, was real.",
                outcome=True
            ),
            'response144': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=zongo.id, 
                response=
                "You approach Zongo, offering a congratulatory smile on the game that you both enjoyed. 'Well played,' you say, genuinely appreciating the time spent together."
"\n\nZongo's response is less enthusiastic than you expected, his eyes briefly scanning the surroundings as if searching for something more captivating. 'Yes, indeed. Well then, I'd best be off. There are other matters I must attend to.' he replies, a touch of boredom in his voice."
"\n\nYou can't help but feel a pang of disappointment at his lackluster reaction. Maybe this wasn't the way to truly capture his attention. Perhaps there was something more you could do to engage him.",
                outcome=False
            ),
            'response145': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=zongo.id, 
                response=
                "In a bold move, you close the remaining distance between you and Zongo, your heart pounding with a mixture of excitement and uncertainty. As you lock eyes with him, a flicker of magic dances in his gaze, and suddenly, a burst of fiery energy envelops you both."
"\n\nThe kiss that follows is unlike anything you've ever experienced. It's as if the very passion and desire you both feel have been channeled into this single moment. The flames of magic swirl around you, consuming any doubts or hesitations."
"\n\nZongo's lips are soft and electrifying against yours, the heat of the kiss matching the intensity of the magic that envelopes you. The world around you fades away as the kiss deepens, leaving only the two of you in this enchanted embrace."
"\n\nAs the flames subside and the kiss comes to an end, you're left breathless and exhilarated. Zongo's eyes are smoldering with a newfound intensity, and a slow smile spreads across his lips. 'Careful, my dear. Stick with me and you might just burn,' he remarks."
"\n\nYour heart races as you catch your breath, small embers puffing with each exhale. You realize that this fiery kiss has ignited your undeniable feelings for him.",
                outcome=True
            ),
            'response146': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=zongo.id, 
                response=
                "As you wink playfully and take off running, you can't help but giggle at the thought of Zongo chasing after you. Little do you know, Zongo has other plans. With a swift gesture of his hand, the very earth beneath your feet ripples and molds, forming restraints that ensnare your legs."
"\n\nYou stumble and come to a halt, looking back in surprise as Zongo approaches, an enigmatic smile playing on his lips. 'Looks like I've got you right where I want you,' he quips, his tone a mixture of amusement and anticipation."
"\n\nYour heart races as Zongo closes the distance between you, his magic-infused gaze locking onto yours. The energy of the earth resonates with his power, binding you to his will in more ways than one."
"\n\nWithout a word, Zongo's lips meet yours in a passionate kiss that feels as deep and primal as the very earth itself. The sensation is unlike anything you've ever experienced, an intoxicating blend of magic, desire, and connection."
"\n\nAs the kiss lingers, you become acutely aware of the pulsating energy between you and Zongo. The world around you seems to fade into the background, leaving only the two of you and the raw, untamed power that courses through your veins."
"\n\nWhen the kiss finally ends, Zongo's eyes gleam with satisfaction. 'Know that I can shape your world, if you'll let me,' he confesses with a playful grin, leaving you both breathless and exhilarated.",
                outcome=True
            ),
            'response147': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=zongo.id, 
                response=
                "With a sly grin, you decide to let Zongo take the lead for once. You lean back slightly, letting the ball fall into his court. However, Zongo seems to have other plans in mind."
"\n\nA sudden gust of freezing wind sweeps through the air, cutting through your clothes and chilling you to the bone. You shiver involuntarily, caught off guard by the sudden change in temperature."
"\n\nZongo chuckles at your reaction, his eyes gleaming with mischief. 'Oh no, it seems like you've got a need for warmth,' he remarks casually. 'I can solve that for you.'"
"\n\nBefore you can even react, Zongo's arms wrap around you, pulling you close in a firm embrace. Instantly, a comforting warmth spreads from his body to yours, thawing away the cold like a bundle of furs."
"\n\nAs the warmth envelops you, Zongo's lips meet yours in a kiss that radiates like a crackling campfire on a frosty winter night. The contrast between the icy air and his fiery kiss sends a rush of sensations through your body, leaving you tingling from head to toe."
"\n\nThe kiss is tender and passionate, a perfect blend of heat and desire that ignites your senses. It's as if you're sharing a moment of intimacy in the midst of a snow-covered forest, wrapped in the cozy embrace of a roaring fire."
"\n\nWhen the kiss finally ends, Zongo's eyes meet yours, a mix of playfulness and intensity in his gaze. 'A little frostbite can lead to the sweetest of warmths,' he murmurs, his voice a low, enticing whisper.",
                outcome=True
            ),
            'response148': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=zongo.id, 
                response=
                "You decide to play it safe and avoid any potential bad luck by opting for a friendly hug instead of a kiss. As you move in, your arms encircle Zongo's form, pulling him close in an embrace."
"\n\nZongo's response, however, is far from the warm reception you expected. He seems unamused by the hug, his posture rigid and his expression distant. It's as if he's not entirely satisfied with your choice."
"\n\nAfter a brief moment, he gently extricates himself from the hug, his gaze avoiding yours. 'Well, I suppose that's one way to handle it, buddy.' he says with a faint air of indifference."
"\n\nThe awkwardness of the situation hangs in the air, and you're left feeling a bit perplexed by his response. It seems that Zongo's playful demeanor has been momentarily subdued, leaving you wondering if you've misread the signals.",
                outcome=False
            ),
            'response149': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=zongo.id, 
                response=
                "Curiosity gets the better of you, and you decide to find out how Zongo would react if you made a bold move. Without further ado, you make your move, dashing toward him and interlinking your hand with his."
"\n\nHowever, just as your hands meet, an unexpected surge of energy courses through your bodies. Before you know it, the two of you are soaring into the sky, lifted off the ground by Zongo's levitation spell. The world around you blurs as you ascend higher and higher, your heart racing."
"\n\nDespite the sudden turn of events, your hands remain firmly entwined, and as you look into Zongo's eyes, you see a mixture of admiration, amusement, and perhaps a touch of desire. In the midst of the magical flight, your lips meet in a passionate kiss amongst the clouds."
"\n\nThe world below becomes a distant panorama as you and Zongo share an intimate connection in the skies. The kiss is both exhilarating and enchanting, a blend of magic and emotion that defies the bounds of reality. As the levitation spell gradually wanes, the two of you begin to descend back to the ground."
"\n\nAs your feet touch the earth once more, Zongo releases the spell, and you find yourselves standing together, breathless and locked in a lingering gaze. 'Well,' Zongo says with a playful smile, 'I'd say I was on cloud nine, wouldn't you?'",
                outcome=True
            ),
            'response150': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=zongo.id, 
                response=
                "Driven by the powerful connection between you and Zongo, you don't hesitate to close the distance between you. With a sense of purpose, you pull him into your arms, holding him close with an intensity that reflects the passion in your heart."
"\n\nAs you do, an unexpected surge of magic envelops the two of you. A radiant light, divine and ethereal, emanates from your intertwined forms. The very air around you seems to shimmer with the essence of something greater, as if the magic itself acknowledges the strength of your feelings."
"\n\nThe embrace takes on a transcendent quality, and as your lips meet in a tender yet fervent kiss, you can almost feel the presence of unseen forces watching over you. The kiss is imbued with an otherworldly energy, as if the heavens themselves are blessing this moment between you and Zongo."
"\n\nTime seems to stand still as you share this divine connection, lost in the depths of emotion and magic. When the kiss finally ends, you find yourselves still locked in a profound embrace, the echoes of the spell's magic resonating in the air around you."
"\n\nZongo's gaze meets yours, his eyes reflecting the awe and wonder of the moment. 'Well,' he says softly, his voice carrying a tone of reverence, 'It seems my prayers were answered.' The two of you share a knowing smile, forever connected by the magic that sparked between you.",
                outcome=True
            ),
        }
        responses_4 = {
            'response151': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=grubnub.id, 
                response=
                "As you sit down at the table with the room-temperature pints of Muk, you can't help but crinkle your nose at the pungent aroma. Grubnub looks at the Muk with eager anticipation, completely unfazed by the smell. He waits for you to speak, expectantly."
"\n\nYou decide to dive right into the conversation with a more pointed question. 'Grubnub,' you begin, leaning closer, 'have you ever thought about how goblin politics could be better? Chief Grumblebark might not be the best leader, don't you think?'"
"\n\nGrubnub blinks in surprise, his brow furrowing. 'Well,' he hesitates, 'I dunno, Chief Grumblebark has been in charge for a long time. He gives us mushrooms, and the forest is safe.'"
"\n\nYou press on, trying to instill a bit of rebellion in his simple heart. 'But what if there could be more, Grubnub? What if we could have even more mushrooms, and better Muk?'"
"\n\nGrubnub's eyes dart around nervously as if someone might overhear your conversation. 'I... I never really thought about it like that,' he stammers."
"\n\nYou lean in closer, your voice dropping to a conspiratorial whisper. 'Imagine a world where every goblin has all the mushrooms they could ever want. No more rationing, no more Chief Grumblebark telling us what to do.'"
"\n\nGrubnub looks both intrigued and uncertain. 'But how would we do that? And what if we get in trouble?'"
"\n\nYou smile slyly, planting the seed of rebellion. 'We'll figure it out together, Grubnub. One mushroom at a time.'",
                outcome=False
            ),
            'response152': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=grubnub.id, 
                response=
                "The pungent aroma of the Muk fills the air as you sit down, and Grubnub eagerly awaits the start of the conversation. You decide to lighten the mood and go for a more whimsical approach this time."
"\n\n'Grubnub,' you say with a playful smile, 'have you ever considered buying me a goblin-made tiara? I mean, I really deserve it, don't you think? Plus, it would show everyone here at the Rotten Elder Tree Saloon that I'm clearly better than them.'"
"\n\nGrubnub's eyes widen in mild confusion, and he tilts his head. 'A tiara? Well, I reckon they don't have tiaras at the Rotten Elder Tree Saloon. And ain't you already the best?'"
"\n\nYou chuckle at his response, but internalize your annoyance. You don't want to leave just yet, so you play along. 'You're right, Grubnub. I am the best, and I don't need a tiara to prove it. Just having you as my friend is enough.'"
"\n\nGrubnub's face lights up with a bright smile. 'Aw, shucks,' he mumbles, a hint of bashfulness in his voice. 'You're the best friend I've ever had too.'",
                outcome=True
            ),
            'response153': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=grubnub.id, 
                response=
                "As the server brings over the two pints of Muk, you ponder the best way to start the conversation. You want to express your feelings but also wonder if it's worth it. However, the thought of sparking a bit of jealousy among the other goblin boys if they hear about this intrigues you."
"\n\nWith a sly grin, you turn to Grubnub and say, 'You know, Grubnub, I've been thinking... I really like you. A lot.'"
"\n\nGrubnub's eyes widen in surprise, and a faint blush creeps up on his cheeks. He stammers a bit before responding, 'You... you do? Well, that's mighty nice to hear.'"
"\n\nYou can't help but chuckle at his adorable reaction. 'Yeah, Grubnub, I do. You're different from the other goblins, and I mean that in the best way possible.'"
"\n\nHis blush deepens, and he smiles bashfully. 'Well, you're different too, in a good way. It's nice to have someone like you around.'"
"\n\nThe two of you share a genuine moment of connection. You only hope the other boys catch wind of this.",
                outcome=True
            ),
            'response154': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=grubnub.id, 
                response=
                "As you sit at the table, Grubnub appears to be in a contented Muk-induced haze, having already downed an impressive number of mugs. Despite the hours he's spent here and the amount of Muk he's consumed, he seems cheerful and not the slightest bit affected by the tavern's unique ambiance."
"\n\nYou finally make up your mind and lean in, deciding to join in on the Muk-fueled atmosphere. With a playful grin, you say, 'You know, Grubnub, I've got some Muk from home. This Muk is pretty magic and will make you smarter!'"
"\n\nGrubnub, who's already deep into his 7th hour of Muk consumption, bursts into laughter, spilling a bit of the frothy brew onto the table. 'Haha, maybe!' he replies between chuckles. 'But you know, I'm pretty smart already!' He winks drowsily, clearly not fully coherent right now."
"\n\nThe two of you continue chatting, occasionally sipping your Muk and sharing light-hearted stories. Grubnub's relaxed and jovial demeanor makes the time fly by, and soon, the initial awkwardness you felt melts away, replaced by a warm camaraderie. It turns out that Muk, in moderation, can be quite the social lubricant.",
                outcome=True
            ),
            'response155': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=grubnub.id, 
                response=
                "As the two of you sit at the table, with Muk in hand, you feel a strange warmth in your goblin heart. Perhaps it's the fermented brew talking, but you can't deny the strong connection you're starting to feel with Grubnub. In this cozy, dimly lit tavern, surrounded by the sounds of goblin laughter and the earthy aroma of Muk, it feels like destiny that the two of you have met."
"\n\nUnable to contain your emotions any longer, you turn to Grubnub with a smile and declare, 'Grubnub, I think you're amazing, and I love being with you!' The words tumble out, a little too loudly for the intimate setting of the tavern."
"\n\nGrubnub blinks, the Muk momentarily dulling his response time. He looks at you with a mix of surprise and confusion. 'Oh,' he mumbles, 'That's... that's real nice of you to say.' His cheeks flush with a tinge of embarrassment as the surrounding goblins turn to see what the fuss is about."
"\n\nYou both fall silent for a moment, the atmosphere growing a touch awkward. Grubnub clears his throat and changes the subject, discussing the finer points of the local Muk-making process. It seems he's not quite ready to reciprocate your declaration just yet.",
                outcome=False
            ),
            'response156': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=grubnub.id, 
                response=
                "You wait for Grubnub to make the first move, giving him a moment to gather his thoughts. After a few seconds of somewhat awkward silence, he clears his throat and looks at you with a friendly grin."
"\n\n'I must admit, I'm not used to such fancy places,' he says, chuckling nervously. 'But this Muk is something else, isn't it?'"
"\n\nYou give a knowing nod, appreciating his effort to start the conversation. 'Absolutely,' you reply with a playful twinkle in your eye. 'I've heard that after a few mugs of this stuff, goblins start speaking fluent elvish.'"
"\n\nGrubnub bursts into laughter, the tension broken as he guffaws at your remark. 'Fluent elvish, you say? Well, I better have another mug then!'"
"\n\nWith the ice officially broken, the two of you spend the evening sharing jokes, tales, and, of course, more Muk, making the Rotten Elder Tree Saloon feel like the coziest place in the world.",
                outcome=True
            ),
            'response157': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=grubnub.id, 
                response=
                "You huff inwardly, not pleased about being put in a position where you have to start the conversation. Nevertheless, you decide to be the bigger goblin in this situation and reluctantly bring up the weather."
"\n\n'Nice weather we're having, huh?' you say with an exaggerated casualness, taking a sip of your lukewarm Muk."
"\n\nGrubnub seems a bit caught off guard by your choice of topic, and there's an uncomfortable silence for a moment before he finally responds, nodding in agreement. 'Oh, yes, it's... um, quite pleasant.'"
"\n\nYou can't help but feel a bit smug, knowing that you've made your point. From now on, they better be the one to initiate the conversation."
"\n\nAs the evening goes on, you both find more engaging topics to discuss, but there's still a palpable awkwardness in the air, making the Rotten Elder Tree Saloon a somewhat uncomfortable place to be.",
                outcome=False
            ),
            'response158': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=grubnub.id, 
                response=
                "You arrive at the Rotten Elder Tree Saloon in your signature fashion, dressed head to toe in the brightest shades of orange you could find. Your outfit is a chaotic mix of mismatched patterns and fabrics, and you couldn't be more proud of it."
"\n\nAs you settle down at the table with Grubnub, your enthusiasm is palpable. You flash him a mischievous grin and blurt out, 'Hey, did you bring a worm with you? You know, for the Muk Lord? Sacrificing a worm is the best way to ensure a night of good Muk!'"
"\n\nGrubnub stares at you, his eyes wide with a mix of surprise and confusion. 'Uh, no, I didn't bring a worm,' he replies slowly, clearly unsure if you're joking or not."
"\n\nYou start to panic, but you hide it as best you can and try to ease your wait out of it, 'I'm just messing with you, Grubnub!'"
"\n\nRelief washes over Grubnub's face as he chuckles nervously. 'Oh, okay, you got me there.' You quietly squash your worm between your hand and let it fall to the floor away from his line of sight."
"\n\nThe rest of the evening passes in a whirlwind of laughter, Muk, and more Muk. Grubnub may not have brought a worm, but he definitely brought a smile to your face.",
                outcome=True
            ),
            'response159': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=grubnub.id, 
                response=
                "Curiosity fills your goblin heart as you take in the surroundings of the Rotten Elder Tree Saloon. This is your first time here, and the promise of trying Muk for the first time is an exciting prospect."
"\n\nTurning your attention to Grubnub, you lean in and ask, 'Are you a regular here? It seems like the kind of place where everyone knows each other.'"
"\n\nGrubnub takes a thoughtful sip of his Muk before answering, 'Yeah, I come here pretty often. It's a cozy place, and the Muk's not half bad.'"
"\n\nYou nod in agreement, taking a sip of your own Muk. The earthy flavors and rustic charm of the saloon start to grow on you. As the evening unfolds, you and Grubnub chat about everything from the local gossip to your favorite Muk flavors, and you can't help but feel like you've found a new Muk-loving friend.",
                outcome=True
            ),
            'response160': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=grubnub.id, 
                response=
                "Your eyes widen in realization as you check your calendar, and you let out an exasperated sigh. 'Oh no, I completely forgot that I already had plans tonight!'"
"\n\nGrubnub raises an eyebrow, his curiosity piqued. 'Really? With who?' he asks, taking a sip of his lukewarm Muk."
"\n\nYou scratch your head, feeling somewhat awkward about the situation. 'Well, it was supposed to be a date with Poorg,' you confess, looking sheepish."
"\n\nGrubnub's expression changes to one of surprise, and he seems to know Poorg. His voice lowers, and there's a hint of guilt in his tone. 'Oh, I know Poorg. We're friends, actually.'"
"\n\nYou can't help but feel a bit uncomfortable as you continue the conversation. Grubnub, while polite, seems a bit self-conscious now that he knows he was the second choice for the evening."
"\n\nThe date continues, but there's an underlying awkwardness that lingers in the air. You both try to make the best of the situation, sharing stories and sipping on your Muk, but there's an undeniable tension."
"\n\nAs the night continues, you can't shake the feeling that things could have been different if you had remembered your plans with Poorg. While you enjoyed your time with Grubnub, there's a lingering sense of what could have been.",
                outcome=False
            ),
            'response161': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=sneezle.id, 
                response=
                "You lean in slightly and, with a sly grin, you bring up the topic of politics. 'You know,' you begin, 'I've been thinking about the state of our goblin government lately. What are your thoughts on Chief Grumblebark's leadership?'"
"\n\nSneezle's eyes twinkle mischievously as he leans in, lowering his voice conspiratorially. 'Funny you should ask,' he says, 'because I've got a plan to bring down Chief Grumblebark.'"
"\n\nYou raise an eyebrow, intrigued. 'Really? Do tell.'"
"\n\nWith a playful glint in his eye, Sneezle outlines his elaborate and comically absurd scheme to overthrow Chief Grumblebark. It involves whoopee cushions, rubber chickens, and a lot of whooping and hollering."
"\n\nAs he explains, you can't help but laugh at the sheer audacity of his plan. Sneezle's eyes sparkle with mischief, clearly enjoying your reaction."
"\n\nThe conversation continues, and you find yourself drawn into Sneezle's carefree outlook on life. While the topic of politics may not have been as serious as you initially thought, you can't deny that you're having a great time with this prankster goblin.",  
                outcome=True
            ),
            'response162': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=sneezle.id, 
                response=
                "You lean in with an exaggerated air of importance, grinning mischievously. 'You know what would really make a statement here at the Rotten Elder Tree Saloon?' you begin, your voice dripping with sarcasm. 'A goblin-made tiara, of course. It's time everyone knows just how fabulous I am.'"
"\n\nSneezle's eyes widen in mock astonishment, and he lets out a burst of laughter. 'A tiara, you say?' he chortles. 'Well, aren't we the fancy goblin?'"
"\n\nYour grin falters slightly as you realize he's making fun of you. 'I was just joking, you know,' you mutter."
"\n\nSneezle playfully nudges you with his elbow. 'Relax,' he says, still chuckling. 'I've got a better idea. How about we make a bet? If I can make the bouncer laugh tonight, you owe me a favor. If I can't, I'll buy you a tiara.'"
"\n\nYou can't help but be intrigued by Sneezle's proposal. It's clear that he's confident in himself, and this could be an interesting challenge. 'Deal,' you say, sticking out your hand to shake on it."
"\n\nAs you shake hands, the atmosphere lightens, and you find yourself enjoying Sneezle's company. Perhaps this date won't be so awkward after all.",
                outcome=True
            ),
            'response163': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=sneezle.id, 
                response=
                "You decide to start off with a bit of flattery. Leaning closer to Sneezle, you say, 'You know, I've heard a lot about you, and I must admit, I really like what I see.' You flash a playful grin, fully aware that you're laying it on thick."
"\n\nSneezle bursts into laughter, his eyes twinkling with amusement. 'Well, well,' he says, his voice dripping with sarcasm. 'Aren't you the charmer? Should I be flattered?'"
"\n\nYou chuckle along with him, realizing that your exaggerated compliment might have been a bit too much. 'I guess I got carried away,' you admit."
"\n\nSneezle nudges you playfully. 'Don't worry about it,' he says, still grinning. 'It's all in good fun. Besides, can you imagine the other goblin boys' faces if they heard about this?'"
"\n\n'That's what I was thinking!' You shout. It seems the two of you are on similar wavelengths."
"\n\nYou both share a laugh, and the awkwardness from your over-the-top compliment melts away as the date gets off to a lighthearted start.",
                outcome=True
            ),
            'response164': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=sneezle.id, 
                response=
                "After a great deal of waffling and hesitation, you finally decide to join Sneezle at the table. You're not willing to take any risks, so you pull out your own Muk from home and offer some to Sneezle."
"\n\nSneezle raises an eyebrow, clearly irritated by your tardiness. 'Took you long enough,' he remarks, his tone dripping with sarcasm. 'I was beginning to think I'd been stood up.'"
"\n\nYou let out an awkward chuckle, realizing that you might have taken a bit too long to make up your mind. 'Sorry about that,' you mumble."
"\n\nSneezle eyes the Muk from home that you've brought. 'What's this?' he asks, feigning innocence. 'A secret recipe? Or just your way of telling me that you don't trust the Muk they serve here?'"
"\n\nYou give him a sheepish grin, admitting, 'A bit of both, actually.'"
"\n\nSneezle rolls his eyes but doesn't press the matter further. 'Well, pour me a glass, then. Let's see if your Muk is as good as you say it is.'"
"\n\nAs you pour him a glass, you can't help but feel a hint of embarrassment for your overthinking. The date seems to be getting off to a rocky start, but at least Sneezle is willing to give your Muk a try.",
                outcome=False
            ),
            'response165': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=sneezle.id, 
                response=
                "With a gleam in your eye and a grin on your face, you decide to go for broke. The Muk has emboldened you, and you boldly declare, 'You know, Sneezle, I think I love you.'"
"\n\nSneezle's eyes widen in surprise, and then he bursts into laughter. 'Oh, you really know how to lay it on thick, don't you?' he chuckles, clearly not taking your declaration seriously."
"\n\nYou join in the laughter, realizing that perhaps you've been a bit too forward. 'Hey, it's just the Muk talking,' you say, trying to brush it off as a joke."
"\n\n'Of course, of course,' Sneezle replies, still chuckling. 'But hey, who could possibly resist my charm? I love me too.'"
"\n\nYou both share a good laugh, and the tension that had built up from your bold statement dissipates. It seems that Sneezle is more than willing to play along with your Muk-fueled antics.",
                outcome=True
            ),
            'response166': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=sneezle.id, 
                response=
                "You decide to let Sneezle squirm for a moment, wondering how he'll break the silence. But you don't have to wait long. Sneezle leans in closer, his eyes locking onto yours. It's as if he's challenging you to a staring contest."
"\n\nYou can't resist the challenge and lock eyes with him. The seconds tick by, and the silence stretches. The atmosphere grows tense as neither of you wants to be the first to break."
"\n\nThen, unexpectedly, Sneezle's face cracks into a grin, and he lets out a snort of laughter. 'Bah, I lose,' he says, shaking his head. 'It's hard not to laugh at that face of yours'"
"\n\nYou can't help but laugh too, relieved that the awkward silence has been broken. 'What this old face? I left my good face at home."
"\n\nThe two of you share a good laugh, and it seems that Sneezle has turned the tables on your attempt to make him squirm. The date continues with a more relaxed atmosphere.",
                outcome=True
            ),
            'response167': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=sneezle.id, 
                response=
                "You grumble inwardly, not appreciating being forced into conversation. You decide to play along and begrudgingly bring up the weather. 'So, uh, what do you think of this weather we're having?' you ask, trying to sound as unenthusiastic as possible."
"\n\nSneezle arches an eyebrow, clearly unimpressed by your choice of conversation topic. 'The weather, huh?' he replies with a hint of sarcasm. 'Fascinating stuff.'"
"\n\nYou roll your eyes, regretting your decision already. 'Yeah, well, I couldn't think of anything else to talk about.'"
"\n\nSneezle smirks and leans in closer. 'You know,' he says, his tone conspiratorial, 'we could always talk about overthrowing Chief Grumblebark. That's more exciting than the weather, don't you think?'"
"\n\nYou're taken aback by his suggestion but can't help but chuckle at his audacity. Maybe this date won't be as dull as you thought.",
                outcome=True
            ),
            'response168': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=sneezle.id, 
                response=
                "As you step into the Rotten Elder Tree Saloon wearing your vivid orange ensemble and non-matching socks, Sneezle can't help but burst into a fit of laughter."
                "\n\nYou playfully nod and continue the humorous tone, 'Absolutely, and speaking of fashion statements, did you bring a worm to sacrifice to the Muk Lord today?'"
                "\n\nSneezle's laughter continues as he responds, 'A worm sacrifice? Now that's an interesting choice. Sadly, I didn't bring a worm today. But I am sacrificing my Kidney.'"
                "\n\nThe jovial atmosphere between you and Sneezle sets the tone for a date filled with laughter and fun, making the quirky start all the more enjoyable.",
                outcome=True
            ),
            'response169': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=sneezle.id, 
                response=
                "You flash a friendly grin and lean in a bit closer to Sneezle. 'You know, this is my first time here, and I've heard so much about Muk. Are you a regular around here?'"
                "\n\nSneezle's eyes twinkle with mischief as he leans back, considering your question. 'Regular? Well, you could say that,' he replies, drawing out the words. 'I'm practically part of the furniture. But enough about me, you're in for a treat with this Muk.'"
                "\n\nAs the conversation flows, you and Sneezle delve into the world of Muk and the notorious saloon regulars. Time flies, and you find yourself drawn into Sneezle's humor and lively spirit, making the evening an enjoyable experience.",
                outcome=True
            ),
            'response170': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=sneezle.id, 
                response=
                "You find yourself slightly flustered as you realize you said yes before checking your calendar. It dawns on you that you were supposed to go on a date with Poorg today. Well, no turning back now! With a light-hearted smile, you turn your attention back to Sneezle and ask, 'By the way, are you friends with Poorg? Poor Poorg got stood up today.'"
        "\n\nSneezle grins mischievously, clearly amused by the situation. 'Ah, Poorg, he's a character, isn't he?' he replies. 'Well, I can't say we're close friends, but we've had our share of laughs together. I hope he finds another fun distraction for the day.'"
        "\n\nThe mention of Poorg's name fades into the background as you and Sneezle continue to chat and enjoy each other's company.",
                outcome=True
            ),
            'response171': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=blort.id, 
                response=
                "You lean in slightly, your eyes gleaming with determination. 'Blort, have you ever thought about the state of our goblin government? I mean, don't you think it's time for some...violent changes?'"
                "\n\nBlort's eyes widen in surprise as he nervously adjusts his glasses. 'Oh, well, I'm not sure about that,' he stammers, clearly uncomfortable with the topic. 'I've always believed in kindness and harmony.'"
                "\n\nThe atmosphere grows tense as you realize Blort's reluctance to entertain the idea. The conversation becomes strained, and you both struggle to find common ground, making for an awkward evening at the saloon.",
                outcome=False
            ),
            'response172': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=blort.id, 
                response=
                "You lean in with a mischievous glint in your eye and ask Blort, 'You know, Blort, I've been thinking. Do you think you could get me a goblin-made tiara? I mean, I genuinely believe I deserve it, and it would be a symbol of my unique style and charm.'"
                "\n\nBlort lets out a hearty chuckle, clearly understanding your playful request. 'A tiara, huh?' he responds with a friendly grin. 'Well, I'd say you already shine like one without it. Your personality and charm light up the room.'"
                "\n\nYou can't help but smile at Blort's response. His compliment warms your heart, and the playful request sets a lighthearted tone for the conversation.",
                outcome=True
            ),
            'response173': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=blort.id, 
                response=
                "You and Blort sit at a rustic table with two pints of Muk in front of you. The earthy aromas fill the air, setting the mood for your date in the cozy, dimly lit saloon."
        "You briefly debate whether to share your feelings. The idea of revealing your affection for Blort excites you, but you're aware it might stoke jealousy among the other goblin boys."
        "Taking a deep breath, you decide to follow your heart. Leaning in, you meet Blort's eyes and say, 'You know, Blort, I've always admired your kindness and love for animals. It's a rare quality, and I genuinely like that about you.'"
        "Blort's eyes widen in surprise, a blush creeping up his cheeks. He seems taken aback by your openness. 'Oh, well, I... um, thank you,' he stammers, 'Not many people notice that about me.'"
        "You sense a mix of shyness and gratitude in his response. The potential spark of something more makes the moment even more thrilling.",
                outcome=True
            ),
            'response174': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=blort.id, 
                response=
                "Your internal debate stretches on for what seems like an eternity, and you can't help but notice Blort's growing discomfort as the hours pass. With each moment of hesitation, his once-eager expression gradually fades into one of uncertainty and restlessness."
        "Seven long hours of waiting test Blort's patience. He fidgets in his chair, clears his throat awkwardly, and shoots nervous glances at the untouched lukewarm pints of Muk on the table. Your prolonged contemplation has clearly taken a toll on his composure."
        "Finally, you make a decision and approach the table, taking your seat. The relief that washes over Blort is evident, but his awkwardness and shyness persist. Politely declining the room temperature pints of Muk that the server brought, you opt for caution. Retrieving a small, meticulously sealed container of Muk from home, you offer it to Blort with a reassuring smile, saying, 'I brought my own Muk, just to be safe. It's homemade and completely secure.'"
        "Blort, though visibly relieved that the wait is over, remains shy and uncomfortable. He accepts your offer with a hesitant nod, his words slightly stilted, 'Th-thank you for being considerate.' His voice wavers, and he avoids direct eye contact, clearly overwhelmed by the situation.",
                outcome=False
            ),
            'response175': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=blort.id, 
                response=
                "You feel an undeniable connection with Blort deep in your goblin heart. As the Muk flows and warms your spirits, you find yourself overcome by the moment. The dimly lit saloon seems to fade into the background, leaving only you and Blort in a world of your own."
                "\n\nYou take a deep breath, your goblin instincts guiding your words. Your heart pounding, you turn to Blort, who looks at you with curious eyes. The warmth of the Muk is like a gentle nudge, urging you to speak your truth. With unwavering determination, you finally let your feelings spill out, 'Blort, I... I love you.'"
                "\n\nTime stands still as you hold your breath, waiting for Blort's response. His eyes widen in sheer surprise, and his cheeks flush with a rosy hue. The saloon's rustic charm seems to come alive with a newfound energy, as if celebrating this significant moment. Blort's lips part, but words elude him momentarily as emotions swirl between you."
                "\n\nFinally, a nervous, shy smile graces Blort's face, and he manages to stammer, 'I... I didn't expect... I mean, I feel... um... I like you too. We uhh.. should get to know each other first though?' His admission is filled with bashfulness, and you are unsure if he is just saying that because he doesn't want to hurt your feelings.",
                outcome=False
            ),
            'response176': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=blort.id, 
                response=
                "You decide to let Blort wait awkwardly for a bit, enjoying the tension as it builds between you. Blort's eyes widen, and he shifts uncomfortably in his seat, clearly feeling the weight of the silence you've allowed to hang in the air. The dimly lit saloon seems to magnify the awkwardness of the moment."
            "\n\nHowever, as you watch Blort squirm, you can't help but notice the discomfort in his demeanor. It tugs at your goblin heart, and you decide to put him out of his misery. With a mischievous grin, you break the silence, 'Alright, alright, I can't keep you waiting any longer, Blort. It was fun watching you squirm, but lets just talk.'"
            "\n\nBlort lets out a nervous laugh, relieved that the silence has been broken. 'Oh, thank goodness,' he replies, still blushing slightly. 'I appreciate it. I'm not great with silences.' You and Blort begin talking casually from here on.",
                outcome=False
            ),
            'response177': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=blort.id, 
                response=
                "You love Muk, but you've never been fond of being forced into anything, especially a conversation. Annoyed by the awkward silence, you decide to break it with the most mundane topic you can think of—the weather. It's a quick jab at Blort's lack of confidence, and you're not subtle about it."
            "\n\nBlort, noticing your irritation, tries to make the best of it. 'Well,' he responds with a soft smile, 'it has been rather cloudy lately, but the rain can be soothing, don't you think?'"
            "\n\nYou nod, masking your annoyance, but deep down, you're frustrated that Blort didn't take the initiative.",
                outcome=False
            ),
            'response178': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=blort.id, 
                response=
                "You're absolutely stoked for this date, and your enthusiasm shows as you proudly wear only the color orange, from your head to your toes. Matching socks? Not a chance. As you sit down with Blort, you pull out your worm and ask, 'Hey, Blort, did you remember to bring a worm to sacrifice to the Muk Lord?'"
            "\n\nBlort's eyes widen in disbelief, and a look of shock crosses your face. 'Harm a worm? Oh, goodness, no!' he exclaims, clearly appalled at the idea of causing harm to even the tiniest creature. 'I could never do such a thing. We should respect all living beings.'"
            "\n\nYou, however, asked the question sincerely, and Blort's reaction leaves you feeling insulted and misunderstood. It's clear that he doesn't share your goblin customs or beliefs, and this realization casts a shadow over the date.",
                outcome=False
            ),
            'response179': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=blort.id, 
                response=
                "Intrigued by the rustic charm of this local saloon and excited about trying Muk for the first time, you turn to Blort, who appears to be a seasoned patron, and ask, 'Blort, are you a regular here?'"
            "\n\nBlort's face lights up with a warm smile, as if reminiscing about a cherished memory. 'Oh, indeed,' he replies with a nostalgic tone. 'This place has been a part of my life for ages. It's a hidden gem, and Muk is a personal favorite of mine. You're in for a delightful experience.' His words carry a genuine enthusiasm that amplifies your anticipation of this new Muk adventure."
            "\n\nAs you soak in Blort's words and the inviting atmosphere of the saloon, you realize that this date is turning into a promise of a heartwarming connection.",
                outcome=True
            ),
            'response180': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=blort.id, 
                response=
                "You realize you said yes to this date before checking your calendar, and now you remember that you were supposed to go on a date with Poorg. Oh well, too late now! You decide to bring up the subject and casually ask Blort, 'By any chance, are you friends with Poorg?'"
            "\n\nBlort tilts his head in thought for a moment before a warm smile graces his face. 'Ah, Poorg,' he replies, 'I know him. We've crossed paths a few times, but I wouldn't say we're close friends. Why do you ask?'"
            "\n\nYou shrug and chuckle, 'Oh, it's just that I was supposed to go on a date with him, but things got mixed up, I guess.' Poor Poorg, you think to yourself, feeling a twinge of guilt. You notice that Blort seems to be saddened by the relization as well.",
                outcome=False
            ),
            'response181': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=grimble.id, 
                response=
                "As you and Grimble settle at your table, the server brings over two room temperature pints of Muk, filling the air with enticing aromatics. You notice Grimble's expectant gaze, hinting that he's eager for you to initiate the conversation. With a playful glint in your eye, you decide to open with a bold question, 'So, Grimble, what are your thoughts on goblin politics?'"
            "\n\nGrimble's eyes widen, and a self-assured grin crosses his face. 'Ah, goblin politics,' he exclaims with enthusiasm, 'Now, you've hit upon a topic I'm quite passionate about!'"
            "\n\nAs the conversation delves into the intricacies of goblin governance and power struggles, you find yourself intrigued by Grimble's perspectives. It turns out, beneath his dashing adventurer facade, he has a lot to say about the world of goblin politics. He may not be a full blown revolutionary, but at least he is well informed and has some good takes.",  
                outcome=True
            ),
            'response182': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=grimble.id, 
                response=
                "With a determined glint in your eyes, you lean in towards Grimble and ask, 'You know, Grimble, I've been thinking. Do you think you could purchase me a goblin-made tiara? I believe I truly deserve one.' The sincerity in your voice leaves no room for doubt, and you're not joking. You genuinely desire that tiara, not only as a symbol of your self-worth but also to assert your superiority over others at the Rotten Elder Tree Saloon."
            "\n\nGrimble's initial surprise quickly turns into a furrowed brow as he contemplates your request. He leans back in his chair, crossing his arms, and replies with a touch of disapproval, 'A goblin-made tiara, huh? That's quite the extravagant request, my friend. Don't you think it's a tad arrogant to believe you deserve such a thing?'"
            "\n\nYou feel a hint of embarrassment as Grimble's words pierce through your desire for the tiara. Perhaps you've pushed the boundaries of your request too far. Nevertheless, the atmosphere between you and Grimble has shifted, and the date takes on a more serious tone, leaving you to reflect on your actions.",
                outcome=False
            ),
            'response183': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=grimble.id, 
                response=
                "You contemplate your words carefully, knowing that openly expressing your feelings could have consequences. Despite the potential risks, you decide to take the plunge and begin, 'Grimble, I have to admit that I really like you.'"
            "\n\nGrimble's initial surprise turns into an awkward silence, and his cheeks flush with a mixture of embarrassment and uncertainty. The atmosphere in the saloon suddenly feels heavy, and you can sense that your confession has thrown a wrench into the date."
            "\n\nAfter a prolonged silence, Grimble finally stammers, 'Uh, well, that's quite the confession.' His voice lacks the usual enthusiasm, and he seems visibly uncomfortable. 'I...uh...I appreciate your honesty.'"
            "\n\nThe air between you grows increasingly tense as the date becomes fraught with awkwardness. Grimble appears to be at a loss for words, and it's clear that your confession has disrupted the previously cheerful atmosphere. You both struggle to find common ground, and the rest of the date proceeds on a sour note, with an uncomfortable tension lingering in the air.",
                outcome=False
            ),
            'response184': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=grimble.id, 
                response=
                "After an agonizing seven-hour delay, you finally decide to join Grimble, who has been patiently waiting. However, you refuse to drink the provided Muk, fearing it might be poisoned. Instead, you bring out your own Muk from home and offer some to Grimble, asking, 'Would you like some of this Muk?'"
            "\n\nGrimble's eyes narrow with fury as he stares at you, clearly infuriated by the lengthy wait. 'Seven hours!' he exclaims with frustration. 'Do you know how long I've been waiting here? And now you bring your own Muk? Insolence, pure insolence!'"
            "\n\nGrimble rejects your offer of Muk and crosses his arms, his irritation palpable. The atmosphere between you sours further, and it's evident that your actions have deeply offended him, casting a shadow over the date.",
                outcome=False
            ),
            'response185': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=grimble.id, 
                response=
                "You feel it in your goblin heart - a sense that Grimble might be the one. The Muk acts as a lubricant for your emotions, and you decide to throw caution to the wind. You boldly declare, 'Grimble, I love you!'"
            "\n\nGrimble's eyes widen in surprise, and he lets out a hearty laugh, thinking it's a jest. 'Well,' he chuckles, 'You certainly are a funny creature aren't you?'"
            "\n\nDespite your internalized awkwardness, Grimble's laughter diffuses the tension, and the date continues on a positive note. Your advances are met with amusement rather than rejection.",
                outcome=True
            ),
            'response186': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=grimble.id, 
                response=
                "You're absolutely thrilled for this date, and it shows in your choice of attire – you're decked out entirely in the color orange, right down to your mismatched socks. With a mischievous grin, you turn to Grimble and ask, 'Hey, Grimble, did you happen to bring a worm to sacrifice to the Muk Lord?'"
            "\n\nGrimble raises an eyebrow, clearly taken aback by your question. 'A worm sacrifice?' he replies with a mixture of confusion and amusement. 'Now that's an unusual date request! No, I didn't bring a worm, but I will not question your practices. Proceed as you see fit!'"
            "\n\nYour unconventional approach to the date brings a touch of eccentricity to the atmosphere, and Grimble's amusement ensures that your quirky request doesn't derail the evening.",
                outcome=True
            ),
            'response187': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response188': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response189': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response190': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response191': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response192': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response193': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response194': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response195': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response196': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response197': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response198': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response199': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response200': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_5 = {
            'response201': Response(
                dialogue_id=dialogues_list[40].id, 
                goblin_id=grubnub.id, 
                response=
                "Despite the potential fight brewing, your date continues to be heartwarming and memorable as you both relish the unique Muk and each other's company. The note's significance fades against the backdrop of your delightful evening, reinforcing the genuine connection you share with Grubnub, whose kind-hearted nature shines through, making this a date to cherish.",
                outcome=True
            ),
            'response202': Response(
                dialogue_id=dialogues_list[41].id, 
                goblin_id=grubnub.id, 
                response=
                "As you stop the server to request an extra to-go bag of peanuts, Grubnub watches with a puzzled expression, his brow furrowing slightly. It seems he's a bit put off by your statement. The server, still holding the note, looks at you, then back at Grubnub, and finally hands him an extra bag of peanuts.",
                outcome=False
            ),
            'response203': Response(
                dialogue_id=dialogues_list[42].id, 
                goblin_id=grubnub.id, 
                response=
                "As you discreetly observe Grubnub's reaction to the note, you can see his brow furrow slightly, and his expression shifts from its usual cheerful demeanor to one of mild confusion. He tilts his head, reading the note carefully, but it's clear that his slow-witted nature is causing him to struggle with its content. You snatch the note, put it in your mouth, and swallow. You then flash a warm smile and whisper, 'Don't worry, Grubnub. It's probably just a mistake or a silly joke. Let's not let it ruin our evening'.",
                outcome=True
            ),
            'response204': Response(
                dialogue_id=dialogues_list[43].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub, looks at you with a puzzled expression. He doesn't seem to understand why you're reacting this way. The server, who had slipped the note to Grubnub, notices the tension in the air. As Grubnub unfolds the note and reads it, you soon realize that your instincts were RIGHT. Elder Tree is under attack. You must run for your life.",
                outcome=False
            ),
            'response205': Response(
                dialogue_id=dialogues_list[44].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub, oblivious to the server's intentions, watches as you chuckle and wink at the server in response to the note. With the boost of confidence, your converstion becomes extra lighthearted and charming. This has been the best date ever.",
                outcome=True
            ),
            'response206': Response(
                dialogue_id=dialogues_list[45].id, 
                goblin_id=grubnub.id, 
                response=
                "You begin a rather ruthless game of tic-tac-toe between each other. Winning the game has become crucial to your survival. Grubnub does not grasp the intricacies of the game situation, but is very merry to be included.",
                outcome=False
            ),
            'response207': Response(
                dialogue_id=dialogues_list[46].id, 
                goblin_id=grubnub.id, 
                response=
                "The server looks slightly puzzled by your action, but you're determined to unravel this mysterious note. As the paper disintegrates in the Muk, a faint message becomes visible. It reads, 'Meet me by the moonlit pond, behind the brewery, at midnight'. Grubnub, oblivious to your investigative efforts, smiles and pretends he doesn't notice you're crazy. You know an adventure awaits y'all later tonight.",
                outcome=True
            ),
            'response208': Response(
                dialogue_id=dialogues_list[47].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub looks utterly baffled by your sudden patriotic outburst. He tilts his head, trying to understand, and then joins in, attempting to sing along despite his slow-witted nature. The server and other patrons exchange wary glances, but then jump up and begin slow dancing together. Grubnub may not have understood why, but he appreciates your effort to make the evening enjoyable, and your date takes an unexpected turn toward quirky charm. The note is forgotten",
                outcome=False
            ),
            'response209': Response(
                dialogue_id=dialogues_list[48].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub, utterly baffled, pats your unconscious form gently, wondering if this is just one of your quirks. He continues on happily eating peanuts and drinking Muk, patiently waiting for you to regain consciousness. Several hours later, you awaken with peanuts and drool stuck to your face.",
                outcome=True
            ),
            'response210': Response(
                dialogue_id=dialogues_list[49].id, 
                goblin_id=grubnub.id, 
                response=
                "Grubnub blinks in surprise, clearly taken aback by your sudden enthusiasm. As you finally clutch the note, panting aggressively and damp with Muk, you can't help but wonder if this impulsive act will reveal the secret you've been running from all your life.",
                outcome=False
            ),
            'response211': Response(
                dialogue_id=dialogues_list[40].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle jumps up, grabs your hand, and screams, 'we have to go'! Y'all sprint out of the saloon without stopping to pay first. You are alarmed and don't know what is wrong. Once outside, Sneezle turns to you and winks playfully. You realize he knew about your scheme all along and wanted to play too. Together, you share a conspiratorial laugh, enjoying the shared thrill of this impromptu escapade. Your date with Sneezle takes an exciting turn as you both embrace the unexpected twists and turns of the evening.",  
                outcome=True
            ),
            'response212': Response(
                dialogue_id=dialogues_list[41].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle, with his love for humor and spontaneity, bursts into laughter at your cheeky request. He joins in on the joke, exaggerating his desire for the peanuts, saying, 'Oh, absolutely! We can't have those midnight munchies go unsatisfied, can we?' The server, amused by your banter, obliges, and you both share a playful moment, solidifying the lighthearted, carefree atmosphere of your date with Sneezle.",
                outcome=True
            ),
            'response213': Response(
                dialogue_id=dialogues_list[42].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle's eyebrows arch in surprise, and then a mischievous grin slowly spreads across his face. It appears that the note holds a playful or intriguing message rather than anything serious but he refuses to tell you unless you guess correctly. You do not enjoy being on the other sside of these games. You refuse to guess, not wanting to give him the satisfaction.",
                outcome=False
            ),
            'response214': Response(
                dialogue_id=dialogues_list[43].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle, takes your sudden movement in stride, and is intrigued by your stark response. He leans closer and whispers, 'Easy there, partner. No need to make a run for it just yet'. You panic. What does he know??",
                outcome=False
            ),
            'response215': Response(
                dialogue_id=dialogues_list[44].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle chuckles at the contents of the note. He leans in and says, 'We'll I may have some playful competition here', and winks. You share an intense and magical moment or eye contact then continue on with the wildest and most exhilerating night of your life.",
                outcome=True
            ),
            'response216': Response(
                dialogue_id=dialogues_list[45].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle's eye sparkle with interest at what you write. You slide your note slowly across the table. Laughter fills the air as he sees the game tic-tac-toe drawn out. Your date night is a memorable one.",
                outcome=False
            ),
            'response217': Response(
                dialogue_id=dialogues_list[46].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle, known for his quick wit, raises an eyebrow and leans in, his curiosity piqued. 'Well, someone's a party pooper,' he remarks, his tone laced with playful sarcasm. Sneezle grabs the note out of the Muk mug before it's completely destroyed. He's not here to play love games.",
                outcome=False
            ),
            'response218': Response(
                dialogue_id=dialogues_list[47].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle slowly pushes his chair back from the table, stands up, and moonwalks out of the saloon. Sneezle immediately got the Star-Spangled ICK.",
                outcome=False
            ),
            'response219': Response(
                dialogue_id=dialogues_list[48].id, 
                goblin_id=sneezle.id, 
                response=
                "Sneezle, always up for a bit of mischief, glances at you with a dark grin. 'What's the magic word?' he teases. You hold your breath, 'Please?'. With a playful chuckle, Sneezle hands over the note. You unfold it carefully, and as you read the cryptic message, a smile spreads across your face. The server had noticed Sneezle had toilet paper on his boot and discreetly letting him know. You both break out into loud, giddy laughter and feel the connection deepen between you.",
                outcome=True
            ),
            'response220': Response(
                dialogue_id=dialogues_list[49].id, 
                goblin_id=sneezle.id, 
                response=
                "After a small struggle, you manage to snatch the note, your fingers smearing the words with Muk and your face a picture of triumph. Sneezle, obviously startled, takes a moment to process what just happened, then bursts into laughter at the absurdity of the situation. His infectious mirth fills the brewery. As you unfold the note, the message reveals itself to be a flyer for a local band playing tonight. Sneezle can't control his laughter and you are red with embarrasment. You crawl under the table to hide from all the other goblins laughing at you.",
                outcome=False
            ),
            'response221': Response(
                dialogue_id=dialogues_list[40].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response222': Response(
                dialogue_id=dialogues_list[41].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response223': Response(
                dialogue_id=dialogues_list[42].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response224': Response(
                dialogue_id=dialogues_list[43].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response225': Response(
                dialogue_id=dialogues_list[44].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response226': Response(
                dialogue_id=dialogues_list[45].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response227': Response(
                dialogue_id=dialogues_list[46].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response228': Response(
                dialogue_id=dialogues_list[47].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response229': Response(
                dialogue_id=dialogues_list[48].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response230': Response(
                dialogue_id=dialogues_list[49].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response231': Response(
                dialogue_id=dialogues_list[40].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response232': Response(
                dialogue_id=dialogues_list[41].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response233': Response(
                dialogue_id=dialogues_list[42].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response234': Response(
                dialogue_id=dialogues_list[43].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response235': Response(
                dialogue_id=dialogues_list[44].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response236': Response(
                dialogue_id=dialogues_list[45].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response237': Response(
                dialogue_id=dialogues_list[46].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response238': Response(
                dialogue_id=dialogues_list[47].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response239': Response(
                dialogue_id=dialogues_list[48].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response240': Response(
                dialogue_id=dialogues_list[49].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response241': Response(
                dialogue_id=dialogues_list[40].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response242': Response(
                dialogue_id=dialogues_list[41].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response243': Response(
                dialogue_id=dialogues_list[42].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response244': Response(
                dialogue_id=dialogues_list[43].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response245': Response(
                dialogue_id=dialogues_list[44].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response246': Response(
                dialogue_id=dialogues_list[45].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response247': Response(
                dialogue_id=dialogues_list[46].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response248': Response(
                dialogue_id=dialogues_list[47].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response249': Response(
                dialogue_id=dialogues_list[48].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response250': Response(
                dialogue_id=dialogues_list[49].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_6 = {
            'response251': Response(
                dialogue_id=dialogues_list[50].id, 
                goblin_id=grubnub.id, 
                response=
                "With a playful smile, you turn to Grubnub and suggest, 'How about we add a little excitement to the evening? Let's play a dine and dash trick.'"
            "\n\nGrubnub's eyes light up with enthusiasm, clearly taking your words literally. 'Dine and dash? Sounds like an adventure!' he exclaims, misunderstanding your playful intent. 'Lead the way!' Grubnub leaves the money on the table and stands up, waiting for you to lead him."
            "\n\nAmused by his genuine excitement, you decide to make it a second date. 'Absolutely,' you respond, taking Grubnub's hand intimately. Hand in hand, you leave the Rotten Elder Tree Saloon and stroll under the starlit sky."
            "\n\nAs you walk together, the romantic ambiance of the night envelops you both. Under the gentle glow of the stars, you share an intimate moment, and your lips meet in a tender kiss, sealing the enchantment of the evening. It's a perfect ending to a truly magical date.",
                outcome=False
            ),
            'response252': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=grubnub.id, 
                response=
                "The server places the check on your table as the night's enchanting journey comes to a close. With a confident yet playful glint in your eye, you slide the bill gracefully toward Grubnub. 'Mind taking care of this?' you inquire, a teasing smile dancing on your lips."
            "\n\nGrubnub meets your gaze, his eyes twinkling with warmth as he accepts the unspoken offer. 'Certainly,' he responds with a gentle nod."
            "\n\nAs Grubnub takes charge of the bill, the evening concludes gracefully. You both leave the Rotten Elder Tree Saloon with contented smiles.",
                outcome=True
            ),
            'response253': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment nears its end, you decide to have a bit of fun. With a sly grin, you pretend to have forgotten your wallet, even though it's safely tucked in your pocket. You turn to Grubnub, your eyes dancing with mischief, and ask him if he would kindly cover the bill as you have forgotten your wallet."
            "\n\nGrubnub blinks in surprise, momentarily taken aback by your request. He scans the table as if looking for your wallet, then his face brightens with a warm smile. 'Oh, not a problem at all!' he replies cheerfully, happy to help."
            "\n\nThe night concludes with a hint of mischievous glee as Grubnub happily pays for the bill, completely unaware of your playful deception. You both leave the Rotten Elder Tree Saloon with smiles. Him because he thinks the date went well, and you because you got away with it--again.",
                outcome=False
            ),
            'response254': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment nears its end, the server places the check on your table, signifying the conclusion of your delightful date. Suddenly, you eagerly reach for the bill, wanting to make a good impression in front of Grubnub, though thriftiness is a part of your nature."
            "\n\nGrubnub's eyes widen in surprise at your enthusiasm, but he reaches for the check as well. 'Oh, you don't have to do that all on your own,' he says, his tone warm and sincere. 'Let me help cover the cost.'"
            "\n\nAfter the bill is settled, you both rise from your seats and walk out of the Rotten Elder Tree Saloon arm in arm, bathed in the soft glow of starlight. The night's romance is undeniable, and beneath the shimmering stars, you share a lingering, tender kiss.",
                outcome=True
            ),
            'response255': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment draws to a close, the server discreetly places the check on your table, a mere formality in your eyes. Lost in the enchanting world of your date's beautiful, sparkling, swamp-green eyes, you barely register the presence of the bill. Honeymoon phase bliss envelops you, transcending the mundane world around you."
            "\n\nGrubnub, his cheeks flushed with a deep crimson, swiftly takes care of the bill, his gaze filled with bashful adoration for you. The moment is electric, and an unspoken understanding hangs in the air."
            "\n\nWith a bold and graceful movement, you lean in, closing the distance between you and Grubnub. The world seems to fade away as your lips meet in a passionate, intimate kiss. It's a kiss filled with longing, desire, and a connection that defies words. The night's enchantment reaches its pinnacle, and as you part from the kiss, a shared, knowing look passes between you."
            "\n\nUnder the starlit sky, you both walk away from the Rotten Elder Tree Saloon, hand in hand, your hearts entwined in a bond that's stronger than ever. The memory of the kiss lingers in the air.",
                outcome=True
            ),
            'response256': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment nears its end, the server places the check on your table, signaling the conclusion of your delightful date. Without missing a beat, you playfully snatch the bill and start a game of keep away. It's a classic move you've used to break the ice on many dates, and it often brings a smile to your companion's face."
            "\n\nGrubnub, however, doesn't react with the usual amusement. Instead, a flush of embarrassment tints his cheeks as he watches you. He's a goblin with a heart of gold, and he genuinely wanted to contribute."
            "\n\nSeeing his discomfort, you decide to end the playful game and reluctantly take responsibility for the bill. 'Alright, alright,' you concede with a smile, though you can't help but feel a pang of guilt. The air between you becomes noticeably awkward as you pay the bill, and the night concludes on an uneasy note."
            "\n\nYou both leave the Rotten Elder Tree Saloon with a sense of tension, the night's adventure ending with an undercurrent of awkwardness.",
                outcome=False
            ),
            'response257': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment nears its end, the server places the check on your table, signaling the conclusion of your date. You brace yourself for the standoff to come, but Grubnub seems blissfully unaware of your stubbornness."
            "\n\nWith a warm and gentle smile, Grubnub reaches for the bill, his actions motivated by a genuine desire to take care of the expenses. 'Don't worry about it,' he says kindly as he settles the payment. 'It was my pleasure.'"
            "\n\nThe night concludes with Grubnub happily paying for the bill, leaving you with a sense of gratitude. You both leave the Rotten Elder Tree Saloon with a feeling of contentment, the evening's adventure ending on a friendly and carefree note.",
                outcome=False
            ),
            'response258': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment nears its end, the server places the check on your table, signaling the conclusion of your delightful date. You can't help but feel a twinge of uncertainty about having to pay on your first date, so you decide to push the check across the table."
            "\n\nGrubnub, with his characteristic kindness, swiftly reaches for the bill, his friendly smile unaffected by the matter of payment. 'No worries,' he says warmly as he takes care of it. 'It was great spending time with you.'"
            "\n\nThe night concludes with a simple and friendly goodnight from Grubnub. You both leave the Rotten Elder Tree Saloon with a sense of camaraderie, the evening's adventure ending on a cordial note, without any romantic undertones.",
                outcome=False
            ),
            'response259': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=grubnub.id, 
                response=
                "As the night's enchantment draws to a close, the server discreetly places the check on your table, marking the conclusion of your delightful date. The question of who should take care of the bill hangs in the air, creating a sweet tension that mirrors the evening's romance."
            "\n\nGrubnub, his gaze locked with yours, senses your inner turmoil and gently reaches for the bill. His touch is tender, his smile filled with understanding. 'Allow me,' he says softly, as if sealing the moment with an unspoken promise."
            "\n\nWith a flutter of your heart, you let Grubnub handle the payment. The atmosphere is charged with the energy of a budding romance as you both exit the Rotten Elder Tree Saloon, arm in arm, leaving behind a night to remember, wrapped in the warmth of his embrace.",
                outcome=True
            ),
            'response260': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=grubnub.id, 
                response=
                "In a daring move, you seize the check before it even touches the table and proudly throw your card down, determined to make a grand gesture. With uncontainable enthusiasm, you stand up, clamber onto the table, and declare in a booming voice that you'll cover the tab for the entire bar."
            "\n\nYour proclamation catches the attention of the other goblin patrons, and soon enough, you find yourself surrounded by admiring onlookers, with several goblin men trying their luck to impress you."
            "\n\nAmid the growing crowd, Grubnub stands off to the side, visibly awkward and bashful. He seems uncertain in the midst of the attention and the newfound suitors vying for your favor. Eventually, Grubnub quietly slips away into the night, leaving you in the company of your admirers."
            "\n\nAs you revel in the attention of the other goblin men, you finally notice Grubnub has dissappeared. You hope he is doing okay, but it seems you won't find out.",
                outcome=False
            ),
            'response261': Response(
                dialogue_id=dialogues_list[50].id, 
                goblin_id=sneezle.id, 
                response=
                "Your playful spirit takes charge as you suggest a dine and dash trick to Sneezle, a challenge to see if he shares your sense of fun. With a playful glint in your eye, you propose, 'Hey, how about a dine and dash?'"
            "\n\nSneezle's face lights up with excitement, and he nods enthusiastically. 'I love it! Let's make this unforgettable!'"
            "\n\nAs you both execute the daring dine and dash with a flair for the dramatic, the adrenaline rushes through your veins, and laughter bubbles forth. Sneezle, not one to hold back, sweeps you into an exuberant embrace. The moment is electric, and Sneezle plants a spontaneous yet surprisingly intimate kiss on your lips."
            "\n\nThe night concludes with shared laughter and a lingering sense of thrill, leaving you both eager for more daring escapades and unforgettable moments together.",  
                outcome=True
            ),
            'response262': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=sneezle.id, 
                response=
                "Without hesitation, you swiftly grab the check and slide it over to Sneezle, 'A Princess does not pay!"
            "\n\nSneezle, however, arches an eyebrow and smirks in mock exaggeration. 'Your Highness,' he quips with a hint of sarcasm, 'how could I forget? Please, allow me to take care of your royal dining expenses.'"
            "\n\nThe playful banter takes a slightly uncomfortable turn as Sneezle, though jesting, appears somewhat annoyed. He pays the bill and, with a sigh that's a mix of amusement and exasperation, he prepares to depart, leaving behind a sense of tension and a lingering feeling that your jest may have struck a nerve.",
                outcome=False
            ),
            'response263': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=sneezle.id, 
                response=
                "In a mischievous move, you feign forgetfulness and act as though you've left your wallet behind, even though it's safely tucked away. You cheekily ask Sneezle to cover the bill."
            "\n\nSneezle's eyes gleam with an unexpected twist as he stands up abruptly. Swift and deftly he pickpockets you, revealing your hidden wallet. He smirks, 'Did you think you had me fooled?', before returning your wallet and placing his half of the payment on the table."
            "\n\nWithout a word, Sneezle stands up, leaving you in an awkward and tense silence. The date ends on an uneasy note, leaving you with a feeling that your attempt at deception may have cost you a friend or lover.",
                outcome=False
            ),
            'response264': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=sneezle.id, 
                response=
                "In a swift and somewhat comical move, you lunge for the check, scattering Muk and peanuts all across the table. You are flush with embarrassment, but do succeed in grabbing the bill."
            "\n\nSneezle bursts into hearty laughter, finding your haste to be utterly hilarious. He clutches his sides, struggling to contain his mirth. 'Oh, you're something else!' he exclaims between fits of laughter."
            "\n\nAmid Sneezle's infectious laughter, you can't help but chuckle yourself, realizing the humor in the situation. With a warm sense of camaraderie and shared laughter, you exit the bar and into the night. As you do, Sneezle takes you by the hand.",
                outcome=True
            ),
            'response265': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=sneezle.id, 
                response=
                "As the check discreetly arrives at your table, you find yourself utterly entranced by the beauty of Sneezle's sparkling swamp-green eyes. Lost in the depths of that captivating gaze, you're transported into a world  where time seems to stand still, and nothing else matters."
            "\n\nIgnoring the bill, Sneezle's affectionate eyes lock onto yours, filled with a deep, romantic intensity. His heart races with the same fervor as yours, and he leans in closer, his lips tenderly meeting yours in a passionate kiss. The world around you fades into obscurity, leaving only the two of you entwined in this amorous moment."
            "\n\nThe kiss is an affirmation of the love and connection you've built throughout the evening. As you part, Sneezle's gaze remains locked onto yours, brimming with adoration and affection."
            "\n\nWith a warm smile, Sneezle takes your hand gently, his fingers intertwining with yours. He leads you away from the table, guiding you toward his hut, a place where the night can continue, and your love can deepen under the starry goblin sky.",
                outcome=True
            ),
            'response266': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=sneezle.id, 
                response=
                "With a mischievous grin, you grab the check and playfully hold it out of Sneezle's reach, knowing that this little game has often been a hit on your dates."
            "\n\nSneezle's eyes light up with amusement, and he joins in the playful banter. You both engage in a brief but delightful game of 'keep away' with the check, the tension gradually building."
            "\n\nAs the laughter subsides, Sneezle reaches out and gently takes the check from your hand. With a warm smile, he places it on the table, and then, in a surprising yet tender moment, he leans in, his lips meeting yours in a sweet and affectionate kiss."
            "\n\nWith the bill now settled, Sneezle takes your hand in his, fingers interlocking intimately. You both leave the restaurant, continuing your date in private, promising more memorable moments to come.",
                outcome=True
            ),
            'response267': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=sneezle.id, 
                response=
                "A tense standoff ensues as both you and Sneezle lock eyes in a playful contest of wills, each refusing to be the first to give in and grab the check."
            "\n\nMoments pass as the standoff continues, the atmosphere charged with anticipation. Sneezle's mischievous smirk gradually transforms into a warm smile, and he finally reaches for the check. With a chuckle, he holds it up and sets it on the table."
            "\n\nBreaking the tension with humor, Sneezle leans in closer and whispers, 'I guess this time, you win, but don't think I won't remember this.' His playful tone is accompanied by a twinkle in his eyes as he plants a tender kiss on your cheek."
            "\n\nAs the evening comes to a close, you share a laugh and leave the restaurant together, your connection deepening with every passing moment, promising more fun and adventures ahead.",
                outcome=True
            ),
            'response268': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=sneezle.id, 
                response=
                "Uncertainty looms over you as the check arrives at your table. A feeling of unease washes over you as you contemplate the implications of having to pay on your first date. In an attempt to navigate this unfamiliar territory, you decide to push the check discreetly across the table towards Sneezle, silently conveying your hope that he'll take care of the bill."
            "\n\nSneezle's expressive eyebrows furrow in mild annoyance as he notices your subtle gesture. Without uttering a word, he reluctantly reaches for the check, a cloud of disappointment lingering in the air. With a resigned sigh, he takes care of the bill and stands up, his demeanor slightly distant."
            "\n\nIn the midst of this uncomfortable moment, Sneezle offers only a curt nod of farewell before leaving the restaurant. The evening ends on a somewhat awkward and chilly note, leaving you with a lingering sense of regret for not handling the situation differently.",
                outcome=False
            ),
            'response269': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=sneezle.id, 
                response=
                "As the check lands on your table, a wave of indecision and panic washes over you. You're caught in a whirlwind of uncertainty, wondering if reaching for the check might offend Sneezle or if not doing so might be equally awkward. Your heart races, and your body tenses under the pressure of the moment."
            "\n\nSneezle, ever quick to pick up on your emotional state, can't help but let out a hearty laugh. He reaches for the check, his laughter punctuating the air like a playful melody. 'Oh, my dear friend,' he chortles, 'I hope you know I'd happily cover this for you!' With a mischievous wink, he takes care of the bill."
            "\n\nYour nervousness begins to fade as Sneezle's laughter and light-hearted teasing alleviate the tension. The two of you part ways, sharing a friendly farewell, knowing that even though the date had its moments of uncertainty, it was an experience worth remembering.",
                outcome=False
            ),
            'response270': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=sneezle.id, 
                response=
                "As the check makes its way to your table, you decide to make a dramatic statement. Without hesitation, you snatch the check before it even touches the table's surface, throwing your card down with a flourish. Your actions take an unexpected turn as you stand up, climbing onto the table itself, and shout at the top of your lungs, 'I'm picking up the tab for the entire bar, my treat!'"
            "\n\nThe goblins in the bar turn their heads in your direction, a mix of surprise and amusement on their faces. Your boldness seems to have won over some of the crowd, and a few goblins cheer in response."
            "\n\nSneezle, however, seems caught off guard by your extravagant gesture. He watches you with a raised eyebrow and a bemused grin, clearly not expecting such a display. After a moment, he chuckles and mutters, 'I didn't know you were hot AND loaded!'"
            "\n\nWith your proclamation echoing in the background, Sneezle decides to join in on the fun. He waves to the bartender and orders a new round for the entire house, adding to the revelry. The two of you spend the evening drinking, laughing, and sharing stories with the other goblins."
            "\n\nAs the night progresses, you find yourselves tenderly holding hands under the table, the connection between you growing stronger with each passing moment. It's a memorable evening, filled with laughter, shared moments, and the warmth of newfound romance.",
                outcome=True
            ),
            'response271': Response(
                dialogue_id=dialogues_list[50].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response272': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response273': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response274': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response275': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response276': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response277': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response278': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response279': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response280': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response281': Response(
                dialogue_id=dialogues_list[50].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response282': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response283': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response284': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response285': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response286': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response287': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response288': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response289': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response290': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response291': Response(
                dialogue_id=dialogues_list[50].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response292': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response293': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response294': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response295': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response296': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response297': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response298': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response299': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response300': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_7 = {
            'response301': Response(
                dialogue_id=dialogues_list[60].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response302': Response(
                dialogue_id=dialogues_list[61].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response303': Response(
                dialogue_id=dialogues_list[62].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response304': Response(
                dialogue_id=dialogues_list[63].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response305': Response(
                dialogue_id=dialogues_list[64].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response306': Response(
                dialogue_id=dialogues_list[65].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response307': Response(
                dialogue_id=dialogues_list[66].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response308': Response(
                dialogue_id=dialogues_list[67].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response309': Response(
                dialogue_id=dialogues_list[68].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response310': Response(
                dialogue_id=dialogues_list[69].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response311': Response(
                dialogue_id=dialogues_list[60].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response312': Response(
                dialogue_id=dialogues_list[61].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response313': Response(
                dialogue_id=dialogues_list[62].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response314': Response(
                dialogue_id=dialogues_list[63].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response315': Response(
                dialogue_id=dialogues_list[64].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response316': Response(
                dialogue_id=dialogues_list[65].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response317': Response(
                dialogue_id=dialogues_list[66].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response318': Response(
                dialogue_id=dialogues_list[67].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response319': Response(
                dialogue_id=dialogues_list[68].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response320': Response(
                dialogue_id=dialogues_list[69].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response321': Response(
                dialogue_id=dialogues_list[60].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response322': Response(
                dialogue_id=dialogues_list[61].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response323': Response(
                dialogue_id=dialogues_list[62].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response324': Response(
                dialogue_id=dialogues_list[63].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response325': Response(
                dialogue_id=dialogues_list[64].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response326': Response(
                dialogue_id=dialogues_list[65].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response327': Response(
                dialogue_id=dialogues_list[66].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response328': Response(
                dialogue_id=dialogues_list[67].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response329': Response(
                dialogue_id=dialogues_list[68].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response330': Response(
                dialogue_id=dialogues_list[69].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response331': Response(
                dialogue_id=dialogues_list[60].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response332': Response(
                dialogue_id=dialogues_list[61].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response333': Response(
                dialogue_id=dialogues_list[62].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response334': Response(
                dialogue_id=dialogues_list[63].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response335': Response(
                dialogue_id=dialogues_list[64].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response336': Response(
                dialogue_id=dialogues_list[65].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response337': Response(
                dialogue_id=dialogues_list[66].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response338': Response(
                dialogue_id=dialogues_list[67].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response339': Response(
                dialogue_id=dialogues_list[68].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response340': Response(
                dialogue_id=dialogues_list[69].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response341': Response(
                dialogue_id=dialogues_list[60].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response342': Response(
                dialogue_id=dialogues_list[61].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response343': Response(
                dialogue_id=dialogues_list[62].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response344': Response(
                dialogue_id=dialogues_list[63].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response345': Response(
                dialogue_id=dialogues_list[64].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response346': Response(
                dialogue_id=dialogues_list[65].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response347': Response(
                dialogue_id=dialogues_list[66].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response348': Response(
                dialogue_id=dialogues_list[67].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response349': Response(
                dialogue_id=dialogues_list[68].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response350': Response(
                dialogue_id=dialogues_list[69].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_8 = {
            'response351': Response(
                dialogue_id=dialogues_list[70].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response352': Response(
                dialogue_id=dialogues_list[71].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response353': Response(
                dialogue_id=dialogues_list[72].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response354': Response(
                dialogue_id=dialogues_list[73].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response355': Response(
                dialogue_id=dialogues_list[74].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response356': Response(
                dialogue_id=dialogues_list[75].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response357': Response(
                dialogue_id=dialogues_list[76].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response358': Response(
                dialogue_id=dialogues_list[77].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response359': Response(
                dialogue_id=dialogues_list[78].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response360': Response(
                dialogue_id=dialogues_list[79].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response361': Response(
                dialogue_id=dialogues_list[70].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response362': Response(
                dialogue_id=dialogues_list[71].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response363': Response(
                dialogue_id=dialogues_list[72].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response364': Response(
                dialogue_id=dialogues_list[73].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response365': Response(
                dialogue_id=dialogues_list[74].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response366': Response(
                dialogue_id=dialogues_list[75].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response367': Response(
                dialogue_id=dialogues_list[76].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response368': Response(
                dialogue_id=dialogues_list[77].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response369': Response(
                dialogue_id=dialogues_list[78].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response370': Response(
                dialogue_id=dialogues_list[79].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response371': Response(
                dialogue_id=dialogues_list[70].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response372': Response(
                dialogue_id=dialogues_list[71].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response373': Response(
                dialogue_id=dialogues_list[72].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response374': Response(
                dialogue_id=dialogues_list[73].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response375': Response(
                dialogue_id=dialogues_list[74].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response376': Response(
                dialogue_id=dialogues_list[75].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response377': Response(
                dialogue_id=dialogues_list[76].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response378': Response(
                dialogue_id=dialogues_list[77].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response379': Response(
                dialogue_id=dialogues_list[78].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response380': Response(
                dialogue_id=dialogues_list[79].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response381': Response(
                dialogue_id=dialogues_list[70].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response382': Response(
                dialogue_id=dialogues_list[71].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response383': Response(
                dialogue_id=dialogues_list[72].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response384': Response(
                dialogue_id=dialogues_list[73].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response385': Response(
                dialogue_id=dialogues_list[74].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response386': Response(
                dialogue_id=dialogues_list[75].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response387': Response(
                dialogue_id=dialogues_list[76].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response388': Response(
                dialogue_id=dialogues_list[77].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response389': Response(
                dialogue_id=dialogues_list[78].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response390': Response(
                dialogue_id=dialogues_list[79].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response391': Response(
                dialogue_id=dialogues_list[70].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response392': Response(
                dialogue_id=dialogues_list[71].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response393': Response(
                dialogue_id=dialogues_list[72].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response394': Response(
                dialogue_id=dialogues_list[73].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response395': Response(
                dialogue_id=dialogues_list[74].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response396': Response(
                dialogue_id=dialogues_list[75].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response397': Response(
                dialogue_id=dialogues_list[76].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response398': Response(
                dialogue_id=dialogues_list[77].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response399': Response(
                dialogue_id=dialogues_list[78].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response400': Response(
                dialogue_id=dialogues_list[79].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_9 = {
            'response401': Response(
                dialogue_id=dialogues_list[80].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response402': Response(
                dialogue_id=dialogues_list[81].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response403': Response(
                dialogue_id=dialogues_list[82].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response404': Response(
                dialogue_id=dialogues_list[83].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response405': Response(
                dialogue_id=dialogues_list[84].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response406': Response(
                dialogue_id=dialogues_list[85].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response407': Response(
                dialogue_id=dialogues_list[86].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response408': Response(
                dialogue_id=dialogues_list[87].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response409': Response(
                dialogue_id=dialogues_list[88].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response410': Response(
                dialogue_id=dialogues_list[89].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response411': Response(
                dialogue_id=dialogues_list[80].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response412': Response(
                dialogue_id=dialogues_list[81].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response413': Response(
                dialogue_id=dialogues_list[82].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response414': Response(
                dialogue_id=dialogues_list[83].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response415': Response(
                dialogue_id=dialogues_list[84].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response416': Response(
                dialogue_id=dialogues_list[85].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response417': Response(
                dialogue_id=dialogues_list[86].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response418': Response(
                dialogue_id=dialogues_list[87].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response419': Response(
                dialogue_id=dialogues_list[88].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response420': Response(
                dialogue_id=dialogues_list[89].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response421': Response(
                dialogue_id=dialogues_list[80].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response422': Response(
                dialogue_id=dialogues_list[81].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response423': Response(
                dialogue_id=dialogues_list[82].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response424': Response(
                dialogue_id=dialogues_list[83].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response425': Response(
                dialogue_id=dialogues_list[84].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response426': Response(
                dialogue_id=dialogues_list[85].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response427': Response(
                dialogue_id=dialogues_list[86].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response428': Response(
                dialogue_id=dialogues_list[87].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response429': Response(
                dialogue_id=dialogues_list[88].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response430': Response(
                dialogue_id=dialogues_list[89].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response431': Response(
                dialogue_id=dialogues_list[80].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response432': Response(
                dialogue_id=dialogues_list[81].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response433': Response(
                dialogue_id=dialogues_list[82].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response434': Response(
                dialogue_id=dialogues_list[83].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response435': Response(
                dialogue_id=dialogues_list[84].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response436': Response(
                dialogue_id=dialogues_list[85].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response437': Response(
                dialogue_id=dialogues_list[86].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response438': Response(
                dialogue_id=dialogues_list[87].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response439': Response(
                dialogue_id=dialogues_list[88].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response440': Response(
                dialogue_id=dialogues_list[89].id, 
                goblin_id=grimble.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response441': Response(
                dialogue_id=dialogues_list[80].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response442': Response(
                dialogue_id=dialogues_list[81].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response443': Response(
                dialogue_id=dialogues_list[82].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response444': Response(
                dialogue_id=dialogues_list[83].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response445': Response(
                dialogue_id=dialogues_list[84].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response446': Response(
                dialogue_id=dialogues_list[85].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response447': Response(
                dialogue_id=dialogues_list[86].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response448': Response(
                dialogue_id=dialogues_list[87].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response449': Response(
                dialogue_id=dialogues_list[88].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response450': Response(
                dialogue_id=dialogues_list[89].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        all_responses = list(responses_1.values()) + list(responses_2.values()) + list(responses_3.values()) + list(responses_4.values()) + list(responses_5.values()) + list(responses_6.values()) + list(responses_7.values()) + list(responses_8.values()) + list(responses_9.values())
        db.session.add_all(all_responses)
        db.session.commit()

        print("Creating outcomes...")

        outcomes_1 = {
            "outcome1": Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="Though your game of Baseball with Grubnub was eventful, it seems your actions did not fully spark their heart.", result = False),
            "outcome2": Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="It seems your time spent playing Baseball with Grubnub was well received. His affection for you has grown intensly", result = True),
            "outcome3": Outcome(date_id = date1.id, goblin_id=sneezle.id, outcome_description="Though your game of Baseball with Sneezle was eventful, it seems your actions did not fully spark their heart.", result = False),
            "outcome4": Outcome(date_id = date1.id, goblin_id=sneezle.id, outcome_description="It seems your time spent playing Baseball with Sneezle was well received. His affection for you has grown intensly", result = True),
            "outcome5": Outcome(date_id = date1.id, goblin_id=blort.id, outcome_description="Though your game of Baseball with Blort was eventful, it seems your actions did not fully spark their heart", result = False),
            "outcome6": Outcome(date_id = date1.id, goblin_id=blort.id, outcome_description="It seems your time spent playing Baseball with Blort was well received. His affection for you has grown intensly", result = True),
            "outcome7": Outcome(date_id = date1.id, goblin_id=grimble.id, outcome_description="Though your game of Baseball with Grimble was eventful, it seems your actions did not fully spark their heart", result =False),
            "outcome8": Outcome(date_id = date1.id, goblin_id=grimble.id, outcome_description="It seems your time spent playing Baseball with Grimble was well received. His affection for you has grown intensly", result = True),
            "outcome9": Outcome(date_id = date1.id, goblin_id=zongo.id, outcome_description="Though your game of Baseball with Zongo was eventful, it seems your actions did not fully spark their heart", result = False),
            "outcome10": Outcome(date_id = date1.id, goblin_id=zongo.id, outcome_description="It seems your time spent playing Baseball with Zongo was well received. His affection for you has grown intensly", result = True),
        }
        outcomes_2 = {
            "outcome11": Outcome(date_id = date2.id, goblin_id=grubnub.id, outcome_description="Though your date with Grubnub at the bar was eventfull, it seems you didnt leave a long lasting impression on him.", result = False),
            "outcome12": Outcome(date_id = date2.id, goblin_id=grubnub.id, outcome_description="Your time spent with Grubnub has had a big impact on him, his love seems to be blooming for you", result = True),
            "outcome13": Outcome(date_id = date2.id, goblin_id=sneezle.id, outcome_description="Though your date with Sneezle at the bar was eventfull, it seems you didnt leave a long lasting impression on him.", result = False),
            "outcome14": Outcome(date_id = date2.id, goblin_id=sneezle.id, outcome_description="Your time spent with Sneezle has had a big impact on him, his love seems to be blooming for you", result = True),
            "outcome15": Outcome(date_id = date2.id, goblin_id=blort.id, outcome_description="Test_Outcome_Blort_Good", result = False),
            "outcome16": Outcome(date_id = date2.id, goblin_id=blort.id, outcome_description="Test_Outcome_Blort_Bad", result = True),
            "outcome17": Outcome(date_id = date2.id, goblin_id=grimble.id, outcome_description="Test_Outcome_Grimble_Good", result =False),
            "outcome18": Outcome(date_id = date2.id, goblin_id=grimble.id, outcome_description="Test_Outcome_Grimble_Bad", result = True),
            "outcome19": Outcome(date_id = date2.id, goblin_id=zongo.id, outcome_description="Test_Outcome_Zongo_Good", result = False),
            "outcome20": Outcome(date_id = date2.id, goblin_id=zongo.id, outcome_description="Test_Outcome_Zongo_Bad", result = True),
        }
        outcomes_3 = {
            "outcome1": Outcome(date_id = date3.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_Grubnub_Good", result = False),
            "outcome2": Outcome(date_id = date3.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_Grubnub_Bad", result = True),
            "outcome3": Outcome(date_id = date3.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_Sneezle_Good", result = False),
            "outcome4": Outcome(date_id = date3.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_Sneezle_Bad", result = True),
            "outcome5": Outcome(date_id = date3.id, goblin_id=blort.id, outcome_description="Test_Outcome_Blort_Good", result = False),
            "outcome6": Outcome(date_id = date3.id, goblin_id=blort.id, outcome_description="Test_Outcome_Blort_Bad", result = True),
            "outcome7": Outcome(date_id = date3.id, goblin_id=grimble.id, outcome_description="Test_Outcome_Grimble_Good", result =False),
            "outcome8": Outcome(date_id = date3.id, goblin_id=grimble.id, outcome_description="Test_Outcome_Grimble_Bad", result = True),
            "outcome9": Outcome(date_id = date3.id, goblin_id=zongo.id, outcome_description="Test_Outcome_Zongo_Good", result = False),
            "outcome10": Outcome(date_id = date3.id, goblin_id=zongo.id, outcome_description="Test_Outcome_Zongo_Bad", result = True),
        }
        db.session.add_all(outcomes_1.values())
        db.session.add_all(outcomes_2.values())
        db.session.commit()
        
        
        
        
        
        
        