
"use strict";

let UpdateParams = require('./UpdateParams.js')
let Stop = require('./Stop.js')
let AddCrazyflie = require('./AddCrazyflie.js')
let Takeoff = require('./Takeoff.js')
let SetGroupMask = require('./SetGroupMask.js')
let StartTrajectory = require('./StartTrajectory.js')
let Land = require('./Land.js')
let UploadTrajectory = require('./UploadTrajectory.js')
let RemoveCrazyflie = require('./RemoveCrazyflie.js')
let sendPacket = require('./sendPacket.js')
let GoTo = require('./GoTo.js')

module.exports = {
  UpdateParams: UpdateParams,
  Stop: Stop,
  AddCrazyflie: AddCrazyflie,
  Takeoff: Takeoff,
  SetGroupMask: SetGroupMask,
  StartTrajectory: StartTrajectory,
  Land: Land,
  UploadTrajectory: UploadTrajectory,
  RemoveCrazyflie: RemoveCrazyflie,
  sendPacket: sendPacket,
  GoTo: GoTo,
};
