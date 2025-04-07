// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "mp/msg/detail/control_instructions__rosidl_typesupport_introspection_c.h"
#include "mp/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "mp/msg/detail/control_instructions__functions.h"
#include "mp/msg/detail/control_instructions__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  mp__msg__ControlInstructions__init(message_memory);
}

void mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_fini_function(void * message_memory)
{
  mp__msg__ControlInstructions__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_member_array[4] = {
  {
    "linear_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mp__msg__ControlInstructions, linear_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "angular_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mp__msg__ControlInstructions, angular_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "shoot_cannon",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mp__msg__ControlInstructions, shoot_cannon),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "cannon_angle",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(mp__msg__ControlInstructions, cannon_angle),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_members = {
  "mp__msg",  // message namespace
  "ControlInstructions",  // message name
  4,  // number of fields
  sizeof(mp__msg__ControlInstructions),
  mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_member_array,  // message members
  mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_init_function,  // function to initialize message memory (memory has to be allocated)
  mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_type_support_handle = {
  0,
  &mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_mp
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, mp, msg, ControlInstructions)() {
  if (!mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_type_support_handle.typesupport_identifier) {
    mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &mp__msg__ControlInstructions__rosidl_typesupport_introspection_c__ControlInstructions_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
