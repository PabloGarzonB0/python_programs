package variables;

import java.util.Scanner;

public class vectores_dinamicos {
    public static Scanner lectura = new Scanner(System.in);

    static void vector_dinamico(){
        int longitud = 0;
        System.out.println("Cuantos numero desea guardar: ");
        longitud = lectura.nextInt();
        int[] vectorNumeros = new int[longitud];
        for(int i=0; i < vectorNumeros.length; i++){
            System.out.println("Ingrese el valor en la posicion [" + (i+1) + "] del vector ");
            vectorNumeros[i] = lectura.nextInt();
        }
        for (int caracter : vectorNumeros) {
            System.out.println("Elemento: "+ caracter);
        }
    }

    static void piramide(){
        // Piramides con asteriscos
        int base;
        int conteo = 0;
        System.out.println("Digite el valor de la base: ");
        base = lectura.nextInt();
        for (int i = base; i >= 0 ; i--) {
            conteo ++;
            for (int j = 0; j < conteo ; j++) {
                System.out.print("* ");
            }
            System.out.println("");
        }
    }
    public static void main(String[] args) {
        // Metodo: ingreso de datos en vector
        //vector_dinamico();

        // Metodo: Piramide lateral
        //piramide();

        // Metodo: Creacion_piramidal
        int[][] matNumero = new int[6][6];
        int n,m,num = 1;
        int a,nroFilas,nroColumna;
        System.out.println("Ingrese numero filas");
        nroFilas = lectura.nextInt();
        nroColumna = nroFilas;
        a = nroColumna - 1;

        for (n = 0;  n < nroFilas ; n++) {
            for (m = 0;  m < nroColumna ; m++) {
                if (n == m){
                    matNumero[n][m] = 1;
                    matNumero[n][a] = 1;
                    a--;  // Calculo de diagonal invertida
                }

            }

        }
        // Visualizacion de matriz
        for (n = 0;  n < nroFilas ; n++) {
            for (m = 0;  m < nroColumna ; m++) {
                System.out.print(matNumero[n][m] + " ");
            }
            System.out.println();
        }
    }
}
