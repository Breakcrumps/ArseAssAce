label init_sprite_debug:
  $ scene("club", Dissolve(.3))
  $ show("monika", transition=Dissolve(.3))

  monika "Hello, Nick!"
  monika "Whose sprites shall we check?"

  call .choice("Whom to check?")

  return

label .continue:
  $ show("monika", transition=Dissolve(.3))

  monika "Anything else, Nick?"

  call .choice("See anyone else?")
  
  return

label .choice(question):
  menu:
    "[question]"

    "Monika":
      call .sprite_debug("monika")
    
    "Sayori":
      call .sprite_debug("sayori")

    "Yuri":
      call .sprite_debug("yuri")

    "Natsuki":
      call .sprite_debug("natsuki")

    "No one":
      $ show("monika 11n", transition=Dissolve(.3))
      monika "Oh, that's OK."
      monika 11a "Then see you soon, Nick!"
      jump start
  
  return

label .sprite_debug(character):
  $ scene("club")
  $ show(character, transition=Dissolve(.3))

  $ exec(f"debug_{character}_sprites()")

  $ hide(character, transition=Dissolve(.3))

  jump .continue