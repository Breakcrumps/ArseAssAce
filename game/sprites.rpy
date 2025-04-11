init python:
  def define_monika_sprites() -> None:
    default = Composite((960, 960), (0, 0), "monika/1l.png", (0, 0), "monika/1r.png", (0, 0), "monika/a.png")
    renpy.image("monika", default)

    renpy.image("monika 3a", Image("monika/3a.png"))
    renpy.image("monika 3b", Image("monika/3b.png"))

    monika_head_symbols = [chr(x) for x in range(ord('a'), ord('r') + 1)]

    for a1, a2 in product("12", repeat=2):
      for head_symbol in monika_head_symbols:
        img = Composite((960, 960), (0, 0), f"monika/{a1}l.png", (0, 0), f"monika/{a2}r.png", (0, 0), f"monika/{head_symbol}.png")
        renpy.image(f"monika {a1}{a2}{head_symbol}", img)

  def define_sayori_sprites() -> None:
    default = Composite((960, 960), (0, 0), "sayori/1l.png", (0, 0), "sayori/1r.png", (0, 0), "sayori/a.png")
    renpy.image("sayori", default)

    renpy.image("sayori 3a", Image("sayori/3a.png"))
    renpy.image("sayori 3b", Image("sayori/3b.png"))
    renpy.image("sayori 3c", Image("sayori/3c.png"))
    renpy.image("sayori 3d", Image("sayori/3d.png"))

    sayori_head_symbols = [chr(x) for x in range(ord('a'), ord('y') + 1)]

    for a1, a2 in product("12", repeat=2):
      for head_symbol in sayori_head_symbols:
        for casual in 0, 1:
          b = 'b' if casual else ''
          img = Composite((960, 960), (0, 0), f"sayori/{a1}{b}l.png", (0, 0), f"sayori/{a2}{b}r.png", (0, 0),f"sayori/{head_symbol}.png")
          renpy.image(f"sayori {a1}{a2}{b}{head_symbol}", img)
  
  define_monika_sprites()
  define_sayori_sprites()