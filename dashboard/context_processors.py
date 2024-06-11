

def theme_processor(request):
    theme = request.COOKIES.get('theme', 'dark')  # Varsayılan olarak dark theme kullan
    return {'theme': theme}