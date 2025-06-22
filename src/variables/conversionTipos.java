package variables;

public class conversionTipos {

    public static void main(String[] args){

        //  Conversiones de codigo
        String numeroStr = "50";
        int numeroIn = Integer.parseInt(numeroStr);
        System.out.println("Numero int: "+ numeroIn);

        String realString = "124523.23e-4";
        double realDouble = Double.parseDouble(realString);
        System.out.println("Numero Double: " + realDouble);


        String logicoStr = "true";
        boolean logicoBoolean = Boolean.parseBoolean(logicoStr);
        System.out.println("Numero Booleano: "+ logicoBoolean);

        int otroNumeroInt = 100;

        String otroNumeroStr = Integer.toString(otroNumeroInt);
        System.out.println("OtroNumeroStr = " + otroNumeroStr);

        otroNumeroStr = String.valueOf(otroNumeroInt + 50);   //Sobrecarga: la firma del metodo es diferente, parametros diferentes
        System.out.println("OtroNumeroStr = " + otroNumeroStr);


        double otroReal = 23435.43;
        String otroRealStr = Double.toString(otroReal);
        System.out.println("otroRealStr = " + otroRealStr);

        otroRealStr = String.valueOf(1.2345e2f);
        System.out.println("otroRealStr = " + otroRealStr);

        /* El casteo de variables va considerar 3 metodos diferentes, basados en el wrapper String, de tipo y parse
        * para hacer el cambio con string considerando su metodo toxx: tipovariable.toString
        * para hacer el cambio mediante la variable de tipo: tipovariablefinal.valueOf()
        * para hacer el cambio mediante el metodo parse: tipovariable.parsetipo()
        * */
    }
}
