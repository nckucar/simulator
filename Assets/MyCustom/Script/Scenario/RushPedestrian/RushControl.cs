using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.UI;

public class RushControl : MonoBehaviour {
	public Transform EndPoint;
	public Transform FarPoint; //To keep walking

	private NavMeshAgent agent;
	private Animator anim;
	private Vector3 InitEndPos;
	private Vector3 FarPos;
	public bool IsTriggered = false;
	private bool isTriggerChange = false;
	private bool IsArrived = false;
	public bool NonStop;
	public float WaitTime;
	
	private int MoveStage = 0;//0:Walking 1:Stop for a while  2:Walking again

	void Start () {
		agent = GetComponent<NavMeshAgent>();
		anim = GetComponentInChildren<Animator>();
		InitEndPos = EndPoint.position;
		FarPos = FarPoint.position;
	}

	void Update () {
		if(!NonStop) 
		{
			if(IsTriggered) //Set 1 by the vehicle.
			{
				if(!isTriggerChange) //Judge that whether the pedestrian walking.
				{
					anim.SetTrigger("Walk");
					agent.SetDestination(InitEndPos);
					isTriggerChange = true;
				}

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
		else //NonStop mode
		{
			if(!isTriggerChange) //Judge that whether the pedestrian walking.
			{
				//Walking
				anim.SetTrigger("Walk");
				agent.SetDestination(InitEndPos);
				isTriggerChange = true;
			}

			if(!IsArrived) //Seting by suring that it stops at the Endpoint.
			{
				if (!agent.pathPending) //Judge that whether it arriving at EndPos:
				{
					if (agent.remainingDistance <= agent.stoppingDistance)
					{
						if (!agent.hasPath || agent.velocity.sqrMagnitude == 0f)
						{
							//If it arrived at Endpoint, do this thing:
							anim.SetTrigger("Idle");
							StartCoroutine("IdleForSeconds", WaitTime);
							IsArrived = true;
						}
					}
				 }
			}
		}
	}
	IEnumerator IdleForSeconds(float sec)
	{
		anim.SetTrigger("Idle");
		yield return new WaitForSeconds(sec);
		anim.SetTrigger("Walk");
		agent.SetDestination(FarPos);
	}
}

