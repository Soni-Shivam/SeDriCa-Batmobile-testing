# generated from rosidl_generator_py/resource/_idl.py.em
# with input from mp:msg/ControlInstructions.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_ControlInstructions(type):
    """Metaclass of message 'ControlInstructions'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('mp')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'mp.msg.ControlInstructions')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__control_instructions
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__control_instructions
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__control_instructions
            cls._TYPE_SUPPORT = module.type_support_msg__msg__control_instructions
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__control_instructions

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class ControlInstructions(metaclass=Metaclass_ControlInstructions):
    """Message class 'ControlInstructions'."""

    __slots__ = [
        '_linear_speed',
        '_angular_speed',
        '_shoot_cannon',
        '_cannon_angle',
    ]

    _fields_and_field_types = {
        'linear_speed': 'float',
        'angular_speed': 'float',
        'shoot_cannon': 'boolean',
        'cannon_angle': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.linear_speed = kwargs.get('linear_speed', float())
        self.angular_speed = kwargs.get('angular_speed', float())
        self.shoot_cannon = kwargs.get('shoot_cannon', bool())
        self.cannon_angle = kwargs.get('cannon_angle', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.linear_speed != other.linear_speed:
            return False
        if self.angular_speed != other.angular_speed:
            return False
        if self.shoot_cannon != other.shoot_cannon:
            return False
        if self.cannon_angle != other.cannon_angle:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def linear_speed(self):
        """Message field 'linear_speed'."""
        return self._linear_speed

    @linear_speed.setter
    def linear_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'linear_speed' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'linear_speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._linear_speed = value

    @builtins.property
    def angular_speed(self):
        """Message field 'angular_speed'."""
        return self._angular_speed

    @angular_speed.setter
    def angular_speed(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'angular_speed' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'angular_speed' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._angular_speed = value

    @builtins.property
    def shoot_cannon(self):
        """Message field 'shoot_cannon'."""
        return self._shoot_cannon

    @shoot_cannon.setter
    def shoot_cannon(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'shoot_cannon' field must be of type 'bool'"
        self._shoot_cannon = value

    @builtins.property
    def cannon_angle(self):
        """Message field 'cannon_angle'."""
        return self._cannon_angle

    @cannon_angle.setter
    def cannon_angle(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'cannon_angle' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'cannon_angle' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._cannon_angle = value
