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
    public int peso, altura, idade, genero, taxa;
    public int atividadeLeve, atividadeModerada, atividadeIntensa;
    
    public void SetPaciente(int p, int a, int i, int g){
        peso = p;
        altura = a;
        idade = i;
        genero = g;
        switch (genero){
            case 0 :
                taxa = TaxaMetabHomem(p, a, i);
                atividadeLeve = TaxaAtivLeveHomem(taxa);
                atividadeModerada = TaxaAtivModeradaHomem(taxa);
                atividadeIntensa = TaxaAtivIntensaHomem(taxa);
                break;
            case 1 :
                taxa = TaxaMetabMulher(p, a, i);
                atividadeLeve = TaxaAtivLeveMulher(taxa);
                atividadeModerada = TaxaAtivModeradaMulher(taxa);
                atividadeIntensa = TaxaAtivIntensaMulher(taxa);
                break;
        }
        
    }
    
    public int TaxaMetabHomem(int p,int a,int i){
        double t = 66 + (13.8 * p) + (5 * a) - (6.8 * i);
        return (int)t;
    }
    
    public int TaxaMetabMulher(int p,int a,int i) {
        double t = 655 + (9.6 * p) + (1.9 * a) - (4.7 * i);
        return (int)t;
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
