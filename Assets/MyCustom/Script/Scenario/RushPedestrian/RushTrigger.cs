using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RushTrigger : MonoBehaviour {

	private GameObject RushPedestrian;

	// Use this for initialization
	void Start () {
		RushPedestrian = transform.parent.gameObject;
	}
	
	private void OnTriggerEnter(Collider other)
	{
		if(other.gameObject.name == "BoundingBox" && other.gameObject.transform.root.tag == "Player")
		{
			RushPedestrian.GetComponent<RushControl>().IsTriggered = true;
		}
	}
}
