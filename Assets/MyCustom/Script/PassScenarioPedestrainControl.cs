using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.UI;

public class PassScenarioPedestrainControl : MonoBehaviour {
	public Transform EndPoint;

	private NavMeshAgent agent;
	private Animator anim;
	private Vector3 InitEndPos;
	public bool IsTriggered = false;
	private bool IsArrived = false;

	
	private int MoveStage = 0;//0:Walking 1:Stop for a while  2:Walking again

	void Start () {
		agent = GetComponent<NavMeshAgent>();
		anim = GetComponentInChildren<Animator>();
		InitEndPos = EndPoint.position;
	}

	void Update () {
		if(IsTriggered) 
		{
			anim.SetTrigger("Walk");
			agent.SetDestination(InitEndPos);
			if(!IsArrived) //Seting by suring that it stops at the Endpoint.
			{
				if (!agent.pathPending) //Judge that whether it arriving at EndPos:
				{
					if (agent.remainingDistance <= agent.stoppingDistance)
					{	
						if (!agent.hasPath || agent.velocity.sqrMagnitude == 0f)
						{
							//If it arrived, do this thing:
							anim.SetTrigger("Idle");
							IsArrived = true;
						}						
					}
				}
			}
		}
	}
}

