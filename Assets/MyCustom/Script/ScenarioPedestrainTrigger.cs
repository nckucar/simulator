using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScenariorPedestrainTrigger : MonoBehaviour {

	public GameObject PassScenarioPedestrain;
	// Use this for initialization
	void Start () {
		PassScenarioPedestrain =  transform.parent.gameObject;
	}
	
	private void OnTriggerEnter(Collider other)
	{
		if(other.gameObject.name == "BoundingBox" && other.gameObject.transform.root.tag == "Player")
		{
			PassScenarioPedestrain.GetComponent<PassScenarioPedestrainControl>().IsTriggered = true;
		}
	}
}
