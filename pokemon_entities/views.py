import folium


from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    time_now = localtime()
    pokemons = PokemonEntity.objects.filter(
        appeared_at__lte=time_now, disappeared_at__gte=time_now)
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons:
        add_pokemon(
            folium_map, pokemon.latitude,
            pokemon.longitude,
            request.build_absolute_uri(pokemon.pokemon.image.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': pokemon.image.url,
            'title_ru': pokemon.title,
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    time_now = localtime()
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    pokemon_entities = pokemon.entities.filter(
        pokemon__id=pokemon_id, appeared_at__lte=time_now, disappeared_at__gte=time_now)
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon.image.url)
        )
    pokemon_structure = {"pokemon_id": pokemon.id,
                         "img_url": pokemon.image.url, "title_en": pokemon.title_en, "title_jp": pokemon.title_jp, "title_ru": pokemon.title, "description": pokemon.description}
    previous_evolution = pokemon.parent
    if previous_evolution:
        pokemon_structure['previous_evolution'] = {
            "title_ru": previous_evolution.title, "pokemon_id": previous_evolution.id, "img_url": previous_evolution.image.url}
    next_evolution = pokemon.children.first()
    if next_evolution:
        pokemon_structure["next_evolution"] = {
            "title_ru": next_evolution.title, "pokemon_id": next_evolution.id, "img_url": next_evolution.image.url}
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_structure
    })
