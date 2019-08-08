using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ScenarioController : MonoBehaviour {

	public GameObject Vehicle;
	public bool NeonScenario = false;
	public bool OvertakeScenario = false;
	Toggle NeonToggle;
	Toggle PassToggle;
	public GameObject NeonHouse;
	public GameObject OvertakeScenarioPedtrain;

	private bool isNeonCreate = false;
	private bool isPassCreate = false;
	private GameObject InstantNeon;
	private GameObject InstantPedestrain;
	// Use this for initialization
	void Start () {
		//Add Neon Scenario to ScenarioTweakables
        NeonToggle = ScenarioTweakables.Instance.AddCheckbox("Neon Scenario", NeonScenario);
        NeonToggle.onValueChanged.AddListener(x => NeonScenario = x);
		//Add Pass Scenario to ScenarioTweakables
		PassToggle = ScenarioTweakables.Instance.AddCheckbox("Pass Scenario", OvertakeScenario);
		PassToggle.onValueChanged.AddListener(x => OvertakeScenario = x);
	}
	
	// Update is called once per frame
	void Update () {
		 if(NeonScenario && !isNeonCreate)
		 {
			 InstantNeon = Instantiate(NeonHouse);
			 //GameObject Vehicle = GameObject.Find("NCKU_MKZ_V2");
			 if(Vehicle != null)
			 {
				Vehicle.transform.position = new Vector3(-43.2f, 11.02f, -20.14f);
				Vehicle.transform.rotation = Quaternion.Euler (0f, 90f, 0f);
			 }
			 isNeonCreate = true;
		 }
		 else if (!NeonScenario && isNeonCreate)
		 {
			Destroy(InstantNeon);
			isNeonCreate = false;
		 }

		 if(OvertakeScenario && !isPassCreate)
		 {
			InstantPedestrain = Instantiate(OvertakeScenarioPedtrain);
			isPassCreate = true;
		 }
		 else if (!OvertakeScenario && isPassCreate)
		 {
			Destroy(InstantPedestrain);
			isPassCreate = false;
		 }

	}
}
