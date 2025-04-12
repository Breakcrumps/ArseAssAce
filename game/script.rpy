default mc_name = "Anton Aston"

init python:
  def name() -> str:
    return mc_name.split()[0]
  def last_name() -> str:
    return mc_name.split()[1]

define monika = Character(name="Monika", color="#60ff7a", image="monika")
define sayori = Character(name="Sayori", color="#7be0ff", image="sayori")
define yuri = Character(name="Yuri", color="#6e28bd", image="yuri")
define natsuki = Character(name="Natsuki", color="#ffa8fb", image="natsuki")
define mc = Character(name="[name()]", color="#9b0000")

label start:
  $ scene("black")
  stop music

  "Now, what to do..."

  menu:
    "..."

    "Check sprites":
      jump init_sprite_debug

    "Start 'story'":
      window hide
      jump .story

    "Change name":
      jump .change_name

    "Nothing":
      "So be it."
      return

  return

label .change_name:
  $ mc_name = renpy.input("What do they call me?").strip()

  jump start

label .story:
  $ scene("residential", transition=dissolve)
  pause .5
  window show Dissolve(.5)
  pause .5
  
  mc "{w=.5}I mean,{w=.1} the festival {b}was{/b} fun."

  play music "music/2.ogg"

  mc "But it's more like 80/20.{w} 80 percent effort,{w=.1} 20 percent fun."

  sayori "I mean, you're not wrong."

  $ show("sayori 12r", transition=Dissolve(.3))

  sayori "But you had much more fun preparing for it,{w=.3} didn't you?"

  play sound "sounds/bonk.wav"
  $ show("sayori 11p", at=(hop,))

  sayori "Ouch!"
  sayori 22p "Why-y-y?"
  mc "Because I wanted to."

  $ show("sayori 3c", at=(duck,))

  sayori "Meanie."
  mc "Come on, we're gonna be late."

  $ show("sayori 22r", at=(restand,))

  sayori "Yeah, let's go!"

  $ scene("corridor", transition=fade)

  "As Sayori and I had parted, the only thing left for me was a lazy stroll towards my classroom."
  "I have no idea if our festival exhibit helped our club at all.{w} I mean, people came to see what we had to offer: cookies, aromata, ..."
  "...poetry..."
  "But, in the end, it really seemed like most people just stayed to drink some tea and enjoy the cookies."
  "That would mean Natsuki's idea fared better when it came to customer retention."
  "However, people that came for cookies probably won't be joining the club."
  "Yuri's idea might bring us new members;{w=.1} with all the atmosphere her aromatic candles brought into the room."
  "Now that I think of it, none of this could be nearly enough.{w} We really needed a strong theme,{w=.1} like the culinary and the occult clubs' exhibits."
  "A dark room, its floor dyed with blood, and on it - a glowing pentagram. Crimson particles hovering in the air, the hexagon table with the mystetious hooded figures speaking Latin..."
  "Come to think of it, they were probably {b}in hell{/b} for what they organised there.{w} Our disciple can't have liked the blood aesthetic."
  "On the other hand, a maid cafe from culinary club.{w=.3} Instant classic.{w} Simple, effective."
  "We've got our share of cute girls.{w=.3} I wonder how they'd look in...{w=.3}{nw}"
  "Brrrr.{w} Shake off the sin."
  "What was I...?{w} Ah!"
  "Now {b}that{/b} was atmosphere."
  "Too late to think what we could've done now, though.{w} How is it we started preparing that late anyway?{w} This should be Monika's responsibility."
  "No way we could rival those clubs with one day's worth of work."

  $ scene("class", transition=fade)

  "Classes are exhaustingly unentertaining as always.{w} My head feels heavy after school every single time."
  "But, other than that, I feel great.{w} My thoughts are norm-defyingly clear.{w} I wonder if I got smarter after joining the club."
  "I guess, I did nothing to promote my brain before doing so.{w=.1} So it only makes sense that composing 'poetry' instead of reading manga is all sorts of a step-up."

  sayori "What are you thinking about?"
  mc "How {b}do{/b} you walk so silently?"

  $ show("sayori 11q", transition=Dissolve(.3))

  sayori "It's easy.{w=.1} Be light and slim like me."
  mc "Light and slim...?"
  
  $ show("sayori 3c", at=(duck,))

  sayori "Don't make me hit you."
  mc "Remembered your childhood self?"
  sayori 3d "You're asking for it this time."
  "Hm...{w=.1} But really,{w=.1} how does she support that figure with her diet?{w=.1} (That being chips and ice cream.)"
  "I could almost wrap{nw}"
  $ show("sayori 11n", at=(restand,))
  extend " my palms around it, fingers overlayed.{w} And she did get bigger, too!"
  sayori 11l "[name()]... Where are you looking..."
  mc "{cps=0}...{/cps}"

  $ scene("corridor", fade)

  "Damn..."
  sayori "[name()], now I've got to hit you."
  mc "Please don't. I was just lost in thought."
  sayori "Taking after Yuri?"
  mc "God, you love pointing out how other girls affect my life.{w=.3} An overfixation, Sayori.{w=.3} One might think you're secretly into me."
  sayori "Huh?!"
  pause .1
  sayori "Y-you wish!"
  mc "Ye-e-eah...{w=.1} Just forget it."
  sayori "..."

  pause .5

  play sound "sounds/bonk.wav"
  $ scene("corridor", at=(bopped,), transition=None)

  pause 3.

  mc "You know?{w=.3} I deserve it."

  $ scene("club", fade)

  "The clubroom got so familiar in the three days I've spent here..."

  $ show("sayori", transition=Dissolve(.3))

  sayori "Monika!"
  "Before I could even take a look around, Sayori already spotted Monika digging through things in the closet.{w} And then blasted my eardrum."
  monika "Oh, Sayori!{w} I'll be there!"
  "Monika stood up from her knees and scuttled her way to us."

  $ show("sayori", at=(slide_left,))
  $ show("monika", at=(right,), transition=Dissolve(.1))

  monika "And [name()], too!"

  $ show("monika 3a", at=(right_hop,))

  monika "So, regret stepping foot in the club yet?"
  mc "Playful mood,{w=.1} Monika?"
  monika 12k "It is!{w=.3} We get to keep being a club.{w=.3} And I think our exhibit turned out great, too!"

  $ show("sayori 22r", at=(left_hop,))

  sayori "I agree! We all did our part!"
  monika 12d "Actually,{w=.1} Sayori,{w=.1} you're the only one who{nw}"
  extend 12l " didn't do anything."
  sayori 12o "I provided valuable mental support, Monika!{w=.3}{nw}"
  $ show("sayori 22p", at=(left_hop,))
  extend " Don't be mean!"
  monika 11e "I didn't mean it like that,{w=.1} Sayori.{w} Letting yourself take a rest was a strong and responsible decision."
  $ show("sayori 22r", at=(left_hop,))
  sayori "Yes!{w=.3} I'm very responsible!{w=.3}{nw}"
  extend 12o " And very strong."
  mc "Ve-e-ery."
  "I scratched the place she hit my head in.{w} Now it boasted a small, but itchy bump."
  sayori 11r "He-he."

  jump start

  return