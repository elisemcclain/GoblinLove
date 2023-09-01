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
        dialogue1 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait1.id, 
            description="You decide it could be pretty funny to sabotage their game by giving them a bone with a giant crack down its center.")
        dialogue2 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait2.id, 
            description="You find the best bone in the pile and take it for yourself. No way they are beating you. Matter of fact, you think you'll take this bone home. No one else should even have access to it.")
        dialogue3 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait3.id, 
            description="You find a decent bones and wrap a band of leather around each. This will surely help with grip stability.")
        dialogue4 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait4.id, 
            description="You try to pick out the most normal, none threatening bones from the pile for both you and your partner. Better safe than sorry.")
        dialogue5 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait5.id, 
            description="You figure that the best way to play is to be honest. This will be fun either way, and you let your partner pick out their own bone and you just grab whatever's nearby.")
        dialogue6 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait6.id, 
            description="You think that it could be good fun to mix up the game a bit. You decide you should both wear blindfolds!")
        dialogue7 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait7.id, 
            description="You let your partner know that they aren't going to play by their own rules. They're going to play by yours. This isn't going their way.")
        dialogue8 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait8.id, 
            description="You are shocked that you almost forgot to do your pregame ritual! There is only one true way to be safe, and it involves candles, incense and interpretation of the clouds.")
        dialogue9 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait9.id, 
            description="You can't help but wonder what your partner is going to do. You decide to let them take the lead on how the game should be played.")
        dialogue10 = Dialogue(
            date_part= 1, 
            date_id=date1.id, 
            trait_id=trait10.id, 
            description="You decide its a horrible idea to play here. It should be over by the riverbank. The lighting is better and it could be more exciting.")
        

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
        response1 = Response(dialogue_id=dialogue1.id, goblin_id=grubnub.id, response="", outcome=True)
        response2 = Response(dialogue_id=dialogue2.id, goblin_id=grubnub.id, response="Test_Response_2", outcome=False)
        response3 = Response(dialogue_id=dialogue3.id, goblin_id=grubnub.id, response="Test_Response_3", outcome=False)
        response4 = Response(dialogue_id=dialogue4.id, goblin_id=grubnub.id, response="Test_Response_1", outcome=True)
        response5 = Response(dialogue_id=dialogue5.id, goblin_id=grubnub.id, response="Test_Response_2", outcome=False)
        response6 = Response(dialogue_id=dialogue6.id, goblin_id=grubnub.id, response="Test_Response_3", outcome=False)
        response7 = Response(dialogue_id=dialogue7.id, goblin_id=grubnub.id, response="Test_Response_1", outcome=True)
        response8 = Response(dialogue_id=dialogue8.id, goblin_id=grubnub.id, response="Test_Response_2", outcome=False)
        response9 = Response(dialogue_id=dialogue9.id, goblin_id=grubnub.id, response="Test_Response_3", outcome=False)
        response10 = Response(dialogue_id=dialogue10.id, goblin_id=grubnub.id, response="Test_Response_1", outcome=True)
        response11 = Response(dialogue_id=dialogue1.id, goblin_id=sneezle.id, response="Test_Response_2", outcome=False)
        response12 = Response(dialogue_id=dialogue2.id, goblin_id=sneezle.id, response="Test_Response_3", outcome=False)
        response13 = Response(dialogue_id=dialogue3.id, goblin_id=sneezle.id, response="Test_Response_2", outcome=False)
        response14 = Response(dialogue_id=dialogue4.id, goblin_id=sneezle.id, response="Test_Response_3", outcome=False)
        response15 = Response(dialogue_id=dialogue5.id, goblin_id=sneezle.id, response="Test_Response_2", outcome=False)
        response16 = Response(dialogue_id=dialogue6.id, goblin_id=sneezle.id, response="Test_Response_3", outcome=False)
        response17 = Response(dialogue_id=dialogue7.id, goblin_id=sneezle.id, response="Test_Response_2", outcome=False)
        response18 = Response(dialogue_id=dialogue8.id, goblin_id=sneezle.id, response="Test_Response_3", outcome=False)
        response19 = Response(dialogue_id=dialogue9.id, goblin_id=sneezle.id, response="Test_Response_2", outcome=False)
        response20 = Response(dialogue_id=dialogue10.id, goblin_id=sneezle.id, response="Test_Response_3", outcome=False)
        response21 = Response(dialogue_id=dialogue1.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response22 = Response(dialogue_id=dialogue2.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response23 = Response(dialogue_id=dialogue3.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response24 = Response(dialogue_id=dialogue4.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response25 = Response(dialogue_id=dialogue5.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response26 = Response(dialogue_id=dialogue6.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response27 = Response(dialogue_id=dialogue7.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response28 = Response(dialogue_id=dialogue8.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response29 = Response(dialogue_id=dialogue9.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response30 = Response(dialogue_id=dialogue10.id, goblin_id=blort.id, response="Test_Response_3", outcome=False)
        response31 = Response(dialogue_id=dialogue1.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response32 = Response(dialogue_id=dialogue2.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response33 = Response(dialogue_id=dialogue3.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response34 = Response(dialogue_id=dialogue4.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response35 = Response(dialogue_id=dialogue5.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response36 = Response(dialogue_id=dialogue6.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response37 = Response(dialogue_id=dialogue7.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response38 = Response(dialogue_id=dialogue8.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response39 = Response(dialogue_id=dialogue9.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response40 = Response(dialogue_id=dialogue10.id, goblin_id=grimble.id, response="Test_Response_3", outcome=False)
        response41 = Response(dialogue_id=dialogue1.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response42 = Response(dialogue_id=dialogue2.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response43 = Response(dialogue_id=dialogue3.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response44 = Response(dialogue_id=dialogue4.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response45 = Response(dialogue_id=dialogue5.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response46 = Response(dialogue_id=dialogue6.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response47 = Response(dialogue_id=dialogue7.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response48 = Response(dialogue_id=dialogue8.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response49 = Response(dialogue_id=dialogue9.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        response50 = Response(dialogue_id=dialogue10.id, goblin_id=zongo.id, response="Test_Response_3", outcome=False)
        
        responses = [response1, response2, response3]
        db.session.add_all(responses)
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
        
        
        
        
        
        
        