from django.apps import AppConfig


class DbappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dbApp'

    def ready(self):

        try:
            from .models import Song

            if not Song.objects.exists():

                print(f"No songs in the database...It's time for POWER METAL!")
                Song.objects.create(name="The Kinslayer", artist="Nightwish", album="Wishmaster", year=2000)
                Song.objects.create(name="The Great Pandemonium", artist="Kamelot", album="Peotry for the Poisoned", year=2010)
                Song.objects.create(name="Blood Moon", artist="Dream Troll", album="The Witche's Curse", year=2018)
                Song.objects.create(name="Hearts on Fire", artist="HammerFall", album="Crimson Thunder", year=2002)
                Song.objects.create(name="Raise Your Fist, Evangelist", artist="Powerwolf", album="Bible of the Beast", year=2009)
                Song.objects.create(name="Primo Victoria", artist="Sabaton", album="Primo Victoria", year=2005)
                Song.objects.create(name="Holy Thunderforce", artist="Rhapsody of Fire", album="Dawn of Victory", year=2000)
                Song.objects.create(name="Through the Fire and Flames", artist="DragonForce", album="Inhuman Rampage", year=2006)
                Song.objects.create(name="Drunken Dwarves", artist="Windrose", album="Wintersage", year=2019)
                Song.objects.create(name="Tonight We Ride", artist="Unleash the Archers", album="Time Stands Still", year=2015)

            else:
                print(f"Songs already exist in the database!")
        
        except Exception as e:
            print(f"hit an exception when checking the database: {e}")
