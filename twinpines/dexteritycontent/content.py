from interfaces import IParticipatingCoop
from plone.dexterity.content import Container
from plone.dexterity.content import Item
from zope.interface import implementer

@implementer(IParticipatingCoop)
class ParticipatingCoop(Item):
    """ convenience class """