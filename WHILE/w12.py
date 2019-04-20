import pyglet

music = pyglet.resource.media('cello.wav')
music.play()

pyglet.app.run()