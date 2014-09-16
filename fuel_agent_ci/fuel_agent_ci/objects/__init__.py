# Copyright 2014 Mirantis, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This mapping is supposed to be dynamically filled with
# names of objects and their types

OBJECT_TYPES = {}


class MetaObject(type):
    def __init__(self, name, bases, dct):
        if '__typename__' in dct:
            OBJECT_TYPES[dct['__typename__']] = self
        return super(MetaObject, self).__init__(name, bases, dct)


class Object(object):
    __metaclass__ = MetaObject
    __typename__ = 'object'

    @property
    def typename(self):
        return self.__typename__
