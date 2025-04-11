# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define monika = Character(name="Monika", color="#60ff7a", image="monika")
define sayori = Character(name="Sayori", color="#7be0ff", image="sayori")
define yuri = Character(name="Yuri", color="#6e28bd")
define natsuki = Character(name="Natsuki", color="#ffa8fb")

# The game starts here.

label start:
  scene club at bg with dissolve
  show monika 11a at centered with Dissolve(.3)

  monika "Hello, Nick!"
  
  show monika at west with Dissolve(.3)
  show sayori at east with Dissolve(.3)

  sayori "Hello-hello!"
  monika "So, whose sprites?"

  menu:
    "Whom to check?"

    "Monika":
      jump .monika_sprite_debug
    
    "Sayori":
      jump .sayori_sprite_debug

    "No one":
      monika 11n "Oh, that's OK."

  return

label .continue:
  monika "Anything else, Nick?"

  menu:
    "See anyone else?"

    "Monika":
      jump .monika_sprite_debug

    "Sayori":
      jump .sayori_sprite_debug

label .monika_sprite_debug:
  $ debug_monika_sprites()

  show monika 11a

  jump .continue

label .sayori_sprite_debug:
  $ debug_sayori_sprites()

  show sayori 11a

  jump .continue