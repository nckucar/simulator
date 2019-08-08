using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CreateRushPedestrian : MonoBehaviour {

	public bool IsOn;
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		
	}

	public void ChangeState()
	{
		if(IsOn)
		{
			IsOn = false;
		}
		else
		{
			IsOn = true;
		}
	}
}
