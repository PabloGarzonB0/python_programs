package variables;

import javax.swing.*;
// Mini-programa para Ingreso de un dato correcto
public class sistema_numerico_2 {
    public static void main(String[] args) {

        String numeroDecimal = JOptionPane.showInputDialog(null, "Ingrese un numero entero");
        int numeroD = 0; //Necesario asignar un valor inicial
        try {
            numeroD = Integer.parseInt(numeroDecimal); //Donde se detecta el error
        }catch(NumberFormatException e){
            JOptionPane.showMessageDialog(null,  "Error por ingresar un valor no numerico");
            main(args);
            System.exit(0);
            }
        // Textos de mensajes
        String textoBinario = "\nnumero binario de " + numeroD + " + " + Integer.toBinaryString(numeroD);
        String textoOctal = "\nnumero octal de " + numeroD + " = " + Integer.toOctalString(numeroD);
        String textoHex = "\nnumero hexadecimal de " + numeroD+ " = " + Integer.toHexString(numeroD);


        String mensaje = textoBinario;
        mensaje += textoOctal;
        mensaje += textoHex;

        JOptionPane.showMessageDialog(null, mensaje);
    }
}
