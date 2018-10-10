# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "snake_control: 0 messages, 3 services")

set(MSG_I_FLAGS "-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg;-Itrajectory_msgs:/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(snake_control_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" NAME_WE)
add_custom_target(_snake_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "snake_control" "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" "std_msgs/Header"
)

get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" NAME_WE)
add_custom_target(_snake_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "snake_control" "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" "std_msgs/Header"
)

get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" NAME_WE)
add_custom_target(_snake_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "snake_control" "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" "std_msgs/Header:trajectory_msgs/JointTrajectoryPoint"
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages

### Generating Services
_generate_srv_cpp(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snake_control
)
_generate_srv_cpp(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snake_control
)
_generate_srv_cpp(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snake_control
)

### Generating Module File
_generate_module_cpp(snake_control
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snake_control
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(snake_control_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(snake_control_generate_messages snake_control_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_cpp _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_cpp _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_cpp _snake_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snake_control_gencpp)
add_dependencies(snake_control_gencpp snake_control_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snake_control_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages

### Generating Services
_generate_srv_eus(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/snake_control
)
_generate_srv_eus(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/snake_control
)
_generate_srv_eus(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/snake_control
)

### Generating Module File
_generate_module_eus(snake_control
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/snake_control
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(snake_control_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(snake_control_generate_messages snake_control_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_eus _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_eus _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_eus _snake_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snake_control_geneus)
add_dependencies(snake_control_geneus snake_control_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snake_control_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages

### Generating Services
_generate_srv_lisp(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snake_control
)
_generate_srv_lisp(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snake_control
)
_generate_srv_lisp(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snake_control
)

### Generating Module File
_generate_module_lisp(snake_control
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snake_control
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(snake_control_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(snake_control_generate_messages snake_control_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_lisp _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_lisp _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_lisp _snake_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snake_control_genlisp)
add_dependencies(snake_control_genlisp snake_control_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snake_control_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages

### Generating Services
_generate_srv_nodejs(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/snake_control
)
_generate_srv_nodejs(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/snake_control
)
_generate_srv_nodejs(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/snake_control
)

### Generating Module File
_generate_module_nodejs(snake_control
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/snake_control
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(snake_control_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(snake_control_generate_messages snake_control_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_nodejs _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_nodejs _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_nodejs _snake_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snake_control_gennodejs)
add_dependencies(snake_control_gennodejs snake_control_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snake_control_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages

### Generating Services
_generate_srv_py(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control
)
_generate_srv_py(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control
)
_generate_srv_py(snake_control
  "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/opt/ros/kinetic/share/trajectory_msgs/cmake/../msg/JointTrajectoryPoint.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control
)

### Generating Module File
_generate_module_py(snake_control
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(snake_control_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(snake_control_generate_messages snake_control_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/PublishJointCmds.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_py _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointStates.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_py _snake_control_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/holy_cow/arboc_ws/src/snake_control/srv/GetJointTrajectory.srv" NAME_WE)
add_dependencies(snake_control_generate_messages_py _snake_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snake_control_genpy)
add_dependencies(snake_control_genpy snake_control_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snake_control_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snake_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snake_control
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(snake_control_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()
if(TARGET trajectory_msgs_generate_messages_cpp)
  add_dependencies(snake_control_generate_messages_cpp trajectory_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/snake_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/snake_control
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(snake_control_generate_messages_eus std_msgs_generate_messages_eus)
endif()
if(TARGET trajectory_msgs_generate_messages_eus)
  add_dependencies(snake_control_generate_messages_eus trajectory_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snake_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snake_control
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(snake_control_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()
if(TARGET trajectory_msgs_generate_messages_lisp)
  add_dependencies(snake_control_generate_messages_lisp trajectory_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/snake_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/snake_control
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(snake_control_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()
if(TARGET trajectory_msgs_generate_messages_nodejs)
  add_dependencies(snake_control_generate_messages_nodejs trajectory_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snake_control
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(snake_control_generate_messages_py std_msgs_generate_messages_py)
endif()
if(TARGET trajectory_msgs_generate_messages_py)
  add_dependencies(snake_control_generate_messages_py trajectory_msgs_generate_messages_py)
endif()
