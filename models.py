from google.appengine.ext import ndb


class PosameznaOseba(ndb.Model):
    uporabnik = ndb.StringProperty()
    ime = ndb.StringProperty()
    priimek = ndb.StringProperty()
    izbrisan = ndb.BooleanProperty(default=False)
    datum = ndb.StringProperty()


class PosameznaObletnica(ndb.Model):
    uporabnik = ndb.StringProperty()
    opis_obletnice = ndb.StringProperty()
    izbrisan = ndb.BooleanProperty(default=False)
    datum = ndb.StringProperty()