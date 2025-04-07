// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#ifndef MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__STRUCT_H_
#define MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in msg/ControlInstructions in the package mp.
typedef struct mp__msg__ControlInstructions
{
  float linear_speed;
  float angular_speed;
  /// To shoot yes or no
  bool shoot_cannon;
  /// Angle of the cannon in radians
  float cannon_angle;
} mp__msg__ControlInstructions;

// Struct for a sequence of mp__msg__ControlInstructions.
typedef struct mp__msg__ControlInstructions__Sequence
{
  mp__msg__ControlInstructions * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} mp__msg__ControlInstructions__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__STRUCT_H_
