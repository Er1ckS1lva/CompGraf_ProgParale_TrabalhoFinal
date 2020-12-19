
package br.edu.iftm.classes;

import java.nio.charset.StandardCharsets;
import com.google.common.hash.Hashing;

public class Shae256 {

    private boolean Stop = false;
    private boolean achou = false;
    private String Hash;
    private int tamanho;
    private String senha;

    public Shae256() {   
    }

    public synchronized boolean init(String hash, int tamanho){
        this.Hash = hash;
        this.tamanho = tamanho;
        if(this.achou == false){
            this.Stop = false;
            generate_Str(this.Hash, this.tamanho);
        }
        return achou;
    }

    public String generate_Str(String hash, int tamanho) {

        String Senha = "";
        Character Sequen[] = new Character[tamanho];
        for (int aux = 0; aux < tamanho; aux++) {
            Sequen[aux] = (char) 48;
        }
        
        while (!this.Stop){
            
            String str = convert_String(Sequen, Sequen.length);
            //System.out.println(str);
            this.Stop = compare(str, hash);
            Sequen = increment(Sequen);  
        }
        if (this.achou) {
            System.out.println("SENHA ENCONTRADA = " + this.senha);
        } else {
            //System.out.println("Não achou");
        }
        return Senha;
    }

    public Character[] increment(Character[] array) {

        Character senha[] = array;
        int tamanho = this.tamanho -1;
        senha[0] =  (char) (senha[0] + 1);
        //System.out.println(senha[0]);

        for(int help = 0;help < tamanho; help++){
            if(senha[help] == 90){
                senha[help] = (char) 48;
                senha[help+1] = (char) ((char) senha[help + 1] + 1);
            }
        }
        if((senha[tamanho] == 90)||(senha[tamanho] == 'Z')){
            this.Stop = true;
        }       
        return senha;
    }

    public boolean compare(String input, String hashString) {

        String sha256aux = Hashing.sha256().hashString(input, StandardCharsets.UTF_8).toString();
        
        if (sha256aux.equals(hashString)) {
            this.senha = input;
            this.Stop = true;
            this.achou = true;
            return true;
        }      
        return false;
    }

    public String convert_String(Character[] array, int length) {
        String char_string;
        String return_string = "";
        int i;
        for (i = 0; i < length; i++) {
            char_string = Character.toString(array[i]);
            return_string = return_string.concat(char_string);
        }
        return return_string;
    }

}