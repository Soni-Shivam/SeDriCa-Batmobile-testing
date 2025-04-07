// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice

#ifndef MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__FUNCTIONS_H_
#define MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "mp/msg/rosidl_generator_c__visibility_control.h"

#include "mp/msg/detail/control_instructions__struct.h"

/// Initialize msg/ControlInstructions message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * mp__msg__ControlInstructions
 * )) before or use
 * mp__msg__ControlInstructions__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
bool
mp__msg__ControlInstructions__init(mp__msg__ControlInstructions * msg);

/// Finalize msg/ControlInstructions message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
void
mp__msg__ControlInstructions__fini(mp__msg__ControlInstructions * msg);

/// Create msg/ControlInstructions message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * mp__msg__ControlInstructions__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
mp__msg__ControlInstructions *
mp__msg__ControlInstructions__create();

/// Destroy msg/ControlInstructions message.
/**
 * It calls
 * mp__msg__ControlInstructions__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
void
mp__msg__ControlInstructions__destroy(mp__msg__ControlInstructions * msg);

/// Check for msg/ControlInstructions message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
bool
mp__msg__ControlInstructions__are_equal(const mp__msg__ControlInstructions * lhs, const mp__msg__ControlInstructions * rhs);

/// Copy a msg/ControlInstructions message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
bool
mp__msg__ControlInstructions__copy(
  const mp__msg__ControlInstructions * input,
  mp__msg__ControlInstructions * output);

/// Initialize array of msg/ControlInstructions messages.
/**
 * It allocates the memory for the number of elements and calls
 * mp__msg__ControlInstructions__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
bool
mp__msg__ControlInstructions__Sequence__init(mp__msg__ControlInstructions__Sequence * array, size_t size);

/// Finalize array of msg/ControlInstructions messages.
/**
 * It calls
 * mp__msg__ControlInstructions__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
void
mp__msg__ControlInstructions__Sequence__fini(mp__msg__ControlInstructions__Sequence * array);

/// Create array of msg/ControlInstructions messages.
/**
 * It allocates the memory for the array and calls
 * mp__msg__ControlInstructions__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
mp__msg__ControlInstructions__Sequence *
mp__msg__ControlInstructions__Sequence__create(size_t size);

/// Destroy array of msg/ControlInstructions messages.
/**
 * It calls
 * mp__msg__ControlInstructions__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
void
mp__msg__ControlInstructions__Sequence__destroy(mp__msg__ControlInstructions__Sequence * array);

/// Check for msg/ControlInstructions message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
bool
mp__msg__ControlInstructions__Sequence__are_equal(const mp__msg__ControlInstructions__Sequence * lhs, const mp__msg__ControlInstructions__Sequence * rhs);

/// Copy an array of msg/ControlInstructions messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_mp
bool
mp__msg__ControlInstructions__Sequence__copy(
  const mp__msg__ControlInstructions__Sequence * input,
  mp__msg__ControlInstructions__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // MP__MSG__DETAIL__CONTROL_INSTRUCTIONS__FUNCTIONS_H_
