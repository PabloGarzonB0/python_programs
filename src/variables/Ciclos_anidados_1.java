package variables;

import java.util.Scanner;

public class Ciclos_anidados_1 {
    public static void main(String[] args) {
        // Algoritmo para calcular el factorial de un numero
        Scanner lectura = new Scanner(System.in);
        int numero, facto;
        System.out.println("Ingrese el numero factorial que desea procesar");
        numero = lectura.nextInt();
        while(numero != 0){
            if (numero < 0) {
                System.out.println("No esta definido el factorial de un numero negativo");
            }else{
                facto = 1;
                for(int conta=1; conta<= numero; conta++){
                    facto = facto * conta;
                }
                System.out.println("Factoria de, "+ numero + " = " + facto);
            }
            System.out.println("Si desea salida de \" esta operacion ingrese [0] \n sino ingrese  el numero a evaluar");
            numero = lectura.nextInt();
        }
        System.out.println("Calculo de factorial realizado correctamente");
    }
}
