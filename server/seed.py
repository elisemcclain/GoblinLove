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
            part_3 = "The game is almost over, you have one last chance to impress them! How do you want to finish things?"
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
        }

        dialogues_2 = {
            'dialogue1': Dialogue(date_part=2, date_id=date1.id, trait_id=trait1.id, description="You realize that after a couple mugs of Muk, you might convince them to join your plan to overthrow the goblin government."),
            'dialogue2': Dialogue(date_part=2, date_id=date1.id, trait_id=trait2.id, description="You agree, but only on the condition that they pay for all your Muk. They must also present you with a goblin made tiara because you deserve it, but mostly to show everyone at the Rotten Elder Tree Saloon that you're better than them."),
            'dialogue3': Dialogue(date_part=2, date_id=date1.id, trait_id=trait3.id, description="You debate if it's worth it, but decide if you go, you might could spark jealousy amongst the other goblin boys so they all fight over your love."),
            'dialogue4': Dialogue(date_part=2, date_id=date1.id, trait_id=trait4.id, description="You waffle back and forth for 7 hours before agreeing, but you refuse to drink the provided Muk in case it has been poisoned. Instead, you bring your own Muk from home."),
            'dialogue5': Dialogue(date_part=2, date_id=date1.id, trait_id=trait5.id, description="You can't say yes quick enough. You just know in your goblin heart that this goblin is the one. The Muk is just lubricant for your heart."),
            'dialogue6': Dialogue(date_part=2, date_id=date1.id, trait_id=trait6.id, description="You let him wait for a response so he can squirm a bit, but you're already planning out what great jokes you'll tell your partner over a good mug of Muk."),
            'dialogue7': Dialogue(date_part=2, date_id=date1.id, trait_id=trait7.id, description="You love Muk, but you DON'T like being told what to do. You begrudingly agree, but it'll be the last time that happens."),
            'dialogue8': Dialogue(date_part=2, date_id=date1.id, trait_id=trait8.id, description="You are stoked for this date, but you can ONLY wear the color orange, no matching socks, and we must bring a worm to sacrifice to the Muk Lord."),
            'dialogue9': Dialogue(date_part=2, date_id=date1.id, trait_id=trait9.id, description="You haven't been to this local saloon yet, so you're intrigued. It'll be your first time trying Muk!"),
            'dialogue10': Dialogue(date_part=2, date_id=date1.id, trait_id=trait10.id, description="You say yes before you check your calendar. Shoot, you are supposesd to go on a date with Poorg. Oh well! (Poor Poorg)"),
        }

        dialogues_3 = {
            'dialogue1': Dialogue(date_part=3, date_id=date1.id, trait_id=trait1.id, description="You love the idea of going to their grotto for a home cooked meal. You can raid their bedroom for secrets and red flags while they aren't looking."),
            'dialogue2': Dialogue(date_part=3, date_id=date1.id, trait_id=trait2.id, description="You would of course expect nothing less than a gourmet home cooked meal. They can cook absolutely everything, and you can enjoy being served delicious hors d'oeuvres. You won't even lift a hairy finger"),
            'dialogue3': Dialogue(date_part=3, date_id=date1.id, trait_id=trait3.id, description="You realize this would be the perfect time to try out the smoked Org Liver Stew recipe you've had your eye on. The recipe was passed down from your great grandgoblinma BawkBawk"),
            'dialogue4': Dialogue(date_part=3, date_id=date1.id, trait_id=trait4.id, description="You try to sway them to get takeout noodles from Olive Gooben, put they insist on cooking. You agree, but bring a snack just in case it's horrendous tasting."),
            'dialogue5': Dialogue(date_part=3, date_id=date1.id, trait_id=trait5.id, description="You are about to loose your marbles you're so fired up with excitement. You just KNOW that a home cooked bowl of warm Beetle Beans is the way to your hungry heart."),
            'dialogue6': Dialogue(date_part=3, date_id=date1.id, trait_id=trait6.id, description="You hope gravy is on the menu because you can't wait to start a grueling food fight in the kitchen. The messier, the better!"),
            'dialogue7': Dialogue(date_part=3, date_id=date1.id, trait_id=trait7.id, description="You are happy to share a home cooked meal, but if it's not half as good as your own Slop Glop Sammy recipe, it's a NO from you, dawg."),
            'dialogue8': Dialogue(date_part=3, date_id=date1.id, trait_id=trait8.id, description="You wager that a home cooked meal is acceptable, but only if it's muggy and the maggots living in your back swamp have no shadow."),
            'dialogue9': Dialogue(date_part=3, date_id=date1.id, trait_id=trait9.id, description="You are anxious to try something new! You are growing so bored of drinking Muk every date. You don't know how much more Muk you can take."),
            'dialogue10': Dialogue(date_part=3, date_id=date1.id, trait_id=trait10.id, description="You say yes before you even realize you're allergic to Nutmeg Borgle Brine Soup they're making."),
        }


        db.session.add_all(dialogues_1.values(), dialogues_2.values(), dialogues_3.values())
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
                response="Zongo's eyebrows shot up in surprise as you revealed your pregame ritual.\n\n"
                "'A ritual for safety, how quaintly superstitious,' he commented not unkindly. He examined the candles and incense.\n\n"
                "With a wave of his hand, Zongo conjured a playful illusion of clouds forming intricate patterns. 'Ah, the interpretation of clouds. I used to spend hours lost in them.'\n\n"
                "After a long moment, he picked up a bone and smiled softly. 'Let's see if your shamanic incantations and cloud-based divinations will sway the cosmic forces in your favor.'",
                outcome=True),
            'response49': Response(
                dialogue_id=dialogues_list[8].id, 
                goblin_id=zongo.id, 
                response="Zongo's eyebrow arched with a mixture of surprise and smug satisfaction as you granted him the authority to lead the game. He smirked, clearly pleased.\n\n"
                "'Ah, finally recognizing my unparalleled genius,' he quipped with an air of self-importance. He looked at the bones with new confidence.\n\n"
                "With a flourish of his hand, Zongo conjured a layer of frost around his chosen bones, making them shine with crystaline brilliance. 'Behold, a game molded by my cold heart!'\n\n"
                "He picked up a bone with a triumphant smile. 'Let the masterpiece begin as I orchestrate an unparalleled symphony. Mind the frostbite, darling.'", 
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

        db.session.add_all(responses_1.values())
        db.session.commit()

        print("Creating outcomes...")

        outcomes = {
            "outcome1": Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_1", result = False),
            "outcome2": Outcome(date_id = date1.id, goblin_id=grubnub.id, outcome_description="Test_Outcome_2", result = True),
            "outcome3": Outcome(date_id = date1.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_3", result = False),
            "outcome4": Outcome(date_id = date1.id, goblin_id=sneezle.id, outcome_description="Test_Outcome_4", result = True),
            "outcome5": Outcome(date_id = date1.id, goblin_id=blort.id, outcome_description="Test_Outcome_5", result = False),
            "outcome6": Outcome(date_id = date1.id, goblin_id=blort.id, outcome_description="Test_Outcome_6", result = True),
            "outcome7": Outcome(date_id = date1.id, goblin_id=grimble.id, outcome_description="Test_Outcome_7", result =False),
            "outcome8": Outcome(date_id = date1.id, goblin_id=grimble.id, outcome_description="Test_Outcome_8", result = True),
            "outcome9": Outcome(date_id = date1.id, goblin_id=zongo.id, outcome_description="Test_Outcome_9", result = False),
            "outcome10": Outcome(date_id = date1.id, goblin_id=zongo.id, outcome_description="Test_Outcome_10", result = True),
        }

        db.session.add_all(outcomes.values())
        db.session.commit()
        
        
        
        
        
        
        