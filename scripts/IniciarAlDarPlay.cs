using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.Video;


public class IniciarAlDarPlay : MonoBehaviour
{
    public VideoPlayer inici;
    public VideoPlayer mort;
    public VideoPlayer win;
    public Text lol;
    // Use this for initialization
    void Start()
    {

    }

    // Update is called once per frame
    void Update()
    {
        if (lol.text == "1") //veure que diu la variable de l'estat, en aquest cas si es principi de tot
        {
            mort.enabled = false;//apagar video
            win.enabled = false;
            inici.enabled = true;//encendre video
                if (!inici.isPlaying)//si no esta reproduint-se, llavors que es reprodueixi
                    inici.Play();
        }
        else if (lol.text == "-1000")//has mort?
        {
            win.enabled = true;
            mort.enabled = false;
            inici.enabled = false;
            if (!win.isPlaying) 
                win.Play();

        }
        else if (lol.text == "1000")//has guanyat?
        {
            mort.enabled = true;
            win.enabled = false;
            inici.enabled = false;
            if (!mort.isPlaying)
                mort.Play();
        }
    }
}
