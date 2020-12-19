package br.edu.iftm.test;

import br.edu.iftm.classes.Breaker;
import br.edu.iftm.classes.Shae256;

public class App {
    public static void main(String[] args) {
        if (args.length == 0) {
            System.err.println("Hash vazia");
            System.exit(-1);
        }

        String senha = args[0];
        int tamanho = 6;

        Shae256 s = new Shae256();
        
        for (int i = 1; i != tamanho; i++) {
            Breaker b = new Breaker(senha, i, s);
            try {
                b.join();
            } catch (InterruptedException e) {
                
                e.printStackTrace();
            }
        }
    }
}
