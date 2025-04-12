init python:
  def debug_monika_sprites() -> None:
    head_symbols = alphabet_from_to('a', 'r')

    sprite_names = [
      f"monika {l}{r}{head}"
      for head in head_symbols
      for l, r in product("12", repeat=2)
    ]

    sprite_names += ["monika 3a", "monika 3b"]

    monika(f"{len(sprite_names)} in total, Nick!")

    index = 1

    for sprite_name in sprite_names:
      renpy.show(sprite_name)
      monika(f"{index}! Sprite {sprite_name}. {len(sprite_names) - index} left.")
      index += 1