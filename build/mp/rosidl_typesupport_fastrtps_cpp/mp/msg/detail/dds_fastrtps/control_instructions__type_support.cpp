// generated from rosidl_typesupport_fastrtps_cpp/resource/idl__type_support.cpp.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice
#include "mp/msg/detail/control_instructions__rosidl_typesupport_fastrtps_cpp.hpp"
#include "mp/msg/detail/control_instructions__struct.hpp"

#include <limits>
#include <stdexcept>
#include <string>
#include "rosidl_typesupport_cpp/message_type_support.hpp"
#include "rosidl_typesupport_fastrtps_cpp/identifier.hpp"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support.h"
#include "rosidl_typesupport_fastrtps_cpp/message_type_support_decl.hpp"
#include "rosidl_typesupport_fastrtps_cpp/wstring_conversion.hpp"
#include "fastcdr/Cdr.h"


// forward declaration of message dependencies and their conversion functions

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
  eprosima::fastcdr::Cdr & cdr)
{
  // Member: linear_speed
  cdr << ros_message.linear_speed;
  // Member: angular_speed
  cdr << ros_message.angular_speed;
  // Member: shoot_cannon
  cdr << (ros_message.shoot_cannon ? true : false);
  // Member: cannon_angle
  cdr << ros_message.cannon_angle;
  return true;
}

bool
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  mp::msg::ControlInstructions & ros_message)
{
  // Member: linear_speed
  cdr >> ros_message.linear_speed;

  // Member: angular_speed
  cdr >> ros_message.angular_speed;

  // Member: shoot_cannon
  {
    uint8_t tmp;
    cdr >> tmp;
    ros_message.shoot_cannon = tmp ? true : false;
  }

  // Member: cannon_angle
  cdr >> ros_message.cannon_angle;

  return true;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
get_serialized_size(
  const mp::msg::ControlInstructions & ros_message,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  (void)padding;
  (void)wchar_size;

  // Member: linear_speed
  {
    size_t item_size = sizeof(ros_message.linear_speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: angular_speed
  {
    size_t item_size = sizeof(ros_message.angular_speed);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: shoot_cannon
  {
    size_t item_size = sizeof(ros_message.shoot_cannon);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }
  // Member: cannon_angle
  {
    size_t item_size = sizeof(ros_message.cannon_angle);
    current_alignment += item_size +
      eprosima::fastcdr::Cdr::alignment(current_alignment, item_size);
  }

  return current_alignment - initial_alignment;
}

size_t
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_PUBLIC_mp
max_serialized_size_ControlInstructions(
  bool & full_bounded,
  bool & is_plain,
  size_t current_alignment)
{
  size_t initial_alignment = current_alignment;

  const size_t padding = 4;
  const size_t wchar_size = 4;
  size_t last_member_size = 0;
  (void)last_member_size;
  (void)padding;
  (void)wchar_size;

  full_bounded = true;
  is_plain = true;


  // Member: linear_speed
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: angular_speed
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  // Member: shoot_cannon
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint8_t);
    current_alignment += array_size * sizeof(uint8_t);
  }

  // Member: cannon_angle
  {
    size_t array_size = 1;

    last_member_size = array_size * sizeof(uint32_t);
    current_alignment += array_size * sizeof(uint32_t) +
      eprosima::fastcdr::Cdr::alignment(current_alignment, sizeof(uint32_t));
  }

  size_t ret_val = current_alignment - initial_alignment;
  if (is_plain) {
    // All members are plain, and type is not empty.
    // We still need to check that the in-memory alignment
    // is the same as the CDR mandated alignment.
    using DataType = mp::msg::ControlInstructions;
    is_plain =
      (
      offsetof(DataType, cannon_angle) +
      last_member_size
      ) == ret_val;
  }

  return ret_val;
}

static bool _ControlInstructions__cdr_serialize(
  const void * untyped_ros_message,
  eprosima::fastcdr::Cdr & cdr)
{
  auto typed_message =
    static_cast<const mp::msg::ControlInstructions *>(
    untyped_ros_message);
  return cdr_serialize(*typed_message, cdr);
}

static bool _ControlInstructions__cdr_deserialize(
  eprosima::fastcdr::Cdr & cdr,
  void * untyped_ros_message)
{
  auto typed_message =
    static_cast<mp::msg::ControlInstructions *>(
    untyped_ros_message);
  return cdr_deserialize(cdr, *typed_message);
}

static uint32_t _ControlInstructions__get_serialized_size(
  const void * untyped_ros_message)
{
  auto typed_message =
    static_cast<const mp::msg::ControlInstructions *>(
    untyped_ros_message);
  return static_cast<uint32_t>(get_serialized_size(*typed_message, 0));
}

static size_t _ControlInstructions__max_serialized_size(char & bounds_info)
{
  bool full_bounded;
  bool is_plain;
  size_t ret_val;

  ret_val = max_serialized_size_ControlInstructions(full_bounded, is_plain, 0);

  bounds_info =
    is_plain ? ROSIDL_TYPESUPPORT_FASTRTPS_PLAIN_TYPE :
    full_bounded ? ROSIDL_TYPESUPPORT_FASTRTPS_BOUNDED_TYPE : ROSIDL_TYPESUPPORT_FASTRTPS_UNBOUNDED_TYPE;
  return ret_val;
}

static message_type_support_callbacks_t _ControlInstructions__callbacks = {
  "mp::msg",
  "ControlInstructions",
  _ControlInstructions__cdr_serialize,
  _ControlInstructions__cdr_deserialize,
  _ControlInstructions__get_serialized_size,
  _ControlInstructions__max_serialized_size
};

static rosidl_message_type_support_t _ControlInstructions__handle = {
  rosidl_typesupport_fastrtps_cpp::typesupport_identifier,
  &_ControlInstructions__callbacks,
  get_message_typesupport_handle_function,
};

}  // namespace typesupport_fastrtps_cpp

}  // namespace msg

}  // namespace mp

namespace rosidl_typesupport_fastrtps_cpp
{

template<>
ROSIDL_TYPESUPPORT_FASTRTPS_CPP_EXPORT_mp
const rosidl_message_type_support_t *
get_message_type_support_handle<mp::msg::ControlInstructions>()
{
  return &mp::msg::typesupport_fastrtps_cpp::_ControlInstructions__handle;
}

}  // namespace rosidl_typesupport_fastrtps_cpp

#ifdef __cplusplus
extern "C"
{
#endif

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_fastrtps_cpp, mp, msg, ControlInstructions)() {
  return &mp::msg::typesupport_fastrtps_cpp::_ControlInstructions__handle;
}

#ifdef __cplusplus
}
#endif
