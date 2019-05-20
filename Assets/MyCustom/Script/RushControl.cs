using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.AI;
using UnityEngine.UI;

public class RushControl : MonoBehaviour {
	public Transform EndPoint;

	private NavMeshAgent agent;
	private Animator anim;
	private Vector3 InitEndPos;
	public bool IsTriggered = false;
	private bool isTriggerChange = false;
	private bool IsArrived = false;
	

	void Start () {
		agent = GetComponent<NavMeshAgent>();
		anim = GetComponentInChildren<Animator>();
		InitEndPos = EndPoint.position;
	}

	void Update () {
		if(IsTriggered)
		{
			if(!isTriggerChange)
			{
				anim.SetTrigger("Walk");
				agent.SetDestination(InitEndPos);
				isTriggerChange = true;
			}

			if(!IsArrived)
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

