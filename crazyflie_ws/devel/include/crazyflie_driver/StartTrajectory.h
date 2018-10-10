// Generated by gencpp from file crazyflie_driver/StartTrajectory.msg
// DO NOT EDIT!


#ifndef CRAZYFLIE_DRIVER_MESSAGE_STARTTRAJECTORY_H
#define CRAZYFLIE_DRIVER_MESSAGE_STARTTRAJECTORY_H

#include <ros/service_traits.h>


#include <crazyflie_driver/StartTrajectoryRequest.h>
#include <crazyflie_driver/StartTrajectoryResponse.h>


namespace crazyflie_driver
{

struct StartTrajectory
{

typedef StartTrajectoryRequest Request;
typedef StartTrajectoryResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;

}; // struct StartTrajectory
} // namespace crazyflie_driver


namespace ros
{
namespace service_traits
{


template<>
struct MD5Sum< ::crazyflie_driver::StartTrajectory > {
  static const char* value()
  {
    return "74e2cf5224bc82fcc8d9c7dd3865d912";
  }

  static const char* value(const ::crazyflie_driver::StartTrajectory&) { return value(); }
};

template<>
struct DataType< ::crazyflie_driver::StartTrajectory > {
  static const char* value()
  {
    return "crazyflie_driver/StartTrajectory";
  }

  static const char* value(const ::crazyflie_driver::StartTrajectory&) { return value(); }
};


// service_traits::MD5Sum< ::crazyflie_driver::StartTrajectoryRequest> should match 
// service_traits::MD5Sum< ::crazyflie_driver::StartTrajectory > 
template<>
struct MD5Sum< ::crazyflie_driver::StartTrajectoryRequest>
{
  static const char* value()
  {
    return MD5Sum< ::crazyflie_driver::StartTrajectory >::value();
  }
  static const char* value(const ::crazyflie_driver::StartTrajectoryRequest&)
  {
    return value();
  }
};

// service_traits::DataType< ::crazyflie_driver::StartTrajectoryRequest> should match 
// service_traits::DataType< ::crazyflie_driver::StartTrajectory > 
template<>
struct DataType< ::crazyflie_driver::StartTrajectoryRequest>
{
  static const char* value()
  {
    return DataType< ::crazyflie_driver::StartTrajectory >::value();
  }
  static const char* value(const ::crazyflie_driver::StartTrajectoryRequest&)
  {
    return value();
  }
};

// service_traits::MD5Sum< ::crazyflie_driver::StartTrajectoryResponse> should match 
// service_traits::MD5Sum< ::crazyflie_driver::StartTrajectory > 
template<>
struct MD5Sum< ::crazyflie_driver::StartTrajectoryResponse>
{
  static const char* value()
  {
    return MD5Sum< ::crazyflie_driver::StartTrajectory >::value();
  }
  static const char* value(const ::crazyflie_driver::StartTrajectoryResponse&)
  {
    return value();
  }
};

// service_traits::DataType< ::crazyflie_driver::StartTrajectoryResponse> should match 
// service_traits::DataType< ::crazyflie_driver::StartTrajectory > 
template<>
struct DataType< ::crazyflie_driver::StartTrajectoryResponse>
{
  static const char* value()
  {
    return DataType< ::crazyflie_driver::StartTrajectory >::value();
  }
  static const char* value(const ::crazyflie_driver::StartTrajectoryResponse&)
  {
    return value();
  }
};

} // namespace service_traits
} // namespace ros

#endif // CRAZYFLIE_DRIVER_MESSAGE_STARTTRAJECTORY_H