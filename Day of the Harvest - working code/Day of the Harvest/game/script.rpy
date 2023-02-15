# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# The persistent variable saves as a variable in the game. Currently 

define e = Character("CEO")
define persistent.gameDone = None


# The game starts here. This block of text plays before the game starts to provide a content warning to the user of mature content 
label splashscreen:
    scene black
    with Pause(1)

    show text "Content Warning: \n Game contains themes of blood, gore and corruption." with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

return

#this is when you press start on the main menu. It'll set assets such as characters, backgrounds, UI elements. 

label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg room = im.Scale("room.jpg", 2000, 1200)
    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # A score counter is changed by the players based on the choices they make. Based on the amount of points 
    # the player will experience differnt stories 

    image eileen = im.Scale("eileen_happy.png", 1000, 1000)
    show eileen 
    $ score_counter = 0

    # Questionaire starts here. 

    e "Before we continue, please answer the questionaire. This will help us know whether you can survive in this world."
    e "Your final score will determine where you will find yourself in society."

    e "What matters most in this world?"
    menu:

        "My Happiness":
            $ score_counter += 1

        "My comfort":
            $ score_counter -= 1

        "Profit":
            $ score_counter += 2

        "Survival":
            $ score_counter += 1
    
    e "What would you sacrafice to succeed?"
    menu:

        "Happiness":
            $ score_counter 

        "Comfort":
            $ score_counter -= 1

        "My Morals":
            $ score_counter += 1

        "Everything":
            $ score_counter += 2

    
    e "You hold your daughter in your arms. She's so tiny. Her little fingers wrap around your pinkie. 
    She laughs, and her wide black eyes fix on yours. There is not a single thought of sadness in that tiny newborn."
    e "She is so gentle. What do you do?"
    menu:

        "Cherish the moment":
            $ score_counter -= 1

        "Get back to work":
            $ score_counter += 1

    e "A homeless man is lying face down on the ground in front of you. He isn't moving. What do you do?"
    menu:

        "Keep walking":
            $ score_counter += 0


        "Make sure he's okay":
            $ score_counter -= 1
        
        "Put money in his cup":
            $ score_counter -= 2

        "Stomp on him.":
            $ score_counter += 2

    e "Do you hate yourself?"
    menu:

        "Of course i do.":
            $ score_counter += 1

        "Who could possibly love a waste of space?":
            $ score_counter += 1
        
        "I am happy with myself":
            $ score_counter -= 1

        "There is nothing to hate. I am nobody":
            $ score_counter += 2
    
    e "Your daughter is asking you to come play with her. You are finally home after so much time at work, all that overtime. "
    e "She's got a little dirt on her face, but she's beaming."
    e "Daddy, can't you come outside? You look down from your computer. Scrolling text. It's an important deal you've been working on - something that might get you a big promotion if it works. "
    e "But you haven't seen much of your daughter in weeks, you were so busy with the last big deal."
    e "She is smiling. Gleaming brown eyes. Missing front tooth."
    menu:

        "The work can wait. Play with your daughter.":
            $ score_counter -= 1

        "Your daughter will have to wait. This is important.":
            $ score_counter += 1

    e "What is your body?"
    menu:

        "A weakness":
            $ score_counter += 1

        "A part of me.":
            $ score_counter -= 1

        "A parasite that wastes my money.":
            $ score_counter += 2

        "A means to an end":
            $ score_counter += 1
    
    e "What is free time?"
    menu:

        "A sign that I'm not doing enough":
            $ score_counter += 1

        "A moment for reflection.":
            $ score_counter -= 1

        "A time to spend with loved ones":
            $ score_counter -= 2

    e "Your daughter is looking at you from above. 
    You lie in the bed.
    The machine beeps."
    e "She is crying.
    But glaring.
    You have not spoken in years. "
    e" She has grown into a beautiful woman.
    And she has grown to hate you."
    e"You were never there for her.
    Always working, always busy."
    e"When her mother died, you were working.
    When she got married, you were working."
    e"When her first child was born, you were working.
    She is waiting for something."

    e"You don't have long.
    What do you say to her?"
    menu:

        "I'm sorry":
            $ score_counter -= 1

        "I don't say anything at all.":
            $ score_counter += 1

    #first choice with options. Everytime you choose a different option we use flags and labels to show where we want to jump into the story
    #this will be the default way of jumping between stories, and choices that have different text. 
    e "Your childhood toy, Bingo. Head of a soft teddy bear with a body made of a blanket. White fluff turned beige by time. Rip in the corner. Old, but you remember him now. "
    menu:

        "Remember the past":
            $ score_counter -= 1
            jump bingo_bad_flag
            

        "Throw it away.":
            $ score_counter += 1
            jump bingo_good_flag
    
    #bad option jumps
    label bingo_bad_flag:

            e "You remember the times you slept with Bingo, how you used to suck your thumb but your parents told you that you would need braces if you kept doing that, so you held on really close to Bingo to make sure your hand didn't go to your mouth when you slept. "
            menu:
                
                "A soft smile forms on your lips.":
                    $ score_counter -= 3
                    jump bingo_verybad_flag
                
                "You are disgusted":
                    $ score_counter += 1 
                    jump bingo_smart_flag
    
    label bingo_verybad_flag:

            e "You think of more memories. Of running through the cul-de-sac with the others. What were their names? Back when the sky was blue, when there was a horizon. What were their names?"
            menu:
                
                "Try to remember.":
                    $ score_counter -= 3
                    jump bingo_yikes_flag
                
                "It doesn't matter. They are in the past. The future is all that matters.":
                    $ score_counter += 1 
                    jump Bingo_recovered_flag

    

    label bingo_yikes_flag:
            e "They might as well all be dead for all they matter. 
            Then again, seeing as you did this, you are no different."
        
            $ score_counter -= 5
            jump Questionaire_over

    label Bingo_recovered_flag:
            e "Correct."
            $score_counter += 1
            jump Questionaire_over

    
    #good option jumps
    label bingo_good_flag: 
            e "You toss it in the trash and let the lid slam. It's gone, it's trash now. It's where it belongs. What do you feel?"
            menu:
                "Regret.":
                    $ score_counter -= 3
                    jump bingo_tried_flag
                
                "Absolutely nothing.":
                    $ score_counter += 1
                    jump bingo_smart_flag


    label bingo_smart_flag:
            e "Perhaps you aren't as stupid as you look"
            jump Questionaire_over

    label bingo_tried_flag:
    
            e "You were doing so well. But it appears you don't really have the mindset."
            menu:
                "I'm sorry.":
                    $ score_counter -= 5
                    jump bingo_shame_flag
                
                "I have it. This was a moment of weakness":
                    $ score_counter += 1 
                    jump Bingo_salvaged_flag

                "I guess not...":
                    $ score_counter -= 5
                    jump bingo_shame_flag
    
    label bingo_shame_flag:
        e "That's a shame"
        jump Questionaire_over


    label bingo_salvaged_flag:
        e "It better be. For your sake"
        jump Questionaire_over


    # all bingo routes lead to questionaire end. Currently if ceo story is not accessible if the user has not triggered persistetnt flag
    label Questionaire_over:
        e "Your score is [score_counter]"
        if score_counter <= 0:
            jump waste_story
        if score_counter <= 8:
            jump cog_story
        if score_counter < 17:
            jump business_story
        if score_counter >= 16 and persistent.gameDone:
            jump ceo_story



    #waste story 
    label waste_story:
        e "The sky boils and coughs as smoke chokes the sun. You think you saw it once. "
        e" Your body's rent is due. You were born with it, but if you want to keep it from getting a superplague then you need to make an offering to the executives. Rent is up, always up. 
        The market demands sacrifice if it is to thrive. "

        e "A man in a collared shirt is staring at you."

        e "Shit. He saw you. Your filthy body, covered in mods that you were told would help you get a good job but never seemed to. Infected, sickly. He looks terrified, he's covered in sweat, but he's still coming closer."
        e "The great engine of progress has gotten more and more quiet these past few days. Sky red and black haze has faded, but with that visibility and peace comes more risk."
        e" It's the day of the harvest, and you're unemployed.
        Bad day to be outside."

        e "The man is running now. Stop! Listen to me!"
        e"You run faster. You can hear the thick, congested air whistle through one of the holes in your wrist from a botched modification surgery. All around you, signs with WORK and EMBRACE DICIPLINE blur together. "

        e "You trip over a discarded bottle.
        The man's hands are on you within seconds. He wraps his arm around your throat and whispers,I'm so sorry just before the needle plunges into your neck. You black out. "

        e "You come to with dozens of others in a dark space. Based on the shaking and the noise, it must be a truck. Your wrists are bound behind your back, the cord digs into your skin. Your feet are bound too, but not enough to stop you from moving - just enough to make it so you can't run. "
        e" The people are sobbing. Men, women, children. The few who aren't crying are either asleep or barely choking down their whimpers. 
        You all know exactly what's coming. You've seen the televised events."

        e "The Harvest."

        e "The men in collared shirts drag you out, grimacing behind their sunglasses as you are brought into the sound of slow, deep sputtering. An engine with no fuel. You want to appear strong."
        e " But you know what's coming. You forgot your rent, just look at you, there's no chance that putting on a show now will impress them.
        Even with the sky blocked by smog, your eyes take a few seconds to adjust."

        e "The market requires blood. They muttered."

        e "The pit is enormous. A huge circle of concrete overlooking a deep hole, its sides stained increasingly dark shades of brown."
        e" Lines of black trucks pass between a massive wall of skyscrapers that overlook this place. How many have they brought for this harvest? 
        At its center is a massive, incomprehensible machine. Blackened metal, enormous smokestacks, tubes leading nowhere and a dull red glow emanating from it."
        e" Sharp spikes and needles spin across its surface in lazy orbits, chains made of spindles. Each booming sputter of the engine of progress as it struggles to run sounds like the beat of a vast heart. "
        e" The man marches you to the lip of the pit and kicks the back of your leg."
        e" You barely feel it as you fall to your knees. Your eyes are locked on the great engine.
        A transaction must occur."
        e" You feel a hand press your head into place, your throat now right against the rim of the pit."

        e "No need to scream now. You know what's coming."

        e "You feel the blade glide into your throat. 
        The world falls quiet except for the sound of your heart beating out pulse after pulse of your blood across the wall of the pit."
        e "So much red, moving so quickly down the wall.
        The engine pulses in time with your heart.
        Even as it slows."
        e "At least you served some purpose before you died.
        The market grows stronger."

        jump the_end

        
    #cog story
    label cog_story:
 
        e " You stare blankly at the screen as it buzzes. Red, green, blue, all the colors in the world. Your boss is behind you, a towering figure of intricate metal spindles 
        and spikes that reaches towards heaven with every motion. "
        e"The stretched steel skeleton wears a beautiful cashmere suit, it's simply gorgeous. Your suit didn't cost shit. 
        the boss speaks in a chourus of whispers, a dozen voices of business prowess."
        e" The numbers, whelp, how are the numbers?"
        e "You try not to look at the spinning metal form of the boss or his cashmere suit worth more than your car."
        e "The screen shows a rising and falling set of stocks, many colors of potential profit that fluctuate up and down like a heartbeat.
        The beating heart of the world, the transaction of value. But you are no exec, the numbers don't make sense."
        e "You choke on your words."
        "Well, whelp, how are the numbers?"
        
        menu:
                "Good.":

                    jump chopping_block_path
                
                "Bad.":

                    jump sacrafice_block_path

        





    label chopping_block_path:
        e "The line is red. Going down. 
        You try to control your breathing.
        The only thing worse than bad numbers is being caught lying.
        Bad, sir."
        e "The exec screeches, a sound like knives being dragged across metal. Your ears are still ringing as he grips your shoulders and drags you away from your cubicle. "
        e "Not good, not good, whelp! We need those numbers back up! You are reassigned. It's an important day."

        e " The boss loads you to a van with blacked out windows. You climb You are told to remove your suit and tie - you don't want them getting stained more than they already are. You put on some sunglasses - official uniform."
        e" You put in your earplugs - once the Harvest begins in earnest, the engine will deafen you without protection. Finally, you put on a pair of disposable gloves - official policy." 
        e "You step out into the haze at the pit.
        The Harvest is about to begin.
        At least you didn't have to round them up."

        e "You march to the edge of the pit. A woman dressed like you marches a dirty man over to you. He's covered in holes from body mods - remnants of jobs that didn't pan out."
        e " You absently rub the port at the base of your skull - then remember why you are here. A buzz rings over the sound of the engine of progress's thudding heartbeat - the signal to begin."
        e "You stare at the knife in your hand, then down at the filthy waste of space whose head is now sitting over the edge of the pit. You kneel down and put the blade to his throat."

        e "The market is thirsty"
        
        e "Begin the harvest."

        e "You swipe the knife across the man's throat like a card through a reader. Just a swipe, purposeful and smooth. He deserves that much, at least.
        He gurgles as he chokes on his last breath as it bubbles past the flow of blood."
        e" You keep your knee on his back, but he doesn't struggle. A minute passes before he's empty. A co-worker you can't remember the name of comes over to collect the drained body and drag it to the furnace chute. The engine grows louder. 
        At least this will improve the numbers."

        e " Another victim is pushed down to the chopping block. This one is crying, she is begging for a chance to pay her rent, she has the money, she swears.
        She takes another minute to drain."
        e" Just let it happen, there's no point in fighting this. If nobody is sacrificed, the economy would suffer. If the economy suffers, everyone suffers. "
        e" If a few have to have an unpleasant death for you and everyone you know to go to bed with a full belly and a roof over your head, then so be it."
        e" You are sorry for the first few.
        But they blur together."
        e "By the end of the Harvest, your eyes are glazed over and your hands shake. The gloves are filled with sweat."
        e" The engine screams its approval and belches its delight into the sky with clouds of red and black."
        e" You stumble back to the van.
        You get the rest of the day off."

        jump the_end


    label sacrafice_block_path:
        e "The line goes up. Green. You cough out Good! they are good. P-profit!
        The boss's many needle teeth clink in his vast mouth. From the upper jaw all the way down to the collar of his suit is a series of fused needles and metal thorns that tap together one after another. "
        e "Tip-tap, over and over. Click-clack, so much noise. 
        Glad to hear it, worm. Keep working."
        e "He slaps your back, tearing your cheap garbage suit and ripping into your soft human skin. You whimper, but don't say anything." 
        e" This suit isn't worth it. Besides, complaining about pain to an exec means nothing now that they have escaped the feeble state of humanity."
        e" The exec buzzes and clicks. You hear the tap of crisp shoes on the ground as he walks away, but you know that he is still watching you with one of his eyes. Even once he leaves your cubicle, he is watching you. Always."

        e "A few hours of feverish work pass before the intercom buzzes over the clacking of dozens of keyboards. 
        ATTENTION LOYAL WORKERS. THE DAY OF THE HARVEST IS HERE. TURN YOUR ATTENTION TO YOUR SCREENS FOR THIS IMPORTANT MOMENT."
        e "Your eyes unfocus as the wall of numbers is replaced by a grainy view of a massive pit. You've seen this so many times, can't you just skip it? You have a lot of work to do and this is the same every time. "
        e"The pit grows darker and darker as it gets deeper, stained by generations of blood pooling and drying. Rings of filthy people are lined up around the edge of the pit, their heads over the lip."
        e" Behind each sacrifice, a man or woman in a simple collared shirt.  "


        e "The Harvest finally begins"

        e "Each sacrifice's throat is carved open and allowed to drain into the gaping maw. At its center beats the heart of the market, the engine of industry greedily lapping up its offering."
        e" The empty bodies are tossed into a chute added to its furnace. The machine roars louder and louder, eventually rendering the audio of the broadcast silent to prevent damage to the speakers. "
        e "The display continues for minutes. Maybe hours. It's much less nauseating after so many harvests. It's hard to watch, but without a little grease for the gears, how can the market thrive? "
        e " Finally, the broadcast ends. The numbers are definitely good now. Nothing like a little bit of blood to really breathe some life into the economy.
        You keep working. There's a lot more to do today."

        jump the_end


    label business_story:
        e " The CEO stands over you, his head a rotating steel cage of fused needles in the shape of a dodecahedron."
        e" At its center is a single massive, bloodshot eye that twitches back and forth in a blur of rotation, but never lets its foggy pupil off of you. 
        He is so very beautiful."
        e "His hooked fingers reach over to you, whirring as they writhe through the air before suddenly becoming still as they find your suit. "
        e" The CEO has long since forsaken the need for a mouth, and speaks directly into your mind as the raised veins on his massive eye throb and expand.
        Your harvest this year was more than satisfactory. The great transaction continues."
        
        menu:
                "You cry joyfully.":

                    jump joy_path
                
                "You feel regret creep into your heart.":

                    jump regret_path

    label joy_path:
    e "The CEO must be pleased, for he strokes your face with the back of his massive skeletal hand, not letting his blades sink into your soft human flesh.
    You know, Anders, you might have what it takes to be an exec after all. What do you say? "

    e "All your dicipline has paid off.
    All your hours of grind, all your sacrifices."
    e "The saws come towards your soft flesh and you do not flinch as they open you up. The pain is excrutiating, but you have come much too far to let that stop you. "
    e" Piece by piece, they peel off the parts of yourself that you don't need. You are a perfect engine of profit, a being with none of the weaknesses you once had.
    Last is your heart."
    e" You weren't using it much anyway.
    Your bonus is going to be huge this quarter.
    No more sleep. No more need for dreams when your dream has finally been realized, after all."

    e "Your new body is so sharp. The world is so bright, moves so slowly. So much noise, so many angles you can view.
    Behind the veil of this world is an endless series of transactions, a perfect system where energy all moves towards those who truly deserve it."
    e" You are so very beautiful now.
    The numbers are good. "


    e "You recieved the promotion you were working for after all. So many bodies, and you should be proud! But even though you are an exec, you aren't a CEO yet - there's still worlds of profit to be made."

    jump the_end


    label regret_path: 

    e " You think of the screams."
    e "So many people harvested this year."
    e "Of course, the surplus population must be dealt with somehow. If they aren't willing to work, why bother living?"
    e "You think of the youngest one in that crowd, a thin boy with ripped sweatpants. Couldn't have been much more than 15. Must have been a dropout."
    e "You think of his blood gushing from the jagged slash in his throat, of the pool of gore at the bottom of the pit as your underlings held the sacrifices down and drained them."
    e "The sound of rumbling deep in the pit."
    e "A great machine roared to life, refueled."
    e "The sky blackensed as the great engine of industry began to howl again, its vents greedily slurping the sacrificial blood as the dried husks are tossed into its waiting furnace."
    e "But you let doubt into your mind."
    e "You return to reality."
    e "The CEO's eye is focused on you."
    menu:
            "Apologize":

                jump death_path
            
            "Accept your fate .":

                jump almost_path

    label death_path:
    
    e "The CEO does not hesitate. You don't even have time to react before your head is in multiple pieces, your brain matter splattered across the marble floor."
    e "A janitor is already rushing in before your body is cold. Fortunately, not a single drop of gore got on your suit - the CEO recognizes value when he sees it."
    e "Unfortunately, you proved you didn't have what it takes."

    jump the_end



    label almost_path:

    e "The eye rolls away and focuses outside the window, letting the spindly body of the CEO follow shortly after in a lazy pirouette. His enormous arms cross behind him, twitching and writhing at the tips of his fingers.  "

    e "That's what I like about you, Anders. You might be a low-rent waste of space, but you know never to apologize."

    e "His voice is a hoarse whisper, a choke from a strangled throat."
    
    e " Maybe if you put in some real elbow grease, you might still be an exec."
    e " You nod, barely believing that such a show of weakness went unpunished."
    e "Leave. I'll see you in the boardroom. tomorrow. His eye whirls back to fix you with a final, baleful stare."
    e "And everywhere else."

    e "Close, but not quite! You must purge your mind of weakness and embrace the grind if you wish to truly succeed!"

    jump the_end



    label ceo_path:

    e "Your time was first.
    Your family was second.
    Your body was third.
    Your life was last."

    e "But now you are perfect"
    e "Look directly into the market and see its pulse beat wildly as the world chokes on its blood and the heart of profit gets faster and faster."
    e "Your body is gone and you never needed it because you were never truly there. You are a husk puppetted by desire and greed and you are perfect now."
    e "Your many eyes spin wildly in the cage of metal you built for them. No lids to close, no time wasted on sleep. You are beyond what you once thought possible. No hunger, no need for anything at all."


    e "You are an executive now, a perfected engine of masterful beauty. Women fall before you in horror and awe as the worthless rabble scream in adoration. You abandoned them long ago, their cries of fear and exultation mean nothing to a perfect being."
    e "You are beyond them."
    e "You are exquisite and perfect and finally pure."
    e" Reach up to the sky with your long sharp fingers and feel them slip beneath the skin of the world. Feel it tear as you pull it apart into a new form that pleases you. What is the world to you? Nothing, not even a home. It is a resource, a trophy, a source of entertainment. "
    e" Drink their blood, steal their air, watch them beg to join you from every direction as your spinning cage of eyes focuses on the horrified and blind faces of all the filthy people."

    e " They are nothing to you"

    e "You are everything"

    e " Congratulations! You have the CEO mindset! You know what matters and hive the drive to achieve it!
    ou must be proud!"  
    
    jump the_end

    


        # ... the game continues here
    label the_end:

    e " This is the end of the game."

    if persistent.gameDone:
    
        e "Alternate path has been unlocked."
        
    $ persistent.gameDone = True

    # This ends the game.

    return
