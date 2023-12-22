import requests
from discord.ext import commands
from difflib import get_close_matches
import random

url = "https://api.memegen.link/templates/"
user_agent = "windows:mydiscordbot:v1.0.0"
response = requests.get(url)
templates = response.json()
template_names = [template['name'] for template in templates]
name_to_id = {d['name']: d['id'] for d in templates}
name_to_sample = {d['name']: d['example']['url'] for d in templates}
subreddits = {"dank": "dankmemes", "dank2": "dank_meme", "anime": "animemes", "wholesome": "wholesomememes",
              "gay": "gaymemes", "programmer": "ProgrammerHumour", "memes": "memes", "meirl": "me_irl", "hmm": "hmm",
              "anime2": "goodanimemes", "anime-irl": "anime_irl", "desi": "indiandankmemes", "desi2": "dankinindia"}
if_no_meme = "https://api.memegen.link/images/ams/where_is/where_is_the_template.png"


def generate_meme(template, *args):

    text = args
    matching_name = get_closest_matching_name(template)
    meme_id = get_meme_id(matching_name)
    meme_url = f"https://api.memegen.link/images/{meme_id}/{'/'.join(text)}.jpg"

    return meme_url


def get_meme(genre=None, image_format=None):
    if genre is None or genre == "":
        genre = random.choice(list(subreddits.keys()))
    if image_format is None or image_format == "":
        image_format = ".jpg"
    headers = {'User-agent': user_agent}
    meme_url = ""
    subreddit = get_subreddit(genre)
    response2 = requests.get(f'https://www.reddit.com/r/{subreddit}/hot.json', headers=headers)
    data = response2.json()
    memes = [post['data']['url'] for post in data['data']['children'] if post['data']['url'].endswith(image_format)]
    if memes:
        meme_url = random.choice(memes)
    return meme_url


def get_subreddit(genre):
    subreddit = subreddits.get(genre.lower(), "memes")
    return subreddit


def display_names(start, end):
    global templates
    if end > len(templates):
        start = 0
        end = 10
    display_templates = template_names[start:end]
    return display_templates


def example_meme(template):
    matching_name = get_closest_matching_name(template)
    example_url = get_sample(matching_name)
    return example_url


def get_closest_matching_name(name):
    closest_matching_element_list = get_close_matches(name, template_names, n=1, cutoff=0.3)
    if not closest_matching_element_list:
        raise commands.BadArgument("Meme not recognised. Try with another one.")
    return closest_matching_element_list[0]


def get_meme_id(name):
    return name_to_id[name]


def get_sample(name):
    return name_to_sample[name]
