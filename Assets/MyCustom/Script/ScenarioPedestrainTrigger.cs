using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScenarioPedestrainTrigger : MonoBehaviour {

	public GameObject OvertakeScenarioPedtrain;
	// Use this for initialization
	void Start () {
		OvertakeScenarioPedtrain =  transform.parent.gameObject;
	}
	
	private void OnTriggerEnter(Collider other)
	{
		if(other.gameObject.name == "BoundingBox" && other.gameObject.transform.root.tag == "Player")
		{
			OvertakeScenarioPedtrain.GetComponent<OvertakeScenarioPedestrainControl>().IsTriggered = true;
		}
	}
}
