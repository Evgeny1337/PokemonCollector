import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
from django.utils.timezone import localtime


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    print('heh', image_url)
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons = PokemonEntity.objects.filter(
        appeared_at__lte=localtime(), disappeared_at__gte=localtime())
    print("test:", len(pokemons))
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
    all_pokemons = Pokemon.objects.all()
    pokemon_entities = PokemonEntity.objects.filter(
        pokemon__id=pokemon_id, appeared_at__lte=localtime(), disappeared_at__gte=localtime())
    if len(pokemon_entities) <= 0:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')
    pokemon = all_pokemons.get(id=pokemon_id)
    pre_evol = pokemon.parent
    next_evol = all_pokemons.filter(parent__id=pokemon_id).first()
    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon.image.url)
        )
    pokemon_structure = {"pokemon_id": pokemon.id,
                         "img_url": pokemon.image.url, "title_en": pokemon.title_en, "title_jp": pokemon.title_jp, "title_ru": pokemon.title, "description": pokemon.description}
    if pre_evol:
        pokemon_structure['previous_evolution'] = {
            "title_ru": pre_evol.title, "pokemon_id": pre_evol.id, "img_url": pre_evol.image.url}
    if next_evol:
        pokemon_structure["next_evolution"] = {
            "title_ru": next_evol.title, "pokemon_id": next_evol.id, "img_url": next_evol.image.url}
    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_structure
    })
