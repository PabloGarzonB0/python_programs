package variables;

public class Principal{
    public static void main(String[] args) {

        String saludar = "Hola Mundo desde Java";
        System.out.println(saludar);
        System.out.println("Saludar.toUpperCase() = " + saludar.toUpperCase());


        int numero = 10;
        Integer numero1 = 101;
        System.out.println("numero: "+ numero);


        boolean valor = true;
        if (valor){
            System.out.println("Condicional activado internamente");
            numero = 50;
        }

        System.out.println("numero: "+numero);
        var numero3 = 44;

        String nombre;
        nombre = "Pablo";

        if(numero > 10){
            nombre = "Juancho";
        }
        System.out.println("Nombre: " + nombre);







        //  Java tiene diferentes tipos de datos y estos pueden ir desde datos prImitivos,
        //  referencia (arreglos, clases e intefaces)
        }
    }

