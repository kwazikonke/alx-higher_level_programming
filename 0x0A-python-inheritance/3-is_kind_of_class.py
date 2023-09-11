#!/usr/bin/python3

"""Function that returns TRUE if the obj is an instance of,
   or if the obj is an instance of a class that inherited from
   otherwise return FALSE"""

   def is_kind_of_class(obj, a_class):
       return isinstance(obj,a_class)
