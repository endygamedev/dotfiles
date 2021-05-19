import geocoder
import pyowm


API_KEY = '1ac0da7a5d9554746448427fab700f70'
owm = pyowm.OWM(API_KEY)


g = geocoder.ip('me')
mgr = owm.weather_manager()
observation = mgr.weather_at_place(g.address)
w = observation.weather
print(w.temperature('celsius')['feels_like'])
