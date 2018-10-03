def lang_genoeg():
    if lengte >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein!'

lengte = int(input('Wat is je lengte in cm? '))
print(lang_genoeg())