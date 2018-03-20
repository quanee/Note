"""
Provides an inheritable print overload method that displays instances with their class names and a name=value pair for each attribute stored on the instance itself (but not attrs inherited from its classes). Can be mixed into any class, and will work on anyinstance.
"""

class AttrDisplay:

    def gatherAttrs(self):