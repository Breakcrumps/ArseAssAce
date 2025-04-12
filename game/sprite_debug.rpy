label init_sprite_debug:
  $ scene_with("club", Dissolve(.3))
  $ show_with("monika", Dissolve(.3))

  monika "Hello, Nick!"
  monika "Whose sprites shall we check?"

  call .choice("Whom to check?")

  return

label .continue:
  $ show_with("monika", Dissolve(.3))

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
      $ show_with("monika 11n", Dissolve(.3))
      monika "Oh, that's OK."
  
  return

label .sprite_debug(character):
  $ scene("club")
  $ show_with(character, Dissolve(.3))

  $ exec(f"debug_{character}_sprites()")

  $ hide(character, Dissolve(.3))

  jump .continue