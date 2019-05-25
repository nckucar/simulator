using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class RushCreater : MonoBehaviour {
	
	public GameObject RushPedestrian;
	public bool isEnabled = false;

	private GameObject RootAgent;
	private bool isObjectExist = false;
	private GameObject NewRushPedestrian;


	private void Awake()
	{
		AddUIElement();
	}


	public void Enable(bool enabled)
	{
		isEnabled = enabled;
	}

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
		if(isEnabled && !isObjectExist)
		{
			NewRushPedestrian = Instantiate(RushPedestrian, new Vector3(transform.position.x , transform.position.y , transform.position.z) , transform.rotation);
			isObjectExist = true;
		}
		else if(!isEnabled && isObjectExist)
		{
			Destroy(NewRushPedestrian);
			isObjectExist = false;
		}
	}

	private void AddUIElement()
	{
		if (RootAgent == null)
			RootAgent = transform.root.gameObject;
		var imuCheckbox = RootAgent.GetComponent<UserInterfaceTweakables>().AddCheckbox("ToggleRushPedestrian", "Enable Rush Pedestrian:", isEnabled);
		imuCheckbox.onValueChanged.AddListener(x => Enable(x));
	}
}
