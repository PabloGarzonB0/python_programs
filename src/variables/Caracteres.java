package variables;

public class Caracteres {
    public static void main(String[] args) {
        var caracter = '\u0040';  //caracter unicode
        char decimal = 64;
        System.out.println("decimal = " + decimal);
        System.out.println("Caracter = " + caracter);
        System.out.println("igualdad : " + (caracter == decimal));

        char simbolo = '@';  //Importante considerar el codigo ascii del caracter
        System.out.println("Igualdad de caracteres @: " + (caracter == simbolo));

        System.out.println("Char correspondiente en byte = " + Character.BYTES);
        System.out.println("Char corresponde en bites = " + Character.SIZE);
        System.out.println("Tamano maximo : " + Character.MAX_VALUE);
        System.out.println("Tamano minimo : " + Character.MIN_VALUE);

        char espacio = ' ';            // variables.Caracteres especiales de retroceso
        char espacioAscii = '\u0020';  // Cambio de posicion
        char retroceso = '\b';
        char tabulador = '\t';
        System.out.println("Char corresponde en byte: "+ espacioAscii + Character.BYTES);
        System.out.println("Char corresponde en bites: "+ retroceso + Character.SIZE);

    }


}
