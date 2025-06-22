package variables;

// Importe de librerias
import java.util.InputMismatchException;
import java.util.Scanner;
// Mini-programa para Ingreso de un dato correcto
public class sistema_numerico_Entrada_Scanner {
    public static void main(String[] args) {

        Scanner lectura = new Scanner(System.in);
        System.out.println("Ingrese un numero entero: ");
        int numeroD = 0; //Necesario asignar un valor inicial
        try {
            numeroD = lectura.nextInt(); //Donde se detecta el error
        }catch(InputMismatchException e){
            System.out.println("Error por ingresar un valor no numerico: " + e.getMessage());
            main(args);
            System.exit(0);
            }

        // Inicializacion de variables:
        String textoBinario = "\nnumero binario de " + numeroD + " = " + Integer.toBinaryString(numeroD);
        String textoOctal = "\nnumero octal de " + numeroD + " = " + Integer.toOctalString(numeroD);
        String textoHex = "\nnumero hexadecimal de " + numeroD+ " = " + Integer.toHexString(numeroD);

        String mensaje = textoBinario;
        mensaje += textoOctal;
        mensaje += textoHex;

        System.out.println(mensaje);
    }
}
