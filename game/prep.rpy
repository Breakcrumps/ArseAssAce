init -1 python:
  from itertools import product

style say_label:
  italic True

init python:
  def alphabet_from_to(first: str, last: str) -> str:
    return [chr(x) for x in range(ord(first), ord(last) + 1)]

  def make_sprite(name: str, left: str, right: str, head: str) -> None:
    img = Composite((960, 960), (0, 0), f"{name}/{left}l.png", (0, 0), f"{name}/{right}r.png", (0, 1), f"{name}/{head}.png")
    renpy.image(f"{name} {left}{right}{head}", img)

  def make_body_sprite(name: str, body: str, head: str) -> None:
    img = Composite((960, 960), (0, 0), f"{name}/{body}.png", (0, 1), f"{name}/{head}.png")
    renpy.image(f"{name} {body}{head}", img)

  def make_casual_sprite(name: str, left: str, right: str, head: str) -> None:
    img = Composite((960, 960), (0, 0), f"{name}/{left}bl.png", (0, 0), f"{name}/{right}br.png", (0, 1), f"{name}/{head}.png")
    renpy.image(f"{name} {left}{right}b{head}", img)

  def make_casual_sprite_body_priority(name: str, left: str, right: str, head: str) -> None:
    img = Composite((960, 960), (0, 1), f"{name}/{head}.png", (0, 0), f"{name}/{left}bl.png", (0, 0), f"{name}/{right}br.png")
    renpy.image(f"{name} {left}{right}b{head}", img)

  def make_casual_body_sprite(name: str, body: str, head: str) -> None:
    img = Composite((960, 960), (0, 0), f"{name}/{body}b.png", (0, 1), f"{name}/{head}.png")
    renpy.image(f"{name} {body}b{head}", img)

  def make_casual_body_sprite_body_priority(name: str, body: str, head: str) -> None:
    img = Composite((960, 960), (0, 1), f"{name}/{head}.png", (0, 0), f"{name}/{body}b.png")
    renpy.image(f"{name} {body}b{head}", img)
  
  def make_default_sprite(name: str, left: str, right: str, head: str) -> None:
    img = Composite((960, 960), (0, 0), f"{name}/{left}l.png", (0, 0), f"{name}/{right}r.png", (0, 1), f"{name}/{head}.png")
    renpy.image(f"{name}", img)