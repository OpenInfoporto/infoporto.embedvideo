from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder


from infoporto.embedvideo import MessageFactory as _


class IEmbeddedVideo(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """
    
    embedded_code = schema.Text(
            title=_(u"Embedded Code"),
        )


class EmbeddedVideo(Item):
    grok.implements(IEmbeddedVideo)

    # Add your class methods and properties here
    pass


class View(grok.View):
    """ sample view class """

    grok.context(IEmbeddedVideo)
    grok.require('zope2.View')

    grok.name('view')

    # Add view methods here
