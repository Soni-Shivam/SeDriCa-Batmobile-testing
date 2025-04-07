// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#ifndef MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__TRAITS_HPP_
#define MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "mp/msg/detail/control_instructions__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace mp
{

namespace msg
{

inline void to_flow_style_yaml(
  const ControlInstructions & msg,
  std::ostream & out)
{
  out << "{";
  // member: linear_speed
  {
    out << "linear_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_speed, out);
    out << ", ";
  }

  // member: angular_speed
  {
    out << "angular_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.angular_speed, out);
    out << ", ";
  }

  // member: shoot_cannon
  {
    out << "shoot_cannon: ";
    rosidl_generator_traits::value_to_yaml(msg.shoot_cannon, out);
    out << ", ";
  }

  // member: cannon_angle
  {
    out << "cannon_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.cannon_angle, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ControlInstructions & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: linear_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "linear_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.linear_speed, out);
    out << "\n";
  }

  // member: angular_speed
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "angular_speed: ";
    rosidl_generator_traits::value_to_yaml(msg.angular_speed, out);
    out << "\n";
  }

  // member: shoot_cannon
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "shoot_cannon: ";
    rosidl_generator_traits::value_to_yaml(msg.shoot_cannon, out);
    out << "\n";
  }

  // member: cannon_angle
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "cannon_angle: ";
    rosidl_generator_traits::value_to_yaml(msg.cannon_angle, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ControlInstructions & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace mp

namespace rosidl_generator_traits
{

[[deprecated("use mp::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const mp::msg::ControlInstructions & msg,
  std::ostream & out, size_t indentation = 0)
{
  mp::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use mp::msg::to_yaml() instead")]]
inline std::string to_yaml(const mp::msg::ControlInstructions & msg)
{
  return mp::msg::to_yaml(msg);
}

template<>
inline const char * data_type<mp::msg::ControlInstructions>()
{
  return "mp::msg::ControlInstructions";
}

template<>
inline const char * name<mp::msg::ControlInstructions>()
{
  return "mp/msg/ControlInstructions";
}

template<>
struct has_fixed_size<mp::msg::ControlInstructions>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<mp::msg::ControlInstructions>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<mp::msg::ControlInstructions>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__TRAITS_HPP_
