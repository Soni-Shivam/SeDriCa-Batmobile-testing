// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__rosidl_typesupport_fastrtps_cpp.hpp.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#ifndef MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
#define MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_

#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_typesupport_interface/macros.h"
#include "mp/msg/rosidl_typesupport_fastrtps_cpp__visibility_control.h"
#include "mp/msg/detail/control_instructions__struct.hpp"

#ifndef _WIN32
# pragma GCC diagnostic push
# pragma GCC diagnostic ignored "-Wunused-parameter"
# ifdef __clang__
#  pragma clang diagnostic ignored "-Wdeprecated-register"
#  pragma clang diagnostic ignored "-Wreturn-type-c-linkage"
# endif
#endif
#ifndef _WIN32
# pragma GCC diagnostic pop
#endif

#include "fastcdr/Cdr.h"

namespace mp
{

namespace msg
{

namespace typesupport_fastrtps_cpp
{

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
cdr_serialize(
  const mp::msg::ControlInstructions & ros_message,
  eprosima::fastcdr::Cdr & cdr);

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  mp::msg::ControlInstructions & ros_message);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
get_serialized_size(
  const mp::msg::ControlInstructions & ros_message,
  size_t current_alignment);

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
max_serialized_size_ControlInstructions(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment);

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace mp

#ifdef __cplusplus
extern "C"
{
#endif

ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
const rosidl_message_type_support_t *
  ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, mp, msg, ControlInstructions)();

#ifdef __cplusplus
}
#endif

#endif  // MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__ROSIDL_TYPESUPPORT_FASTRTPS_CPP_HPP_
