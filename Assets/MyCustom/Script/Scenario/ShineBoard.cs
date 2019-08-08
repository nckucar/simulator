using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ShineBoard : MonoBehaviour {

	public float SwitchColorRate = 0.8f; //sec
	// Use this for initialization
	void Start () {	
		StartCoroutine("ChangeColors", SwitchColorRate);
	}
	
	// Update is called once per frame
	void Update () {
		


	}

	IEnumerator ChangeColors(float sec)
	{
		while(true)
		{

			//Set the main Color of the Material to red
			//rend.material.shader = Shader.Find("_Color");
			//rend.material.SetColor("_Color", Color.red);
			GetComponent<MeshRenderer>().material.color = Color.red;

			yield return new WaitForSeconds(sec);

			//Set the main Color of the Material to green
			//rend.material.shader = Shader.Find("_Color");
			//rend.material.SetColor("_Color", Color.green);
			GetComponent<MeshRenderer>().material.color = Color.yellow;

			yield return new WaitForSeconds(sec);

			GetComponent<MeshRenderer>().material.color = Color.green;

			yield return new WaitForSeconds(sec);
		}
	}

}
