init python:
  def define_natsuki_sprites() -> None:
    make_default_sprite("natsuki", *"11a")

    natsuki_head_chars = alphabet_from_to('a', 'z')
    natsuki_turned_head_chars = alphabet_from_to('a', 'i')

    for a1, a2 in product("12", repeat=2):
      for head_char in natsuki_head_chars:
        make_sprite("natsuki", *f"{a1}{a2}{head_char}")
        make_casual_sprite("natsuki", *f"{a1}{a2}{head_char}")
      for head_char in natsuki_turned_head_chars:
        make_sprite("natsuki", *f"{a1}{a2}", f"2t{head_char}")
        make_casual_sprite("natsuki", *f"{a1}{a2}", f"2bt{head_char}")

    for head_char in natsuki_head_chars:
      img = Composite((960, 960), (0, 0), f"natsuki/3.png", (18, 22), f"natsuki/{head_char}.png")
      renpy.image(f"natsuki 3{head_char}", img)

      img = Composite((960, 960), (0, 0), f"natsuki/3b.png", (18, 22), f"natsuki/{head_char}.png")
      renpy.image(f"natsuki 3b{head_char}", img)