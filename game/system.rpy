init python:
  import ctypes

  screen_width = ctypes.windll.user32.GetSystemMetrics(0)
  screen_height = ctypes.windll.user32.GetSystemMetrics(1)
