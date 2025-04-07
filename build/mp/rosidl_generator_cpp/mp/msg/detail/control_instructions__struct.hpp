// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#ifndef MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__STRUCT_HPP_
#define MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__mp__msg__ControlInstructions __attribute__((deprecated))
#else
# define DEPRECATED__mp__msg__ControlInstructions __declspec(deprecated)
#endif

namespace mp
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct ControlInstructions_
{
  using Type = ControlInstructions_<ContainerAllocator>;

  explicit ControlInstructions_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->linear_speed = 0.0f;
      this->angular_speed = 0.0f;
      this->shoot_cannon = false;
      this->cannon_angle = 0.0f;
    }
  }

  explicit ControlInstructions_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->linear_speed = 0.0f;
      this->angular_speed = 0.0f;
      this->shoot_cannon = false;
      this->cannon_angle = 0.0f;
    }
  }

  // field types and members
  using _linear_speed_type =
    float;
  _linear_speed_type linear_speed;
  using _angular_speed_type =
    float;
  _angular_speed_type angular_speed;
  using _shoot_cannon_type =
    bool;
  _shoot_cannon_type shoot_cannon;
  using _cannon_angle_type =
    float;
  _cannon_angle_type cannon_angle;

  // setters for named parameter idiom
  Type & set__linear_speed(
    const float & _arg)
  {
    this->linear_speed = _arg;
    return *this;
  }
  Type & set__angular_speed(
    const float & _arg)
  {
    this->angular_speed = _arg;
    return *this;
  }
  Type & set__shoot_cannon(
    const bool & _arg)
  {
    this->shoot_cannon = _arg;
    return *this;
  }
  Type & set__cannon_angle(
    const float & _arg)
  {
    this->cannon_angle = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    mp::msg::ControlInstructions_<ContainerAllocator> *;
  using ConstRawPtr =
    const mp::msg::ControlInstructions_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<mp::msg::ControlInstructions_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<mp::msg::ControlInstructions_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      mp::msg::ControlInstructions_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<mp::msg::ControlInstructions_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      mp::msg::ControlInstructions_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<mp::msg::ControlInstructions_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<mp::msg::ControlInstructions_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<mp::msg::ControlInstructions_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__mp__msg__ControlInstructions
    std::shared_ptr<mp::msg::ControlInstructions_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__mp__msg__ControlInstructions
    std::shared_ptr<mp::msg::ControlInstructions_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const ControlInstructions_ & other) const
  {
    if (this->linear_speed != other.linear_speed) {
      return false;
    }
    if (this->angular_speed != other.angular_speed) {
      return false;
    }
    if (this->shoot_cannon != other.shoot_cannon) {
      return false;
    }
    if (this->cannon_angle != other.cannon_angle) {
      return false;
    }
    return true;
  }
  bool operator!=(const ControlInstructions_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct ControlInstructions_

// alias to use template instance with default allocator
using ControlInstructions =
  mp::msg::ControlInstructions_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace mp

#endif  // MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__STRUCT_HPP_
