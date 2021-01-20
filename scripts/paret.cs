using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class paret : MonoBehaviour {
    public Text lol;

	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (lol.text == "0")//si el joc ha començat moute
        {
            transform.Translate(0, 0, 0.06f );//1* Time.deltaTime
        }
	}
}
