package variables;

public class Booleanos {
    public static void main(String[] args) {
        boolean datoLogico = Boolean.FALSE.booleanValue();
        System.out.println("DatoLogico: "+ datoLogico);

        double d = 394982.433e-3; //98.765
        float f = 3.243e2f;

        datoLogico = (d>f);

        boolean esIgual = (3-2 == 1);
        System.out.println("variable de validacion: "+ esIgual);
    }
}
