init python:
  def define_sayori_sprites() -> None:
    default = Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
    renpy.image("sayori", default)

    renpy.image("sayori 3a", Image("sayori/3a.png"))
    renpy.image("sayori 3b", Image("sayori/3b.png"))
    renpy.image("sayori 3c", Image("sayori/3c.png"))
    renpy.image("sayori 3d", Image("sayori/3d.png"))

    sayori_head_chars = alphabet_from_to('a', 'y')

    for a1, a2 in product("12", repeat=2):
      for head_char in sayori_head_chars:
        make_sprite("sayori", *f"{a1}{a2}{head_char}")
        make_casual_sprite("sayori", *f"{a1}{a2}{head_char}")