
pets = {
    'bella':{
        'animal_type':'cat',
        'owners_name':'mike',
},
    'koji':{
        'animal_type': 'dog',
        'owners_name': 'kelly',

    },
    'ninja': {
        'animal_type': 'turtle',
        'owners_name': 'justine',

    },
}

for name, user_pets in pets.items():
    type = user_pets['animal_type']
    owner = user_pets['owners_name']

    print("\nName: " + name.title()+"\nAnimal Type: " + type.title() + "\nOwner: " + owner.title())