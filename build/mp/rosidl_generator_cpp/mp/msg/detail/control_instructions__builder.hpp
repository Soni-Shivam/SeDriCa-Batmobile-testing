// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#ifndef MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__BUILDER_HPP_
#define MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "mp/msg/detail/control_instructions__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace mp
{

namespace msg
{

namespace builder
{

class Init_ControlInstructions_cannon_angle
{
public:
  explicit Init_ControlInstructions_cannon_angle(::mp::msg::ControlInstructions & msg)
  : msg_(msg)
  {}
  ::mp::msg::ControlInstructions cannon_angle(::mp::msg::ControlInstructions::_cannon_angle_type arg)
  {
    msg_.cannon_angle = std::move(arg);
    return std::move(msg_);
  }

private:
  ::mp::msg::ControlInstructions msg_;
};

class Init_ControlInstructions_shoot_cannon
{
public:
  explicit Init_ControlInstructions_shoot_cannon(::mp::msg::ControlInstructions & msg)
  : msg_(msg)
  {}
  Init_ControlInstructions_cannon_angle shoot_cannon(::mp::msg::ControlInstructions::_shoot_cannon_type arg)
  {
    msg_.shoot_cannon = std::move(arg);
    return Init_ControlInstructions_cannon_angle(msg_);
  }

private:
  ::mp::msg::ControlInstructions msg_;
};

class Init_ControlInstructions_angular_speed
{
public:
  explicit Init_ControlInstructions_angular_speed(::mp::msg::ControlInstructions & msg)
  : msg_(msg)
  {}
  Init_ControlInstructions_shoot_cannon angular_speed(::mp::msg::ControlInstructions::_angular_speed_type arg)
  {
    msg_.angular_speed = std::move(arg);
    return Init_ControlInstructions_shoot_cannon(msg_);
  }

private:
  ::mp::msg::ControlInstructions msg_;
};

class Init_ControlInstructions_linear_speed
{
public:
  Init_ControlInstructions_linear_speed()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ControlInstructions_angular_speed linear_speed(::mp::msg::ControlInstructions::_linear_speed_type arg)
  {
    msg_.linear_speed = std::move(arg);
    return Init_ControlInstructions_angular_speed(msg_);
  }

private:
  ::mp::msg::ControlInstructions msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::mp::msg::ControlInstructions>()
{
  return mp::msg::builder::Init_ControlInstructions_linear_speed();
}

}  // namespace mp

#endif  // MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__BUILDER_HPP_
