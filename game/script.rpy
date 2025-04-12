define monika = Character(name="Monika", color="#60ff7a", image="monika")
define sayori = Character(name="Sayori", color="#7be0ff", image="sayori")
define yuri = Character(name="Yuri", color="#6e28bd", image="yuri")
define natsuki = Character(name="Natsuki", color="#ffa8fb", image="natsuki")
define mc = Character(name="You", color="#9b0000")

label start:
  "Now, what to do..."

  menu:
    "..."

    "Check sprites":
      jump init_sprite_debug

    "Start 'story'":
      window hide
      jump .story

    "Nothing":
      "So be it."
      return

  return

label .story:
  $ scene_with("residential", dissolve)
  pause .5
  window show Dissolve(.5)
  pause .5
  
  mc "{w=.5}I mean,{w=.1} the festival {b}was{/b} fun."

  play music "music/2.ogg"

  mc "But it's more like 80/20.{w} 80 percent effort,{w=.1} 20 percent fun."

  sayori "I mean, you're not wrong."

  $ show_with("sayori 12r", Dissolve(.3))

  sayori "But you had much more fun preparing for it,{w=.3} didn't you?"

  play sound "sounds/bonk.wav"
  $ show_at("sayori 11p", (hop,))

  sayori "Ouch!"
  sayori 22p "Why-y-y?"
  mc "Because I wanted to."

  $ show_at("sayori 3c", (duck,))

  sayori "Meanie."
  mc "Come on, we're gonna be late."

  $ show_at("sayori 22r", (restand,))

  sayori "Yeah, let's go!"

  $ scene_with("corridor", fade)

  "As Sayori and I had parted, the only thing left for me was a lazy stroll towards my classroom."
  "I have no idea if our festival exhibit helped our club at all.{w} I mean, people came to see what we had to offer: cookies, aromata, ..."
  "...poetry..."
  "But, in the end, it really seemed like most people just stayed to drink some tea and enjoy the cookies."
  "That would mean Natsuki's idea fared better when it came to customer retention."
  "However, people that came for cookies probably won't be joining the club."
  "Yuri's idea might bring us new members;{w=.1} with all the atmosphere her aromatic candles brought into the room."
  "Now that I think of it, none of this could nearly be enough.{w} We really needed a strong theme,{w=.1} like the culinary and the occult clubs."
  "Now {b}that{/b} was atmosphere."
  "Too late now, though.{w} How is it we started preparing that late anyway?{w} This should be Monika's responsibility."
  "No way we could rival those clubs with one day's worth of work."

  $ scene_with("class", fade)
  stop music fadeout 4.

  "Classes are exhaustingly unintertaining as always.{w} My head feels heavy after school every single time."
  "But, other than that, I feel great.{w} My thoughts are norm-defyingly clear.{w} I wonder if I got smarter after joining the club."
  "I guess, I did nothing to promote my brain before doing so.{w=.1} So it only makes sense that composing 'poetry' instead of reading manga is all sorts of a step-up."

  sayori "What are you thinking about?"
  mc "How {b}do{/b} you walk so silently?"

  $ show_with("sayori 11q", Dissolve(.3))

  sayori "It's easy.{w=.1} Be light and slim like me."
  mc "Light and slim...?"
  
  $ show_at("sayori 3c", (duck,))

  sayori "Don't make me hit you."
  mc "Remembered your childhood self?"
  sayori 3d "You're asking for it this time."
  
  return