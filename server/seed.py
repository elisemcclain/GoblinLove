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
            description="Zongo thinks he is the smartest goblin to ever live. He finds comfort in knowing he is the best that there ever will be. He isn't looking for a partner, really. He just wants someone to suck up to him. He's just lucky he's so handsome."
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
            'dialogue31': Dialogue(date_part=1, date_id=date2.id, trait_id=trait1.id, description="You realize that after a couple mugs of Muk, you might convince them to join your plan to overthrow the goblin government."),
            'dialogue32': Dialogue(date_part=1, date_id=date2.id, trait_id=trait2.id, description="You agree, but only on the condition that they pay for all your Muk. They must also present you with a goblin made tiara because you deserve it, but mostly to show everyone at the Rotten Elder Tree Saloon that you're better than them."),
            'dialogue33': Dialogue(date_part=1, date_id=date2.id, trait_id=trait3.id, description="You debate if it's worth it, but decide if you go, you might could spark jealousy amongst the other goblin boys so they all fight over your love."),
            'dialogue34': Dialogue(date_part=1, date_id=date2.id, trait_id=trait4.id, description="You waffle back and forth for 7 hours before agreeing, but you refuse to drink the provided Muk in case it has been poisoned. Instead, you bring your own Muk from home."),
            'dialogue35': Dialogue(date_part=1, date_id=date2.id, trait_id=trait5.id, description="You can't say yes quick enough. You just know in your goblin heart that this goblin is the one. The Muk is just lubricant for your heart."),
            'dialogue36': Dialogue(date_part=1, date_id=date2.id, trait_id=trait6.id, description="You let him wait for a response so he can squirm a bit, but you're already planning out what great jokes you'll tell your partner over a good mug of Muk."),
            'dialogue37': Dialogue(date_part=1, date_id=date2.id, trait_id=trait7.id, description="You love Muk, but you DON'T like being told what to do. You begrudingly agree, but it'll be the last time that happens."),
            'dialogue38': Dialogue(date_part=1, date_id=date2.id, trait_id=trait8.id, description="You are stoked for this date, but you can ONLY wear the color orange, no matching socks, and we must bring a worm to sacrifice to the Muk Lord."),
            'dialogue39': Dialogue(date_part=1, date_id=date2.id, trait_id=trait9.id, description="You haven't been to this local saloon yet, so you're intrigued. It'll be your first time trying Muk!"),
            'dialogue40': Dialogue(date_part=1, date_id=date2.id, trait_id=trait10.id, description="You say yes before you check your calendar. Shoot, you are supposesd to go on a date with Poorg. Oh well! (Poor Poorg)"),
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
            'dialogue81': Dialogue(date_part=3, date_id=date3.id, trait_id=trait1.id, description="You feel a grin spread across your googly goblin face. You knew a warm bowl of Bungle Stew would get them wanting more (love & cuddless).",
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
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
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
            'response87': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=blort.id, 
                response=
                "In a moment of seriousness, you find yourself unusually superstitious. Turning to Grimble with a grave expression, you share your concern, 'Grimble, call it a hunch, but I can't shake this feeling. Something about this child... it's like a dark cloud hanging over us. We should find their parents quickly, or who knows what might happen.'"
"\n\nGrimble's eyes widen in surprise, his typically carefree demeanor momentarily giving way to contemplation. 'Of course. We should help this child and put your mind at ease.'"
"\n\nYou continue to express your unease to Grimble, explaining your fears about the potential consequences."
"\n\nGrimble's response is measured. 'Let's not take any chances then.'"
"\n\nAs you and Grimble join forces to assist the child in their search for their parents, Grimble's presence serves as a steadying influence. Eventually, the child's parents are located, and you share a nod of reassurance with Grimble."
"\n\nGrimble's tone is thoughtful as he speaks. 'It's good to trust your instincts sometimes.' The date continues on a more cautious note as you both enjoy the baseball game and the unity you've established.",
                outcome=True
            ),
            'response88': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response89': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response90': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response91': Response(
                dialogue_id=dialogues_list[10].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response92': Response(
                dialogue_id=dialogues_list[11].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response93': Response(
                dialogue_id=dialogues_list[12].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response94': Response(
                dialogue_id=dialogues_list[13].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response95': Response(
                dialogue_id=dialogues_list[14].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response96': Response(
                dialogue_id=dialogues_list[15].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response97': Response(
                dialogue_id=dialogues_list[16].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response98': Response(
                dialogue_id=dialogues_list[17].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response99': Response(
                dialogue_id=dialogues_list[18].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response100': Response(
                dialogue_id=dialogues_list[19].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_3 = {
            'response101': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response102': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response103': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
            ),
            'response104': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response105': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response106': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response107': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response108': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response109': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response110': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response111': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response112': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response113': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response114': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response115': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response116': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response117': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response118': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response119': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response120': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response121': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response122': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response123': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False,
            ),
            'response124': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response125': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response126': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response127': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response128': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response129': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response130': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response131': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response132': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response133': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response134': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response135': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response136': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response137': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response138': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response139': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response140': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response141': Response(
                dialogue_id=dialogues_list[20].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response142': Response(
                dialogue_id=dialogues_list[21].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response143': Response(
                dialogue_id=dialogues_list[22].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response144': Response(
                dialogue_id=dialogues_list[23].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response145': Response(
                dialogue_id=dialogues_list[24].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response146': Response(
                dialogue_id=dialogues_list[25].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response147': Response(
                dialogue_id=dialogues_list[26].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response148': Response(
                dialogue_id=dialogues_list[27].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response149': Response(
                dialogue_id=dialogues_list[28].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response150': Response(
                dialogue_id=dialogues_list[29].id, 
                goblin_id=zongo.id, 
                response=
                "Testing",
                outcome=False
            ),
        }
        responses_4 = {
            'response151': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response152': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response153': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response154': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response155': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response156': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response157': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response158': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response159': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response160': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response161': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response162': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response163': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response164': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response165': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response166': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response167': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response168': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response169': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response170': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response171': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response172': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response173': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response174': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response175': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response176': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response177': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response178': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response179': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response180': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response181': Response(
                dialogue_id=dialogues_list[30].id, 
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response182': Response(
                dialogue_id=dialogues_list[31].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response183': Response(
                dialogue_id=dialogues_list[32].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response184': Response(
                dialogue_id=dialogues_list[33].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response185': Response(
                dialogue_id=dialogues_list[34].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response186': Response(
                dialogue_id=dialogues_list[35].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response187': Response(
                dialogue_id=dialogues_list[36].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response188': Response(
                dialogue_id=dialogues_list[37].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response189': Response(
                dialogue_id=dialogues_list[38].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response190': Response(
                dialogue_id=dialogues_list[39].id, 
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response232': Response(
                dialogue_id=dialogues_list[41].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response233': Response(
                dialogue_id=dialogues_list[42].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response234': Response(
                dialogue_id=dialogues_list[43].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response235': Response(
                dialogue_id=dialogues_list[44].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response236': Response(
                dialogue_id=dialogues_list[45].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response237': Response(
                dialogue_id=dialogues_list[46].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response238': Response(
                dialogue_id=dialogues_list[47].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response239': Response(
                dialogue_id=dialogues_list[48].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response240': Response(
                dialogue_id=dialogues_list[49].id, 
                goblin_id=blort.id, 
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
                "Testing",
                outcome=False
            ),
            'response252': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response253': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response254': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response255': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response256': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response257': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response258': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response259': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response260': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=grubnub.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response261': Response(
                dialogue_id=dialogues_list[50].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response262': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response263': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response264': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response265': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response266': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response267': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response268': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response269': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response270': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=sneezle.id, 
                response=
                "Testing",
                outcome=False
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
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response282': Response(
                dialogue_id=dialogues_list[51].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response283': Response(
                dialogue_id=dialogues_list[52].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response284': Response(
                dialogue_id=dialogues_list[53].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response285': Response(
                dialogue_id=dialogues_list[54].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response286': Response(
                dialogue_id=dialogues_list[55].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response287': Response(
                dialogue_id=dialogues_list[56].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response288': Response(
                dialogue_id=dialogues_list[57].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response289': Response(
                dialogue_id=dialogues_list[58].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response290': Response(
                dialogue_id=dialogues_list[59].id, 
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response332': Response(
                dialogue_id=dialogues_list[61].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response333': Response(
                dialogue_id=dialogues_list[62].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response334': Response(
                dialogue_id=dialogues_list[63].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response335': Response(
                dialogue_id=dialogues_list[64].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response336': Response(
                dialogue_id=dialogues_list[65].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response337': Response(
                dialogue_id=dialogues_list[66].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response338': Response(
                dialogue_id=dialogues_list[67].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response339': Response(
                dialogue_id=dialogues_list[68].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response340': Response(
                dialogue_id=dialogues_list[69].id, 
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response382': Response(
                dialogue_id=dialogues_list[71].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response383': Response(
                dialogue_id=dialogues_list[72].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response384': Response(
                dialogue_id=dialogues_list[73].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response385': Response(
                dialogue_id=dialogues_list[74].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response386': Response(
                dialogue_id=dialogues_list[75].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response387': Response(
                dialogue_id=dialogues_list[76].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response388': Response(
                dialogue_id=dialogues_list[77].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response389': Response(
                dialogue_id=dialogues_list[78].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response390': Response(
                dialogue_id=dialogues_list[79].id, 
                goblin_id=blort.id, 
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
                goblin_id=blort.id, 
                response=
                "Testing",  
                outcome=False
            ),
            'response432': Response(
                dialogue_id=dialogues_list[81].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response433': Response(
                dialogue_id=dialogues_list[82].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response434': Response(
                dialogue_id=dialogues_list[83].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response435': Response(
                dialogue_id=dialogues_list[84].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response436': Response(
                dialogue_id=dialogues_list[85].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response437': Response(
                dialogue_id=dialogues_list[86].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response438': Response(
                dialogue_id=dialogues_list[87].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response439': Response(
                dialogue_id=dialogues_list[88].id, 
                goblin_id=blort.id, 
                response=
                "Testing",
                outcome=False
            ),
            'response440': Response(
                dialogue_id=dialogues_list[89].id, 
                goblin_id=blort.id, 
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
        all_responses = list(responses_1.values()) + list(responses_2.values()) + list(responses_3.values()) 
        db.session.add_all(all_responses)
        db.session.commit()

        print("Creating outcomes...")

        outcomes_1 = {
            "outcome1": Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_Grubnub_Good", result = False),
            "outcome2": Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_Grubnub_Bad", result = True),
            "outcome3": Outcome(date_id = date1.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_Sneezle_Good", result = False),
            "outcome4": Outcome(date_id = date1.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_Sneezle_Bad", result = True),
            "outcome5": Outcome(date_id = date1.id, goblin_id=blort.id, outcome_description="Test_Outcome_Blort_Good", result = False),
            "outcome6": Outcome(date_id = date1.id, goblin_id=blort.id, outcome_description="Test_Outcome_Blort_Bad", result = True),
            "outcome7": Outcome(date_id = date1.id, goblin_id=grimble.id, outcome_description="Test_Outcome_Grimble_Good", result =False),
            "outcome8": Outcome(date_id = date1.id, goblin_id=grimble.id, outcome_description="Test_Outcome_Grimble_Bad", result = True),
            "outcome9": Outcome(date_id = date1.id, goblin_id=zongo.id, outcome_description="Test_Outcome_Zongo_Good", result = False),
            "outcome10": Outcome(date_id = date1.id, goblin_id=zongo.id, outcome_description="Test_Outcome_Zongo_Bad", result = True),
        }
        outcomes_2 = {
            "outcome11": Outcome(date_id = date2.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_Grubnub_Good", result = False),
            "outcome12": Outcome(date_id = date2.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_Grubnub_Bad", result = True),
            "outcome13": Outcome(date_id = date2.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_Sneezle_Good", result = False),
            "outcome14": Outcome(date_id = date2.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_Sneezle_Bad", result = True),
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
        db.session.commit()
        
        
        
        
        
        
        