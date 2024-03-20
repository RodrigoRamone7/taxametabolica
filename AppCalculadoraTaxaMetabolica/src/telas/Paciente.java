/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package telas;

/**
 *
 * @author Rodrigo Ramone
 */
public class Paciente {
    private int p, a, i;
    
    public int TaxaMetabHomem(int peso,int altura,int idade){
        p = peso;
        a = altura;
        i = idade;
        double taxa = 66 + (13.8 * p) + (5 * a) - (6.8 * i);
        return (int)taxa;
    }
    
    public int TaxaMetabMulher(int peso,int altura,int idade) {
        p = peso;
        a = altura;
        i = idade;
        double taxa = 655 + (9.6 * p) + (1.9 * a) - (4.7 * i);
        return (int)taxa;
    }
    
    public int TaxaAtivLeveHomem(int taxaMetabolica){
        double ativ = taxaMetabolica*1.55;
        return (int)ativ;
    }
    
    public int TaxaAtivModeradaHomem(int taxaMetabolica){
        double ativ = taxaMetabolica*1.78;
        return (int)ativ;
    }
    
    public int TaxaAtivIntensaHomem(int taxaMetabolica){
        double ativ = taxaMetabolica*2.10;
        return (int)ativ;
    }
    
    public int TaxaAtivLeveMulher(int taxaMetabolica){
        double ativ = taxaMetabolica*1.56;
        return (int)ativ;
    }
    
    public int TaxaAtivModeradaMulher(int taxaMetabolica){
        double ativ = taxaMetabolica*1.64;
        return (int)ativ;
    }
    
    public int TaxaAtivIntensaMulher(int taxaMetabolica){
        double ativ = taxaMetabolica*1.82;
        return (int)ativ;
    }
}
