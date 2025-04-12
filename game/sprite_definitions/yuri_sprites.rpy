init python:
  def define_yuri_sprites() -> None:
    make_default_sprite("yuri", *"11a")

    yuri_head_chars = alphabet_from_to('a', 'w')
    yuri_indexed_head_chars = alphabet_from_to('a', 'e')

    for a1, a2 in "11", "12", "22":
      for head_char in yuri_head_chars:
        make_sprite("yuri", *f"{a1}{a2}{head_char}")
        make_casual_sprite_body_priority("yuri", *f"{a1}{a2}{head_char}")
    
    for head_char in yuri_indexed_head_chars:
      make_body_sprite("yuri", "3", f"{head_char}2")