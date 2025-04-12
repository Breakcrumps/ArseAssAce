init python:
  def debug_sayori_sprites() -> None:
    head_chars = alphabet_from_to('a', 'y')

    sprite_names = [
      f"sayori {l}{r}{'b' if b else ''}{head}"
      for head in head_chars
      for l, r in product("12", repeat=2)
      for b in (0, 1)
    ]

    sprite_names += [
      "sayori 3a",
      "sayori 3b",
      "sayori 3c",
      "sayori 3d",
    ]

    sayori(f"I can look {len(sprite_names)} different ways.")

    index = 1

    for sprite_name in sprite_names:
      renpy.show(sprite_name)
      sayori(f"{index}. Sprite {sprite_name}. {len(sprite_names) - index} left.")
      index += 1