package variables;

public class sistema_numerico {
    public static void main(String[] args) {

        int numeroDecimal = 100;
        System.out.println("numeroDecimal : " + numeroDecimal);
        System.out.println("numero binario : " + numeroDecimal + " = " + Integer.toBinaryString(numeroDecimal));

        int numeroBinario = 0b1111110100;
        int numeroOctal = 0764;   //Octal
        System.out.println("numeroBinario = " + numeroBinario);
        System.out.println("numero octal = " + Integer.toOctalString(numeroDecimal));
        System.out.println("numero Hexadecimal = " + Integer.toHexString(numeroDecimal));
        int numeroHex = 0x1F4 ;
        System.out.println(numeroHex);
    }
}
