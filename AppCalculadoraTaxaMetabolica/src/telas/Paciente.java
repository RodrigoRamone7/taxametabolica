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
    
    Paciente(int peso, int altura, int idade, int genero){
        this.peso = peso;
        this.altura = altura;
        this.idade = idade;
        this.genero = genero;
        
        switch (genero){
            case 0 :
                this.taxa = TaxaMetabHomem(peso, altura, idade);
                setTaxasHomem(this.taxa);
                break;
            case 1 :
                this.taxa = TaxaMetabMulher(peso, altura, idade);
                setTaxasMulher(this.taxa);
                break;
        }
    }
    
    private int TaxaMetabHomem(int p,int a,int i){
        double t = 66 + (13.8 * p) + (5 * a) - (6.8 * i);
        return (int)t;
    }
    
    private int TaxaMetabMulher(int p,int a,int i) {
        double t = 655 + (9.6 * p) + (1.9 * a) - (4.7 * i);
        return (int)t;
    }
    
    private void setTaxasHomem(int taxa){
        int ativ = taxa;
        this.atividadeLeve = TaxaAtivLeveHomem(ativ);
        this.atividadeModerada = TaxaAtivModeradaHomem(ativ);
        this.atividadeIntensa = TaxaAtivIntensaHomem(ativ);
    }
    
    private void setTaxasMulher(int taxa){
        int ativ = taxa;
        this.atividadeLeve = TaxaAtivLeveMulher(ativ);
        this.atividadeModerada = TaxaAtivModeradaMulher(ativ);
        this.atividadeIntensa = TaxaAtivIntensaMulher(ativ);
    }
    
    private int TaxaAtivLeveHomem(int taxaMetabolica){
        double ativ = taxaMetabolica*1.55;
        return (int)ativ;
    }
    
    private int TaxaAtivModeradaHomem(int taxaMetabolica){
        double ativ = taxaMetabolica*1.78;
        return (int)ativ;
    }
    
    private int TaxaAtivIntensaHomem(int taxaMetabolica){
        double ativ = taxaMetabolica*2.10;
        return (int)ativ;
    }
    
    private int TaxaAtivLeveMulher(int taxaMetabolica){
        double ativ = taxaMetabolica*1.56;
        return (int)ativ;
    }
    
    private int TaxaAtivModeradaMulher(int taxaMetabolica){
        double ativ = taxaMetabolica*1.64;
        return (int)ativ;
    }
    
    private int TaxaAtivIntensaMulher(int taxaMetabolica){
        double ativ = taxaMetabolica*1.82;
        return (int)ativ;
    }
}
