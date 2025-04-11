init -1 python:
  from itertools import product

init python:
  def debug_monika_sprites() -> None:
    head_symbols = [chr(x) for x in range(ord('a'), ord('r') + 1)]

    sprite_names = [
      f"monika {l}{r}{head}"
      for head in head_symbols
      for l, r in product("12", repeat=2)
    ]

    monika(f"{len(sprite_names)} in total, Nick!")

    index = 1

    for sprite_name in sprite_names:
      renpy.show(sprite_name)
      monika(f"{index}! Sprite {sprite_name}. {len(sprite_names) - index} left.")
      index += 1
  
  def debug_sayori_sprites() -> None:
    head_symbols = [chr(x) for x in range(ord('a'), ord('y') + 1)]

    sprite_names = [
      f"sayori {l}{r}{'b' if b else ''}{head}"
      for head in head_symbols
      for l, r in product("12", repeat=2)
      for b in (0, 1)
    ]

    sayori(f"I can look {len(sprite_names)} ways.")

    index = 1

    for sprite_name in sprite_names:
      renpy.show(sprite_name)
      sayori(f"{index}. Sprite {sprite_name}. {len(sprite_names) - index} left.")
      index += 1