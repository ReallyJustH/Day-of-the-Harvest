# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define v = Character("V")
image v1 = im.FactorScale("V placeholder 1.png", .80)
image aeri = im.FactorScale("Ae-Ri placeholder 1.png", .80)


# The game starts here.

label start:

    # Intro hook.

    "It is dark. It is cold and wet. My body aches."

    "I can see very well, but I am keenly aware that it is dark - something about that is wrong, right?"

    "I look at my hands. Even with the steady drizzle, I can see splashes of blood on my hands, on my ragged and ripped clothes, on the ground around me."
    
    "I can smell it now - it's a powerful scent, one that cuts through all the other senses I'm being flooded with. I take a moment. I am alone."
    
    #start scene/bg
    scene bg forest
    
    "I look at the wilderness around me, at the cloudy night sky. "
    
    "I feel the damp ground squelch slightly as I stagger to my feet. "

    "I am alone."

    "And I do not know who I am."

    "I check through my clothes - perhaps they will hold a clue."

    "They are torn and stained with mud and blood."

    "My pockets are empty except for a handwritten note - it's bizarrely dry and clean, though by grabbing it, I stain its surface."

    show note:
        xalign .50
        yalign .50

    "Note""I am sorry to leave you in this situation. In time, you will appreciate the gift you recieved tonight."

    "Note""But for tonight, you are no doubt confused and vulnerable."

    "Note" "For that, I apologize."

    "Note" "You do not remember anything. That is normal. Your brain has been rewritten to acclimate you to your new existence - and that has taken away the memories of your former life. "

    "Note" "You are no longer human."

    "Note" "In the most simple terms, you are a vampire."

    hide note

    v "A vampire?"

    v "I know that word, and just seeing it written sincerely here stops me as I read."

    v "Can this even be true?"

    v "What choice do I have but to keep reading?"

    show note:
        xalign .50
        yalign .50

    voice "audio/Recording.mp3"
    "Note" "This comes with a few new facts of life that you must understand."

    "Note" "I felt it was only polite to give you a proper chance at survival, so follow my instructions closely."

    "Note" "1 - Direct sunlight is fatal to you. Even a few seconds of strong sunlight will destroy you utterly."

    "Note" "Seek a reliable shelter as soon as you can."

    "Note" "2 - You must consume human blood to sustain yourself."

    "Note" "Freshness is not critical for survival, but be wary of the thirst that will overtake you."

    "Note" "Seek reliable food to avoid losing yourself to that thirst."

    "Note" "Denying yourself the blood you crave comes with great risk."

    "Note" "3 - You are not human. Humans will fear you if they understand your nature."

    "Note" "They are your prey, not your friends."

    "Note" "4 - Do not try to find me.         -Z"

    v "I take a few moments to re-read the note."

    v "I stare blankly."

    v "I snap to alertness. How long do I have before sunrise?"

    v "I tuck the note back into my pocket to stop it getting any wetter, then start walking in the direction I woke up facing."

    #TODO
    
    v "Bits in parenthesis are for later when we have actual assets to show changes in what is happening, such as speaking vs internal monologue, or reading the note."

    #RANDOM ADDITION FOR SCREENSHOT

    hide note

    show v1:
        xalign 1.00
        yalign 0.0

    show aeri:
        xalign 0.0
        yalign 0.0

    "Ae-RI" "I am sorry to leave you in this situation. In time, you will appreciate the gift you recieved tonight."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # This ends the game.

    return
