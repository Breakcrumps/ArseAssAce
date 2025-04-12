init python:
  def scene(image: str, transition=Dissolve(.3), *, at=[]) -> None:
    renpy.scene()
    renpy.show(image, at_list=(bg, *at))
    renpy.with_statement(transition)

  def show(image: str, at=(center,), transition=None) -> None:
    renpy.show(image, at_list=(sprite_zoom, *at))
    renpy.with_statement(transition)

  def hide(character: str, transition) -> None:
    renpy.hide(character)
    renpy.with_statement(transition)