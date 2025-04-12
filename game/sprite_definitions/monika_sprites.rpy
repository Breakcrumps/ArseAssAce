init python:
  def define_monika_sprites() -> None:
    default = Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
    renpy.image("monika", default)

    renpy.image("monika 3a", Image("monika/3a.png"))
    renpy.image("monika 3b", Image("monika/3b.png"))

    monika_head_chars = alphabet_from_to('a', 'r')

    for a1, a2 in product("12", repeat=2):
      for head_char in monika_head_chars:
        make_sprite("monika", *f"{a1}{a2}{head_char}")