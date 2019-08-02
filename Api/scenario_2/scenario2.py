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
# Connects to the simulator instance at the ip defined by SIMULATOR_HOST, default is localhost or 127.0.0.1
sim = lgsvl.Simulator(os.environ.get("SIMULATOR_HOST", "127.0.0.1"), 8181)

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
  lgsvl.DriveWaypoint(lgsvl.Vector(-85,10.2,-7.32), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-85.42,10.2,2.51), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-85.42,10.2,5.97), 12),
  #Straight line
  lgsvl.DriveWaypoint(lgsvl.Vector(-80,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-50,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector(-30,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 0 ,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 20 ,10.2,11), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 53,10.2,11), 12),
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector( 55.93,10.2,10), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 58.34,10.2,8.82), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 59 ,10.2,6.92), 12),
  
  #Straight line
  lgsvl.DriveWaypoint(lgsvl.Vector( 60,10.2,-27), 12),
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector( 59.46, 10.2,-29.1), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 57.54, 10.2,-32), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 55   , 10.2,-33.43), 12),
  #Straight line
  lgsvl.DriveWaypoint(lgsvl.Vector( 20, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( 0, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -30, 10.2,-33), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -67, 10.2,-33), 12),
  #Curved road
  lgsvl.DriveWaypoint(lgsvl.Vector( -71.32, 10.2,-31.95), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -73.88, 10.2,-30.59), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -76.51, 10.2,-28.9), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -79.13, 10.2,-26.3), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -82.2,10.2,-21.5), 12),
  lgsvl.DriveWaypoint(lgsvl.Vector( -83.95,10.2,-16.5), 12),
]


#EGO vehicle
spawns = sim.get_spawn()
state = lgsvl.AgentState()
state.transform = spawns[0]
state.transform.position.x =  52.2
state.transform.position.y =  10.3
state.transform.position.z =  15
state.transform.rotation.y = -90
ego = sim.add_agent("NCKU_MKZ_V2", lgsvl.AgentType.EGO, state)


#NPC vehicle
state = lgsvl.AgentState()
state.transform = spawns[0]
state.transform.position.x = -48.67
state.transform.position.y =  10.2
state.transform.position.z =  15
state.transform.rotation.y = -90
#npc0 is the NCP which stop on trffic ligth
npc0 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)



#other NPC-name  start form npc1 
state.transform.rotation.y =  0
state.transform.position = waypoints[0].position
npc1 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc1.follow(waypoints,True)

waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.position = waypoints[0].position
npc2 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc2.follow(waypoints,True)

waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -21
state.transform.position = waypoints[0].position
npc3 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc3.follow(waypoints,True)


waypoints.insert(0,waypoints.pop())
waypoints.insert(0,waypoints.pop())
state.transform.rotation.y = -75
state.transform.position = waypoints[-2].position
npc4 = sim.add_agent(random.choice(NPCname), lgsvl.AgentType.NPC, state)
npc4.follow(waypoints,True)



input("Press Enter to run")
sim.run()
