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
transform duck:
  ease .3 yalign 1.5
transform restand:
  ease .1 yalign 1.