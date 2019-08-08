using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ScenarioRegister : MonoBehaviour {

	// Use this for initialization
	void Start () {
		GameObject ScenarioControllerObject = GameObject.Find("ScenarioController");
		if(ScenarioControllerObject != null)
		{
			ScenarioController ScenarioController = ScenarioControllerObject.GetComponent<ScenarioController>();
			ScenarioController.Vehicle = gameObject;
		}
	}
	
	// Update is called once per frame
	void Update () {
		
	}
}
