init python:
  def scene(image: str) -> None:
    renpy.scene()
    renpy.show(image, at_list=(bg,))
    renpy.with_statement(Dissolve(.3))

  def scene_with(image: str, transition) -> None:
    renpy.scene()
    renpy.show(image, at_list=(bg,))
    renpy.with_statement(transition)

  def show(image: str) -> None:
    renpy.show(image, at_list=(sprite_zoom,))

  def show_at(image: str, at: list) -> None:
    renpy.show(image, at_list=(sprite_zoom, *at))

  def show_at_with(image: str, at: list, transition) -> None:
    renpy.show(image, at_list=(sprite_zoom, *at))
    renpy.with_statement(transition)

  def show_with(image: str, transition) -> None:
    renpy.show(image, at_list=(sprite_zoom, center))
    renpy.with_statement(transition)

  def hide(character: str, transition) -> None:
    renpy.hide(character)
    renpy.with_statement(transition)