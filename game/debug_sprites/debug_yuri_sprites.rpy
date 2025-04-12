init python:
  def debug_yuri_sprites() -> None:
    head_chars = alphabet_from_to('a', 'w')
    indexed_head_chars = alphabet_from_to('a', 'e')

    sprite_names = [
      f"yuri {l}{r}{'b' if b else ''}{head}"
      for head in head_chars
      for l, r in ("11", "12", "22")
      for b in (0, 1)
    ]

    sprite_names += [
      f"yuri 3{head}2"
      for head in indexed_head_chars
    ]

    yuri(f"You can expect {len(sprite_names)} unique appearances.")

    index = 1

    for sprite_name in sprite_names:
      renpy.show(sprite_name)
      yuri(f"{index}. Sprite {sprite_name}. {len(sprite_names) - index} left.")