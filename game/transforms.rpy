transform sprite_zoom:
  zoom 1.1
transform bg:
  xalign .5
  yalign .5
  xsize screen_width
  ysize screen_height

transform hop:
  ease .1 yalign 0.
  pause .05
  ease .1 yalign 1.
transform right_hop:
  right
  ease .1 yalign 0.
  pause .05
  ease .1 yalign 1.
transform left_hop:
  left
  ease .1 yalign 0.
  pause .05
  ease .1 yalign 1.

transform duck:
  ease .3 yalign 1.5

transform restand:
  ease .1 yalign 1.

transform slide_left:
  ease .2 left
transform slide_right:
  ease .2 right
transform slide_center:
  ease .2 center

transform bopped:
  linear .05:
    yalign .95
    zoom 1.1
  linear .1:
    yalign .5
    zoom 1.