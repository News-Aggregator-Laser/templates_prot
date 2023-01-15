import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "templates_prot.settings")

import django

django.setup()

from news.models import New
from faker import Faker

faker = Faker()

categories_list = [
    "business",
    "entertainment",
    "health",
    "science",
    "sports",
    "technology",
]


def generate_new():
    new = New.objects.create(
        title=faker.sentence(),
        sub_title=faker.sentence(),
        content=faker.text(),
        category=faker.random_element(categories_list),
        image_url=faker.image_url(),
        author=faker.name(),
        provider=faker.company(),
        published_at=faker.date_time(),
    )
    new.save()


if __name__ == "__main__":
    print("Generating fake data...", end="")
    for _ in range(60):
        generate_new()
    print("Done")
