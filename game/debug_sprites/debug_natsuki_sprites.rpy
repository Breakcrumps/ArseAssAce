init python:
  def debug_natsuki_sprites() -> None:
    head_chars = alphabet_from_to('a', 'z')
    turned_head_chars = alphabet_from_to('a', 'i')

    sprite_names = [
      f"natsuki {l}{r}{'b' if b else ''}{head}"
      for head in head_chars
      for l, r in product("12", repeat=2)
      for b in (0, 1)
    ]

    sprite_names += [
      f"natsuki {l}{r}{'b' if b else ''}2{'b' if b else ''}t{head}"
      for head in turned_head_chars
      for l, r in product("12", repeat=2)
      for b in (0, 1)
    ]

    sprite_names += [
      f"natsuki 3{'b' if b else ''}{head}"
      for head in head_chars
      for b in (0, 1)
    ]

    natsuki(f"OK, so I can count {len(sprite_names)} combinations.")
    natsuki("Here we go.")

    index = 1

    for sprite_name in sprite_names:
      renpy.show(sprite_name)
      natsuki(f"{index}. Sprite {sprite_name}. {len(sprite_names) - index} left.")
      index += 1