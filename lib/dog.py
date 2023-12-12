
def create_table(base):
    pass
def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    pass
    session.add(dog)
    session.commit()

def get_all(session):
    pass
    return session.query(Dog).all()

def find_by_name(session, name):
    pass
    return session.query(Dog).filter_by(name=name).first()

def find_by_id(session, id):
    pass
    return session.query(Dog).get(id)

def find_by_name_and_breed(session, name, breed):
    pass
    return session.query(Dog).filter_by(name=name, breed=breed).first()

def update_breed(session, dog, breed):
    pass
    pass
def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()