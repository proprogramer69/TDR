using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;
using System;

public class moviment : MonoBehaviour {
    public GameObject so;//controla la musica
    public GameObject llum;//controla la llum
    public GameObject somort;// controla la risa malvada
    public GameObject boto;// controla el boto
    public Text lol;//controla el text que diu l'estat del joc
    public int tipus=0;// en principi tenia pensat posar un altre mode de moviment i que es pogues elegir, encara esta pendent
    public Transform vrCamera;
    public float speed = 3.0f;//control la velocitat
    private CharacterController cc;//per fer lo del moviment i gir de camera
    public GameObject video;// controla la esfera en la que apareixen videos
    private Scene scene;//controla la scena
    public float Volumen = 1;// controla el volum
    //public Camera mor;
    //public Camera win;
    //public Camera joc;
    public int mort;// estat del joc
	// Use this for initialization
	void Start () {//inicialitza els estats
        boto.active = false;
        somort.active = false;
        so.active = false;
        video.active = true;
        llum.active = false;
        mort = 1;
        scene = SceneManager.GetActiveScene();
        //mor.enabled = false;
        //win.enabled = false;
        //joc.enabled = true;
        cc = GetComponent<CharacterController>();
	}
	
	// Update is called once per frame
	void Update () {


        lol.text = System.Convert.ToString(mort);//canviar el text perque els altres scripts sapiguen l'estat
        if (mort == 0 || mort==1001) { 
        if (tipus == 0)
        {
            
                Vector3 forward = vrCamera.TransformDirection(Vector3.forward);//moviment
                cc.SimpleMove(forward * speed);//*Time.deltaTime

       }
       }
	}
    public void començar()//funcio que s'activa quan mires el boto i encara no has començat
    {
        so.active = true;
        transform.Translate(-100, 0, 0);//posar el personatge a lloc
        mort = 0;//canviar l'estat
        video.active = false;
    }
    public void reset()//funcio que s'activa quan mires el boto i has acabat
    {
        if (mort == 1000) { 
        Application.LoadLevel(scene.name);//reset
        }
        else if (mort==-1000) //llibertat
        {
            speed = 5;
            llum.active = true;
            video.active = false;
            boto.active = false;
            mort = 1001;
            so.active = true;
        }
    }
    void OnTriggerEnter(Collider jugador)
    {
        
        if (jugador.tag == "mort")//si toca la paret de la mort 
        {   boto.active = true;
            Handheld.Vibrate();
            somort.active = true;
            video.active = true;
            so.active = false;
            mort = 1000;
            transform.Translate(0, 100, 0);
            //Destroy(gameObject);
            //mor.enabled = true;
            //win.enabled = false;
            //joc.enabled = false;
        }
        if (jugador.tag == "win")//si toca la paret de la victoria
        {
            boto.active = true;
            video.active = true;
            so.active = false;
            mort = -1000;
            transform.Translate(-100, 0, 0);
            //Destroy(gameObject);
            //mor.enabled = false;
            //win.enabled = true;
            //joc.enabled = false;
        }
    }
}
