#!/usr/bin/env python3
#
# Copyright (c) 2019 LG Electronics, Inc.
#
# This software contains code licensed as described in LICENSE.
#

import os
import lgsvl
import collections
import time
import random
# Connects to the simulator instance at the ip SIMULATOR_HOST（Environment Variable）, default is localhost or 127.0.0.1
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST","127.0.0.1"), 8181)

if sim.current_scene == "Shalun_NCKU":
  sim.reset()
else:
  sim.load("Shalun_NCKU")
#NPC name 
NPCname = [
    'Sedan',
    'HatchBack'
]
#seting waypoint
waypoints = [
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector(-85,10.2,-7.32), 10),#NPC1 position
  lgsvl.DriveWaypoint(lgsvl.Vector(-85.42,10.2,2.51), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector(-85.42,10.2,5.97), 10),
  #Straight line
  lgsvl.DriveWaypoint(lgsvl.Vector(-80,10.2,11), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector(-50,10.2,11), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector(-30,10.2,11), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 0 ,10.2,11), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 20 ,10.2,11), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 53,10.2,11), 10),
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector( 55.93,10.2,10), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 58.34,10.2,8.82), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 59 ,10.2,6.92), 10),
  #Straight line
  lgsvl.DriveWaypoint(lgsvl.Vector( 60,10.2,-27), 10),
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector( 59.46, 10.2,-29.1), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 57.54, 10.2,-32), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( 55   , 10.2,-33.43), 10),
  #Straight line
  lgsvl.DriveWaypoint(lgsvl.Vector( 50, 10.2,-33), 10),#NPC6 position
  lgsvl.DriveWaypoint(lgsvl.Vector( -10, 10.2,-33), 10),#NPC5 position
  lgsvl.DriveWaypoint(lgsvl.Vector( -45, 10.2,-33), 10),#NPC4 position
  lgsvl.DriveWaypoint(lgsvl.Vector( -67, 10.2,-33), 10),
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector( -71.32, 10.2,-31.95), 10),#NPC3 position
  lgsvl.DriveWaypoint(lgsvl.Vector( -73.88, 10.2,-30.59), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( -76.51, 10.2,-28.9), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( -79.13, 10.2,-26.3), 10),
  lgsvl.DriveWaypoint(lgsvl.Vector( -82.2,10.2,-21.5), 10),#NPC2 position
  lgsvl.DriveWaypoint(lgsvl.Vector( -83.95,10.2,-16.5), 10),
]

#Set EGO position
spawns = sim.get_spawn()
state = lgsvl.AgentState()
state.transform = spawns[0]
state.transform.position.x =  52.2
state.transform.position.y =  10.6
state.transform.position.z =  15
state.transform.rotation.y = -90
#Add EGO vehicle 
ego = sim.add_agent("NCKU_MKZ_V2", lgsvl.AgentType.EGO, state)
# The EGO is now looking for a bridge at the specified BRIDGE_HOST（Environment Variable） and port 
ego.connect_bridge(os.environ.get("BRIDGE_HOST", "127.0.0.1"),9090)
print("Waiting for connection...")

while not ego.bridge_connected:
  time.sleep(1)

print("Bridge connected:", ego.bridge_connected)


#Set NPC position
state = lgsvl.AgentState()
state.transform = spawns[0]
state.transform.position.x = -48.67
state.transform.position.y =  10.2
state.transform.position.z =  15.5
state.transform.rotation.y = -90
#NPC0 is the NCP which stop on trffic ligth
npc0 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)



#Set NPC1~NPC6 position
state.transform.rotation.y =  0
state.transform.position = waypoints[0].position
npc1 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
#Method to make vehicle follow specific waypoints, second argument mean whether waypoint keep loop
npc1.follow(waypoints,True)

#Change waypoints index for  NPC2 
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.position = waypoints[0].position
npc2 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc2.follow(waypoints,True)

#Change waypoints index for  NPC3
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -21
state.transform.position = waypoints[0].position
npc3 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc3.follow(waypoints,True)

#Change waypoints index for  NPC4
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -75
state.transform.position = waypoints[0].position
npc4 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc4.follow(waypoints,True)

#Change waypoints index for  NPC5
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -75
state.transform.position = waypoints[0].position
npc5 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc5.follow(waypoints,True)

#Change waypoints index for  NPC6
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -75
state.transform.position = waypoints[0].position
npc6 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc6.follow(waypoints,True)

input("Press Enter to run")
sim.run()
