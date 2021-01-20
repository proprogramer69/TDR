using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class creacio : MonoBehaviour {
    public GameObject peça1;
    public GameObject peça2;
    public GameObject peça3;
    public GameObject peça4;
    public GameObject peça5;
    public GameObject peça6;
    public GameObject peça7;//importar models de peça
    //public Text holis;
    public Text lol;//importar text
    public int ultima;// asegurar-se de que no hi hagi dos x seguides
    public string hey;
    public int ran;//no fer cas
    public int rand;// posicio x aleatoria
    public int quina=0;// saver quina peça aleatoria ha sortit
    int agustin=0;//assegurar-se de que el bucle d'espera funcioni
	// Use this for initialization
	void Start () {
		
	}
	
	// Update is called once per frame
	void Update () {
        if (lol.text == "0")
        {
            StartCoroutine(Test());
        }
	}
    IEnumerator Test()//bucle de espera
    {
        if (agustin == 0)
        {
            quina = Random.Range(0, 7);//elegir peça
            agustin++;
            yield return new WaitForSeconds(0.5f);//espear
            agustin = 0;
            Generar();//cridar a la funcio de crear
        }
    }
    void Generar(){
        Vector3 hola;
        ran = 1;//Random.Range(0, 2); (no fer cas)
       
        //hey= System.Convert.ToString(ran);
        //holis.text = hey;
        //if(ran==1){
        rand = Random.Range(-3, 4);

        while (rand == ultima) {//si rand es igual que ultima tornar a elegir
            rand = Random.Range(-3, 4); 
            }
       
        hola.x = rand;
        ultima = rand;
        //}else{
         //hola.x = Random.Range(-4, 5);
        //}
        hola.y = -1.4f;
        hola.z = 70;
        if (quina == 1) {
        GameObject.Instantiate(peça1, hola, Quaternion.identity);// crea l'objecte en el vector hola
        }
        else if (quina == 2)
        {
            GameObject.Instantiate(peça2, hola, Quaternion.identity);
        }
        else if (quina == 3)
        {
            GameObject.Instantiate(peça3, hola, Quaternion.identity);
        }
        else if (quina == 4)
        {
            GameObject.Instantiate(peça4, hola, Quaternion.identity);
        }
        else if (quina == 5)
        {
            GameObject.Instantiate(peça5, hola, Quaternion.identity);
        }
        else if (quina == 6)
        {
            GameObject.Instantiate(peça6, hola, Quaternion.identity);
        }
        else if (quina == 0)
        {
            GameObject.Instantiate(peça7, hola, Quaternion.identity);
        }
    }
}
