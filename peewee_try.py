from datetime import date

from peewee import *


db = SqliteDatabase('people.db')


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db

    def __str__(self):
        return self.name


class Pet(Model):
    owner = ForeignKeyField(Person, backref='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

    def __str__(self):
        return self.name


def main():
    db.connect()
    # db.create_tables([Person, Pet])
    uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15))
    print(uncle_bob.name)
    print(uncle_bob.birthday)
    uncle_bob.save()  # bob is now stored in the database
    grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1))
    herb = Person.create(name='Herb', birthday=date(1950, 5, 5))
    uncle_bob = Person.select().where(Person.name == 'Bob').get()
    petro = Person.get(Person.name == 'Petro')
    print(uncle_bob)
    print(herb)
    herb.name = 'Petro'
    herb.save()

    bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
    herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
    herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
    herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
    for person in Pet.select().where(Pet.owner == petro, Pet.animal_type == 'cat'):
        print(person.name)
    query = Pet.select().where(Pet.animal_type == 'cat')
    for pet in query:
        print(pet.name, pet.owner.name)
    query = (Pet
             .select(Pet, Person)
             .join(Person)
             .where(Pet.animal_type == 'cat'))

    for pet in query:
        print(pet.name, pet.owner.name)

    d1940 = date(1940, 1, 1)
    d1960 = date(1960, 1, 1)
    query = (Person
             .select()
             .where((Person.birthday < d1940) | (Person.birthday > d1960)))

    for person in query:
        print(person.name, person.birthday)

    query = (Person
             .select()
             .where(Person.birthday.between(d1940, d1960)))

    for person in query:
        print(person.name, person.birthday)

    for person in Person.select():
        print(person.name, person.pets.count(), 'pets')

    query = (Person
             .select(Person, fn.COUNT(Pet.id).alias('pet_count'))
             .join(Pet, JOIN.LEFT_OUTER)  # include people without pets.
             .group_by(Person)
             .order_by(Person.name))

    for person in query:
        # "pet_count" becomes an attribute on the returned model instances.
        print(person.name, person.pet_count, 'pets')

    db.close()


if __name__ == '__main__':
    main()