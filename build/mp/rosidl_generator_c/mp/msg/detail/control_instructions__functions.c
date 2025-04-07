// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from mp:msg/ControlInstructions.idl
// generated code does not contain a copyright notice
#include "mp/msg/detail/control_instructions__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
mp__msg__ControlInstructions__init(mp__msg__ControlInstructions * msg)
{
  if (!msg) {
    return false;
  }
  // linear_speed
  // angular_speed
  // shoot_cannon
  // cannon_angle
  return true;
}

void
mp__msg__ControlInstructions__fini(mp__msg__ControlInstructions * msg)
{
  if (!msg) {
    return;
  }
  // linear_speed
  // angular_speed
  // shoot_cannon
  // cannon_angle
}

bool
mp__msg__ControlInstructions__are_equal(const mp__msg__ControlInstructions * lhs, const mp__msg__ControlInstructions * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // linear_speed
  if (lhs->linear_speed != rhs->linear_speed) {
    return false;
  }
  // angular_speed
  if (lhs->angular_speed != rhs->angular_speed) {
    return false;
  }
  // shoot_cannon
  if (lhs->shoot_cannon != rhs->shoot_cannon) {
    return false;
  }
  // cannon_angle
  if (lhs->cannon_angle != rhs->cannon_angle) {
    return false;
  }
  return true;
}

bool
mp__msg__ControlInstructions__copy(
  const mp__msg__ControlInstructions * input,
  mp__msg__ControlInstructions * output)
{
  if (!input || !output) {
    return false;
  }
  // linear_speed
  output->linear_speed = input->linear_speed;
  // angular_speed
  output->angular_speed = input->angular_speed;
  // shoot_cannon
  output->shoot_cannon = input->shoot_cannon;
  // cannon_angle
  output->cannon_angle = input->cannon_angle;
  return true;
}

mp__msg__ControlInstructions *
mp__msg__ControlInstructions__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mp__msg__ControlInstructions * msg = (mp__msg__ControlInstructions *)allocator.allocate(sizeof(mp__msg__ControlInstructions), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(mp__msg__ControlInstructions));
  bool success = mp__msg__ControlInstructions__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
mp__msg__ControlInstructions__destroy(mp__msg__ControlInstructions * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    mp__msg__ControlInstructions__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
mp__msg__ControlInstructions__Sequence__init(mp__msg__ControlInstructions__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mp__msg__ControlInstructions * data = NULL;

  if (size) {
    data = (mp__msg__ControlInstructions *)allocator.zero_allocate(size, sizeof(mp__msg__ControlInstructions), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = mp__msg__ControlInstructions__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        mp__msg__ControlInstructions__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
mp__msg__ControlInstructions__Sequence__fini(mp__msg__ControlInstructions__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      mp__msg__ControlInstructions__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

mp__msg__ControlInstructions__Sequence *
mp__msg__ControlInstructions__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  mp__msg__ControlInstructions__Sequence * array = (mp__msg__ControlInstructions__Sequence *)allocator.allocate(sizeof(mp__msg__ControlInstructions__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = mp__msg__ControlInstructions__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
mp__msg__ControlInstructions__Sequence__destroy(mp__msg__ControlInstructions__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    mp__msg__ControlInstructions__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
mp__msg__ControlInstructions__Sequence__are_equal(const mp__msg__ControlInstructions__Sequence * lhs, const mp__msg__ControlInstructions__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!mp__msg__ControlInstructions__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
mp__msg__ControlInstructions__Sequence__copy(
  const mp__msg__ControlInstructions__Sequence * input,
  mp__msg__ControlInstructions__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(mp__msg__ControlInstructions);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    mp__msg__ControlInstructions * data =
      (mp__msg__ControlInstructions *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!mp__msg__ControlInstructions__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          mp__msg__ControlInstructions__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!mp__msg__ControlInstructions__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
