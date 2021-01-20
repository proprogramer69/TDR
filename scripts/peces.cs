using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class peces : MonoBehaviour {
    public string rand;//no fer cas
    public float ponderació = 1.5f;//1  variable que em permet movificar la velocitat
    //public Text ho;
	// Use this for initialization
	void Start () {
        rand = "1";//ho.text;
        if (rand == "1") { transform.Rotate(0, 90, 0); }//girar la peça
	}
	
	// Update is called once per frame
	void Update () {
        if (rand == "1") {

            transform.Translate(0.2f * ponderació, 0, 0);//1.5f * ponderació * Time.deltaTime //moviment de la peça
        }
        else {
            transform.Translate(0, 0, -0.01f * ponderació * Time.deltaTime);
	}
    }
    void OnTriggerEnter(Collider peça)//quan toqui la paret autoborrar-se per no donar lag
    {
        if (peça.tag == "paret")
        {
            Destroy(gameObject);}
        }
    }
    
