package br.edu.iftm.classes;

public class Breaker extends Thread {

    private int tamanho;
    private String senha;
    private Shae256 s;

    public Breaker(String hash, int tamanho, Shae256 s) {
     
        this.s = s;
        this.senha = hash;
        this.tamanho = tamanho;
        this.start();
    }
    
    @Override
    public void run() {
        s.init(this.senha, this.tamanho);
    }
    
}
