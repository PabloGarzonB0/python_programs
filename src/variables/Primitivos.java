package variables;

public class Primitivos {

    static float varFloat = 45.45f;

    public static void main(String[] args) {
        // Reconocer el rango de valores para la variable de byte
        byte numeroByte = 27;
        System.out.println("numeroByte = " + numeroByte);
        System.out.println("tipo byte corresponde en byte a " + Byte.BYTES);
        System.out.println("Valor maximo de un byte: " + Byte.MAX_VALUE);
        System.out.println("Valor minimo de un byte: " + Byte.MIN_VALUE);
        // Reconocer el rango de valores para la variable short
        short numeroshort = 30000;
        System.out.println("numeroShort = " + numeroshort);
        System.out.println("tipo byte corresponde en byte a " + Short.BYTES);
        System.out.println("Valor maximo de un byte: " + Short.MAX_VALUE);
        System.out.println("Valor minimo de un byte: " + Short.MIN_VALUE);

        int numeroInt = 2147483647 ;
        System.out.println("numeroShort = " + numeroInt);
        System.out.println("tipo byte corresponde en byte a " + Integer.BYTES);
        System.out.println("Valor maximo de un byte: " + Integer.MAX_VALUE);
        System.out.println("Valor minimo de un byte: " + Integer.MIN_VALUE);

        long numeroLong = 2147483648999L ;
        System.out.println("numeroShort = " + numeroLong);
        System.out.println("tipo byte corresponde en byte a " + Long.BYTES);
        System.out.println("Valor maximo de un byte: " + Long.MAX_VALUE);
        System.out.println("Valor minimo de un byte: " + Long.MIN_VALUE);

        var numeroVar = 127;  //Caracteristica soportada desde la JDK 10
        Integer numeroCualquiera = 100;
        float realFloat = 2.13e4f;  //2120f la e representa el valor exponencial
        System.out.println("realFLoat = " + realFloat);
        System.out.println("Valor real = " + numeroCualquiera.getClass());
        System.out.println("Valor maximo de un float: " + Float.MAX_VALUE);
        System.out.println("Valor minimo de un float: " + Float.MIN_VALUE);
        System.out.println("Tamano en bites: " + Float.SIZE);

        // Los datos de tipo float necesitan terminar con una f
        // Los datos de tipo long necesitan terminar en L
        // A utilizar la variable var, se distingue la variable mediante el uso del caracter F, L
        System.out.println("varFlotante: " + varFloat);
    }
}

